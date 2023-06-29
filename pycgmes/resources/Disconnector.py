"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Switch import Switch


@dataclass(config=DataclassConfig)
class Disconnector(Switch):
    """
    A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or
      for isolating a circuit or equipment from a source of power. It is required to open or close circuits when
      negligible current is broken or made.

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
            Profile.SSH,
        }
