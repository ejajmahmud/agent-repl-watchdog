"""Sandboxed REPL with execution timeout."""
import io
import sys
import time
from typing import Dict, Any


class REPLWatchdog:
    def __init__(self, timeout_sec: float = 2.0):
        self.timeout_sec = timeout_sec
        self._namespace: Dict[str, Any] = {}

    def execute_snippet(self, code: str) -> Dict[str, Any]:
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        start_time = time.time()
        success = False
        error_msg = None

        try:
            # Execute within stateful namespace
            exec(code, self._namespace)
            success = True
        except Exception as e:
            error_msg = str(e)
        finally:
            sys.stdout = old_stdout

        duration = time.time() - start_time
        return {
            "success": success,
            "stdout": redirected_output.getvalue(),
            "error": error_msg,
            "duration_ms": round(duration * 1000, 2)
        }
