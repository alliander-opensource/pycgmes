"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcPIC(ExcitationSystemDynamics):
    """
    Proportional/integral regulator excitation system.  This model can be used to represent excitation systems with a
      proportional-integral (PI) voltage regulator controller.

    ka: PI controller gain (Ka).  Typical value = 3,15.
    ta1: PI controller time constant (Ta1) (>= 0).  Typical value = 1.
    vr1: PI maximum limit (Vr1).  Typical value = 1.
    vr2: PI minimum limit (Vr2).  Typical value = -0,87.
    ta2: Voltage regulator time constant (Ta2) (>= 0).  Typical value = 0,01.
    ta3: Lead time constant (Ta3) (>= 0).  Typical value = 0.
    ta4: Lag time constant (Ta4) (>= 0).  Typical value = 0.
    vrmax: Voltage regulator maximum limit (Vrmax) (> ExcPIC.vrmin).  Typical value = 1.
    vrmin: Voltage regulator minimum limit (Vrmin) (< ExcPIC.vrmax).  Typical value = -0,87.
    kf: Rate feedback gain (Kf).  Typical value = 0.
    tf1: Rate feedback time constant (Tf1) (>= 0).  Typical value = 0.
    tf2: Rate feedback lag time constant (Tf2) (>= 0).  Typical value = 0.
    efdmax: Exciter maximum limit (Efdmax) (> ExcPIC.efdmin).  Typical value = 8.
    efdmin: Exciter minimum limit (Efdmin) (< ExcPIC.efdmax).  Typical value = -0,87.
    ke: Exciter constant (Ke).  Typical value = 0.
    te: Exciter time constant (Te) (>= 0).  Typical value = 0.
    e1: Field voltage value 1 (E1).  Typical value = 0.
    se1: Saturation factor at E1 (Se1).  Typical value = 0.
    e2: Field voltage value 2 (E2).  Typical value = 0.
    se2: Saturation factor at E2 (Se2).  Typical value = 0.
    kp: Potential source gain (Kp).  Typical value = 6,5.
    ki: Current source gain (Ki).  Typical value = 0.
    kc: Exciter regulation factor (Kc).  Typical value = 0,08.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #PU in CIM
    ta1: int = 0  # Type #Seconds in CIM
    vr1: float = 0.0  # Type #PU in CIM
    vr2: float = 0.0  # Type #PU in CIM
    ta2: int = 0  # Type #Seconds in CIM
    ta3: int = 0  # Type #Seconds in CIM
    ta4: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf1: int = 0  # Type #Seconds in CIM
    tf2: int = 0  # Type #Seconds in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    e1: float = 0.0  # Type #PU in CIM
    se1: float = 0.0  # Type #PU in CIM
    e2: float = 0.0  # Type #PU in CIM
    se2: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcPIC\n"
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
            "ka": [
                self.profiles.DY.value,
            ],
            "ta1": [
                self.profiles.DY.value,
            ],
            "vr1": [
                self.profiles.DY.value,
            ],
            "vr2": [
                self.profiles.DY.value,
            ],
            "ta2": [
                self.profiles.DY.value,
            ],
            "ta3": [
                self.profiles.DY.value,
            ],
            "ta4": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf1": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
            "efdmax": [
                self.profiles.DY.value,
            ],
            "efdmin": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "e1": [
                self.profiles.DY.value,
            ],
            "se1": [
                self.profiles.DY.value,
            ],
            "e2": [
                self.profiles.DY.value,
            ],
            "se2": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
        }
