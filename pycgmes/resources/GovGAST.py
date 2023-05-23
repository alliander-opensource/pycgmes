"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovGAST(TurbineGovernorDynamics):
    """
    Single shaft gas turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R) (>0). Typical value = 0,04.
    t1: Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.
    t2: Turbine power time constant (T2) (>= 0).  T2 represents delay due to internal energy storage of the gas turbine
      engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the
      compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power
      turbine of an aero-derivative unit, for example.  Typical value = 0,5.
    t3: Turbine exhaust temperature time constant (T3) (>= 0).  Typical value = 3.
    at: Ambient temperature load limit (Load Limit).  Typical value = 1.
    kt: Temperature limiter gain (Kt).  Typical value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax) (> GovGAST.vmin).  Typical value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin) (< GovGAST.vmax).  Typical value = 0.
    dturb: Turbine damping factor (Dturb).  Typical value = 0,18.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    r: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    at: float = 0.0  # Type #PU in CIM
    kt: float = 0.0  # Type #PU in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    dturb: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovGAST\n"
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
            "mwbase": [
                self.profiles.DY.value,
            ],
            "r": [
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
            "at": [
                self.profiles.DY.value,
            ],
            "kt": [
                self.profiles.DY.value,
            ],
            "vmax": [
                self.profiles.DY.value,
            ],
            "vmin": [
                self.profiles.DY.value,
            ],
            "dturb": [
                self.profiles.DY.value,
            ],
        }
