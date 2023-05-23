"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Measurement import Measurement


@dataclass
class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker
      position.

    DiscreteValues: The values connected to this measurement.
    ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # DiscreteValues : list = field(default_factory=list)  # Type M:0..n in CIM
    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Discrete\n"
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
            "DiscreteValues": [
                self.profiles.OP.value,
            ],
            "ValueAliasSet": [
                self.profiles.OP.value,
            ],
        }
