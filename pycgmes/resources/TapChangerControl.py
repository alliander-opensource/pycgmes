"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .RegulatingControl import RegulatingControl


@dataclass(config=DataclassConfig)
class TapChangerControl(RegulatingControl, ModuleType):
    """
    Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level
      and compensation of the voltage drop by tap adjustment.

    TapChanger: The tap changers that participates in this regulating tap control scheme.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return TapChangerControl(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # TapChanger : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import TapChangerControl"
# work as well as
# "from TapChangerControl import TapChangerControl".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = TapChangerControl
