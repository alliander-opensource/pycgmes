"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


@dataclass(config=DataclassConfig)
class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """
    IEEE VAR controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005,
      11.3.

    tvarc: Var controller time delay (TVARC) (>= 0).  Typical value = 5.
    vvar: Synchronous machine power factor (VVAR).
    vvarcbw: Var controller deadband (VVARC_BW).  Typical value = 0,02.
    vvarref: Var controller reference (VVARREF).
    vvtmax: Maximum machine terminal voltage needed for pf/VAr controller to be enabled (VVTMAX) (>
      PVFArType1IEEEVArController.vvtmin).
    vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (VVTMIN) (<
      PVFArType1IEEEVArController.vvtmax).
    """

    tvarc: int = 0  # Type #Seconds in CIM
    vvar: float = 0.0  # Type #PU in CIM
    vvarcbw: float = 0.0  # Type #Float in CIM
    vvarref: float = 0.0  # Type #PU in CIM
    vvtmax: float = 0.0  # Type #PU in CIM
    vvtmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PFVArType1IEEEVArController"]
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
                Profile.DY.value,
            ],
            # Attributes
            "tvarc": [
                Profile.DY.value,
            ],
            "vvar": [
                Profile.DY.value,
            ],
            "vvarcbw": [
                Profile.DY.value,
            ],
            "vvarref": [
                Profile.DY.value,
            ],
            "vvtmax": [
                Profile.DY.value,
            ],
            "vvtmin": [
                Profile.DY.value,
            ],
        }
