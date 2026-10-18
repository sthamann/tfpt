#!/usr/bin/env bash
# Optional legacy filtered export utility; the tfpt5-shadow mirror is retired.
# No active GitHub workflow invokes this utility (retired 2026-10-18).
# The remote is archived/read-only; no shadow-sync token renewal is needed.
#
# Included:  all git-tracked files except the exclusions below.
#            figures/*.pdf ARE mirrored (the manifest references them).
# Excluded: website/, editor/agent hook configurations, and compiled PDFs.
#            (compiled paper/archive PDFs).
#
# Usage:
#   bash scripts/export-shadow.sh /path/to/shadow-checkout
#
# Typical local test:
#   rm -rf /tmp/tfpt5-shadow && mkdir /tmp/tfpt5-shadow
#   bash scripts/export-shadow.sh /tmp/tfpt5-shadow
#
# Run explicitly only when a filtered local/Overleaf export is wanted.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?Usage: bash scripts/export-shadow.sh <destination-directory>}"

# This exporter prunes its destination. Admit only a dedicated empty/owned
# export directory or the actual shadow repository, never a research checkout.
DEST="$(python3 - "$ROOT" "$DEST" <<'PYGUARD'
from pathlib import Path
import json
import os
import re
import subprocess
import sys
from urllib.parse import urlsplit
root = Path(sys.argv[1]).resolve()
requested = Path(sys.argv[2])
if requested.is_symlink():
    raise SystemExit("Refusing a symbolic-link export destination")
target = requested.resolve()
if target == root or root.is_relative_to(target):
    raise SystemExit("Refusing export into the source checkout or its ancestors")
if target.exists() and not target.is_dir():
    raise SystemExit("Export destination must be a directory")
if target.exists() and any(target.iterdir()):
    marker = target / ".tfpt-shadow-export"
    owned = False
    if marker.is_file():
        try:
            state = json.loads(marker.read_text())
            owned = state.get("owner") == "tfpt-shadow-export" and state.get("source_repository") == "sthamann/tfpt"
        except (OSError, ValueError):
            pass
    if (target / ".git").exists():
        result = subprocess.run(["git", "-C", str(target), "remote", "get-url", "origin"], text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        # Never echo remote URLs: an authenticated checkout can embed a token.
        remote = result.stdout.strip()
        if remote.startswith("git@github.com:"):
            verified_shadow = remote.removeprefix("git@github.com:").rstrip("/").removesuffix(".git") == "sthamann/tfpt5-shadow"
        else:
            parsed = urlsplit(remote)
            verified_shadow = (parsed.scheme in {"https", "ssh"} and parsed.hostname == "github.com"
                               and parsed.path.rstrip("/").removesuffix(".git") == "/sthamann/tfpt5-shadow")
        owned = result.returncode == 0 and verified_shadow
    if not owned:
        raise SystemExit("Refusing to prune a nonempty destination without dedicated shadow-export ownership")
    for folder, dirs, files in os.walk(target):
        dirs[:] = [name for name in dirs if name != ".git"]
        for name in [*dirs, *files]:
            if name != ".git" and (Path(folder) / name).is_symlink():
                raise SystemExit("Refusing a shadow export containing symbolic links")
print(target)
PYGUARD
)"

should_export() {
  local f="$1"
  case "$f" in
    website/*|.cursor/*|.github/*|.agents/*|.codex/*|.claude/*) return 1 ;;
  esac
  case "$f" in
    figures/*.pdf) return 0 ;;   # ship the figures: manifest.sha256 references them
    *.pdf) return 1 ;;           # but no compiled paper / archive PDFs
  esac
  return 0
}

mkdir -p "$DEST"
printf '%s\n' '{"owner":"tfpt-shadow-export","source_repository":"sthamann/tfpt"}' > "$DEST/.tfpt-shadow-export"

LIST="$(mktemp)"
trap 'rm -f "$LIST"' EXIT

git -C "$ROOT" ls-files | while IFS= read -r f; do
  should_export "$f" && printf '%s\n' "$f"
done | sort > "$LIST"

# Copy in one process rather than starting thousands of cp/mkdir subprocesses.
python3 - "$ROOT" "$DEST" "$LIST" <<'PYCOPY'
from pathlib import Path
import shutil
import sys
source, target, listing = map(Path, sys.argv[1:])
for name in listing.read_text().splitlines():
    if not name:
        continue
    destination = target / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / name, destination)
PYCOPY

file_count=0
while IFS= read -r _; do
  file_count=$((file_count + 1))
done < "$LIST"

# Drop mirror files that no longer belong (keeps incremental git diffs small).
python3 - "$DEST" "$LIST" <<'PYPRUNE'
from pathlib import Path
import os
import sys
root = Path(sys.argv[1])
keep = set(Path(sys.argv[2]).read_text().splitlines())
keep.update({"SHADOW_MIRROR.md", ".tfpt-shadow-export", ".git"})
for folder, dirs, files in os.walk(root, topdown=False):
    folder = Path(folder)
    relative = folder.relative_to(root)
    if relative.parts and relative.parts[0] == ".git":
        continue
    for name in files:
        path = folder / name
        if path.relative_to(root).as_posix() not in keep:
            path.unlink()
    if folder != root and not any(folder.iterdir()):
        folder.rmdir()
PYPRUNE

cat > "$DEST/SHADOW_MIRROR.md" <<EOF
# Optional legacy TFPT filtered export

This directory is an explicitly requested filtered export of the main TFPT
repository. The automated \`tfpt5-shadow\` mirror was retired on 2026-10-18;
no active GitHub workflow maintains that remote. The remote repository is
archived/read-only with its history retained; no shadow-sync token renewal is
needed. This optional utility can still prepare a coherent local/Overleaf
source bundle.

| Included | Excluded |
|----------|----------|
| Modular \`documents/\`, entry \`.tex\`, \`tex-artefacts/\`, figures | \`website/\` |
| \`verification/\` (Python suite, ledger, maps, redteam, wolfram) | \`.cursor/\`, \`.github/\` |
| \`experiments/\` (Lean, discovery) | Compiled paper \`*.pdf\` (non-figure) |
| \`_archive/\` sources, central registry, build tools and manifests | |

**Shadow-mode note.** This subset ships \`figures/\` (so \`python3 verification/make_manifest.py --check\`
passes literally on the export) but **not** \`website/\`. The single-source generators
(\`verification/make_script_index.py\`, \`make_changelog_web.py\`, \`make_docs_map.py\`) detect the
missing \`website/\` and skip their website mirrors (\`ScriptIndex.tsx\`, \`lib/changelog.ts\`,
\`website_map.csv\`), so \`bash build.sh notes\` and \`bash build.sh gen\` run on the subset
non-destructively. \`bash build.sh audit\` is likewise shadow-aware: it skips the website mirror,
website version and website wolfram-page checks and prints which sections it skipped.

**Export coherence gate.** \`scripts/export-shadow.sh\` re-runs \`make_manifest.py --check\` and the
(shadow-aware) \`audit_sync.py\` on this filtered tree before the mirror is published, so a package
that says \"ALL CHECKS PASSED\" cannot ship unless it actually reproduces as exported.

**Generated export.** Make source changes in the main repository and rerun this
utility explicitly when another filtered export is needed.

Source: \`${GITHUB_REPOSITORY:-sthamann/tfpt}\` @ \`${GITHUB_SHA:-local}\`
Last export: $(date -u +"%Y-%m-%d %H:%M:%SZ")
Files exported: ${file_count}
EOF

printf 'export-shadow: %s files -> %s\n' "$file_count" "$DEST"

# --- export coherence gate --------------------------------------------------
# The mirror must be reproducible AS SHIPPED.  Two cheap, stdlib-only checks run
# on the FILTERED tree before it is ever pushed/zipped, catching exactly the
# Alessandro shadow-export findings:
#   * make_manifest.py --check  -> every manifest-referenced file is present and
#     current in the export (catches uncommitted modules dropped by git ls-files,
#     and a stale manifest.sha256), so run_all.py can't reference a missing vN;
#   * audit_sync.py (shadow-aware) -> suite <-> run_all <-> registry <-> ledger
#     and the non-website generated surfaces agree on the subset.
# A failure here means: regenerate manifest.sha256 (python3 verification/make_manifest.py)
# and/or commit the missing files in the MAIN repo, then re-export.
if command -v python3 >/dev/null 2>&1; then
  echo "== shadow export coherence gate =="
  if ! ( cd "$DEST" && python3 verification/make_manifest.py --check ); then
    echo "::error::shadow export FAILED make_manifest.py --check on the filtered tree." >&2
    echo "  Fix in the MAIN repo: ensure every manifest-referenced file is committed, then" >&2
    echo "  re-run 'python3 verification/make_manifest.py' as the LAST step and re-export." >&2
    exit 1
  fi
  if ! ( cd "$DEST" && python3 verification/make_content_registry.py --check ); then
    echo "::error::shadow export FAILED central content registry consistency." >&2
    exit 1
  fi
  if ! ( cd "$DEST" && python3 verification/audit_sync.py ); then
    echo "::error::shadow export FAILED the (shadow-aware) sync audit on the filtered tree." >&2
    exit 1
  fi
  echo "shadow export coherence gate: PASS"
else
  echo "WARNING: python3 not found -- skipping shadow export coherence gate" >&2
fi
