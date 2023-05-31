"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovGAST3(TurbineGovernorDynamics):
    """
    Generic turbogas with acceleration and temperature controller.

    bp: Droop (bp).  Typical value = 0,05.
    tg: Time constant of speed governor (Tg) (>= 0).  Typical value = 0,05.
    rcmx: Maximum fuel flow (RCMX).  Typical value = 1.
    rcmn: Minimum fuel flow (RCMN).  Typical value = -0,1.
    ky: Coefficient of transfer function of fuel valve positioner (Ky).  Typical value = 1.
    ty: Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,2.
    tac: Fuel control time constant (Tac) (>= 0).  Typical value = 0,1.
    kac: Fuel system feedback (KAC).  Typical value = 0.
    tc: Compressor discharge volume time constant (Tc) (>= 0).  Typical value = 0,2.
    bca: Acceleration limit set-point (Bca).  Unit = 1/s.  Typical value = 0,01.
    kca: Acceleration control integral gain (Kca). Unit = 1/s.  Typical value = 100.
    dtc: Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical value = 390.
    ka: Minimum fuel flow (Ka).  Typical value = 0,23.
    tsi: Time constant of radiation shield (Tsi) (>= 0).  Typical value = 15.
    ksi: Gain of radiation shield (Ksi).  Typical value = 0,8.
    ttc: Time constant of thermocouple (Ttc) (>= 0).  Typical value = 2,5.
    tfen: Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical value = 540.
    td: Temperature controller derivative gain (Td) (>= 0).  Typical value = 3,3.
    tt: Temperature controller integration rate (Tt).  Typical value = 250.
    mxef: Fuel flow maximum positive error value (MXef).  Typical value = 0,05.
    mnef: Fuel flow maximum negative error value (MNef).  Typical value = -0,05.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    bp: float = 0.0  # Type #PU in CIM
    tg: int = 0  # Type #Seconds in CIM
    rcmx: float = 0.0  # Type #PU in CIM
    rcmn: float = 0.0  # Type #PU in CIM
    ky: float = 0.0  # Type #Float in CIM
    ty: int = 0  # Type #Seconds in CIM
    tac: int = 0  # Type #Seconds in CIM
    kac: float = 0.0  # Type #Float in CIM
    tc: int = 0  # Type #Seconds in CIM
    bca: float = 0.0  # Type #Float in CIM
    kca: float = 0.0  # Type #Float in CIM
    dtc: float = 0.0  # Type #Temperature in CIM
    ka: float = 0.0  # Type #PU in CIM
    tsi: int = 0  # Type #Seconds in CIM
    ksi: float = 0.0  # Type #Float in CIM
    ttc: int = 0  # Type #Seconds in CIM
    tfen: float = 0.0  # Type #Temperature in CIM
    td: int = 0  # Type #Seconds in CIM
    tt: float = 0.0  # Type #Temperature in CIM
    mxef: float = 0.0  # Type #PU in CIM
    mnef: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovGAST3\n"
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
            "bp": [
                self.profiles.DY.value,
            ],
            "tg": [
                self.profiles.DY.value,
            ],
            "rcmx": [
                self.profiles.DY.value,
            ],
            "rcmn": [
                self.profiles.DY.value,
            ],
            "ky": [
                self.profiles.DY.value,
            ],
            "ty": [
                self.profiles.DY.value,
            ],
            "tac": [
                self.profiles.DY.value,
            ],
            "kac": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "bca": [
                self.profiles.DY.value,
            ],
            "kca": [
                self.profiles.DY.value,
            ],
            "dtc": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "tsi": [
                self.profiles.DY.value,
            ],
            "ksi": [
                self.profiles.DY.value,
            ],
            "ttc": [
                self.profiles.DY.value,
            ],
            "tfen": [
                self.profiles.DY.value,
            ],
            "td": [
                self.profiles.DY.value,
            ],
            "tt": [
                self.profiles.DY.value,
            ],
            "mxef": [
                self.profiles.DY.value,
            ],
            "mnef": [
                self.profiles.DY.value,
            ],
        }
