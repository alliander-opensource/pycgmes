"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class PowerSystemResource(IdentifiedObject, ModuleType):
    """
    A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many
      individual items of equipment such as a substation, or an organisational entity such as sub-control area.
      Power system resources can have measurements associated.

    Location: Location of this power system resource.
    Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a
      synchronous machine or capacitor bank breaker actuator.
    Measurements: The measurements associated with this power system resource.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PowerSystemResource(*args, **kwargs)

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # Location : Optional[str] = Field(default=None, in_profiles = [Profile.GL, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Controls : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Measurements : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import PowerSystemResource"
# work as well as
# "from PowerSystemResource import PowerSystemResource".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PowerSystemResource
