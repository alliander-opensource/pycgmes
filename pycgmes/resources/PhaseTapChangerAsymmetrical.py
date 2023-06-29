"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


@dataclass(config=DataclassConfig)
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

    windingConnectionAngle: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
