"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadDynamics import LoadDynamics


@dataclass(config=DataclassConfig)
class LoadComposite(LoadDynamics):
    """
    Combined static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the
      induction machine equations.

    epvs: Active load-voltage dependence index (static) (Epvs).  Typical value = 0,7.
    epfs: Active load-frequency dependence index (static) (Epfs).  Typical value = 1,5.
    eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical value = 2.
    eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical value = 0.
    epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical value = 0,7.
    epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical value = 1,5.
    eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical value = 2.
    eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical value = 0.
    lfac: Loading factor (Lfac). The ratio of initial P to motor MVA base.  Typical value = 0,8.
    h: Inertia constant (H) (>= 0).  Typical value = 2,5.
    pfrac: Fraction of constant-power load to be represented by this motor model (PFRAC) (>= 0,0 and <= 1,0).  Typical
      value = 0,5.
    """

    epvs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    epfs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eqvs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eqfs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    epvd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    epfd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eqvd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eqfd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lfac: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    h: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pfrac: float = Field(
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
