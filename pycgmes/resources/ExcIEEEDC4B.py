"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEDC4B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled DC commutator exciter with a
      continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. Reference:
      IEEE 421.5-2005, 5.4.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 1.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,2.
    kp: Regulator proportional gain (KP) (>= 0).  Typical value = 20.
    ki: Regulator integral gain (KI) (>= 0).  Typical value = 20.
    kd: Regulator derivative gain (KD) (>= 0).  Typical value = 20.
    td: Regulator derivative filter time constant (TD) (> 0 if ExcIEEEDC4B.kd > 0).  Typical value = 0,01.
    vrmax: Maximum voltage regulator output (VRMAX) (> ExcIEEEDC4B.vrmin).  Typical value = 2,7.
    vrmin: Minimum voltage regulator output (VRMIN) (<= 0 and < ExcIEEEDC4B.vrmax).  Typical value = -0,9.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gain (KF) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 1,75.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,08.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 2,33.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,27.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    oelin: OEL input (OELin). true = LV gate false = subtract from error signal. Typical value = true.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = true.
    """

    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
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
    vemin: float = 0.0  # Type #PU in CIM
    oelin: bool = False  # Type #Boolean in CIM
    uelin: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEDC4B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "td": [
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
            "vemin": [
                Profile.DY.value,
            ],
            "oelin": [
                Profile.DY.value,
            ],
            "uelin": [
                Profile.DY.value,
            ],
        }
