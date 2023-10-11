# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class IdentifiedObject(Base):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.

    description: The description is a free human readable text describing or naming the object. It may be non unique and
      may not correlate to a naming hierarchy.
    energyIdentCodeEic: The attribute is used for an exchange of the EIC code (Energy identification Code). The length
      of the string is 16 characters as defined by the EIC code. For details on EIC scheme
      please refer to ENTSO-E web site.
    mRID: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global
      uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID
      is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is
      mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
    name: The name is any free human readable and possibly non unique text naming the object.
    shortName: The attribute is used for an exchange of a human readable short name with length of the string 12
      characters maximum.
    DiagramObjects: The diagram objects that are associated with the domain object.
    """

    description: str = Field(
        default="",
        in_profiles=[
            Profile.TP,
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.DY,
            Profile.OP,
        ],
    )

    energyIdentCodeEic: str = Field(
        default="",
        in_profiles=[
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    mRID: str = Field(
        default="",
        in_profiles=[
            Profile.TP,
            Profile.GL,
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        ],
    )

    name: str = Field(
        default="",
        in_profiles=[
            Profile.TP,
            Profile.GL,
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SV,
            Profile.DY,
            Profile.OP,
        ],
    )

    shortName: str = Field(
        default="",
        in_profiles=[
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DiagramObjects : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.GL,
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
