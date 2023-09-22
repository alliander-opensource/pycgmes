"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class TownDetail(Base, ModuleType):
    """
    Town details, in the context of address.

    code: Town code.
    section: Town section. For example, it is common for there to be 36 sections per township.
    name: Town name.
    stateOrProvince: Name of the state or province.
    country: Name of the country.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return TownDetail(*args, **kwargs)

    code: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    section: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    name: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    stateOrProvince: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    country: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import TownDetail"
# work as well as
# "from TownDetail import TownDetail".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = TownDetail
