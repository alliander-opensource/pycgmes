"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    TapSchedules: A TapChanger can have TapSchedules.
    highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep.
    lowStep: Lowest possible tap step position, retard from neutral.
    ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities.
    neutralStep: The neutral tap step position for this winding. The attribute shall be equal to or greater than lowStep
      and equal or less than highStep. It is the step position where the voltage is neutralU when the
      other terminals of the transformer are at the ratedU.  If there are other tap changers on the
      transformer those taps are kept constant at their neutralStep.
    neutralU: Voltage at which the winding operates at the neutral tap setting. It is the voltage at the terminal of the
      PowerTransformerEnd associated with the tap changer when all tap changers on the transformer are at
      their neutralStep position.  Normally neutralU of the tap changer is the same as ratedU of the
      PowerTransformerEnd, but it can differ in special cases such as when the tapping mechanism is
      separate from the winding more common on lower voltage transformers. This attribute is not relevant
      for PhaseTapChangerAsymmetrical, PhaseTapChangerSymmetrical and PhaseTapChangerLinear.
    normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer
      indicates the current physical tap setting. The attribute shall be equal to or greater than
      lowStep and equal to or less than highStep.
    TapChangerControl: The regulating control scheme in which this tap changer participates.
    SvTapStep: The tap step state associated with the tap changer.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support
      continuous tap variables. The reasons for continuous value are to support study cases where no discrete
      tap changer has yet been designed, a solution where a narrow voltage band forces the tap step to
      oscillate or to accommodate for a continuous solution as input. The attribute shall be equal to or
      greater than lowStep and equal to or less than highStep.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TapSchedules : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    highStep: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    lowStep: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ltcFlag: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    neutralStep: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    neutralU: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    normalStep: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    TapChangerControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # SvTapStep : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    controlEnabled: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    step: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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
            Profile.SV,
            Profile.SSH,
        }
