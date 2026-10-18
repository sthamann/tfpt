#!/usr/bin/env python3
"""Prepare explicitly scoped reading editions from the shared TeX source reader."""
from pathlib import Path
import argparse
import json
import re
from tex_sources import source_chunks

ROOT = Path(__file__).resolve().parents[1]


def build():
    config = json.loads((ROOT / "docs/editions.json").read_text())
    outputs = {}
    for edition in config["editions"]:
        if "generated_source" not in edition:
            continue
        omitted = {(ROOT / rel).resolve() for rel in edition["omit_include_chains"]}
        chunks = source_chunks(ROOT / edition["source_owner"])
        text = "".join(chunk.text for chunk in chunks
                       if not omitted.intersection(chunk.include_chain))
        appendix = edition.get("omit_reference_appendix_marker")
        if appendix:
            if text.count(appendix) != 1:
                raise ValueError("Reading edition requires its unique named appendix boundary")
            text = text.split(appendix, 1)[0] + "\n\\end{document}\n"
        marker = r"\maketitle"
        note = r"""
\par\medskip\noindent\textbf{Compact reading edition.}
This edition retains the introduction's scientific text and omits the computational reference appendix and its full dated history.
Read them separately as \texttt{verification\_catalog.pdf} and
\texttt{changelog.pdf}; the original complete \texttt{introduction.pdf} remains
available. Source ownership and evidence links are listed at
\url{https://www.fixpoint-theory.com/documentation}.
\par\medskip
"""
        if marker not in text:
            raise ValueError("Reading edition requires an explicit title boundary")
        # The original title is followed by a negative gap before its first
        # box. Remove that title-only skip before inserting an edition note;
        # otherwise it pulls the first box over the note's final line.
        text = re.sub(r"(\\maketitle)\s*\\vspace\{-0\.8cm\}", r"\1\n", text, count=1)
        text = text.replace(marker, marker + note, 1)
        outputs[ROOT / edition["generated_source"]] = text
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, text in build().items():
        if args.check:
            if not path.exists() or path.read_text() != text:
                stale.append(path.name)
        else:
            path.write_text(text)
            print("Prepared reading edition:", path.name)
    if stale:
        raise SystemExit("Stale reading editions: " + ", ".join(stale))


if __name__ == "__main__":
    main()
