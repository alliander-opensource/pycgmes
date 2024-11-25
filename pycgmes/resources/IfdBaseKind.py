"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class IfdBaseKind(str, Enum):
    """
    Excitation base system mode.  # noqa: E501
    """

    ifag = "ifag"  # Air gap line mode.  # noqa: E501
    ifnl = "ifnl"  # No load system with saturation mode.  # noqa: E501
    iffl = "iffl"  # Full load system mode.  # noqa: E501
