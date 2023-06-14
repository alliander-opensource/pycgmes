"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker
      position.

    DiscreteValues: The values connected to this measurement.
    ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name.
    """

    # *Association not used*
    # DiscreteValues : list = field(default_factory=list)  # Type M:0..n in CIM
    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Discrete"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "DiscreteValues": [
                Profile.OP.value,
            ],
            "ValueAliasSet": [
                Profile.OP.value,
            ],
        }
