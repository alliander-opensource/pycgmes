"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovGAST4(TurbineGovernorDynamics):
    """
    Generic turbogas.

    bp: Droop (bp).  Typical value = 0,05.
    ty: Time constant of fuel valve positioner (Ty) (>= 0).  Typical value = 0,1.
    ta: Maximum gate opening velocity (TA) (>= 0).  Typical value = 3.
    tc: Maximum gate closing velocity (TC) (>= 0).  Typical value = 0,5.
    tcm: Fuel control time constant (Tcm) (>= 0).  Typical value = 0,1.
    ktm: Compressor gain (Ktm).  Typical value = 0.
    tm: Compressor discharge volume time constant (Tm) (>= 0).  Typical value = 0,2.
    rymx: Maximum valve opening (RYMX).  Typical value = 1,1.
    rymn: Minimum valve opening (RYMN).  Typical value = 0.
    mxef: Fuel flow maximum positive error value (MXef).  Typical value = 0,05.
    mnef: Fuel flow maximum negative error value (MNef).  Typical value = -0,05.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    bp: float = 0.0  # Type #PU in CIM
    ty: int = 0  # Type #Seconds in CIM
    ta: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    tcm: int = 0  # Type #Seconds in CIM
    ktm: float = 0.0  # Type #PU in CIM
    tm: int = 0  # Type #Seconds in CIM
    rymx: float = 0.0  # Type #PU in CIM
    rymn: float = 0.0  # Type #PU in CIM
    mxef: float = 0.0  # Type #PU in CIM
    mnef: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovGAST4\n"
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
            "ty": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "tcm": [
                self.profiles.DY.value,
            ],
            "ktm": [
                self.profiles.DY.value,
            ],
            "tm": [
                self.profiles.DY.value,
            ],
            "rymx": [
                self.profiles.DY.value,
            ],
            "rymn": [
                self.profiles.DY.value,
            ],
            "mxef": [
                self.profiles.DY.value,
            ],
            "mnef": [
                self.profiles.DY.value,
            ],
        }
