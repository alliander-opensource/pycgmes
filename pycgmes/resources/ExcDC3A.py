"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcDC3A(ExcitationSystemDynamics):
    """
    Modified IEEE DC3A direct current commutator exciter with speed input, and deadband.  DC old type 4.

    trh: Rheostat travel time (Trh) (> 0).  Typical value = 20.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    kr: Deadband (Kr).  Typical value = 0.
    kv: Fast raise/lower contact setting (Kv) (> 0).  Typical value = 0,05.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (Vrmin) (<= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 2,6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]) (>= 0).  Typical
      value = 0,1.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 3,45.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]) (>= 0).  Typical
      value = 0,35.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero not applied to integrator output. Typical
      value = true.
    efdmax: Maximum voltage exciter output limiter (Efdmax) (> ExcDC3A.efdmin).  Typical value = 99.
    efdmin: Minimum voltage exciter output limiter (Efdmin) (< ExcDC3A.efdmax).  Typical value = -99.
    efdlim: (Efdlim). true = exciter output limiter is active false = exciter output limiter not active. Typical value =
      true.
    """

    trh: int = 0  # Type #Seconds in CIM
    ks: float = 0.0  # Type #PU in CIM
    kr: float = 0.0  # Type #PU in CIM
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
    efdmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    efdlim: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcDC3A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ks": [
                Profile.DY.value,
            ],
            "kr": [
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
            "efdmax": [
                Profile.DY.value,
            ],
            "efdmin": [
                Profile.DY.value,
            ],
            "efdlim": [
                Profile.DY.value,
            ],
        }
