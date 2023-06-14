"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .CrossCompoundTurbineGovernorDynamics import CrossCompoundTurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamCC(CrossCompoundTurbineGovernorDynamics):
    """
    Cross compound turbine governor.  Unlike tandem compound units, cross compound units are not on the same shaft.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    pmaxhp: Maximum HP value position (Pmaxhp).  Typical value = 1.
    rhp: HP governor droop (Rhp) (> 0).  Typical value = 0,05.
    t1hp: HP governor time constant (T1hp) (>= 0).  Typical value = 0,1.
    t3hp: HP turbine time constant (T3hp) (>= 0).  Typical value = 0,1.
    t4hp: HP turbine time constant (T4hp) (>= 0).  Typical value = 0,1.
    t5hp: HP reheater time constant (T5hp) (>= 0).  Typical value = 10.
    fhp: Fraction of HP power ahead of reheater (Fhp).  Typical value = 0,3.
    dhp: HP damping factor (Dhp).  Typical value = 0.
    pmaxlp: Maximum LP value position (Pmaxlp).  Typical value = 1.
    rlp: LP governor droop (Rlp) (> 0).  Typical value = 0,05.
    t1lp: LP governor time constant (T1lp) (>= 0).  Typical value = 0,1.
    t3lp: LP turbine time constant (T3lp) (>= 0).  Typical value = 0,1.
    t4lp: LP turbine time constant (T4lp) (>= 0).  Typical value = 0,1.
    t5lp: LP reheater time constant (T5lp) (>= 0).  Typical value = 10.
    flp: Fraction of LP power ahead of reheater (Flp).  Typical value = 0,7.
    dlp: LP damping factor (Dlp).  Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    pmaxhp: float = 0.0  # Type #PU in CIM
    rhp: float = 0.0  # Type #PU in CIM
    t1hp: int = 0  # Type #Seconds in CIM
    t3hp: int = 0  # Type #Seconds in CIM
    t4hp: int = 0  # Type #Seconds in CIM
    t5hp: int = 0  # Type #Seconds in CIM
    fhp: float = 0.0  # Type #PU in CIM
    dhp: float = 0.0  # Type #PU in CIM
    pmaxlp: float = 0.0  # Type #PU in CIM
    rlp: float = 0.0  # Type #PU in CIM
    t1lp: int = 0  # Type #Seconds in CIM
    t3lp: int = 0  # Type #Seconds in CIM
    t4lp: int = 0  # Type #Seconds in CIM
    t5lp: int = 0  # Type #Seconds in CIM
    flp: float = 0.0  # Type #PU in CIM
    dlp: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteamCC"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "pmaxhp": [
                Profile.DY.value,
            ],
            "rhp": [
                Profile.DY.value,
            ],
            "t1hp": [
                Profile.DY.value,
            ],
            "t3hp": [
                Profile.DY.value,
            ],
            "t4hp": [
                Profile.DY.value,
            ],
            "t5hp": [
                Profile.DY.value,
            ],
            "fhp": [
                Profile.DY.value,
            ],
            "dhp": [
                Profile.DY.value,
            ],
            "pmaxlp": [
                Profile.DY.value,
            ],
            "rlp": [
                Profile.DY.value,
            ],
            "t1lp": [
                Profile.DY.value,
            ],
            "t3lp": [
                Profile.DY.value,
            ],
            "t4lp": [
                Profile.DY.value,
            ],
            "t5lp": [
                Profile.DY.value,
            ],
            "flp": [
                Profile.DY.value,
            ],
            "dlp": [
                Profile.DY.value,
            ],
        }
