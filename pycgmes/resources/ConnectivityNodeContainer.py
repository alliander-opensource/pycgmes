"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    TopologicalNode: The topological nodes which belong to this connectivity node container.
    ConnectivityNodes: Connectivity nodes which belong to this connectivity node container.
    """

    # *Association not used*
    # TopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # ConnectivityNodes : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ConnectivityNodeContainer"]
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
                Profile.TP.value,
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                Profile.TP.value,
            ],
            "ConnectivityNodes": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
        }
