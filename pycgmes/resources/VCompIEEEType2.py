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

from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass(config=DataclassConfig)
class VCompIEEEType2(VoltageCompensatorDynamics, ModuleType):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return VCompIEEEType2(*args, **kwargs)

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:2..n in CIM  # pylint: disable-next=line-too-long
    # GenICompensationForGenJ : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import VCompIEEEType2"
# work as well as
# "from VCompIEEEType2 import VCompIEEEType2".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = VCompIEEEType2
