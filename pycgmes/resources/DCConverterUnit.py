"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .DCEquipmentContainer import DCEquipmentContainer


@dataclass
class DCConverterUnit(DCEquipmentContainer):
    """
    Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the
      point of common coupling - DC side, essentially one or more converters, together with one or more converter
      transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any,
      used for conversion.

    Substation: The containing substation of the DC converter unit.
    operationMode: The operating mode of an HVDC bipole (bipolar, monopolar metallic return, etc).
    """

    Substation: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    operationMode: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
