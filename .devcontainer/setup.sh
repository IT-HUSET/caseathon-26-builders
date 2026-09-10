#!/usr/bin/env bash
# Claude Code is installed at image build time by the claude-code dev container feature
set -e
echo "Claude Code: $(claude --version 2>/dev/null || echo 'not found (check devcontainer.json features)')"
echo "Installing dependencies..."
uv sync
echo "Done. Run 'uv run check.py', then 'claude'."
