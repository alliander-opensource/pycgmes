"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class HydroTurbineKind(str, Enum):
    """
    Type of turbine.  # noqa: E501
    """

    francis = "francis"  # Francis.  # noqa: E501
    pelton = "pelton"  # Pelton.  # noqa: E501
    kaplan = "kaplan"  # Kaplan.  # noqa: E501
