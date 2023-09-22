"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .TapChanger import TapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChanger(TapChanger, ModuleType):
    """
    A transformer phase shifting tap model that controls the phase angle difference across the power transformer and
      potentially the active power flow through the power transformer.  This phase tap model may also impact the
      voltage magnitude.

    TransformerEnd: Transformer end to which this phase tap changer belongs.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PhaseTapChanger(*args, **kwargs)

    TransformerEnd: Optional[str] = Field(
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
            Profile.EQ,
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import PhaseTapChanger"
# work as well as
# "from PhaseTapChanger import PhaseTapChanger".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PhaseTapChanger
