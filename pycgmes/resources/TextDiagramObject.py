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

from .DiagramObject import DiagramObject


@dataclass(config=DataclassConfig)
class TextDiagramObject(DiagramObject, ModuleType):
    """
    A diagram object for placing free-text or text derived from an associated domain object.

    text: The text that is displayed by this text diagram object.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return TextDiagramObject(*args, **kwargs)

    text: str = Field(
        default="",
        in_profiles=[
            Profile.DL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import TextDiagramObject"
# work as well as
# "from TextDiagramObject import TextDiagramObject".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = TextDiagramObject
