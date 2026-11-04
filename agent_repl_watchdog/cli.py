"""CLI for agent-repl-watchdog."""
import sys
import argparse
from .repl import REPLWatchdog


def main():
    parser = argparse.ArgumentParser(description="Agent REPL Watchdog")
    parser.add_argument("--code", default="print(40 + 2)", help="Code to evaluate")
    args = parser.parse_args()

    w = REPLWatchdog()
    res = w.execute_snippet(args.code)
    print(f"Result: {res}")
    sys.exit(0)


if __name__ == "__main__":
    main()
