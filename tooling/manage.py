"""
Python-native workspace management commands.

Usage examples:
    python tooling/manage.py bootstrap
    python tooling/manage.py install
    python tooling/manage.py gateway run
    python tooling/manage.py gateway test
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SERVICE_ROOT = REPO_ROOT / "services" / "gateway"


def run_command(command: list[str], *, cwd: Path | None = None) -> int:
    """Run a subprocess command, streaming output."""
    process = subprocess.run(command, cwd=cwd or REPO_ROOT)
    return process.returncode


def ensure_poetry() -> None:
    """Install Poetry via pip if it is not already available."""
    if shutil.which("poetry"):
        return

    print("Poetry not found. Installing with pip ...")
    result = run_command([sys.executable, "-m", "pip", "install", "--user", "poetry"])
    if result != 0:
        sys.exit(result)
    print("Poetry installed. You may need to add the user scripts directory to PATH.")


def cmd_bootstrap(_: argparse.Namespace) -> None:
    """Install Poetry (if needed) and install workspace dependencies."""
    ensure_poetry()
    run_command(["poetry", "install", "--with", "dev"])


def cmd_install(_: argparse.Namespace) -> None:
    """Install workspace dependencies."""
    ensure_poetry()
    run_command(["poetry", "install", "--with", "dev"])


def cmd_gateway_run(args: argparse.Namespace) -> None:
    """Run the gateway service via Poetry while staying at repo root."""
    ensure_poetry()
    run_command(["poetry", "run", "-C", str(SERVICE_ROOT), "gateway"])


def cmd_gateway_test(args: argparse.Namespace) -> None:
    """Execute the gateway service tests."""
    ensure_poetry()
    run_command(["poetry", "run", "-C", str(SERVICE_ROOT), "pytest"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Workspace management CLI.")
    subparsers = parser.add_subparsers(dest="command")

    bootstrap_parser = subparsers.add_parser("bootstrap", help="Install Poetry and project deps.")
    bootstrap_parser.set_defaults(func=cmd_bootstrap)

    install_parser = subparsers.add_parser("install", help="Install project dependencies.")
    install_parser.set_defaults(func=cmd_install)

    gateway_parser = subparsers.add_parser("gateway", help="Gateway service commands.")
    gateway_subparsers = gateway_parser.add_subparsers(dest="gateway_command")

    gateway_run_parser = gateway_subparsers.add_parser("run", help="Run the gateway service.")
    gateway_run_parser.set_defaults(func=cmd_gateway_run)

    gateway_test_parser = gateway_subparsers.add_parser("test", help="Run gateway tests.")
    gateway_test_parser.set_defaults(func=cmd_gateway_test)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()

