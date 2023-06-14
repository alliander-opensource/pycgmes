"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcDC1A(ExcitationSystemDynamics):
    """
    Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL)
      inputs.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 46.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,06.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (Vrmax) (> ExcDC1A.vrmin).  Typical value = 1.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC1A.vrmax).  Typical value = -0,9.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,46.
    kf: Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 3,1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]) (>= 0).  Typical
      value = 0,33.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 2,3.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Eefd2]) (>= 0).  Typical
      value = 0,1.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical value = true.
    efdmin: Minimum voltage exciter output limiter (Efdmin) (< ExcDC1A.edfmax).  Typical value = -99.
    efdmax: Maximum voltage exciter output limiter (Efdmax) (> ExcDC1A.efdmin).  Typical value = 99.
    """

    ka: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    efd1: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    efd2: float = 0.0  # Type #PU in CIM
    seefd2: float = 0.0  # Type #Float in CIM
    exclim: bool = False  # Type #Boolean in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    efdmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcDC1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ka": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "tf": [
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
            "efdmin": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
        }
