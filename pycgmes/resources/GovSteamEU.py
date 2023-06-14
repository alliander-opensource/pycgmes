"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamEU(TurbineGovernorDynamics):
    """
    Simplified boiler and steam turbine with PID governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tp: Power transducer time constant (Tp) (>= 0).  Typical value = 0,07.
    ke: Gain of the power controller (Ke).  Typical value = 0,65.
    tip: Integral time constant of the power controller (Tip) (>= 0).  Typical value = 2.
    tdp: Derivative time constant of the power controller (Tdp) (>= 0).  Typical value = 0.
    tfp: Time constant of the power controller (Tfp) (>= 0).  Typical value = 0.
    tf: Frequency transducer time constant (Tf) (>= 0).  Typical value = 0.
    kfcor: Gain of the frequency corrector (Kfcor).  Typical value = 20.
    db1: Deadband of the frequency corrector (db1).  Typical value = 0.
    wfmax: Upper limit for frequency correction (Wfmax) (> GovSteamEU.wfmin).  Typical value = 0,05.
    wfmin: Lower limit for frequency correction (Wfmin) (< GovSteamEU.wfmax).  Typical value = -0,05.
    pmax: Maximal active power of the turbine (Pmax).  Typical value = 1.
    ten: Electro hydraulic transducer (Ten) (>= 0).  Typical value = 0,1.
    tw: Speed transducer time constant (Tw) (>= 0).  Typical value = 0,02.
    komegacor: Gain of the speed governor (Kwcor).  Typical value = 20.
    db2: Deadband of the speed governor (db2).  Typical value = 0,0004.
    wwmax: Upper limit for the speed governor (Wwmax) (> GovSteamEU.wwmin).  Typical value = 0,1.
    wwmin: Lower limit for the speed governor frequency correction (Wwmin) (< GovSteamEU.wwmax).  Typical value = -1.
    wmax1: Emergency speed control lower limit (wmax1).  Typical value = 1,025.
    wmax2: Emergency speed control upper limit (wmax2).  Typical value = 1,05.
    tvhp: Control valves servo time constant (Tvhp) (>= 0).  Typical value = 0,1.
    cho: Control valves rate opening limit (Cho).  Unit = PU / s.  Typical value = 0,17.
    chc: Control valves rate closing limit (Chc).  Unit = PU / s.  Typical value = -3,3.
    hhpmax: Maximum control valve position (Hhpmax).  Typical value = 1.
    tvip: Intercept valves servo time constant (Tvip) (>= 0).  Typical value = 0,15.
    cio: Intercept valves rate opening limit (Cio).  Typical value = 0,123.
    cic: Intercept valves rate closing limit (Cic).  Typical value = -2,2.
    simx: Intercept valves transfer limit (Simx).  Typical value = 0,425.
    thp: High pressure (HP) time constant of the turbine (Thp) (>= 0).  Typical value = 0,31.
    trh: Reheater  time constant of the turbine (Trh) (>= 0).  Typical value = 8.
    tlp: Low pressure (LP) time constant of the turbine (Tlp) (>= 0).  Typical value = 0,45.
    prhmax: Maximum low pressure limit (Prhmax).  Typical value = 1,4.
    khp: Fraction of total turbine output generated by HP part (Khp).  Typical value = 0,277.
    klp: Fraction of total turbine output generated by HP part (Klp).  Typical value = 0,723.
    tb: Boiler time constant (Tb) (>= 0).  Typical value = 100.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    tp: int = 0  # Type #Seconds in CIM
    ke: float = 0.0  # Type #PU in CIM
    tip: int = 0  # Type #Seconds in CIM
    tdp: int = 0  # Type #Seconds in CIM
    tfp: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    kfcor: float = 0.0  # Type #PU in CIM
    db1: float = 0.0  # Type #PU in CIM
    wfmax: float = 0.0  # Type #PU in CIM
    wfmin: float = 0.0  # Type #PU in CIM
    pmax: float = 0.0  # Type #PU in CIM
    ten: int = 0  # Type #Seconds in CIM
    tw: int = 0  # Type #Seconds in CIM
    komegacor: float = 0.0  # Type #PU in CIM
    db2: float = 0.0  # Type #PU in CIM
    wwmax: float = 0.0  # Type #PU in CIM
    wwmin: float = 0.0  # Type #PU in CIM
    wmax1: float = 0.0  # Type #PU in CIM
    wmax2: float = 0.0  # Type #PU in CIM
    tvhp: int = 0  # Type #Seconds in CIM
    cho: float = 0.0  # Type #Float in CIM
    chc: float = 0.0  # Type #Float in CIM
    hhpmax: float = 0.0  # Type #PU in CIM
    tvip: int = 0  # Type #Seconds in CIM
    cio: float = 0.0  # Type #PU in CIM
    cic: float = 0.0  # Type #PU in CIM
    simx: float = 0.0  # Type #PU in CIM
    thp: int = 0  # Type #Seconds in CIM
    trh: int = 0  # Type #Seconds in CIM
    tlp: int = 0  # Type #Seconds in CIM
    prhmax: float = 0.0  # Type #PU in CIM
    khp: float = 0.0  # Type #PU in CIM
    klp: float = 0.0  # Type #PU in CIM
    tb: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteamEU"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mwbase": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "tip": [
                Profile.DY.value,
            ],
            "tdp": [
                Profile.DY.value,
            ],
            "tfp": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "kfcor": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "wfmax": [
                Profile.DY.value,
            ],
            "wfmin": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "ten": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "komegacor": [
                Profile.DY.value,
            ],
            "db2": [
                Profile.DY.value,
            ],
            "wwmax": [
                Profile.DY.value,
            ],
            "wwmin": [
                Profile.DY.value,
            ],
            "wmax1": [
                Profile.DY.value,
            ],
            "wmax2": [
                Profile.DY.value,
            ],
            "tvhp": [
                Profile.DY.value,
            ],
            "cho": [
                Profile.DY.value,
            ],
            "chc": [
                Profile.DY.value,
            ],
            "hhpmax": [
                Profile.DY.value,
            ],
            "tvip": [
                Profile.DY.value,
            ],
            "cio": [
                Profile.DY.value,
            ],
            "cic": [
                Profile.DY.value,
            ],
            "simx": [
                Profile.DY.value,
            ],
            "thp": [
                Profile.DY.value,
            ],
            "trh": [
                Profile.DY.value,
            ],
            "tlp": [
                Profile.DY.value,
            ],
            "prhmax": [
                Profile.DY.value,
            ],
            "khp": [
                Profile.DY.value,
            ],
            "klp": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
        }
