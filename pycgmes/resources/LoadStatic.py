"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class LoadStatic(IdentifiedObject):
    """
    General static load. This model represents the sensitivity of the real and reactive power consumed by the load to
      the amplitude and frequency of the bus voltage.

    LoadAggregate: Aggregate load to which this aggregate static load belongs.
    staticLoadModelType: Type of static load model.  Typical value = constantZ.
    kp1: First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ.
    kp2: Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ.
    kp3: Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ.
    kp4: Frequency coefficient for active power (Kp4)  (not = 0 if .staticLoadModelType = zIP2).  Used only when
      .staticLoadModelType = zIP2.
    ep1: First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential.
    ep2: Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential.
    ep3: Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential.
    kpf: Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ.
    kq1: First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ.
    kq2: Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ.
    kq3: Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ.
    kq4: Frequency coefficient for reactive power (Kq4)  (not = 0 when .staticLoadModelType = zIP2).  Used only when
      .staticLoadModelType - zIP2.
    eq1: First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential.
    eq2: Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential.
    eq3: Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential.
    kqf: Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    LoadAggregate: Optional[str] = None  # Type M:1 in CIM
    staticLoadModelType: Optional[str] = None  # Type M:1..1 in CIM
    kp1: float = 0.0  # Type #Float in CIM
    kp2: float = 0.0  # Type #Float in CIM
    kp3: float = 0.0  # Type #Float in CIM
    kp4: float = 0.0  # Type #Float in CIM
    ep1: float = 0.0  # Type #Float in CIM
    ep2: float = 0.0  # Type #Float in CIM
    ep3: float = 0.0  # Type #Float in CIM
    kpf: float = 0.0  # Type #Float in CIM
    kq1: float = 0.0  # Type #Float in CIM
    kq2: float = 0.0  # Type #Float in CIM
    kq3: float = 0.0  # Type #Float in CIM
    kq4: float = 0.0  # Type #Float in CIM
    eq1: float = 0.0  # Type #Float in CIM
    eq2: float = 0.0  # Type #Float in CIM
    eq3: float = 0.0  # Type #Float in CIM
    kqf: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=LoadStatic\n"
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
            "LoadAggregate": [
                self.profiles.DY.value,
            ],
            "staticLoadModelType": [
                self.profiles.DY.value,
            ],
            "kp1": [
                self.profiles.DY.value,
            ],
            "kp2": [
                self.profiles.DY.value,
            ],
            "kp3": [
                self.profiles.DY.value,
            ],
            "kp4": [
                self.profiles.DY.value,
            ],
            "ep1": [
                self.profiles.DY.value,
            ],
            "ep2": [
                self.profiles.DY.value,
            ],
            "ep3": [
                self.profiles.DY.value,
            ],
            "kpf": [
                self.profiles.DY.value,
            ],
            "kq1": [
                self.profiles.DY.value,
            ],
            "kq2": [
                self.profiles.DY.value,
            ],
            "kq3": [
                self.profiles.DY.value,
            ],
            "kq4": [
                self.profiles.DY.value,
            ],
            "eq1": [
                self.profiles.DY.value,
            ],
            "eq2": [
                self.profiles.DY.value,
            ],
            "eq3": [
                self.profiles.DY.value,
            ],
            "kqf": [
                self.profiles.DY.value,
            ],
        }
