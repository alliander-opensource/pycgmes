# We follow the CIM naming convention, not python.
# pylint: disable=invalid-name

"""
Parent element of all CGMES elements
"""
from dataclasses import dataclass
from enum import Enum
from functools import cache, cached_property
from typing import Type


class Profile(Enum):
    """
    Enum containing all CGMES profiles and their export priority.
    todo: enums are ordered, so we can have a short->long enum withuot explicit prio
    todo: default mRID based on name, id, classname
    todo: add an alliander id?
    """

    EQ = 0
    SSH = 1
    TP = 2
    SV = 3
    DY = 4
    OP = 5
    SC = 6
    GL = 7
    # DI = 8 # Initially mentioned but does not seem used?
    DL = 9
    TPBD = 10
    EQBD = 11

    @cached_property
    def long_name(self):
        """From the short name, return the long name of the profile."""
        return self._short_to_long()[self.name]

    @classmethod
    def from_long_name(cls, long_name):
        """From the long name, return the short name of the profile."""
        return cls[cls._long_to_short()[long_name]]

    @classmethod
    @cache
    def _short_to_long(cls) -> dict[str, str]:
        """Returns the long name from a short name"""
        return {
            "DL": "DiagramLayout",
            # "DI": "DiagramLayout",
            "DY": "Dynamics",
            "EQ": "Equipment",
            "EQBD": "EquipmentBoundary",  # Not too sure about that one
            "GL": "GeographicalLocation",
            "OP": "Operation",
            "SC": "ShortCircuit",
            "SV": "StateVariables",
            "SSH": "SteadyStateHypothesis",
            "TP": "Topology",
            "TPBD": "TopologyBoundary",  # Not too sure about that one
        }

    @classmethod
    @cache
    def _long_to_short(cls) -> dict[str, str]:
        """Returns the short name from a long name"""
        return {_long: _short for _short, _long in cls._short_to_long().items()}


@dataclass
class Base:
    """
    Base Class for CIM.
    """

    @cached_property
    def profiles(self) -> Type[Profile]:
        """Returns the profile Enum."""
        return Profile
