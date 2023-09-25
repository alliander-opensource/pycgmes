"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    voltageStepIncrement: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    xMax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    xMin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
