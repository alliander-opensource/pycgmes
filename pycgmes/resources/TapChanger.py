"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
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
    # TapSchedules : list = field(default_factory=list)  # Type M:0..n in CIM
    highStep: int = 0  # Type #Integer in CIM
    lowStep: int = 0  # Type #Integer in CIM
    ltcFlag: bool = False  # Type #Boolean in CIM
    neutralStep: int = 0  # Type #Integer in CIM
    neutralU: float = 0.0  # Type #Voltage in CIM
    normalStep: int = 0  # Type #Integer in CIM
    TapChangerControl: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # SvTapStep : Optional[str] = None  # Type M:0..1 in CIM
    controlEnabled: bool = False  # Type #Boolean in CIM
    step: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TapChanger"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
                Profile.SSH.value,
            ],
            # Attributes
            "TapSchedules": [
                Profile.EQ.value,
            ],
            "highStep": [
                Profile.EQ.value,
            ],
            "lowStep": [
                Profile.EQ.value,
            ],
            "ltcFlag": [
                Profile.EQ.value,
            ],
            "neutralStep": [
                Profile.EQ.value,
            ],
            "neutralU": [
                Profile.EQ.value,
            ],
            "normalStep": [
                Profile.EQ.value,
            ],
            "TapChangerControl": [
                Profile.EQ.value,
            ],
            "SvTapStep": [
                Profile.SV.value,
            ],
            "controlEnabled": [
                Profile.SSH.value,
            ],
            "step": [
                Profile.SSH.value,
            ],
        }
