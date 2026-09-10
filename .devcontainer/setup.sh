#!/usr/bin/env bash
# Claude Code is installed at image build time by the claude-code dev container feature
set -e
echo "Claude Code: $(claude --version 2>/dev/null || echo 'not found (check devcontainer.json features)')"
# Codex CLI and GitHub Copilot CLI (optional alternatives; each has its own login: 'codex' and 'copilot')
echo "Installing Codex CLI and Copilot CLI..."
npm install -g @openai/codex @github/copilot >/dev/null 2>&1 \
  || echo "Note: Codex/Copilot CLI install failed (network?). Retry: npm install -g @openai/codex @github/copilot"

echo "Installing dependencies..."
uv sync
echo "Done. Run 'uv run check.py', then 'claude'."
