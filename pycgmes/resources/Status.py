"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class Status(Base):
    """
    Current status information relevant to an entity.

    value: Status value at `dateTime`; prior status changes may have been kept in instances of activity records
      associated with the object to which this status applies.
    dateTime: Date and time for which status `value` applies.
    remark: Pertinent information regarding the current `value`, as free form text.
    reason: Reason code or explanation for why an object went to the current status `value`.
    """

    value: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    dateTime: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    remark: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    reason: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
