# We follow the CIM naming convention, not python.
# pylint: disable=invalid-name

"""
Parent element of all CGMES elements
"""
import importlib
from dataclasses import fields
from enum import Enum
from functools import cache, cached_property
from typing import Any

# Drop in dataclass replacement, allowing easier json dump and validation in the future.
from pydantic.dataclasses import dataclass


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


class DataclassConfig:  # pylint: disable=too-few-public-methods

    """
    Used to configure pydantic dataclasses.

    See doc at
    https://docs.pydantic.dev/latest/usage/model_config/#options
    """

    # By default with pydantic extra arguments given to a dataclass are silently ignored.
    # This matches the default behaviour by failing noisily.
    extra = "forbid"


# Default namespaces used by CGMES.
NAMESPACES = {
    "cim": "http://iec.ch/TC57/2013/CIM-schema-cim16#",
    "entsoe": "http://entsoe.eu/CIM/SchemaExtension/3/1#",
    "md": "http://iec.ch/TC57/61970-552/ModelDescription/1#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}


@dataclass(config=DataclassConfig)
class Base:
    """
    Base Class for CIM.
    """

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        raise NotImplementedError("Method not implemented because not relevant in Base.")

    @staticmethod
    def parse_json_as(attrs: dict[str, Any]) -> "Base":
        """
        Given a json, returns the original object.
        """
        subclass: str = attrs["__class__"]

        # We want all attributes *except* __class__, and I do not want to modify
        # the dict in params with del() or .pop()
        data_attrs = {k: v for k, v in attrs.items() if k != "__class__"}

        mod = importlib.import_module(f".{subclass}", package="pycgmes.resources")
        # Works because the module and the class have the same name.
        return getattr(mod, subclass)(**data_attrs)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns the class as dict, with:
        - only public attributes
        - adding __class__ with the classname (for deserialisation)

        """
        attrs = {f.name: getattr(self, f.name) for f in fields(self)}
        attrs["__class__"] = self.__class__.__name__
        return attrs
