"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class HydroTurbineKind(str, Enum):
    """
    Type of turbine.
    """

    francis = "francis"  # Francis.  # noqa: E501, E741, RUF003
    pelton = "pelton"  # Pelton.  # noqa: E501, E741, RUF003
    kaplan = "kaplan"  # Kaplan.  # noqa: E501, E741, RUF003
