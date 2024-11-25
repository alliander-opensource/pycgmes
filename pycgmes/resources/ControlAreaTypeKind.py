"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ControlAreaTypeKind(str, Enum):
    """
    The type of control area.  # noqa: E501
    """

    AGC = "AGC"  # Used for automatic generation control.  # noqa: E501
    Forecast = "Forecast"  # Used for load forecast.  # noqa: E501
    Interchange = "Interchange"  # Used for interchange specification or control.  # noqa: E501
