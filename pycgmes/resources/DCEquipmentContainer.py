# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .EquipmentContainer import EquipmentContainer


@dataclass
class DCEquipmentContainer(EquipmentContainer):
    """
    A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from
      the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC
      equipment.

    DCTopologicalNode: The topological nodes which belong to this connectivity node container.
    DCNodes: The DC nodes contained in the DC equipment container.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # DCTopologicalNode : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # DCNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
        }
