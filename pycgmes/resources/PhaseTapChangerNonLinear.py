"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass(config=DataclassConfig)
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

    voltageStepIncrement: float = 0.0  # Type #PerCent in CIM
    xMax: float = 0.0  # Type #Reactance in CIM
    xMin: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PhaseTapChangerNonLinear"]
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
            "voltageStepIncrement": [
                Profile.EQ.value,
            ],
            "xMax": [
                Profile.EQ.value,
            ],
            "xMin": [
                Profile.EQ.value,
            ],
        }
