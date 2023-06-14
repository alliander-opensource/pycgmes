"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ReportingGroup(IdentifiedObject):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.

    TopologicalNode: The topological nodes that belong to the reporting group.
    BusNameMarker: The bus name markers that belong to this reporting group.
    """

    # *Association not used*
    # TopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # BusNameMarker : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ReportingGroup"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.TP.value,
                Profile.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                Profile.TP.value,
            ],
            "BusNameMarker": [
                Profile.EQ.value,
            ],
        }
