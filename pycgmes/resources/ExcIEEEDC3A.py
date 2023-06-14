"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
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

    trh: int = 0  # Type #Seconds in CIM
    kv: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    ke: float = 0.0  # Type #PU in CIM
    efd1: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    efd2: float = 0.0  # Type #PU in CIM
    seefd2: float = 0.0  # Type #Float in CIM
    exclim: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEDC3A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "trh": [
                Profile.DY.value,
            ],
            "kv": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "efd1": [
                Profile.DY.value,
            ],
            "seefd1": [
                Profile.DY.value,
            ],
            "efd2": [
                Profile.DY.value,
            ],
            "seefd2": [
                Profile.DY.value,
            ],
            "exclim": [
                Profile.DY.value,
            ],
        }
