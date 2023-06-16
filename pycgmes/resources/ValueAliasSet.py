"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ValueAliasSet(IdentifiedObject):
    """
    Describes the translation of a set of values into a name and is intendend to facilitate custom translations. Each
      ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open,
      Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g.
      0->"Invalid", 1->"Open", 2->"Closed", 3->"Intermediate". Each ValueToAlias member in ValueAliasSet.Value
      describe a mapping for one particular value to a name.

    Commands: The Commands using the set for translation.
    Discretes: The Measurements using the set for translation.
    RaiseLowerCommands: The Commands using the set for translation.
    Values: The ValueToAlias mappings included in the set.
    """

    # *Association not used*
    # Commands : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # Discretes : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # RaiseLowerCommands : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # Values : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ValueAliasSet"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.OP.value,
            ],
            # Attributes
            "Commands": [
                Profile.OP.value,
            ],
            "Discretes": [
                Profile.OP.value,
            ],
            "RaiseLowerCommands": [
                Profile.OP.value,
            ],
            "Values": [
                Profile.OP.value,
            ],
        }
