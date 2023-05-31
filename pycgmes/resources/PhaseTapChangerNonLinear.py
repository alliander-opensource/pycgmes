"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PhaseTapChanger import PhaseTapChanger


@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """
    The non-linear phase tap changer describes the non-linear behaviour of a phase tap changer. This is a base class for
      the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in IEC
      61970-301.

    voltageStepIncrement: The voltage step increment on the out of phase winding (the PowerTransformerEnd where the
      TapChanger is located) specified in percent of rated voltage of the PowerTransformerEnd.
      A positive value means a positive voltage variation from the Terminal at the
      PowerTransformerEnd, where the TapChanger is located, into the transformer. When the
      increment is negative, the voltage decreases when the tap step increases.
    xMax: The reactance depends on the tap position according to a `u` shaped curve. The maximum reactance (xMax)
      appears at the low and high tap positions. Depending on the `u` curve the attribute can be either higher
      or lower than PowerTransformerEnd.x.
    xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear
      at the mid tap position.   PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and
      PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    voltageStepIncrement: float = 0.0  # Type #PerCent in CIM
    xMax: float = 0.0  # Type #Reactance in CIM
    xMin: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerNonLinear\n"
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
            "voltageStepIncrement": [
                self.profiles.EQ.value,
            ],
            "xMax": [
                self.profiles.EQ.value,
            ],
            "xMin": [
                self.profiles.EQ.value,
            ],
        }
