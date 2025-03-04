"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class AsynchronousMachineKind(str, Enum):
    """
    Kind of Asynchronous Machine.
    """

    generator = "generator"  # The Asynchronous Machine is a generator.  # noqa: E501, E741, RUF003
    motor = "motor"  # The Asynchronous Machine is a motor.  # noqa: E501, E741, RUF003
