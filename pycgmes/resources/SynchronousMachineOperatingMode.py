"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SynchronousMachineOperatingMode(str, Enum):
    """
    Synchronous machine operating mode.
    """

    generator = "generator"  # Operating as generator.  # noqa: E501, E741, RUF003
    condenser = "condenser"  # Operating as condenser.  # noqa: E501, E741, RUF003
    motor = "motor"  # Operating as motor.  # noqa: E501, E741, RUF003
