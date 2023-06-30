"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentShunt(EquivalentEquipment):
    """
    The class represents equivalent shunts.

    b: Positive sequence shunt susceptance.
    g: Positive sequence shunt conductance.
    """

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    g: float = Field(
        default=0.0,
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
        }
