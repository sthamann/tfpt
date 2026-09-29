#!/bin/zsh
set -e
cd "$(dirname "$0")/../../.."
exec python3 -m tfpt_explorer
