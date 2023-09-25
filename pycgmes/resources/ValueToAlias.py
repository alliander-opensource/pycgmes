"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ValueToAlias(IdentifiedObject):
    """
    Describes the translation of one particular value into a name, e.g. 1 as "Open".

    ValueAliasSet: The ValueAliasSet having the ValueToAlias mappings.
    value: The value that is mapped.
    """

    ValueAliasSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    value: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
