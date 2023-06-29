"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .AuxiliaryEquipment import AuxiliaryEquipment


@dataclass(config=DataclassConfig)
class SurgeArrester(AuxiliaryEquipment):
    """
    Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the
      said equipment against transient voltage transients caused by lightning or switching activity.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
