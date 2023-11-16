# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
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

    BaseVoltage: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # ConnectivityNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]}) # noqa: E501

    ConnectivityNodeContainer: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
            ]
        },
    )

    # *Association not used*
    # Type M:1..n in CIM
    # Terminal : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]})

    ReportingGroup: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
            ]
        },
    )

    # *Association not used*
    # Type M:0..1 in CIM
    # SvInjection : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]})

    # *Association not used*
    # Type M:0..1 in CIM
    # SvVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]})

    # *Association not used*
    # Type M:0..1 in CIM
    # AngleRefTopologicalIsland : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # TopologicalIsland : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.SV,
        }
