"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SynchronousMachineKind(str, Enum):
    """
    Synchronous machine type.
    """

    generator = "generator"  # Indicates the synchronous machine can operate as a generator.  # noqa: E501, E741, RUF003
    condenser = "condenser"  # Indicates the synchronous machine can operate as a condenser.  # noqa: E501, E741, RUF003
    generatorOrCondenser = "generatorOrCondenser"  # Indicates the synchronous machine can operate as a generator or as a condenser.  # noqa: E501, E741, RUF003
    motor = "motor"  # Indicates the synchronous machine can operate as a motor.  # noqa: E501, E741, RUF003
    generatorOrMotor = "generatorOrMotor"  # Indicates the synchronous machine can operate as a generator or as a motor.  # noqa: E501, E741, RUF003
    motorOrCondenser = "motorOrCondenser"  # Indicates the synchronous machine can operate as a motor or as a condenser.  # noqa: E501, E741, RUF003
    generatorOrCondenserOrMotor = "generatorOrCondenserOrMotor"  # Indicates the synchronous machine can operate as a generator or as a condenser or as a motor.  # noqa: E501, E741, RUF003
