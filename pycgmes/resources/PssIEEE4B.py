"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
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

    bwh1: float = 0.0  # Type #Float in CIM
    bwh2: float = 0.0  # Type #Float in CIM
    bwl1: float = 0.0  # Type #Float in CIM
    bwl2: float = 0.0  # Type #Float in CIM
    kh: float = 0.0  # Type #PU in CIM
    kh1: float = 0.0  # Type #PU in CIM
    kh11: float = 0.0  # Type #PU in CIM
    kh17: float = 0.0  # Type #PU in CIM
    kh2: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    ki1: float = 0.0  # Type #PU in CIM
    ki11: float = 0.0  # Type #PU in CIM
    ki17: float = 0.0  # Type #PU in CIM
    ki2: float = 0.0  # Type #PU in CIM
    kl: float = 0.0  # Type #PU in CIM
    kl1: float = 0.0  # Type #PU in CIM
    kl11: float = 0.0  # Type #PU in CIM
    kl17: float = 0.0  # Type #PU in CIM
    kl2: float = 0.0  # Type #PU in CIM
    omeganh1: float = 0.0  # Type #Float in CIM
    omeganh2: float = 0.0  # Type #Float in CIM
    omeganl1: float = 0.0  # Type #Float in CIM
    omeganl2: float = 0.0  # Type #Float in CIM
    th1: int = 0  # Type #Seconds in CIM
    th10: int = 0  # Type #Seconds in CIM
    th11: int = 0  # Type #Seconds in CIM
    th12: int = 0  # Type #Seconds in CIM
    th2: int = 0  # Type #Seconds in CIM
    th3: int = 0  # Type #Seconds in CIM
    th4: int = 0  # Type #Seconds in CIM
    th5: int = 0  # Type #Seconds in CIM
    th6: int = 0  # Type #Seconds in CIM
    th7: int = 0  # Type #Seconds in CIM
    th8: int = 0  # Type #Seconds in CIM
    th9: int = 0  # Type #Seconds in CIM
    ti1: int = 0  # Type #Seconds in CIM
    ti10: int = 0  # Type #Seconds in CIM
    ti11: int = 0  # Type #Seconds in CIM
    ti12: int = 0  # Type #Seconds in CIM
    ti2: int = 0  # Type #Seconds in CIM
    ti3: int = 0  # Type #Seconds in CIM
    ti4: int = 0  # Type #Seconds in CIM
    ti5: int = 0  # Type #Seconds in CIM
    ti6: int = 0  # Type #Seconds in CIM
    ti7: int = 0  # Type #Seconds in CIM
    ti8: int = 0  # Type #Seconds in CIM
    ti9: int = 0  # Type #Seconds in CIM
    tl1: int = 0  # Type #Seconds in CIM
    tl10: int = 0  # Type #Seconds in CIM
    tl11: int = 0  # Type #Seconds in CIM
    tl12: int = 0  # Type #Seconds in CIM
    tl2: int = 0  # Type #Seconds in CIM
    tl3: int = 0  # Type #Seconds in CIM
    tl4: int = 0  # Type #Seconds in CIM
    tl5: int = 0  # Type #Seconds in CIM
    tl6: int = 0  # Type #Seconds in CIM
    tl7: int = 0  # Type #Seconds in CIM
    tl8: int = 0  # Type #Seconds in CIM
    tl9: int = 0  # Type #Seconds in CIM
    vhmax: float = 0.0  # Type #PU in CIM
    vhmin: float = 0.0  # Type #PU in CIM
    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    vlmax: float = 0.0  # Type #PU in CIM
    vlmin: float = 0.0  # Type #PU in CIM
    vstmax: float = 0.0  # Type #PU in CIM
    vstmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssIEEE4B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "bwh1": [
                Profile.DY.value,
            ],
            "bwh2": [
                Profile.DY.value,
            ],
            "bwl1": [
                Profile.DY.value,
            ],
            "bwl2": [
                Profile.DY.value,
            ],
            "kh": [
                Profile.DY.value,
            ],
            "kh1": [
                Profile.DY.value,
            ],
            "kh11": [
                Profile.DY.value,
            ],
            "kh17": [
                Profile.DY.value,
            ],
            "kh2": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "ki1": [
                Profile.DY.value,
            ],
            "ki11": [
                Profile.DY.value,
            ],
            "ki17": [
                Profile.DY.value,
            ],
            "ki2": [
                Profile.DY.value,
            ],
            "kl": [
                Profile.DY.value,
            ],
            "kl1": [
                Profile.DY.value,
            ],
            "kl11": [
                Profile.DY.value,
            ],
            "kl17": [
                Profile.DY.value,
            ],
            "kl2": [
                Profile.DY.value,
            ],
            "omeganh1": [
                Profile.DY.value,
            ],
            "omeganh2": [
                Profile.DY.value,
            ],
            "omeganl1": [
                Profile.DY.value,
            ],
            "omeganl2": [
                Profile.DY.value,
            ],
            "th1": [
                Profile.DY.value,
            ],
            "th10": [
                Profile.DY.value,
            ],
            "th11": [
                Profile.DY.value,
            ],
            "th12": [
                Profile.DY.value,
            ],
            "th2": [
                Profile.DY.value,
            ],
            "th3": [
                Profile.DY.value,
            ],
            "th4": [
                Profile.DY.value,
            ],
            "th5": [
                Profile.DY.value,
            ],
            "th6": [
                Profile.DY.value,
            ],
            "th7": [
                Profile.DY.value,
            ],
            "th8": [
                Profile.DY.value,
            ],
            "th9": [
                Profile.DY.value,
            ],
            "ti1": [
                Profile.DY.value,
            ],
            "ti10": [
                Profile.DY.value,
            ],
            "ti11": [
                Profile.DY.value,
            ],
            "ti12": [
                Profile.DY.value,
            ],
            "ti2": [
                Profile.DY.value,
            ],
            "ti3": [
                Profile.DY.value,
            ],
            "ti4": [
                Profile.DY.value,
            ],
            "ti5": [
                Profile.DY.value,
            ],
            "ti6": [
                Profile.DY.value,
            ],
            "ti7": [
                Profile.DY.value,
            ],
            "ti8": [
                Profile.DY.value,
            ],
            "ti9": [
                Profile.DY.value,
            ],
            "tl1": [
                Profile.DY.value,
            ],
            "tl10": [
                Profile.DY.value,
            ],
            "tl11": [
                Profile.DY.value,
            ],
            "tl12": [
                Profile.DY.value,
            ],
            "tl2": [
                Profile.DY.value,
            ],
            "tl3": [
                Profile.DY.value,
            ],
            "tl4": [
                Profile.DY.value,
            ],
            "tl5": [
                Profile.DY.value,
            ],
            "tl6": [
                Profile.DY.value,
            ],
            "tl7": [
                Profile.DY.value,
            ],
            "tl8": [
                Profile.DY.value,
            ],
            "tl9": [
                Profile.DY.value,
            ],
            "vhmax": [
                Profile.DY.value,
            ],
            "vhmin": [
                Profile.DY.value,
            ],
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "vlmax": [
                Profile.DY.value,
            ],
            "vlmin": [
                Profile.DY.value,
            ],
            "vstmax": [
                Profile.DY.value,
            ],
            "vstmin": [
                Profile.DY.value,
            ],
        }
