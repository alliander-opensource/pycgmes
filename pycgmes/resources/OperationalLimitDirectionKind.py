"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class OperationalLimitDirectionKind(str, Enum):
    """
    The direction attribute describes the side of  a limit that is a violation.
    """

    high = "high"  # High means that a monitored value above the limit value is a violation.   If applied to a terminal flow, the positive direction is into the terminal.  # noqa: E501
    low = "low"  # Low means a monitored value below the limit is a violation.  If applied to a terminal flow, the positive direction is into the terminal.  # noqa: E501
    absoluteValue = "absoluteValue"  # An absoluteValue limit means that a monitored absolute value above the limit value is a violation.  # noqa: E501
