"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class CsOperatingModeKind(str, Enum):
    """
    Operating mode for HVDC line operating as Current Source Converter.
    """

    inverter = "inverter"  # Operating as inverter, which is the power receiving end.  # noqa: E501
    rectifier = "rectifier"  # Operating as rectifier, which is the power sending end.  # noqa: E501
