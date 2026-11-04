"""Tests for agent-repl-watchdog."""
import unittest
from agent_repl_watchdog.repl import REPLWatchdog


class TestREPLWatchdog(unittest.TestCase):
    def setUp(self):
        self.repl = REPLWatchdog()

    def test_state_persistence_across_runs(self):
        r1 = self.repl.execute_snippet("x = 100")
        self.assertTrue(r1["success"])
        r2 = self.repl.execute_snippet("print(x + 23)")
        self.assertTrue(r2["success"])
        self.assertEqual(r2["stdout"].strip(), "123")


if __name__ == "__main__":
    unittest.main()
