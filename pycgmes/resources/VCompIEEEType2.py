"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass(config=DataclassConfig)
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    tr: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # GenICompensationForGenJ : list = field(default_factory=list)  # Type M:2..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=VCompIEEEType2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.DY.value,
            ],
            # Attributes
            "tr": [
                Profile.DY.value,
            ],
            "GenICompensationForGenJ": [
                Profile.DY.value,
            ],
        }
