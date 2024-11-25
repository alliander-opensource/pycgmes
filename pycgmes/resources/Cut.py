"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .Switch import Switch
from .Length import Length


@dataclass
class Cut(Switch):
    """
    A cut separates a line segment into two parts. The cut appears as a switch inserted between these two parts and
      connects them together. As the cut is normally open there is no galvanic connection between the two line
      segment parts. But it is possible to close the cut to get galvanic connection. The cut terminals are oriented
      towards the line segment terminals with the same sequence number. Hence the cut terminal with sequence number
      equal to 1 is oriented to the line segment's terminal with sequence number equal to 1. The cut terminals also
      act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this,
      connectivity nodes are placed at the cut terminals. Once the connectivity nodes are in place any conducting
      equipment can be connected at them.

    ACLineSegment: The line segment to which the cut is applied.
    lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line
      segment, i.e. the line segment Terminal with sequenceNumber equal to 1.
    """

    ACLineSegment: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    lengthFromTerminal1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": Length,
        },
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

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
