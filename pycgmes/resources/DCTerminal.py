"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .DCBaseTerminal import DCBaseTerminal


@dataclass(config=DataclassConfig)
class DCTerminal(DCBaseTerminal):
    """
    An electrical connection point to generic DC conducting equipment.

    DCConductingEquipment: An DC  terminal belong to a DC conducting equipment.
    """

    DCConductingEquipment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
            Profile.SSH,
        }
