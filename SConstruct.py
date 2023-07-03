import os
import subprocess  # nosec
import sys

from SCons.Script import COMMAND_LINE_TARGETS

_CHECK_ONLY = "check" in COMMAND_LINE_TARGETS
_SUBJECT = "pycgmes shacl"
_TEST_SUBJECT = "tests"
# Full path to an environment bin directory.
# Not needed if an environment is activated or not used (eg. Jenkins).
_BIN = os.environ.get("PY_VENV", "")

# Remember if a target has been found, to warn if not.
_target_found: bool = False


def _exec(command: str, absolute: bool = False) -> int:
    global _target_found
    _target_found = True
    if not absolute:
        command = f"{_BIN}{command}"

    print(f">>> {command}")

    exit_code = subprocess.call(command, shell=True)
    if exit_code != 0:
        print(f"Exiting with {exit_code}")
        sys.exit(exit_code)
    return exit_code


# Generic targets, which will extend the COMMAND_LINE_TARGETS array.
# Makes sure that generic commands run the tests last, as they are the most likely to fail.
if "all" in COMMAND_LINE_TARGETS:
    COMMAND_LINE_TARGETS += ["quality", "format"]

# Ruff fixes and lints, hence its appearance twice.
if "format" in COMMAND_LINE_TARGETS:
    COMMAND_LINE_TARGETS += ["black", "ruff"]

if "quality" in COMMAND_LINE_TARGETS:
    COMMAND_LINE_TARGETS += ["ruff", "lock", "pylint", "mypy", "bandit", "coverage"]

# Formatting targets, which might change files. Let's run them *before* the linters and friends.
# This is why ruff is the first of the quality target, as it fixes things as well.
if "black" in COMMAND_LINE_TARGETS:
    cmd = f"black  SConstruct.py {_SUBJECT} {_TEST_SUBJECT} "
    if _CHECK_ONLY:
        cmd += " --check"
    _exec(cmd)

# Quality target.
if "ruff" in COMMAND_LINE_TARGETS or "lint" in COMMAND_LINE_TARGETS:
    # Replaces isort, autoflake and probably pylint eventually.
    for param in ["", "--extend-select RUF100"]:
        # RUF100 means: remove #noqa when not relevant.
        # A lot are adding during generation because due to comments, some lines can be too long. They do not all
        # end up being too long, so let's clean up the not relevant one.
        cmd = f"ruff {_SUBJECT} {param}"
        if _CHECK_ONLY:
            cmd += " --no-fix"
        else:
            cmd += " --fix"
        _exec(cmd)


if "lock" in COMMAND_LINE_TARGETS:
    _exec("poetry lock --check")

if "pylint" in COMMAND_LINE_TARGETS or "lint" in COMMAND_LINE_TARGETS:
    _exec(f"pylint --rcfile=pyproject.toml {_SUBJECT}")


if "mypy" in COMMAND_LINE_TARGETS:
    # https://mypy.readthedocs.io/en/stable/running_mypy.html#library-stubs-not-installed
    _exec(f"mypy {_SUBJECT}")
    _target_found = True

if "bandit" in COMMAND_LINE_TARGETS:
    # B101: assert_used
    _exec(f"bandit --recursive --configfile pyproject.toml .")

if "test" in COMMAND_LINE_TARGETS or "tests" in COMMAND_LINE_TARGETS:
    _exec(f"python -m pytest  {_TEST_SUBJECT}")

if "coverage" in COMMAND_LINE_TARGETS:
    _exec(f"coverage run -m pytest {_TEST_SUBJECT}")
    _exec("coverage report -m")

if not _target_found:
    print(f"No valid target in {COMMAND_LINE_TARGETS}. Look at SConstruct.py for what is allowed.")

sys.exit(0)
