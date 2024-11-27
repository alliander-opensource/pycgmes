"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class IfdBaseKind(str, Enum):
    """
    Excitation base system mode.
    """

    ifag = "ifag"  # Air gap line mode.  # noqa: E501, E741, RUF003
    ifnl = "ifnl"  # No load system with saturation mode.  # noqa: E501, E741, RUF003
    iffl = "iffl"  # Full load system mode.  # noqa: E501, E741, RUF003
