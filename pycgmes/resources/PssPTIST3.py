"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssPTIST3(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 3.

    m: (M).  M = 2 x H.  Typical value = 5.
    tf: Time constant (Tf) (>= 0).  Typical value = 0,2.
    tp: Time constant (Tp) (>= 0).  Typical value = 0,2.
    t1: Time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Time constant (T2) (>= 0).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 0,2.
    t4: Time constant (T4) (>= 0).  Typical value = 0,05.
    k: Gain (K).  Typical value = 9.
    dtf: Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).
    dtc: Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).
    dtp: Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125  (0,015 for 50 Hz).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    a0: Filter coefficient (A0).
    a1: Limiter (Al).
    a2: Filter coefficient (A2).
    b0: Filter coefficient (B0).
    b1: Filter coefficient (B1).
    b2: Filter coefficient (B2).
    a3: Filter coefficient (A3).
    a4: Filter coefficient (A4).
    a5: Filter coefficient (A5).
    b3: Filter coefficient (B3).
    b4: Filter coefficient (B4).
    b5: Filter coefficient (B5).
    athres: Threshold value above which output averaging will be bypassed (Athres).  Typical value = 0,005.
    dl: Limiter (Dl).
    al: Limiter (Al).
    lthres: Threshold value (Lthres).
    pmin: (Pmin).
    isw: Digital/analogue output switch (Isw). true = produce analogue output false = convert to digital output, using
      tap selection table.
    nav: Number of control outputs to average (NAV) (1 <=  NAV <= 16).  Typical value = 4.
    ncl: Number of counts at limit to active limit function (NCL) (> 0).
    ncr: Number of counts until reset after limit function is triggered (NCR).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    m: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    dtf: int = 0  # Type #Seconds in CIM
    dtc: int = 0  # Type #Seconds in CIM
    dtp: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    a0: float = 0.0  # Type #PU in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    b0: float = 0.0  # Type #PU in CIM
    b1: float = 0.0  # Type #PU in CIM
    b2: float = 0.0  # Type #PU in CIM
    a3: float = 0.0  # Type #PU in CIM
    a4: float = 0.0  # Type #PU in CIM
    a5: float = 0.0  # Type #PU in CIM
    b3: float = 0.0  # Type #PU in CIM
    b4: float = 0.0  # Type #PU in CIM
    b5: float = 0.0  # Type #PU in CIM
    athres: float = 0.0  # Type #PU in CIM
    dl: float = 0.0  # Type #PU in CIM
    al: float = 0.0  # Type #PU in CIM
    lthres: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    isw: bool = False  # Type #Boolean in CIM
    nav: float = 0.0  # Type #Float in CIM
    ncl: float = 0.0  # Type #Float in CIM
    ncr: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssPTIST3\n"
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
            "m": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "t4": [
                self.profiles.DY.value,
            ],
            "k": [
                self.profiles.DY.value,
            ],
            "dtf": [
                self.profiles.DY.value,
            ],
            "dtc": [
                self.profiles.DY.value,
            ],
            "dtp": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "a0": [
                self.profiles.DY.value,
            ],
            "a1": [
                self.profiles.DY.value,
            ],
            "a2": [
                self.profiles.DY.value,
            ],
            "b0": [
                self.profiles.DY.value,
            ],
            "b1": [
                self.profiles.DY.value,
            ],
            "b2": [
                self.profiles.DY.value,
            ],
            "a3": [
                self.profiles.DY.value,
            ],
            "a4": [
                self.profiles.DY.value,
            ],
            "a5": [
                self.profiles.DY.value,
            ],
            "b3": [
                self.profiles.DY.value,
            ],
            "b4": [
                self.profiles.DY.value,
            ],
            "b5": [
                self.profiles.DY.value,
            ],
            "athres": [
                self.profiles.DY.value,
            ],
            "dl": [
                self.profiles.DY.value,
            ],
            "al": [
                self.profiles.DY.value,
            ],
            "lthres": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "isw": [
                self.profiles.DY.value,
            ],
            "nav": [
                self.profiles.DY.value,
            ],
            "ncl": [
                self.profiles.DY.value,
            ],
            "ncr": [
                self.profiles.DY.value,
            ],
        }
