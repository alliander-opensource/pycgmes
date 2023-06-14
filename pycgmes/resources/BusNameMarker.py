"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to TopologicalNodes. Associated with one or more terminals that are normally
      connected with the bus name.    The associated terminals are normally connected by non-retained switches. For
      a ring bus station configuration, all BusbarSection terminals in the ring are typically associated.   For a
      breaker and a half scheme, both BusbarSections would normally be associated.  For a ring bus, all
      BusbarSections would normally be associated.  For a "straight" busbar configuration, normally only the main
      terminal at the BusbarSection would be associated.

    Terminal: The terminals associated with this bus name marker.
    priority: Priority of bus name marker for use as topology bus name.  Use 0 for do not care.  Use 1 for highest
      priority.  Use 2 as priority is less than 1 and so on.
    ReportingGroup: The reporting group to which this bus name marker belongs.
    """

    # *Association not used*
    # Terminal : list = field(default_factory=list)  # Type M:1..n in CIM
    priority: int = 0  # Type #Integer in CIM
    ReportingGroup: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=BusNameMarker"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "Terminal": [
                Profile.EQ.value,
            ],
            "priority": [
                Profile.EQ.value,
            ],
            "ReportingGroup": [
                Profile.EQ.value,
            ],
        }
