"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindGenUnitKind(str, Enum):
    """
    Kind of wind generating unit.  # noqa: E501
    """

    offshore = "offshore"  # The wind generating unit is located offshore.  # noqa: E501
    onshore = "onshore"  # The wind generating unit is located onshore.  # noqa: E501
