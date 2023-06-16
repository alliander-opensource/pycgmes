"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChangerLinear(PhaseTapChanger):
    """
    Describes a tap changer with a linear relation between the tap step and the phase angle difference across the
      transformer. This is a mathematical model that is an approximation of a real phase tap changer. The phase
      angle is computed as stepPhaseShiftIncrement times the tap position. The voltage magnitude of both sides is
      the same.

    stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive angle variation from
      the Terminal at the  PowerTransformerEnd,  where the TapChanger is located, into the
      transformer. The actual phase shift increment might be more accurately computed from
      the symmetrical or asymmetrical models or a tap step table lookup if those are
      available.
    xMax: The reactance depends on the tap position according to a `u` shaped curve. The maximum reactance (xMax)
      appears at the low and high tap positions. Depending on the `u` curve the attribute can be either higher
      or lower than PowerTransformerEnd.x.
    xMin: The reactance depends on the tap position according to a `u` shaped curve. The minimum reactance (xMin)
      appears at the mid tap position.  PowerTransformerEnd.x shall be consistent with
      PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency,
      PowerTransformerEnd.x shall be used.
    """

    stepPhaseShiftIncrement: float = 0.0  # Type #AngleDegrees in CIM
    xMax: float = 0.0  # Type #Reactance in CIM
    xMin: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerLinear"]
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
            "stepPhaseShiftIncrement": [
                Profile.EQ.value,
            ],
            "xMax": [
                Profile.EQ.value,
            ],
            "xMin": [
                Profile.EQ.value,
            ],
        }
