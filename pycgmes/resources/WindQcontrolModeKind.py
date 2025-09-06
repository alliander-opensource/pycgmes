"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindQcontrolModeKind(str, Enum):
    """
    General wind turbine Q control modes MqG.
    """

    voltage = "voltage"  # Voltage control (<i>M</i><i><sub>qG</sub></i> equals 0).  # noqa: E501
    reactivePower = "reactivePower"  # Reactive power control (<i>M</i><i><sub>qG</sub></i> equals 1).  # noqa: E501
    openLoopReactivePower = "openLoopReactivePower"  # Open loop reactive power control (only used with closed loop at plant level) (<i>M</i><i><sub>qG</sub></i><sub> </sub>equals 2).  # noqa: E501
    powerFactor = "powerFactor"  # Power factor control (<i>M</i><i><sub>qG</sub></i><sub> </sub>equals 3).  # noqa: E501
    openLooppowerFactor = "openLooppowerFactor"  # Open loop power factor control (<i>M</i><i><sub>qG</sub></i><sub> </sub>equals 4).  # noqa: E501
