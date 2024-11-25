"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class VsQpccControlKind(str, Enum):
    """
    Kind of reactive power control at point of common coupling for a voltage source converter.  # noqa: E501
    """

    reactivePcc = "reactivePcc"  # Control is reactive power at point of common coupling. Target is provided by VsConverter.targetQpcc.  # noqa: E501
    voltagePcc = "voltagePcc"  # Control is voltage at point of common coupling. Target is provided by VsConverter.targetUpcc.  # noqa: E501
    powerFactorPcc = "powerFactorPcc"  # Control is power factor at point of common coupling. Target is provided by VsConverter.targetPowerFactorPcc.  # noqa: E501
    pulseWidthModulation = "pulseWidthModulation"  # No explicit control. Pulse-modulation factor is directly set in magnitude (VsConverter.targetPWMfactor) and phase (VsConverter.targetPhasePcc).  # noqa: E501
