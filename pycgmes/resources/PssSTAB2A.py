"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSTAB2A(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer part of an ABB excitation system. [Footnote: ABB excitation systems are an example of
      suitable products available commercially. This information is given for the convenience of users of this
      document and does not constitute an endorsement by IEC of these products.]

    k2: Gain (K2).  Typical value = 1,0.
    k3: Gain (K3).  Typical value = 0,25.
    k4: Gain (K4).  Typical value = 0,075.
    k5: Gain (K5).  Typical value = 2,5.
    t2: Time constant (T2).  Typical value = 4,0.
    t3: Time constant (T3).  Typical value = 2,0.
    t5: Time constant (T5).  Typical value = 4,5.
    hlim: Stabilizer output limiter (HLIM).  Typical value = 0,5.
    """

    k2: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    k4: float = 0.0  # Type #PU in CIM
    k5: float = 0.0  # Type #PU in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    hlim: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssSTAB2A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k2": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "k4": [
                Profile.DY.value,
            ],
            "k5": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "hlim": [
                Profile.DY.value,
            ],
        }
