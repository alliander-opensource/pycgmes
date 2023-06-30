"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    Describes a tap changer with a table defining the relation between the tap step and the phase angle difference
      across the transformer.

    PhaseTapChangerTable: The phase tap changer table for this phase tap changer.
    """

    PhaseTapChangerTable: Optional[str] = Field(
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
            Profile.SSH,
        }
