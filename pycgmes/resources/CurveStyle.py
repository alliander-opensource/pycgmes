"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class CurveStyle(str, Enum):
    """
    Style or shape of curve.
    """

    constantYValue = "constantYValue"  # The Y-axis values are assumed constant until the next curve point and prior to the first curve point.  # noqa: E501, E741, RUF003
    straightLineYValues = "straightLineYValues"  # The Y-axis values are assumed to be a straight line between values.  Also known as linear interpolation.  # noqa: E501, E741, RUF003
