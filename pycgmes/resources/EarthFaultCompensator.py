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

from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class EarthFaultCompensator(ConductingEquipment, ModuleType):
    """
    A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults.
      An earth fault compensator device modelled with a single terminal implies a second terminal solidly connected
      to ground.  If two terminals are modelled, the ground is not assumed and normal connection rules apply.

    r: Nominal resistance of device.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return EarthFaultCompensator(*args, **kwargs)

    r: float = Field(
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
# "import EarthFaultCompensator"
# work as well as
# "from EarthFaultCompensator import EarthFaultCompensator".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = EarthFaultCompensator
