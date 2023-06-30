"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCChopper(DCConductingEquipment):
    """
    Low resistance equipment used in the internal DC circuit to balance voltages. It has typically positive and negative
      pole terminals and a ground.

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
