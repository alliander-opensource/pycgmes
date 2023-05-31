"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class TopologicalNode(IdentifiedObject):
    """
    For a detailed substation model a topological node is a set of connectivity nodes that, in the current network
      state, are connected together through any type of closed switches, including  jumpers. Topological nodes
      change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning
      model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in
      a model builder tool. Topological nodes maintained this way are also called "busses".

    BaseVoltage: The base voltage of the topological node.
    ConnectivityNodes: The connectivity nodes combine together to form this topological node.  May depend on the current
      state of switches in the network.
    ConnectivityNodeContainer: The connectivity node container to which the topological node belongs.
    Terminal: The terminals associated with the topological node.   This can be used as an alternative to the
      connectivity node path to terminal, thus making it unnecessary to model connectivity nodes in some
      cases.   Note that if connectivity nodes are in the model, this association would probably not be
      used as an input specification.
    ReportingGroup: The reporting group to which the topological node belongs.
    SvInjection: The injection flows state variables associated with the topological node.
    SvVoltage: The state voltage associated with the topological node.
    AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle
      reference node for each island.
    TopologicalIsland: A topological node belongs to a topological island.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    BaseVoltage: Optional[str] = None  # Type M:1..1 in CIM
    # *Association not used*
    # ConnectivityNodes : list = field(default_factory=list)  # Type M:0..n in CIM
    ConnectivityNodeContainer: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # Terminal : list = field(default_factory=list)  # Type M:1..n in CIM
    ReportingGroup: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # SvInjection : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # SvVoltage : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # AngleRefTopologicalIsland : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # TopologicalIsland : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TopologicalNode\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "BaseVoltage": [
                self.profiles.TP.value,
            ],
            "ConnectivityNodes": [
                self.profiles.TP.value,
            ],
            "ConnectivityNodeContainer": [
                self.profiles.TP.value,
            ],
            "Terminal": [
                self.profiles.TP.value,
            ],
            "ReportingGroup": [
                self.profiles.TP.value,
            ],
            "SvInjection": [
                self.profiles.SV.value,
            ],
            "SvVoltage": [
                self.profiles.SV.value,
            ],
            "AngleRefTopologicalIsland": [
                self.profiles.SV.value,
            ],
            "TopologicalIsland": [
                self.profiles.SV.value,
            ],
        }
