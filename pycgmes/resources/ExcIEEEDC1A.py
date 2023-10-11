# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

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
class ExcIEEEDC1A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC1A model. This model represents field-controlled DC commutator exciters with continuously
      acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier
      types).  Because this model has been widely implemented by the industry, it is sometimes used to represent
      other types of systems when detailed data for them are not available or when a simplified model is required.
      Reference: IEEE 421.5-2005, 5.1.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 46.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,06.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (VRMAX) (> ExcIEEEDC1A.vrmin).  Typical value = 1.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0 and < ExcIEEEDC1A.vrmax).  Typical value = -0,9.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,46.
    kf: Excitation control system stabilizer gain (KF) (>= 0).  Typical value = 0.1.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 3,1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0.33.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 2,3.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,1.
    uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal.
      Typical value = true.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical value = true.
    """

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

    tb: int = Field(
        default=0,
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

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uelin: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    exclim: bool = Field(
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
