import json
import subprocess
from typing import Any, Dict, List


def run_xurl(cmd: List[str], verbose_if_failed: bool = False) -> Dict[str, Any]:
    """
    Run `xurl` and return its JSON stdout as a Python dict.
    Currently extremely simple without any retry logic.
    """
    try:
        completed = subprocess.run(cmd, check=True, text=True, capture_output=True)
        try:
            return json.loads(completed.stdout)
        except json.JSONDecodeError:
            print(f"[xurl] failed to parse JSON from stdout:")
            print("── stdout ──")
            print(completed.stdout)
            print("── stderr ──")
            print(completed.stderr)
            raise
    except subprocess.CalledProcessError as exc:
        print(f"[xurl] Command failed: {' '.join(cmd)}")
        print(f"Exit code: {exc.returncode}")
        print("── stdout ──")
        print(exc.stdout, end="", flush=True)
        print("── stderr ──")
        print(exc.stderr, end="", flush=True)
        raise
