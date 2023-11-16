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
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssIEEE4B(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS4B power system stabilizer. The PSS4B model represents a structure based on multiple working
      frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency
      modes of oscillations, are used in this delta omega (speed input) PSS. There is an error in the in IEEE
      421.5-2005 PSS4B model: the Pe input should read -Pe. This implies that the input Pe needs to be multiplied by
      -1. Reference: IEEE 4B 421.5-2005, 8.4.  Parameter details: This model has 2 input signals. They have the
      following fixed types (expressed in terms of InputSignalKind values): the first one is of
      rotorAngleFrequencyDeviation type and the second one is of generatorElectricalPower type.

    bwh1: Notch filter 1 (high-frequency band): three dB bandwidth (Bwi).
    bwh2: Notch filter 2 (high-frequency band): three dB bandwidth (Bwi).
    bwl1: Notch filter 1 (low-frequency band): three dB bandwidth (Bwi).
    bwl2: Notch filter 2 (low-frequency band): three dB bandwidth (Bwi).
    kh: High band gain (KH).  Typical value = 120.
    kh1: High band differential filter gain (KH1).  Typical value = 66.
    kh11: High band first lead-lag blocks coefficient (KH11).  Typical value = 1.
    kh17: High band first lead-lag blocks coefficient (KH17).  Typical value = 1.
    kh2: High band differential filter gain (KH2).  Typical value = 66.
    ki: Intermediate band gain (KI).  Typical value = 30.
    ki1: Intermediate band differential filter gain (KI1).  Typical value = 66.
    ki11: Intermediate band first lead-lag blocks coefficient (KI11).  Typical value = 1.
    ki17: Intermediate band first lead-lag blocks coefficient (KI17).  Typical value = 1.
    ki2: Intermediate band differential filter gain (KI2).  Typical value = 66.
    kl: Low band gain (KL).  Typical value = 7.5.
    kl1: Low band differential filter gain (KL1).  Typical value = 66.
    kl11: Low band first lead-lag blocks coefficient (KL11).  Typical value = 1.
    kl17: Low band first lead-lag blocks coefficient (KL17).  Typical value = 1.
    kl2: Low band differential filter gain (KL2).  Typical value = 66.
    omeganh1: Notch filter 1 (high-frequency band): filter frequency (omegani).
    omeganh2: Notch filter 2 (high-frequency band): filter frequency (omegani).
    omeganl1: Notch filter 1 (low-frequency band): filter frequency (omegani).
    omeganl2: Notch filter 2 (low-frequency band): filter frequency (omegani).
    th1: High band time constant (TH1) (>= 0).  Typical value = 0,01513.
    th10: High band time constant (TH10) (>= 0).  Typical value = 0.
    th11: High band time constant (TH11) (>= 0).  Typical value = 0.
    th12: High band time constant (TH12) (>= 0).  Typical value = 0.
    th2: High band time constant (TH2) (>= 0).  Typical value = 0,01816.
    th3: High band time constant (TH3) (>= 0).  Typical value = 0.
    th4: High band time constant (TH4) (>= 0).  Typical value = 0.
    th5: High band time constant (TH5) (>= 0).  Typical value = 0.
    th6: High band time constant (TH6) (>= 0).  Typical value = 0.
    th7: High band time constant (TH7) (>= 0).  Typical value = 0,01816.
    th8: High band time constant (TH8) (>= 0).  Typical value = 0,02179.
    th9: High band time constant (TH9) (>= 0).  Typical value = 0.
    ti1: Intermediate band time constant (TI1) (>= 0).  Typical value = 0,173.
    ti10: Intermediate band time constant (TI10) (>= 0).  Typical value = 0.
    ti11: Intermediate band time constant (TI11) (>= 0).  Typical value = 0.
    ti12: Intermediate band time constant (TI12) (>= 0).  Typical value = 0.
    ti2: Intermediate band time constant (TI2) (>= 0).  Typical value = 0,2075.
    ti3: Intermediate band time constant (TI3) (>= 0).  Typical value = 0.
    ti4: Intermediate band time constant (TI4) (>= 0).  Typical value = 0.
    ti5: Intermediate band time constant (TI5) (>= 0).  Typical value = 0.
    ti6: Intermediate band time constant (TI6) (>= 0).  Typical value = 0.
    ti7: Intermediate band time constant (TI7) (>= 0).  Typical value = 0,2075.
    ti8: Intermediate band time constant (TI8) (>= 0).  Typical value = 0,2491.
    ti9: Intermediate band time constant (TI9) (>= 0).  Typical value = 0.
    tl1: Low band time constant (TL1) (>= 0).  Typical value = 1,73.
    tl10: Low band time constant (TL10) (>= 0).  Typical value = 0.
    tl11: Low band time constant (TL11) (>= 0).  Typical value = 0.
    tl12: Low band time constant (TL12) (>= 0).  Typical value = 0.
    tl2: Low band time constant (TL2) (>= 0).  Typical value = 2,075.
    tl3: Low band time constant (TL3) (>= 0).  Typical value = 0.
    tl4: Low band time constant (TL4) (>= 0).  Typical value = 0.
    tl5: Low band time constant (TL5) (>= 0).  Typical value = 0.
    tl6: Low band time constant (TL6) (>= 0).  Typical value = 0.
    tl7: Low band time constant (TL7) (>= 0).  Typical value = 2,075.
    tl8: Low band time constant (TL8) (>= 0).  Typical value = 2,491.
    tl9: Low band time constant (TL9) (>= 0).  Typical value = 0.
    vhmax: High band output maximum limit (VHmax) (> PssIEEE4B.vhmin).  Typical value = 0,6.
    vhmin: High band output minimum limit (VHmin) (< PssIEEE4V.vhmax).  Typical value = -0,6.
    vimax: Intermediate band output maximum limit (VImax) (> PssIEEE4B.vimin).  Typical value = 0,6.
    vimin: Intermediate band output minimum limit (VImin) (< PssIEEE4B.vimax).  Typical value = -0,6.
    vlmax: Low band output maximum limit (VLmax) (> PssIEEE4B.vlmin).  Typical value = 0,075.
    vlmin: Low band output minimum limit (VLmin) (< PssIEEE4B.vlmax).  Typical value = -0,075.
    vstmax: PSS output maximum limit (VSTmax) (> PssIEEE4B.vstmin).  Typical value = 0,15.
    vstmin: PSS output minimum limit (VSTmin) (< PssIEEE4B.vstmax).  Typical value = -0,15.
    """

    bwh1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bwh2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bwl1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bwl2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kh: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kh1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kh11: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kh17: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kh2: float = Field(
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

    ki1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki11: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki17: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl11: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl17: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omeganh1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omeganh2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omeganl1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    omeganl2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th11: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th12: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    th9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti11: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti12: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl11: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl12: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vhmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vhmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

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

    vlmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vlmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmin: float = Field(
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
