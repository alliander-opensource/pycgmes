"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=TurbLCFB1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "speedReferenceGovernor": [
                Profile.DY.value,
            ],
            "db": [
                Profile.DY.value,
            ],
            "emax": [
                Profile.DY.value,
            ],
            "fb": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "fbf": [
                Profile.DY.value,
            ],
            "pbf": [
                Profile.DY.value,
            ],
            "tpelec": [
                Profile.DY.value,
            ],
            "irmax": [
                Profile.DY.value,
            ],
            "pmwset": [
                Profile.DY.value,
            ],
        }
