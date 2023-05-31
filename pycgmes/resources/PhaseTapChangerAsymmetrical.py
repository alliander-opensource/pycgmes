"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


@dataclass
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """
    Describes the tap model for an asymmetrical phase shifting transformer in which the difference voltage vector adds
      to the in-phase winding. The out-of-phase winding is the transformer end where the tap changer is located.
      The angle between the in-phase and out-of-phase windings is named the winding connection angle. The phase
      shift depends on both the difference voltage magnitude and the winding connection angle.

    windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating
      phase shift. The out-of-phase winding produces what is known as the difference
      voltage.  Setting this angle to 90 degrees is not the same as a symmetrical
      transformer. The attribute can only be multiples of 30 degrees.  The allowed range is
      -150 degrees to 150 degrees excluding 0.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    windingConnectionAngle: float = 0.0  # Type #AngleDegrees in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerAsymmetrical\n"
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
            "windingConnectionAngle": [
                self.profiles.EQ.value,
            ],
        }
