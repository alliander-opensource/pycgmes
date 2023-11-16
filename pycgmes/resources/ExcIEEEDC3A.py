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
class ExcIEEEDC3A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC3A model. This model represents older systems, in particular those DC commutator exciters
      with non-continuously acting regulators that were commonly used before the development of the continuously
      acting varieties.  These systems respond at basically two different rates, depending upon the magnitude of
      voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat.
      Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the
      exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though
      it is bypassed by contactor action. Reference: IEEE 421.5-2005, 5.3.

    trh: Rheostat travel time (TRH) (> 0).  Typical value = 20.
    kv: Fast raise/lower contact setting (KV) (> 0).  Typical value = 0,05.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (VRMIN) (<= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,5.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 0,05.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 3,375.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,267.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 3,15.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,068.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical value = true.
    """

    trh: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kv: float = Field(
        default=0.0,
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

    te: int = Field(
        default=0,
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
