"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Measurement import Measurement


@dataclass
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that
      a positive value measured at the Terminal means power is flowing into the related
      PowerSystemResource.
    AnalogValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    positiveFlowIn: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # AnalogValues : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # LimitSets : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Analog\n"
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
            "positiveFlowIn": [
                self.profiles.OP.value,
            ],
            "AnalogValues": [
                self.profiles.OP.value,
            ],
            "LimitSets": [
                self.profiles.OP.value,
            ],
        }
