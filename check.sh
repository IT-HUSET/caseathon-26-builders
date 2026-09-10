#!/usr/bin/env bash
# Day-before check: runtime, agent CLI, login, tests. Green on every line = ready.
set -u
ok()   { printf '  \033[32mok\033[0m   %s\n' "$1"; }
fail() { printf '  \033[31mFAIL\033[0m %s\n' "$1"; status=1; }
status=0

echo "Caseathon Builders warm-up: environment check"
command -v uv >/dev/null      && ok "uv $(uv --version | cut -d' ' -f2)"        || fail "uv missing: curl -LsSf https://astral.sh/uv/install.sh | sh"
command -v python3 >/dev/null && ok "$(python3 --version)"                      || fail "python3 missing"
command -v claude >/dev/null  && ok "claude $(claude --version 2>/dev/null | head -1)" || fail "claude missing: curl -fsSL https://claude.ai/install.sh | bash"
if command -v claude >/dev/null; then
  if claude auth status >/dev/null 2>&1; then ok "claude logged in"; else fail "not logged in: run 'claude' then /login"; fi
fi
uv sync -q >/dev/null 2>&1 && ok "dependencies installed" || fail "uv sync failed"
if uv run pytest -q >/dev/null 2>&1; then ok "tests pass"; else fail "tests fail: run 'uv run pytest -q'"; fi

if [ "$status" -eq 0 ]; then
  echo "Ready. Now send one smoke-test prompt: run 'claude', type /model opus, then ask: 'What does this app do? Answer in three lines.'"
fi
exit $status
