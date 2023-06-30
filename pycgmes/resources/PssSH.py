"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSH(PowerSystemStabilizerDynamics):
    """
    SiemensTM "H infinity" power system stabilizer with generator electrical power input. [Footnote: Siemens "H
      infinity" power system stabilizers are an example of suitable products available commercially. This
      information is given for the convenience of users of this document and does not constitute an endorsement by
      IEC of these products.]

    k: Main gain (K).  Typical value = 1.
    k0: Gain 0 (K0).  Typical value = 0,012.
    k1: Gain 1 (K1).  Typical value = 0,488.
    k2: Gain 2 (K2).  Typical value = 0,064.
    k3: Gain 3 (K3).  Typical value = 0,224.
    k4: Gain 4 (K4).  Typical value = 0,1.
    td: Input time constant (Td) (>= 0).  Typical value = 10.
    t1: Time constant 1 (T1) (> 0).  Typical value = 0,076.
    t2: Time constant 2 (T2) (> 0).  Typical value = 0,086.
    t3: Time constant 3 (T3) (> 0).   Typical value = 1,068.
    t4: Time constant 4 (T4) (> 0).  Typical value = 1,913.
    vsmax: Output maximum limit (Vsmax) (> PssSH.vsmin).  Typical value = 0,1.
    vsmin: Output minimum limit (Vsmin) (< PssSH.vsmax).  Typical value = -0,1.
    """

    k: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
        default=0,
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

    vsmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmin: float = Field(
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
