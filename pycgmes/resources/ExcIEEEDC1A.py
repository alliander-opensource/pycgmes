"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
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

    ka: float = 0.0  # Type #PU in CIM
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
    uelin: bool = False  # Type #Boolean in CIM
    exclim: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEDC1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "uelin": [
                Profile.DY.value,
            ],
            "exclim": [
                Profile.DY.value,
            ],
        }
