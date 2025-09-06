"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class HydroPlantStorageKind(str, Enum):
    """
    The type of hydro power plant.
    """

    runOfRiver = "runOfRiver"  # Run of river.  # noqa: E501
    pumpedStorage = "pumpedStorage"  # Pumped storage.  # noqa: E501
    storage = "storage"  # Storage.  # noqa: E501
