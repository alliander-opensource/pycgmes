"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
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

    windingConnectionAngle: float = 0.0  # Type #AngleDegrees in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerAsymmetrical"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "windingConnectionAngle": [
                Profile.EQ.value,
            ],
        }
