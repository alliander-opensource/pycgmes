"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
