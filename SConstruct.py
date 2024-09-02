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
    cmd = f"ruff format SConstruct.py {_SUBJECT} {_TEST_SUBJECT} examples"
    if _CHECK_ONLY:
        cmd += " --diff"
    _exec(cmd)

# Quality target.
if "ruff" in COMMAND_LINE_TARGETS or "lint" in COMMAND_LINE_TARGETS:
    # Replaces isort, autoflake and probably pylint eventually.
    for param in ["", "--extend-select RUF100"]:
        # RUF100 means: remove #noqa when not relevant.
        # A lot are adding during generation because due to comments, some lines can be too long. They do not all
        # end up being too long, so let's clean up the not relevant one.
        cmd = f"ruff check {_SUBJECT} {param}"
        # Tries to fix what it can, forget about the rest.
        cmd_test = f"ruff check {_TEST_SUBJECT}  --fix-only"
        if _CHECK_ONLY:
            cmd += " --no-fix"
            cmd_test += " --no-fix"
        else:
            cmd += " --fix"
        _exec(cmd, env=os.environ)
        _exec(cmd_test, env=os.environ)


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
