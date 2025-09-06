"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class DroopSignalFeedbackKind(str, Enum):
    """
    Governor droop signal feedback source.
    """

    electricalPower = "electricalPower"  # Electrical power feedback (connection indicated as 1 in the block diagrams of models, e.g. GovCT1, GovCT2).  # noqa: E501
    none = "none"  # No droop signal feedback, is isochronous governor.  # noqa: E501
    fuelValveStroke = "fuelValveStroke"  # Fuel valve stroke feedback (true stroke) (connection indicated as 2 in the block diagrams of model, e.g. GovCT1, GovCT2).  # noqa: E501
    governorOutput = "governorOutput"  # Governor output feedback (requested stroke) (connection indicated as 3 in the block diagrams of models, e.g. GovCT1, GovCT2).  # noqa: E501
