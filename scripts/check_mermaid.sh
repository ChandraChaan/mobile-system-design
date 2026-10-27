#!/usr/bin/env bash
# Renders every Mermaid diagram in the docs, so a syntax error fails CI.
# Usage: scripts/check_mermaid.sh   (needs Node.js; uses npx)
set -euo pipefail

out="$(mktemp -d)"
python3 - "$out" <<'PY'
import re, sys
from pathlib import Path
out = Path(sys.argv[1])
n = 0
for md in sorted([Path("README.md"), *Path("docs").rglob("*.md")]):
    for i, block in enumerate(re.findall(r"```mermaid\n(.*?)```", md.read_text(encoding="utf-8"), re.S)):
        name = f"{str(md).replace('/', '_')}_{i}.mmd"
        (out / name).write_text(block, encoding="utf-8")
        n += 1
print(f"Found {n} diagrams")
PY

failed=0
for f in "$out"/*.mmd; do
  if ! npx -y @mermaid-js/mermaid-cli@11.17.0 -q -p "${PUPPETEER_CONFIG:-scripts/puppeteer.json}" \
      -i "$f" -o "${f%.mmd}.svg" >"$f.log" 2>&1; then
    echo "error: $(basename "$f")"; cat "$f.log"; failed=1
  fi
done
[ "$failed" = 0 ] && echo "All diagrams render"
exit "$failed"
