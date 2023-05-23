"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # Terminal : list = field(default_factory=list)  # Type M:1..n in CIM
    priority: int = 0  # Type #Integer in CIM
    ReportingGroup: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BusNameMarker\n"
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
            "Terminal": [
                self.profiles.EQ.value,
            ],
            "priority": [
                self.profiles.EQ.value,
            ],
            "ReportingGroup": [
                self.profiles.EQ.value,
            ],
        }
