"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamFV2(TurbineGovernorDynamics):
    """
    Steam turbine governor with reheat time constants and modelling of the effects of fast valve closing to reduce
      mechanical power.

    mwbase: Alternate base used instead of machine base in equipment model if necessary (MWbase) (> 0).  Unit = MW.
    t1: Governor time constant (T1) (>= 0).
    vmax: (Vmax) (> GovSteamFV2.vmin).
    vmin: (Vmin) (< GovSteamFV2.vmax).
    k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K).
    t3: Reheater time constant (T3) (>= 0).
    dt: (Dt).
    tt: Time constant with which power falls off after intercept valve closure (Tt) (>= 0).
    r: (R).
    ta: Time after initial time for valve to close (Ta) (>= 0).
    tb: Time after initial time for valve to begin opening (Tb) (>= 0).
    tc: Time after initial time for valve to become fully open (Tc) (>= 0).
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    t1: int = 0  # Type #Seconds in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    k: float = 0.0  # Type #PU in CIM
    t3: int = 0  # Type #Seconds in CIM
    dt: float = 0.0  # Type #PU in CIM
    tt: int = 0  # Type #Seconds in CIM
    r: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteamFV2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mwbase": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "vmax": [
                Profile.DY.value,
            ],
            "vmin": [
                Profile.DY.value,
            ],
            "k": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "dt": [
                Profile.DY.value,
            ],
            "tt": [
                Profile.DY.value,
            ],
            "r": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
        }
