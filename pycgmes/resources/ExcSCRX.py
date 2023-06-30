"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcSCRX(ExcitationSystemDynamics):
    """
    Simple excitation system with generic characteristics typical of many excitation systems; intended for use where
      negative field current could be a problem.

    tatb: Gain reduction ratio of lag-lead element ([Ta / Tb]). The parameter Ta is not defined explicitly.  Typical
      value = 0.1.
    tb: Denominator time constant of lag-lead block (Tb) (>= 0).  Typical value = 10.
    k: Gain (K) (> 0).  Typical value = 200.
    te: Time constant of gain block (Te) (> 0).  Typical value = 0,02.
    emin: Minimum field voltage output (Emin) (< ExcSCRX.emax).  Typical value = 0.
    emax: Maximum field voltage output (Emax) (> ExcSCRX.emin).  Typical value = 5.
    cswitch: Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage.
    rcrfd: Ratio of field discharge resistance to field winding resistance ([rc / rfd]).  Typical value = 0.
    """

    tatb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb: int = Field(
        default=0,
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

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    cswitch: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    rcrfd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
