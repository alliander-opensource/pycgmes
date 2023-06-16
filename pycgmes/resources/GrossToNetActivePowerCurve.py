"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Curve import Curve


@dataclass(config=DataclassConfig)
class GrossToNetActivePowerCurve(Curve):
    """
    Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the
      machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined
      measurements at the power station). Station service loads, when modelled, should be treated as non-conforming
      bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.

    GeneratingUnit: A generating unit may have a gross active power to net active power curve, describing the losses and
      auxiliary power requirements of the unit.
    """

    GeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GrossToNetActivePowerCurve"]
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
                Profile.EQ.value,
            ],
            # Attributes
            "GeneratingUnit": [
                Profile.EQ.value,
            ],
        }
