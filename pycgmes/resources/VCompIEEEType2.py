"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    tr: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # GenICompensationForGenJ : list = field(default_factory=list)  # Type M:2..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VCompIEEEType2\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "tr": [
                self.profiles.DY.value,
            ],
            "GenICompensationForGenJ": [
                self.profiles.DY.value,
            ],
        }
