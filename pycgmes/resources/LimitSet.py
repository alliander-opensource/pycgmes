"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LimitSet(IdentifiedObject):
    """
    Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets
      corresponding to seasonal or other changing conditions. The condition is captured in the name and description
      attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used
      this way.

    isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for
      Measurements and Controls.
    """

    isPercentageLimits: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
