"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


@dataclass
class TurbLCFB1(TurbineLoadControllerDynamics):
    """
    Turbine load controller model developed by WECC.  This model represents a supervisory turbine load controller that
      acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load
      reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the
      turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load
      reference governor. Typical value = true.
    db: Controller deadband (db).  Typical value = 0.
    emax: Maximum control error (Emax) (see parameter detail 4).  Typical value = 0,02.
    fb: Frequency bias gain (Fb).  Typical value = 0.
    kp: Proportional gain (Kp).  Typical value = 0.
    ki: Integral gain (Ki).  Typical value = 0.
    fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical value = false.
    pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical value =
      false.
    tpelec: Power transducer time constant (Tpelec) (>= 0).  Typical value = 0.
    irmax: Maximum turbine speed/load reference bias (Irmax) (see parameter detail 3).  Typical value = 0.
    pmwset: Power controller setpoint (Pmwset) (see parameter detail 1).  Unit = MW. Typical value = 0.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    speedReferenceGovernor: bool = False  # Type #Boolean in CIM
    db: float = 0.0  # Type #PU in CIM
    emax: float = 0.0  # Type #PU in CIM
    fb: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    fbf: bool = False  # Type #Boolean in CIM
    pbf: bool = False  # Type #Boolean in CIM
    tpelec: int = 0  # Type #Seconds in CIM
    irmax: float = 0.0  # Type #PU in CIM
    pmwset: float = 0.0  # Type #ActivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TurbLCFB1\n"
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
            "speedReferenceGovernor": [
                self.profiles.DY.value,
            ],
            "db": [
                self.profiles.DY.value,
            ],
            "emax": [
                self.profiles.DY.value,
            ],
            "fb": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "fbf": [
                self.profiles.DY.value,
            ],
            "pbf": [
                self.profiles.DY.value,
            ],
            "tpelec": [
                self.profiles.DY.value,
            ],
            "irmax": [
                self.profiles.DY.value,
            ],
            "pmwset": [
                self.profiles.DY.value,
            ],
        }
