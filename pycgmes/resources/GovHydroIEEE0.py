"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroIEEE0(TurbineGovernorDynamics):
    """
    IEEE simplified hydro governor-turbine model.  Used for mechanical-hydraulic and electro-hydraulic turbine
      governors, with or without steam feedback. Typical values given are for mechanical-hydraulic turbine-governor.
      Reference: IEEE Transactions on Power Apparatus and Systems, November/December 1973, Volume PAS-92, Number 6,
      Dynamic Models for Steam and Hydro Turbines in Power System Studies, page 1904.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain (K).
    t1: Governor lag time constant (T1) (>= 0).  Typical value = 0,25.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    t3: Gate actuator time constant (T3) (>= 0).  Typical value = 0,1.
    t4: Water starting time (T4) (>= 0).
    pmax: Gate maximum (Pmax) (> GovHydroIEEE0.pmin).
    pmin: Gate minimum (Pmin) (< GovHydroIEEE.pmax).
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    k: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroIEEE0"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
        }
