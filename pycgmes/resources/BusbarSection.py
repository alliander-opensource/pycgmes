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

from .Connector import Connector


@dataclass(config=DataclassConfig)
class BusbarSection(Connector, ModuleType):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation.  Voltage measurements are typically obtained from voltage transformers that are
      connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled
      with exactly one logical terminal.

    ipMax: Maximum allowable peak short-circuit current of busbar (Ipmax in IEC 60909-0).  Mechanical limit of the
      busbar in the substation itself. Used for short circuit data exchange according to IEC 60909.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return BusbarSection(*args, **kwargs)

    ipMax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
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
            Profile.SC,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import BusbarSection"
# work as well as
# "from BusbarSection import BusbarSection".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = BusbarSection
