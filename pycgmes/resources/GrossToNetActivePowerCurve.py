"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Curve import Curve


@dataclass
class GrossToNetActivePowerCurve(Curve):
    """
    Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the
      machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined
      measurements at the power station). Station service loads, when modelled, should be treated as non-conforming
      bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.

    GeneratingUnit: A generating unit may have a gross active power to net active power curve, describing the losses and
      auxiliary power requirements of the unit.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    GeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GrossToNetActivePowerCurve\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "GeneratingUnit": [
                self.profiles.EQ.value,
            ],
        }
