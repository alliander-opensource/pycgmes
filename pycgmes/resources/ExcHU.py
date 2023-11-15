# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcHU(ExcitationSystemDynamics):
    """
    Hungarian excitation system, with built-in voltage transducer.

    tr: Filter time constant (Tr) (>= 0). If a voltage compensator is used in conjunction with this excitation system
      model, Tr should be set to 0.  Typical value = 0,01.
    te: Major loop PI tag integration time constant (Te) (>= 0).  Typical value = 0,154.
    imin: Major loop PI tag output signal lower limit (Imin) (< ExcHU.imax).  Typical value = 0,1.
    imax: Major loop PI tag output signal upper limit (Imax) (> ExcHU.imin).  Typical value = 2,19.
    ae: Major loop PI tag gain factor (Ae).  Typical value = 3.
    emin: Field voltage control signal lower limit on AVR base (Emin) (< ExcHU.emax).  Typical value = -0,866.
    emax: Field voltage control signal upper limit on AVR base (Emax) (> ExcHU.emin).  Typical value = 0,996.
    ki: Current base conversion constant (Ki).  Typical value = 0,21428.
    ai: Minor loop PI tag gain factor (Ai).  Typical value = 22.
    ti: Minor loop PI control tag integration time constant (Ti) (>= 0).  Typical value = 0,01333.
    atr: AVR constant (Atr).  Typical value = 2,19.
    ke: Voltage base conversion constant (Ke).  Typical value = 4,666.
    """

    tr: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    te: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    imin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    imax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ae: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    emin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    emax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ki: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ai: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ti: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    atr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ke: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
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
