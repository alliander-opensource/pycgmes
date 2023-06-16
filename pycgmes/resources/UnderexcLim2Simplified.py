"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
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

    q0: float = 0.0  # Type #PU in CIM
    q1: float = 0.0  # Type #PU in CIM
    p0: float = 0.0  # Type #PU in CIM
    p1: float = 0.0  # Type #PU in CIM
    kui: float = 0.0  # Type #PU in CIM
    vuimin: float = 0.0  # Type #PU in CIM
    vuimax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=UnderexcLim2Simplified"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "q0": [
                Profile.DY.value,
            ],
            "q1": [
                Profile.DY.value,
            ],
            "p0": [
                Profile.DY.value,
            ],
            "p1": [
                Profile.DY.value,
            ],
            "kui": [
                Profile.DY.value,
            ],
            "vuimin": [
                Profile.DY.value,
            ],
            "vuimax": [
                Profile.DY.value,
            ],
        }
