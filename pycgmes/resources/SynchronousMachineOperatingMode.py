"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SynchronousMachineOperatingMode(str, Enum):
    """
    Synchronous machine operating mode.  # noqa: E501
    """

    generator = "generator"  # Operating as generator.  # noqa: E501
    condenser = "condenser"  # Operating as condenser.  # noqa: E501
    motor = "motor"  # Operating as motor.  # noqa: E501
