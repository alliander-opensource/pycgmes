"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcPIC(ExcitationSystemDynamics):
    """
    Proportional/integral regulator excitation system.  This model can be used to represent excitation systems with a
      proportional-integral (PI) voltage regulator controller.

    ka: PI controller gain (Ka).  Typical value = 3,15.
    ta1: PI controller time constant (Ta1) (>= 0).  Typical value = 1.
    vr1: PI maximum limit (Vr1).  Typical value = 1.
    vr2: PI minimum limit (Vr2).  Typical value = -0,87.
    ta2: Voltage regulator time constant (Ta2) (>= 0).  Typical value = 0,01.
    ta3: Lead time constant (Ta3) (>= 0).  Typical value = 0.
    ta4: Lag time constant (Ta4) (>= 0).  Typical value = 0.
    vrmax: Voltage regulator maximum limit (Vrmax) (> ExcPIC.vrmin).  Typical value = 1.
    vrmin: Voltage regulator minimum limit (Vrmin) (< ExcPIC.vrmax).  Typical value = -0,87.
    kf: Rate feedback gain (Kf).  Typical value = 0.
    tf1: Rate feedback time constant (Tf1) (>= 0).  Typical value = 0.
    tf2: Rate feedback lag time constant (Tf2) (>= 0).  Typical value = 0.
    efdmax: Exciter maximum limit (Efdmax) (> ExcPIC.efdmin).  Typical value = 8.
    efdmin: Exciter minimum limit (Efdmin) (< ExcPIC.efdmax).  Typical value = -0,87.
    ke: Exciter constant (Ke).  Typical value = 0.
    te: Exciter time constant (Te) (>= 0).  Typical value = 0.
    e1: Field voltage value 1 (E1).  Typical value = 0.
    se1: Saturation factor at E1 (Se1).  Typical value = 0.
    e2: Field voltage value 2 (E2).  Typical value = 0.
    se2: Saturation factor at E2 (Se2).  Typical value = 0.
    kp: Potential source gain (Kp).  Typical value = 6,5.
    ki: Current source gain (Ki).  Typical value = 0.
    kc: Exciter regulation factor (Kc).  Typical value = 0,08.
    """

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vr1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vr2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta4: int = Field(
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

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ke: float = Field(
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

    e1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    e2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
