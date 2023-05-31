"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PhaseTapChanger import PhaseTapChanger


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    stepPhaseShiftIncrement: float = 0.0  # Type #AngleDegrees in CIM
    xMax: float = 0.0  # Type #Reactance in CIM
    xMin: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerLinear\n"
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
            "stepPhaseShiftIncrement": [
                self.profiles.EQ.value,
            ],
            "xMax": [
                self.profiles.EQ.value,
            ],
            "xMin": [
                self.profiles.EQ.value,
            ],
        }
