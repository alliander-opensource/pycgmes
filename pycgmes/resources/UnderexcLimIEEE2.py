"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """
    Type UEL2 underexcitation limiter which has either a straight-line or multi-segment characteristic when plotted in
      terms of machine reactive power output vs. real power output. Reference: IEEE UEL2 421.5-2005, 10.2  (limit
      characteristic lookup table shown in Figure 10.4 (p 32)).

    tuv: Voltage filter time constant (TUV) (>= 0).  Typical value = 5.
    tup: Real power filter time constant (TUP) (>= 0).  Typical value = 5.
    tuq: Reactive power filter time constant (TUQ) (>= 0).  Typical value = 0.
    kui: UEL integral gain (KUI).  Typical value = 0,5.
    kul: UEL proportional gain (KUL).  Typical value = 0,8.
    vuimax: UEL integrator output maximum limit (VUIMAX) (> UnderexcLimIEEE2.vuimin).  Typical value = 0,25.
    vuimin: UEL integrator output minimum limit (VUIMIN) (< UnderexcLimIEEE2.vuimax).  Typical value = 0.
    kuf: UEL excitation system stabilizer gain (KUF).  Typical value = 0.
    kfb: Gain associated with optional integrator feedback input signal to UEL (KFB).  Typical value = 0.
    tul: Time constant associated with optional integrator feedback input signal to UEL (TUL) (>= 0).  Typical value =
      0.
    tu1: UEL lead time constant (TU1) (>= 0).  Typical value = 0.
    tu2: UEL lag time constant (TU2) (>= 0).  Typical value = 0.
    tu3: UEL lead time constant (TU3) (>= 0).  Typical value = 0.
    tu4: UEL lag time constant (TU4) (>= 0).  Typical value = 0.
    vulmax: UEL output maximum limit (VULMAX) (> UnderexcLimIEEE2.vulmin).  Typical value = 0,25.
    vulmin: UEL output minimum limit (VULMIN) (< UnderexcLimIEEE2.vulmax).  Typical value = 0.
    p0: Real power values for endpoints (P0).  Typical value = 0.
    q0: Reactive power values for endpoints (Q0).  Typical value = -0,31.
    p1: Real power values for endpoints (P1).  Typical value = 0,3.
    q1: Reactive power values for endpoints (Q1).  Typical value = -0,31.
    p2: Real power values for endpoints (P2).  Typical value = 0,6.
    q2: Reactive power values for endpoints (Q2).  Typical value = -0,28.
    p3: Real power values for endpoints (P3).  Typical value = 0,9.
    q3: Reactive power values for endpoints (Q3).  Typical value = -0,21.
    p4: Real power values for endpoints (P4).  Typical value = 1,02.
    q4: Reactive power values for endpoints (Q4).  Typical value = 0.
    p5: Real power values for endpoints (P5).
    q5: Reactive power values for endpoints (Q5).
    p6: Real power values for endpoints (P6).
    q6: Reactive power values for endpoints (Q6).
    p7: Real power values for endpoints (P7).
    q7: Reactive power values for endpoints (Q7).
    p8: Real power values for endpoints (P8).
    q8: Reactive power values for endpoints (Q8).
    p9: Real power values for endpoints (P9).
    q9: Reactive power values for endpoints (Q9).
    p10: Real power values for endpoints (P10).
    q10: Reactive power values for endpoints (Q10).
    k1: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical value = 2.
    k2: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical value
      = 2.
    """

    tuv: int = 0  # Type #Seconds in CIM
    tup: int = 0  # Type #Seconds in CIM
    tuq: int = 0  # Type #Seconds in CIM
    kui: float = 0.0  # Type #PU in CIM
    kul: float = 0.0  # Type #PU in CIM
    vuimax: float = 0.0  # Type #PU in CIM
    vuimin: float = 0.0  # Type #PU in CIM
    kuf: float = 0.0  # Type #PU in CIM
    kfb: float = 0.0  # Type #PU in CIM
    tul: int = 0  # Type #Seconds in CIM
    tu1: int = 0  # Type #Seconds in CIM
    tu2: int = 0  # Type #Seconds in CIM
    tu3: int = 0  # Type #Seconds in CIM
    tu4: int = 0  # Type #Seconds in CIM
    vulmax: float = 0.0  # Type #PU in CIM
    vulmin: float = 0.0  # Type #PU in CIM
    p0: float = 0.0  # Type #PU in CIM
    q0: float = 0.0  # Type #PU in CIM
    p1: float = 0.0  # Type #PU in CIM
    q1: float = 0.0  # Type #PU in CIM
    p2: float = 0.0  # Type #PU in CIM
    q2: float = 0.0  # Type #PU in CIM
    p3: float = 0.0  # Type #PU in CIM
    q3: float = 0.0  # Type #PU in CIM
    p4: float = 0.0  # Type #PU in CIM
    q4: float = 0.0  # Type #PU in CIM
    p5: float = 0.0  # Type #PU in CIM
    q5: float = 0.0  # Type #PU in CIM
    p6: float = 0.0  # Type #PU in CIM
    q6: float = 0.0  # Type #PU in CIM
    p7: float = 0.0  # Type #PU in CIM
    q7: float = 0.0  # Type #PU in CIM
    p8: float = 0.0  # Type #PU in CIM
    q8: float = 0.0  # Type #PU in CIM
    p9: float = 0.0  # Type #PU in CIM
    q9: float = 0.0  # Type #PU in CIM
    p10: float = 0.0  # Type #PU in CIM
    q10: float = 0.0  # Type #PU in CIM
    k1: float = 0.0  # Type #Float in CIM
    k2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=UnderexcLimIEEE2"]
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
            "tuv": [
                Profile.DY.value,
            ],
            "tup": [
                Profile.DY.value,
            ],
            "tuq": [
                Profile.DY.value,
            ],
            "kui": [
                Profile.DY.value,
            ],
            "kul": [
                Profile.DY.value,
            ],
            "vuimax": [
                Profile.DY.value,
            ],
            "vuimin": [
                Profile.DY.value,
            ],
            "kuf": [
                Profile.DY.value,
            ],
            "kfb": [
                Profile.DY.value,
            ],
            "tul": [
                Profile.DY.value,
            ],
            "tu1": [
                Profile.DY.value,
            ],
            "tu2": [
                Profile.DY.value,
            ],
            "tu3": [
                Profile.DY.value,
            ],
            "tu4": [
                Profile.DY.value,
            ],
            "vulmax": [
                Profile.DY.value,
            ],
            "vulmin": [
                Profile.DY.value,
            ],
            "p0": [
                Profile.DY.value,
            ],
            "q0": [
                Profile.DY.value,
            ],
            "p1": [
                Profile.DY.value,
            ],
            "q1": [
                Profile.DY.value,
            ],
            "p2": [
                Profile.DY.value,
            ],
            "q2": [
                Profile.DY.value,
            ],
            "p3": [
                Profile.DY.value,
            ],
            "q3": [
                Profile.DY.value,
            ],
            "p4": [
                Profile.DY.value,
            ],
            "q4": [
                Profile.DY.value,
            ],
            "p5": [
                Profile.DY.value,
            ],
            "q5": [
                Profile.DY.value,
            ],
            "p6": [
                Profile.DY.value,
            ],
            "q6": [
                Profile.DY.value,
            ],
            "p7": [
                Profile.DY.value,
            ],
            "q7": [
                Profile.DY.value,
            ],
            "p8": [
                Profile.DY.value,
            ],
            "q8": [
                Profile.DY.value,
            ],
            "p9": [
                Profile.DY.value,
            ],
            "q9": [
                Profile.DY.value,
            ],
            "p10": [
                Profile.DY.value,
            ],
            "q10": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
        }
