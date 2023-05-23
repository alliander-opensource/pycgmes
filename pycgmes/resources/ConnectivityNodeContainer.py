"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemResource import PowerSystemResource


@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    TopologicalNode: The topological nodes which belong to this connectivity node container.
    ConnectivityNodes: Connectivity nodes which belong to this connectivity node container.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # TopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # ConnectivityNodes : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ConnectivityNodeContainer\n"
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
                self.profiles.TP.value,
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                self.profiles.TP.value,
            ],
            "ConnectivityNodes": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
        }
