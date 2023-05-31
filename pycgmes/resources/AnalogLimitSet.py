"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .LimitSet import LimitSet


@dataclass
class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

    Measurements: The Measurements using the LimitSet.
    Limits: The limit values used for supervision of Measurements.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Measurements: list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # Limits : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AnalogLimitSet\n"
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
            "Measurements": [
                self.profiles.OP.value,
            ],
            "Limits": [
                self.profiles.OP.value,
            ],
        }
