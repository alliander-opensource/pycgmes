"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS with three inputs (speed, frequency, power).

    komega: Shaft speed power input gain (Komega).  Typical value = 0.
    kf: Frequency power input gain (KF).  Typical value = 5.
    kpe: Electric power input gain (KPE).  Typical value = 0,3.
    pmin: Minimum power PSS enabling (Pmin).  Typical value = 0,25.
    ks: PSS gain (Ks).  Typical value = 1.
    vsmn: Stabilizer output maximum limit (VSMN).  Typical value = -0,06.
    vsmx: Stabilizer output minimum limit (VSMX).  Typical value = 0,06.
    tpe: Electric power filter time constant (TPE) (>= 0).  Typical value = 0,05.
    t5: Washout (T5) (>= 0).  Typical value = 3,5.
    t6: Filter time constant (T6) (>= 0).  Typical value = 0.
    t7: Lead/lag time constant (T7) (>= 0). If = 0, both blocks are bypassed.  Typical value = 0.
    t8: Lead/lag time constant (T8) (>= 0).  Typical value = 0.
    t9: Lead/lag time constant (T9) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    t10: Lead/lag time constant (T10) (>= 0).  Typical value = 0.
    vadat: Signal selector (VADAT). true = closed (generator power is greater than Pmin) false = open (Pe is smaller
      than Pmin). Typical value = true.
    """

    komega: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpe: float = Field(
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

    ks: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpe: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vadat: bool = Field(
        default=False,
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
