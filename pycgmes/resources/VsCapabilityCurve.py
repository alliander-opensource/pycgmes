"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Curve import Curve


@dataclass(config=DataclassConfig)
class VsCapabilityCurve(Curve, ModuleType):
    """
    The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and Qmax on Y1-axis and Y2-axis.

    VsConverterDCSides: All converters with this capability curve.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return VsCapabilityCurve(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # VsConverterDCSides : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import VsCapabilityCurve"
# work as well as
# "from VsCapabilityCurve import VsCapabilityCurve".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = VsCapabilityCurve
