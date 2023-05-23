"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ShuntCompensator import ShuntCompensator


@dataclass
class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of
      the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a
      NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber.

    NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # NonlinearShuntCompensatorPoints : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=NonlinearShuntCompensator\n"
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
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "NonlinearShuntCompensatorPoints": [
                self.profiles.EQ.value,
            ],
        }
