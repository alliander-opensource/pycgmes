"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcELIN1(ExcitationSystemDynamics):
    """
    Static PI transformer fed excitation system ELIN (VATECH) - simplified model.  This model represents an all-static
      excitation system. A PI voltage controller establishes a desired field current set point for a proportional
      current controller. The integrator of the PI controller has a follow-up input to match its signal to the
      present field current.  A power system stabilizer with power input is included in the model.

    tfi: Current transducer time constant (Tfi) (>= 0).  Typical value = 0.
    tnu: Controller reset time constant (Tnu) (>= 0).  Typical value = 2.
    vpu: Voltage controller proportional gain (Vpu).  Typical value = 34,5.
    vpi: Current controller gain (Vpi).  Typical value = 12,45.
    vpnf: Controller follow up gain (Vpnf).  Typical value = 2.
    dpnf: Controller follow up deadband (Dpnf).  Typical value = 0.
    tsw: Stabilizer parameters (Tsw) (>= 0).  Typical value = 3.
    efmin: Minimum open circuit excitation voltage (Efmin) (< ExcELIN1.efmax).  Typical value = -5.
    efmax: Maximum open circuit excitation voltage (Efmax) (> ExcELIN1.efmin).  Typical value = 5.
    xe: Excitation transformer effective reactance (Xe) (>= 0).  Xe represents the regulation of the
      transformer/rectifier unit.  Typical value = 0,06.
    ks1: Stabilizer gain 1 (Ks1).  Typical value = 0.
    ks2: Stabilizer gain 2 (Ks2).  Typical value = 0.
    ts1: Stabilizer phase lag time constant (Ts1) (>= 0).  Typical value = 1.
    ts2: Stabilizer filter time constant (Ts2) (>= 0).  Typical value = 1.
    smax: Stabilizer limit output (smax).  Typical value = 0,1.
    """

    tfi: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tnu: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpnf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    dpnf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tsw: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xe: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ts1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ts2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    smax: float = Field(
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
