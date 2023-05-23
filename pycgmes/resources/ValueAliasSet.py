"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ValueAliasSet\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.OP.value,
            ],
            # Attributes
            "Commands": [
                self.profiles.OP.value,
            ],
            "Discretes": [
                self.profiles.OP.value,
            ],
            "RaiseLowerCommands": [
                self.profiles.OP.value,
            ],
            "Values": [
                self.profiles.OP.value,
            ],
        }
