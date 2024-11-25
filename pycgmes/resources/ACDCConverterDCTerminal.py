"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .DCBaseTerminal import DCBaseTerminal


@dataclass
class ACDCConverterDCTerminal(DCBaseTerminal):
    """
    A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the
      AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC
      equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection
      with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC
      side.

    DCConductingEquipment: A DC converter terminal belong to an DC converter.
    polarity: Represents the normal network polarity condition. Depending on the converter configuration the value shall
      be set as follows: - For a monopole with two converter terminals use DCPolarityKind `positive` and
      `negative`. - For a bi-pole or symmetric monopole with three converter terminals use DCPolarityKind
      `positive`, `middle` and `negative`.
    """

    DCConductingEquipment: Optional[str] = Field(
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

    polarity: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
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
            Profile.SSH,
            Profile.TP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
