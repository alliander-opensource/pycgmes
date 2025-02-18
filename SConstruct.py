# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import os
import subprocess  # nosec
import sys
from typing import Mapping

from SCons.Script import COMMAND_LINE_TARGETS

_CHECK_ONLY = "check" in COMMAND_LINE_TARGETS
_SUBJECT = "pycgmes"
_TEST_SUBJECT = "tests"
_RESOURCES = "pycgmes/resources"

# Remember if a target has been found, to warn if not.
_target_found: bool = False


def _exec(command: str, env: Mapping | None = None) -> int:
    global _target_found
    _target_found = True

    print(f">>> {command}")

    exit_code = subprocess.call(command, shell=True, env=env)
    if exit_code != 0:
        print(f"Exiting with {exit_code}")
        sys.exit(exit_code)
    return exit_code


# Generic targets, which will extend the COMMAND_LINE_TARGETS array.
# Makes sure that generic commands run the tests last, as they are the most likely to fail.
if "all" in COMMAND_LINE_TARGETS:
    COMMAND_LINE_TARGETS += ["quality", "format"]


if "quality" in COMMAND_LINE_TARGETS:
    COMMAND_LINE_TARGETS += ["lint", "lock", "type", "test", "coverage", "license"]

# Formatting targets, which might change files. Let's run them *before* the linters and friends.
# This is why ruff is the first of the quality target, as it fixes things as well.
if "format" in COMMAND_LINE_TARGETS:
    cmd = f"ruff format SConstruct.py {_SUBJECT} {_TEST_SUBJECT} examples --exclude {_RESOURCES}"
    if _CHECK_ONLY:
        cmd += " --diff"
    _exec(cmd)

# Quality target.
if "ruff" in COMMAND_LINE_TARGETS or "lint" in COMMAND_LINE_TARGETS:
    # Replaces isort, autoflake and probably pylint eventually.
    cmd = f"ruff check {_SUBJECT} {_TEST_SUBJECT} --exclude {_RESOURCES}"
    if _CHECK_ONLY:
        cmd += " --no-fix"
    else:
        cmd += " --fix"
    _exec(cmd, env=os.environ)
    # Don't change generated files!
    cmd = f"ruff check {_RESOURCES} --no-fix --ignore I001,F401,N815,N999,RUF100,W291,W293"
    _exec(cmd, env=os.environ)


if "lock" in COMMAND_LINE_TARGETS:
    _exec("poetry check --lock")


if "type" in COMMAND_LINE_TARGETS or "pyright" in COMMAND_LINE_TARGETS:
    _exec("pyright", env=os.environ)
    _target_found = True


if "test" in COMMAND_LINE_TARGETS or "tests" in COMMAND_LINE_TARGETS:
    # Running tests via coverage to only report when asking for coverage
    _exec(f"coverage run --module pytest {_TEST_SUBJECT}")

if "coverage" in COMMAND_LINE_TARGETS:
    if "test" in COMMAND_LINE_TARGETS or "tests" in COMMAND_LINE_TARGETS:
        print("Reusing test output from the tests just run.")
    else:
        print("Need to run the tests first.")
        _exec(f"coverage run --module pytest {_TEST_SUBJECT}")

    _exec("coverage report --show-missing")

if "license" in COMMAND_LINE_TARGETS or "licence" in COMMAND_LINE_TARGETS:
    # To fix:
    # reuse annotate --copyright="Alliander" --license=Apache-2.0 --recursive pycgmes/{resources,utils}
    _exec("reuse lint")

if not _target_found:
    print(f"No valid target in {COMMAND_LINE_TARGETS}. Look at SConstruct.py for what is allowed.")

sys.exit(0)
