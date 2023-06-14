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

        return "\n".join(
            ["class=TopologicalNode"]
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
                Profile.SV.value,
            ],
            # Attributes
            "BaseVoltage": [
                Profile.TP.value,
            ],
            "ConnectivityNodes": [
                Profile.TP.value,
            ],
            "ConnectivityNodeContainer": [
                Profile.TP.value,
            ],
            "Terminal": [
                Profile.TP.value,
            ],
            "ReportingGroup": [
                Profile.TP.value,
            ],
            "SvInjection": [
                Profile.SV.value,
            ],
            "SvVoltage": [
                Profile.SV.value,
            ],
            "AngleRefTopologicalIsland": [
                Profile.SV.value,
            ],
            "TopologicalIsland": [
                Profile.SV.value,
            ],
        }
