"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


@dataclass
class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """
    Describes a symmetrical phase shifting transformer tap model in which the voltage magnitude of both sides is the
      same. The difference voltage magnitude is the base in an equal-sided triangle where the sides corresponds to
      the primary and secondary voltages. The phase angle difference corresponds to the top angle and can be
      expressed as twice the arctangent of half the total difference voltage.

    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerSymmetrical\n"
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
        }
