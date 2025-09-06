"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class CsPpccControlKind(str, Enum):
    """
    Active power control modes for HVDC line operating as Current Source Converter.
    """

    activePower = "activePower"  # Control is active power control at AC side, at point of common coupling. Target is provided by ACDCConverter.targetPpcc.  # noqa: E501
    dcVoltage = "dcVoltage"  # Control is DC voltage  with target value provided by ACDCConverter.targetUdc.  # noqa: E501
    dcCurrent = "dcCurrent"  # Control is DC current  with target value provided by CsConverter.targetIdc.  # noqa: E501
