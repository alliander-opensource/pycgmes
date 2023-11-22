# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    TopologicalNode: The topological nodes at the base voltage.
    nominalVoltage: The power system resource`s base voltage.  Shall be a positive value and not zero.
    VoltageLevel: The voltage levels having this base voltage.
    ConductingEquipment: All conducting equipment with this base voltage.  Use only when there is no voltage level
      container used and only one base voltage applies.  For example, not used for
      transformers.
    TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # TopologicalNode : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]}) # noqa: E501

    nominalVoltage: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQBD,
                Profile.EQ,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # VoltageLevel : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQBD, Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # ConductingEquipment : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # TransformerEnds : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        }
