"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssELIN2(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

    ts1: Time constant (Ts1) (>= 0).  Typical value = 0.
    ts2: Time constant (Ts2) (>= 0).  Typical value = 1.
    ts3: Time constant (Ts3) (>= 0).  Typical value = 1.
    ts4: Time constant (Ts4) (>= 0).  Typical value = 0,1.
    ts5: Time constant (Ts5) (>= 0).  Typical value = 0.
    ts6: Time constant (Ts6) (>= 0).  Typical value = 1.
    ks1: Gain (Ks1).  Typical value = 1.
    ks2: Gain (Ks2).  Typical value = 0,1.
    ppss: Coefficient (p_PSS) (>= 0 and <= 4).  Typical value = 0,1.
    apss: Coefficient (a_PSS).  Typical value = 0,1.
    psslim: PSS limiter (psslim).  Typical value = 0,1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ts1: int = 0  # Type #Seconds in CIM
    ts2: int = 0  # Type #Seconds in CIM
    ts3: int = 0  # Type #Seconds in CIM
    ts4: int = 0  # Type #Seconds in CIM
    ts5: int = 0  # Type #Seconds in CIM
    ts6: int = 0  # Type #Seconds in CIM
    ks1: float = 0.0  # Type #PU in CIM
    ks2: float = 0.0  # Type #PU in CIM
    ppss: float = 0.0  # Type #PU in CIM
    apss: float = 0.0  # Type #PU in CIM
    psslim: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssELIN2\n"
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
            "ts1": [
                self.profiles.DY.value,
            ],
            "ts2": [
                self.profiles.DY.value,
            ],
            "ts3": [
                self.profiles.DY.value,
            ],
            "ts4": [
                self.profiles.DY.value,
            ],
            "ts5": [
                self.profiles.DY.value,
            ],
            "ts6": [
                self.profiles.DY.value,
            ],
            "ks1": [
                self.profiles.DY.value,
            ],
            "ks2": [
                self.profiles.DY.value,
            ],
            "ppss": [
                self.profiles.DY.value,
            ],
            "apss": [
                self.profiles.DY.value,
            ],
            "psslim": [
                self.profiles.DY.value,
            ],
        }
