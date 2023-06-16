"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that
      a positive value measured at the Terminal means power is flowing into the related
      PowerSystemResource.
    AnalogValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    """

    positiveFlowIn: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # AnalogValues : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # LimitSets : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Analog"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "positiveFlowIn": [
                Profile.OP.value,
            ],
            "AnalogValues": [
                Profile.OP.value,
            ],
            "LimitSets": [
                Profile.OP.value,
            ],
        }
