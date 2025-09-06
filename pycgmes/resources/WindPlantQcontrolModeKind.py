"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindPlantQcontrolModeKind(str, Enum):
    """
    Reactive power/voltage controller mode.
    """

    reactivePower = "reactivePower"  # Reactive power reference.  # noqa: E501
    powerFactor = "powerFactor"  # Power factor reference.  # noqa: E501
    uqStatic = "uqStatic"  # UQ static.  # noqa: E501
    voltageControl = "voltageControl"  # Voltage control.  # noqa: E501
