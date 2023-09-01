"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSTAB2A(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer part of an ABB excitation system. [Footnote: ABB excitation systems are an example of
      suitable products available commercially. This information is given for the convenience of users of this
      document and does not constitute an endorsement by IEC of these products.]

    k2: Gain (K2).  Typical value = 1,0.
    k3: Gain (K3).  Typical value = 0,25.
    k4: Gain (K4).  Typical value = 0,075.
    k5: Gain (K5).  Typical value = 2,5.
    t2: Time constant (T2).  Typical value = 4,0.
    t3: Time constant (T3).  Typical value = 2,0.
    t5: Time constant (T5).  Typical value = 4,5.
    hlim: Stabilizer output limiter (HLIM).  Typical value = 0,5.
    """

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

    k5: float = Field(
        default=0.0,
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

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    hlim: float = Field(
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
