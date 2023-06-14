"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroWEH(TurbineGovernorDynamics):
    """
    WoodwardTM electric hydro governor.  [Footnote: Woodward electric hydro governors are an example of suitable
      products available commercially. This information is given for the convenience of users of this document and
      does not constitute an endorsement by IEC of these products.]

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    rpg: Permanent droop for governor output feedback (R-Perm-Gate).
    rpp: Permanent droop for electrical power feedback (R-Perm-Pe).
    tpe: Electrical power droop time constant (Tpe) (>= 0).
    kp: Derivative control gain (Kp).
    ki: Derivative controller Integral gain (Ki).
    kd: Derivative controller derivative gain (Kd).
    td: Derivative controller time constant (Td) (>= 0).  Limits the derivative characteristic beyond a breakdown
      frequency to avoid amplification of high-frequency noise.
    tp: Pilot valve time lag time constant (Tp) (>= 0).
    tdv: Distributive valve time lag time constant (Tdv) (>= 0).
    tg: Value to allow the distribution valve controller to advance beyond the gate movement rate limit (Tg) (>= 0).
    gtmxop: Maximum gate opening rate (Gtmxop).
    gtmxcl: Maximum gate closing rate (Gtmxcl).
    gmax: Maximum gate position (Gmax) (> GovHydroWEH.gmin).
    gmin: Minimum gate position (Gmin) (< GovHydroWEH.gmax).
    dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU).
    tw: Water inertia time constant (Tw) (> 0).
    db: Speed deadband (db).
    dpv: Value to allow the pilot valve controller to advance beyond the gate limits (Dpv).
    dicn: Value to allow the integral controller to advance beyond the gate limits (Dicn).
    feedbackSignal: Feedback signal selection (Sw). true = PID output (if R-Perm-Gate = droop and R-Perm-Pe = 0) false =
      electrical power (if R-Perm-Gate = 0 and R-Perm-Pe = droop) or false = gate position (if
      R-Perm-Gate = droop and R-Perm-Pe = 0). Typical value = false.
    gv1: Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv2: Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv3: Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv4: Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv5: Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    fl1: Flowgate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl2: Flowgate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl3: Flowgate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl4: Flowgate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl5: Flowgate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fp1: Flow P1 (Fp1).  Turbine flow value for point 1 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp2: Flow P2 (Fp2).  Turbine flow value for point 2 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp3: Flow P3 (Fp3).  Turbine flow value for point 3 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp4: Flow P4 (Fp4).  Turbine flow value for point 4 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp5: Flow P5 (Fp5).  Turbine flow value for point 5 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp6: Flow P6 (Fp6).  Turbine flow value for point 6 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp7: Flow P7 (Fp7).  Turbine flow value for point 7 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp8: Flow P8 (Fp8).  Turbine flow value for point 8 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp9: Flow P9 (Fp9).  Turbine flow value for point 9 for lookup table representing PU mechanical power on machine MVA
      rating as a function of turbine flow.
    fp10: Flow P10 (Fp10).  Turbine flow value for point 10 for lookup table representing PU mechanical power on machine
      MVA rating as a function of turbine flow.
    pmss1: Pmss flow P1 (Pmss1).  Mechanical power output for turbine flow point 1 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss2: Pmss flow P2 (Pmss2).  Mechanical power output for turbine flow point 2 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss3: Pmss flow P3 (Pmss3).  Mechanical power output for turbine flow point 3 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss4: Pmss flow P4 (Pmss4).  Mechanical power output for turbine flow point 4 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss5: Pmss flow P5 (Pmss5).  Mechanical power output for turbine flow point 5 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss6: Pmss flow P6 (Pmss6).  Mechanical power output for turbine flow point 6 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss7: Pmss flow P7 (Pmss7).  Mechanical power output for turbine flow point 7 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss8: Pmss flow P8 (Pmss8).  Mechanical power output for turbine flow point 8 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss9: Pmss flow P9 (Pmss9).  Mechanical power output for turbine flow point 9 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    pmss10: Pmss flow P10 (Pmss10).  Mechanical power output for turbine flow point 10 for lookup table representing PU
      mechanical power on machine MVA rating as a function of turbine flow.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    rpg: float = 0.0  # Type #Float in CIM
    rpp: float = 0.0  # Type #Float in CIM
    tpe: int = 0  # Type #Seconds in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    tdv: int = 0  # Type #Seconds in CIM
    tg: int = 0  # Type #Seconds in CIM
    gtmxop: float = 0.0  # Type #PU in CIM
    gtmxcl: float = 0.0  # Type #PU in CIM
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    dturb: float = 0.0  # Type #PU in CIM
    tw: int = 0  # Type #Seconds in CIM
    db: float = 0.0  # Type #PU in CIM
    dpv: float = 0.0  # Type #PU in CIM
    dicn: float = 0.0  # Type #PU in CIM
    feedbackSignal: bool = False  # Type #Boolean in CIM
    gv1: float = 0.0  # Type #PU in CIM
    gv2: float = 0.0  # Type #PU in CIM
    gv3: float = 0.0  # Type #PU in CIM
    gv4: float = 0.0  # Type #PU in CIM
    gv5: float = 0.0  # Type #PU in CIM
    fl1: float = 0.0  # Type #PU in CIM
    fl2: float = 0.0  # Type #PU in CIM
    fl3: float = 0.0  # Type #PU in CIM
    fl4: float = 0.0  # Type #PU in CIM
    fl5: float = 0.0  # Type #PU in CIM
    fp1: float = 0.0  # Type #PU in CIM
    fp2: float = 0.0  # Type #PU in CIM
    fp3: float = 0.0  # Type #PU in CIM
    fp4: float = 0.0  # Type #PU in CIM
    fp5: float = 0.0  # Type #PU in CIM
    fp6: float = 0.0  # Type #PU in CIM
    fp7: float = 0.0  # Type #PU in CIM
    fp8: float = 0.0  # Type #PU in CIM
    fp9: float = 0.0  # Type #PU in CIM
    fp10: float = 0.0  # Type #PU in CIM
    pmss1: float = 0.0  # Type #PU in CIM
    pmss2: float = 0.0  # Type #PU in CIM
    pmss3: float = 0.0  # Type #PU in CIM
    pmss4: float = 0.0  # Type #PU in CIM
    pmss5: float = 0.0  # Type #PU in CIM
    pmss6: float = 0.0  # Type #PU in CIM
    pmss7: float = 0.0  # Type #PU in CIM
    pmss8: float = 0.0  # Type #PU in CIM
    pmss9: float = 0.0  # Type #PU in CIM
    pmss10: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroWEH"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "rpg": [
                Profile.DY.value,
            ],
            "rpp": [
                Profile.DY.value,
            ],
            "tpe": [
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
            "tp": [
                Profile.DY.value,
            ],
            "tdv": [
                Profile.DY.value,
            ],
            "tg": [
                Profile.DY.value,
            ],
            "gtmxop": [
                Profile.DY.value,
            ],
            "gtmxcl": [
                Profile.DY.value,
            ],
            "gmax": [
                Profile.DY.value,
            ],
            "gmin": [
                Profile.DY.value,
            ],
            "dturb": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "db": [
                Profile.DY.value,
            ],
            "dpv": [
                Profile.DY.value,
            ],
            "dicn": [
                Profile.DY.value,
            ],
            "feedbackSignal": [
                Profile.DY.value,
            ],
            "gv1": [
                Profile.DY.value,
            ],
            "gv2": [
                Profile.DY.value,
            ],
            "gv3": [
                Profile.DY.value,
            ],
            "gv4": [
                Profile.DY.value,
            ],
            "gv5": [
                Profile.DY.value,
            ],
            "fl1": [
                Profile.DY.value,
            ],
            "fl2": [
                Profile.DY.value,
            ],
            "fl3": [
                Profile.DY.value,
            ],
            "fl4": [
                Profile.DY.value,
            ],
            "fl5": [
                Profile.DY.value,
            ],
            "fp1": [
                Profile.DY.value,
            ],
            "fp2": [
                Profile.DY.value,
            ],
            "fp3": [
                Profile.DY.value,
            ],
            "fp4": [
                Profile.DY.value,
            ],
            "fp5": [
                Profile.DY.value,
            ],
            "fp6": [
                Profile.DY.value,
            ],
            "fp7": [
                Profile.DY.value,
            ],
            "fp8": [
                Profile.DY.value,
            ],
            "fp9": [
                Profile.DY.value,
            ],
            "fp10": [
                Profile.DY.value,
            ],
            "pmss1": [
                Profile.DY.value,
            ],
            "pmss2": [
                Profile.DY.value,
            ],
            "pmss3": [
                Profile.DY.value,
            ],
            "pmss4": [
                Profile.DY.value,
            ],
            "pmss5": [
                Profile.DY.value,
            ],
            "pmss6": [
                Profile.DY.value,
            ],
            "pmss7": [
                Profile.DY.value,
            ],
            "pmss8": [
                Profile.DY.value,
            ],
            "pmss9": [
                Profile.DY.value,
            ],
            "pmss10": [
                Profile.DY.value,
            ],
        }
