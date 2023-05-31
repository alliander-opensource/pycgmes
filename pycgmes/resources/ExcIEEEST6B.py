"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEST6B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage
      regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and
      the delay in the feedback circuit increase the dynamic response. Reference: IEEE 421.5-2005, 7.6.

    ilr: Exciter output current limit reference (ILR) (> 0).  Typical value = 4,164.
    kci: Exciter output current limit adjustment (KCI) (> 0).  Typical value = 1,0577.
    kff: Pre-control gain constant of the inner loop field regulator (KFF). Typical value = 1.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (KIA) (> 0).  Typical value = 45,094.
    klr: Exciter output current limiter gain (KLR) (> 0).  Typical value = 17,33.
    km: Forward gain constant of the inner loop field regulator (KM).  Typical value = 1.
    kpa: Voltage regulator proportional gain (KPA) (> 0).  Typical value = 18,038.
    oelin: OEL input selector (OELin). Typical value = noOELinput.
    tg: Feedback time constant of inner loop field voltage regulator (TG) (>= 0). Typical value = 0,02.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 4,81.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -3,85.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 4,81.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -3,85.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ilr: float = 0.0  # Type #PU in CIM
    kci: float = 0.0  # Type #PU in CIM
    kff: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    kia: float = 0.0  # Type #PU in CIM
    klr: float = 0.0  # Type #PU in CIM
    km: float = 0.0  # Type #PU in CIM
    kpa: float = 0.0  # Type #PU in CIM
    oelin: Optional[str] = None  # Type M:1..1 in CIM
    tg: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcIEEEST6B\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "ilr": [
                self.profiles.DY.value,
            ],
            "kci": [
                self.profiles.DY.value,
            ],
            "kff": [
                self.profiles.DY.value,
            ],
            "kg": [
                self.profiles.DY.value,
            ],
            "kia": [
                self.profiles.DY.value,
            ],
            "klr": [
                self.profiles.DY.value,
            ],
            "km": [
                self.profiles.DY.value,
            ],
            "kpa": [
                self.profiles.DY.value,
            ],
            "oelin": [
                self.profiles.DY.value,
            ],
            "tg": [
                self.profiles.DY.value,
            ],
            "vamax": [
                self.profiles.DY.value,
            ],
            "vamin": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
        }
