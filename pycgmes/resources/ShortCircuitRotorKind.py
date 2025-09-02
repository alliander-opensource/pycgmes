"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ShortCircuitRotorKind(str, Enum):
    """
    Type of rotor, used by short circuit applications.
    """

    salientPole1 = "salientPole1"  # Salient pole 1 in IEC 60909.  # noqa: E501, E741, RUF003
    salientPole2 = "salientPole2"  # Salient pole 2 in IEC 60909.  # noqa: E501, E741, RUF003
    turboSeries1 = "turboSeries1"  # Turbo Series 1 in IEC 60909.  # noqa: E501, E741, RUF003
    turboSeries2 = "turboSeries2"  # Turbo series 2 in IEC 60909.  # noqa: E501, E741, RUF003
