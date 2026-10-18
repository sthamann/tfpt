"""Read a LaTeX entry point with ordered, source-attributed literal includes.

This is a source reader, not a TeX interpreter: both conditional branches remain
visible, macros are not executed, and dynamic input names remain literal. Literal
input/include commands outside comments and verbatim environments are expanded.
Compile-directory lookup comes first, preserving existing entry-point semantics.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


class TexSourceError(RuntimeError):
    """A literal source dependency could not be expanded safely."""


class MissingTexSourceError(TexSourceError):
    """A literal include has no existing source file."""


class TexIncludeCycleError(TexSourceError):
    """The current include chain re-enters an ancestor source file."""


@dataclass(frozen=True)
class SourceChunk:
    """An unchanged span of one physical UTF-8 source, in expanded order.

    Lines are one-based and inclusive. Bytes are zero-based, end-exclusive;
    their offsets refer to the original physical file, before expansion.
    include_chain contains the entry point through this physical source.
    """
    path: Path
    text: str
    start_line: int
    end_line: int
    start_byte: int
    end_byte: int
    include_chain: tuple[Path, ...]

    @property
    def source_path(self) -> Path:
        return self.path

    @property
    def line_start(self) -> int:
        return self.start_line

    @property
    def line_end(self) -> int:
        return self.end_line


_INPUT = re.compile(r"\\(?:input|include)(?![A-Za-z@])\s*(?:\{([^{}\r\n]+)\}|([^\s{}%\\]+))")
_VERBATIM = re.compile(r"\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}")
_COMMAND = re.compile(r"\\(?:[A-Za-z@]+|.)", re.DOTALL)


def literal_includes(text: str, *, verbatim_names: set[str] | None = None) -> list[tuple[int, int, str]]:
    """Return (character start, end, literal filename), ignoring TeX comments."""
    found: list[tuple[int, int, str]] = []
    verbatim_names = verbatim_names if verbatim_names is not None else set()
    verbatim_names.update({"verbatim", "verbatim*", "Verbatim", "lstlisting", "minted", "comment"})
    verbatim_names.update(re.findall(r"\\DefineVerbatimEnvironment\{([^{}]+)\}", text))
    pos = 0
    while pos < len(text):
        char = text[pos]
        if char == "%":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end + 1
            continue
        if char != "\\":
            pos += 1
            continue
        block = re.match(r"\\begin\{([^{}]+)\}", text[pos:])
        if block and block[1] in verbatim_names:
            end_token = "\\end{" + block[1] + "}"
            end = text.find(end_token, pos + block.end())
            pos = len(text) if end < 0 else end + len(end_token)
            continue
        verb = re.match(r"\\verb\*?(?![A-Za-z@])", text[pos:])
        if verb:
            delimiter_at = pos + verb.end()
            if delimiter_at < len(text):
                end = text.find(text[delimiter_at], delimiter_at + 1)
                pos = len(text) if end < 0 else end + 1
                continue
        command = _INPUT.match(text, pos)
        if command:
            name = (command[1] or command[2]).strip()
            if name and not re.search(r"[\\#$*]", name):
                found.append((pos, command.end(), name))
            pos = command.end()
            continue
        token = _COMMAND.match(text, pos)
        pos = token.end() if token else pos + 1
    return found


def _project_root(path: Path) -> Path:
    for directory in (path.parent, *path.parents):
        if (directory / ".git").exists() or ((directory / "build.sh").exists() and (directory / "verification").is_dir()):
            return directory
    return path.parent


def _resolve(name: str, current: Path, compile_dir: Path, project_root: Path) -> Path | None:
    requested = Path(name)
    locations = [requested] if requested.is_absolute() else [compile_dir / requested, current.parent / requested, project_root / requested]
    for location in locations:
        for candidate in (location, Path(str(location) + ".tex")):
            if candidate.is_file():
                return candidate.resolve()
    return None


def _source_data(path: Path, *, compile_dir: Path | None = None) -> tuple[list[SourceChunk], list[Path]]:
    """Expand literal includes and retain exact physical source spans.

    Missing includes and cycles raise TexSourceError subclasses with the full
    include chain. No newline, whitespace or TeX content is synthesized.
    """
    entry = Path(path).resolve()
    compile_dir = Path(compile_dir).resolve() if compile_dir is not None else entry.parent
    project_root = _project_root(entry)
    chunks: list[SourceChunk] = []
    dependencies: list[Path] = []
    known_verbatim_names: set[str] = set()

    def expand(current: Path, ancestors: tuple[Path, ...]) -> None:
        if current in ancestors:
            chain = (*ancestors, current)
            raise TexIncludeCycleError("TeX include cycle: " + " -> ".join(map(str, chain)))
        chain = (*ancestors, current)
        if not current.is_file():
            raise MissingTexSourceError("Missing TeX source: " + str(current) + "; chain: " + " -> ".join(map(str, chain)))
        if current not in dependencies:
            dependencies.append(current)
        text = current.read_bytes().decode("utf-8")

        def append(start: int, end: int) -> None:
            if start == end:
                return
            part = text[start:end]
            first_line = text.count("\n", 0, start) + 1
            last_line = first_line + part.count("\n") - int(part.endswith("\n"))
            chunks.append(SourceChunk(current, part, first_line, max(first_line, last_line), len(text[:start].encode("utf-8")), len(text[:end].encode("utf-8")), chain))

        offset = 0
        for start, end, name in literal_includes(text, verbatim_names=known_verbatim_names):
            append(offset, start)
            included = _resolve(name, current, compile_dir, project_root)
            if included is None:
                line = text.count("\n", 0, start) + 1
                raise MissingTexSourceError(f"Missing literal TeX include {name!r} at {current}:{line}; chain: " + " -> ".join(map(str, chain)))
            expand(included, chain)
            offset = end
        append(offset, len(text))

    expand(entry, ())
    return chunks, dependencies


def source_chunks(path: Path, *, compile_dir: Path | None = None) -> list[SourceChunk]:
    """Return ordered exact text spans, with physical source provenance."""
    return _source_data(path, compile_dir=compile_dir)[0]


def dependency_paths(path: Path, *, compile_dir: Path | None = None) -> list[Path]:
    """Return every visited physical file once, in first-visit order.

    Unlike text chunks, this also includes empty files and pure include wrappers.
    Missing includes and cycles raise the same explicit errors as read_tex.
    """
    return _source_data(path, compile_dir=compile_dir)[1]


def read_tex(path: Path, *, compile_dir: Path | None = None) -> str:
    """Return the exact ordered text of source_chunks(path)."""
    return "".join(chunk.text for chunk in source_chunks(path, compile_dir=compile_dir))
