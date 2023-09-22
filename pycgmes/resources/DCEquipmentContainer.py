"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .EquipmentContainer import EquipmentContainer


@dataclass(config=DataclassConfig)
class DCEquipmentContainer(EquipmentContainer, ModuleType):
    """
    A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from
      the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC
      equipment.

    DCTopologicalNode: The topological nodes which belong to this connectivity node container.
    DCNodes: The DC nodes contained in the DC equipment container.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCEquipmentContainer(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTopologicalNode : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCNodes : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCEquipmentContainer"
# work as well as
# "from DCEquipmentContainer import DCEquipmentContainer".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCEquipmentContainer
