"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC4A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied controlled-rectifier excitation
      system which is quite different from the other types of AC systems. This high initial response excitation
      system utilizes a full thyristor bridge in the exciter output circuit.  The voltage regulator controls the
      firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its
      output voltage to a constant value. These effects are not modelled; however, transient loading effects on the
      exciter alternator are included. Reference: IEEE 421.5-2005, 6.4.

    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -10.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 200.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,015.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5,64.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -4,53.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0.
    """

    vimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
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

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kc: float = Field(
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
