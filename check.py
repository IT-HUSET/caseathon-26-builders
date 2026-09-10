"""Environment check. Run with: uv run check.py

Works on macOS, Linux, WSL and native Windows (PowerShell or CMD).
"""

import shutil
import subprocess
import sys

failures = 0


def ok(msg):
    print(f"  ok    {msg}")


def fail(msg):
    global failures
    failures += 1
    print(f"  FAIL  {msg}")


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return r.returncode, (r.stdout + r.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, str(e)


print("Caseathon Builders warm-up: environment check")

v = sys.version_info
if v >= (3, 11):
    ok(f"Python {v.major}.{v.minor}.{v.micro}")
else:
    fail(f"Python {v.major}.{v.minor} is too old; uv should have picked 3.11+ (try: uv python install 3.13)")

claude = shutil.which("claude")
if claude:
    code, out = run([claude, "--version"])
    ok(f"claude {out.splitlines()[0] if out else ''}") if code == 0 else fail("claude found but --version failed")
    code, _ = run([claude, "auth", "status"])
    ok("claude logged in") if code == 0 else fail("not logged in: run 'claude' and follow the browser login")
else:
    fail("claude not on PATH. macOS/Linux/WSL: curl -fsSL https://claude.ai/install.sh | bash "
         "| Windows PowerShell: irm https://claude.ai/install.ps1 | iex  (then open a new terminal)")

code, out = run([sys.executable, "-m", "pytest", "-q"])
if code == 0:
    ok(f"tests pass ({out.splitlines()[-1] if out else ''})")
else:
    fail("tests fail: run 'uv run pytest -q' to see why")

if failures == 0:
    print("Ready. Start 'claude' in this directory, type /model opus, then ask: "
          "'What does this app do? Answer in three lines.'")
else:
    print(f"{failures} thing(s) to fix above. Stuck? Open the repo in GitHub Codespaces instead (see README).")
sys.exit(1 if failures else 0)
