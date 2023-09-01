"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class EquivalentEquipment(ConductingEquipment):
    """
    The class represents equivalent objects that are the result of a network reduction. The class is the base for
      equivalent objects of different types.

    EquivalentNetwork: The equivalent where the reduced model belongs.
    """

    EquivalentNetwork: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        }
