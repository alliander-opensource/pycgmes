"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SVCControlMode(str, Enum):
    """
    Static VAr Compensator control mode.
    """

    reactivePower = "reactivePower"  # Reactive power control.  # noqa: E501, E741, RUF003
    voltage = "voltage"  # Voltage control.  # noqa: E501, E741, RUF003
