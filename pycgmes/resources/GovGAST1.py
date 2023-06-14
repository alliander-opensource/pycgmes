"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovGAST1(TurbineGovernorDynamics):
    """
    Modified single shaft gas turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R) (>0).  Typical value = 0,04.
    t1: Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.
    t2: Turbine power time constant (T2) (>= 0). T2 represents delay due to internal energy storage of the gas turbine
      engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the
      compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free
      power turbine of an aero-derivative unit, for example.  Typical value = 0,5.
    t3: Turbine exhaust temperature time constant (T3) (>= 0).  T3 represents delay in the exhaust temperature and load
      limiting system. Typical value = 3.
    lmax: Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust
      gas temperature.  Typical value = 1.
    kt: Temperature limiter gain (Kt).  Typical value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax) (> GovGAST1.vmin).  Typical value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin) (< GovGAST1.vmax).  Typical value = 0.
    fidle: Fuel flow at zero power output (Fidle).  Typical value = 0,18.
    rmax: Maximum fuel valve opening rate (Rmax).  Unit = PU / s.  Typical value = 1.
    loadinc: Valve position change allowed at fast rate (Loadinc).  Typical value = 0,05.
    tltr: Valve position averaging time constant (Tltr) (>= 0).  Typical value = 10.
    ltrate: Maximum long term fuel valve opening rate (Ltrate).  Typical value = 0,02.
    a: Turbine power time constant numerator scale factor (a).  Typical value = 0,8.
    b: Turbine power time constant denominator scale factor (b) (>0).  Typical value = 1.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical value = 0.
    pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain point 2,PU gv (Gv2).  Typical value = 0.
    pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical value = 0.
    gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical value = 0.
    pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical value = 0.
    gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical value = 0.
    pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical value = 0.
    gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical value = 0.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical value = 0.
    gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical value = 0.
    pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical value = 0.
    ka: Governor gain (Ka).  Typical value = 0.
    t4: Governor lead time constant (T4) (>= 0).  Typical value = 0.
    t5: Governor lag time constant (T5) (>= 0).  If = 0, entire gain and lead-lag block is bypassed.  Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    r: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    lmax: float = 0.0  # Type #PU in CIM
    kt: float = 0.0  # Type #PU in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    fidle: float = 0.0  # Type #PU in CIM
    rmax: float = 0.0  # Type #Float in CIM
    loadinc: float = 0.0  # Type #PU in CIM
    tltr: int = 0  # Type #Seconds in CIM
    ltrate: float = 0.0  # Type #Float in CIM
    a: float = 0.0  # Type #Float in CIM
    b: float = 0.0  # Type #Float in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    eps: float = 0.0  # Type #Frequency in CIM
    db2: float = 0.0  # Type #ActivePower in CIM
    gv1: float = 0.0  # Type #PU in CIM
    pgv1: float = 0.0  # Type #PU in CIM
    gv2: float = 0.0  # Type #PU in CIM
    pgv2: float = 0.0  # Type #PU in CIM
    gv3: float = 0.0  # Type #PU in CIM
    pgv3: float = 0.0  # Type #PU in CIM
    gv4: float = 0.0  # Type #PU in CIM
    pgv4: float = 0.0  # Type #PU in CIM
    gv5: float = 0.0  # Type #PU in CIM
    pgv5: float = 0.0  # Type #PU in CIM
    gv6: float = 0.0  # Type #PU in CIM
    pgv6: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovGAST1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "r": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "lmax": [
                Profile.DY.value,
            ],
            "kt": [
                Profile.DY.value,
            ],
            "vmax": [
                Profile.DY.value,
            ],
            "vmin": [
                Profile.DY.value,
            ],
            "fidle": [
                Profile.DY.value,
            ],
            "rmax": [
                Profile.DY.value,
            ],
            "loadinc": [
                Profile.DY.value,
            ],
            "tltr": [
                Profile.DY.value,
            ],
            "ltrate": [
                Profile.DY.value,
            ],
            "a": [
                Profile.DY.value,
            ],
            "b": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "eps": [
                Profile.DY.value,
            ],
            "db2": [
                Profile.DY.value,
            ],
            "gv1": [
                Profile.DY.value,
            ],
            "pgv1": [
                Profile.DY.value,
            ],
            "gv2": [
                Profile.DY.value,
            ],
            "pgv2": [
                Profile.DY.value,
            ],
            "gv3": [
                Profile.DY.value,
            ],
            "pgv3": [
                Profile.DY.value,
            ],
            "gv4": [
                Profile.DY.value,
            ],
            "pgv4": [
                Profile.DY.value,
            ],
            "gv5": [
                Profile.DY.value,
            ],
            "pgv5": [
                Profile.DY.value,
            ],
            "gv6": [
                Profile.DY.value,
            ],
            "pgv6": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
        }
