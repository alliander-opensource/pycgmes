"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass
class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """
    Simplified type UEL2 underexcitation limiter.  This model can be derived from UnderexcLimIEEE2.  The limit
      characteristic (look -up table) is a single straight-line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p
      32), IEEE 421.5-2005 Section 10.2).

    q0: Segment Q initial point (Q0).  Typical value = -0,31.
    q1: Segment Q end point (Q1).  Typical value = -0,1.
    p0: Segment P initial point (P0).  Typical value = 0.
    p1: Segment P end point (P1).  Typical value = 1.
    kui: Gain Under excitation limiter (KUI).  Typical value = 0,1.
    vuimin: Minimum error signal (VUIMIN) (< UnderexcLim2Simplified.vuimax).  Typical value = 0.
    vuimax: Maximum error signal (VUIMAX) (> UnderexcLim2Simplified.vuimin).  Typical value = 1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    q0: float = 0.0  # Type #PU in CIM
    q1: float = 0.0  # Type #PU in CIM
    p0: float = 0.0  # Type #PU in CIM
    p1: float = 0.0  # Type #PU in CIM
    kui: float = 0.0  # Type #PU in CIM
    vuimin: float = 0.0  # Type #PU in CIM
    vuimax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=UnderexcLim2Simplified\n"
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
            "q0": [
                self.profiles.DY.value,
            ],
            "q1": [
                self.profiles.DY.value,
            ],
            "p0": [
                self.profiles.DY.value,
            ],
            "p1": [
                self.profiles.DY.value,
            ],
            "kui": [
                self.profiles.DY.value,
            ],
            "vuimin": [
                self.profiles.DY.value,
            ],
            "vuimax": [
                self.profiles.DY.value,
            ],
        }
