"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.

    OperationalLimit: The operational limits associated with this type of limit.
    acceptableDuration: The nominal acceptable duration of the limit. Limits are commonly expressed in terms of the time
      limit for which the limit is normally acceptable. The actual acceptable duration of a
      specific limit may depend on other local factors such as temperature or wind speed. The
      attribute has meaning only if the flag isInfiniteDuration is set to false, hence it shall
      not be exchanged when isInfiniteDuration is set to true.
    direction: The direction of the limit.
    isInfiniteDuration: Defines if the operational limit type has infinite duration. If true, the limit has infinite
      duration. If false, the limit has definite duration which is defined by the attribute
      acceptableDuration.
    kind: Types of limits defined in the ENTSO-E Operational Handbook Policy 3.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # OperationalLimit : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    acceptableDuration: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    direction: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    isInfiniteDuration: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    kind: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
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
        }
