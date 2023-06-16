"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam0(TurbineGovernorDynamics):
    """
    A simplified steam turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R).  Typical value = 0,05.
    t1: Steam bowl time constant (T1) (> 0).  Typical value = 0,5.
    vmax: Maximum valve position, PU of mwcap (Vmax) (> GovSteam0.vmin).  Typical value = 1.
    vmin: Minimum valve position, PU of mwcap (Vmin) (< GovSteam0.vmax).  Typical value = 0.
    t2: Numerator time constant of T2/T3 block (T2) (>= 0).  Typical value = 3.
    t3: Reheater time constant (T3) (> 0).  Typical value = 10.
    dt: Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    r: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    dt: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteam0"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "r": [
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
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "dt": [
                Profile.DY.value,
            ],
        }
