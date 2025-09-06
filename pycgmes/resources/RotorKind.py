"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class RotorKind(str, Enum):
    """
    Type of rotor on physical machine.
    """

    roundRotor = "roundRotor"  # Round rotor type of synchronous machine.  # noqa: E501
    salientPole = "salientPole"  # Salient pole type of synchronous machine.  # noqa: E501
