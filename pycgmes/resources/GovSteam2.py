"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam2(TurbineGovernorDynamics):
    """
    Simplified governor.

    k: Governor gain (reciprocal of droop) (K).  Typical value = 20.
    dbf: Frequency deadband (DBF).  Typical value = 0.
    t1: Governor lag time constant (T1) (> 0).  Typical value = 0,45.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    pmax: Maximum fuel flow (PMAX) (> GovSteam2.pmin).  Typical value = 1.
    pmin: Minimum fuel flow (PMIN) (< GovSteam2.pmax).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXEF).  Typical value = 1.
    mnef: Fuel flow maximum negative error value (MNEF).  Typical value = -1.
    """

    k: float = 0.0  # Type #Float in CIM
    dbf: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    mxef: float = 0.0  # Type #PU in CIM
    mnef: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteam2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k": [
                Profile.DY.value,
            ],
            "dbf": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "mxef": [
                Profile.DY.value,
            ],
            "mnef": [
                Profile.DY.value,
            ],
        }
