#!/usr/bin/env bash
set -e
echo "Installing Claude Code..."
curl -fsSL https://claude.ai/install.sh | bash || npm install -g @anthropic-ai/claude-code
export PATH="$HOME/.local/bin:$PATH"
echo "Installing dependencies..."
uv sync
echo "Done. Run ./check.sh, then 'claude'."
