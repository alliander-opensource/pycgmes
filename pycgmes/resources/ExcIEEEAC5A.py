"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC5A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC5A model. The model represents a simplified model for brushless excitation systems. The
      regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system
      disturbances.  Unlike other AC models, this model uses loaded rather than open circuit exciter saturation data
      in the same way as it is used for the DC models.  Because the model has been widely implemented by the
      industry, it is sometimes used to represent other types of systems when either detailed data for them are not
      available or simplified models are required. Reference: IEEE 421.5-2005, 6.5.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 7,3.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -7,3.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,03.
    tf1: Excitation control system stabilizer time constant (TF1) (> 0).  Typical value = 1.
    tf2: Excitation control system stabilizer time constant (TF2) (>= 0).  Typical value = 1.
    tf3: Excitation control system stabilizer time constant (TF3) (>= 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 5,6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,86.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 4,2.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,5.
    """

    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf1: int = 0  # Type #Seconds in CIM
    tf2: int = 0  # Type #Seconds in CIM
    tf3: int = 0  # Type #Seconds in CIM
    efd1: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    efd2: float = 0.0  # Type #PU in CIM
    seefd2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEAC5A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tf1": [
                Profile.DY.value,
            ],
            "tf2": [
                Profile.DY.value,
            ],
            "tf3": [
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
        }
