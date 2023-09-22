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
class StreetAddress(Base, ModuleType):
    """
    General purpose street and postal address information.

    streetDetail: Street detail.
    townDetail: Town detail.
    status: Status of this address.
    postalCode: Postal code for the address.
    poBox: Post office box.
    language: The language in which the address is specified, using ISO 639-1 two digit language code.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return StreetAddress(*args, **kwargs)

    streetDetail: float = Field(
        default=0.0,
        in_profiles=[
            Profile.GL,
        ],
    )

    townDetail: float = Field(
        default=0.0,
        in_profiles=[
            Profile.GL,
        ],
    )

    status: float = Field(
        default=0.0,
        in_profiles=[
            Profile.GL,
        ],
    )

    postalCode: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    poBox: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    language: str = Field(
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
# "import StreetAddress"
# work as well as
# "from StreetAddress import StreetAddress".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = StreetAddress
