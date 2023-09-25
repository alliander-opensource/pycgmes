"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCChopper(DCConductingEquipment):
    """
    Low resistance equipment used in the internal DC circuit to balance voltages. It has typically positive and negative
      pole terminals and a ground.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
