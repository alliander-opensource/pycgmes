"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class HydroEnergyConversionKind(str, Enum):
    """
    Specifies the capability of the hydro generating unit to convert energy as a generator or pump.
    """

    generator = "generator"  # Able to generate power, but not able to pump water for energy storage.  # noqa: E501
    pumpAndGenerator = "pumpAndGenerator"  # Able to both generate power and pump water for energy storage.  # noqa: E501
