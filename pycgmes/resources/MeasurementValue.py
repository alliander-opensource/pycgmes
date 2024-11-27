"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IOPoint import IOPoint


@dataclass
class MeasurementValue(IOPoint):
    """
    The current state for a measurement. A state value is an instance of a measurement from a specific source.
      Measurements can be associated with many state values, each representing a different source for the
      measurement.

    MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink,
      manual, etc. User conventions for the names of sources are contained in the
      introduction to IEC 61970-301.
    sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the
      sensor is used under  reference conditions.
    timeStamp: The time when the value was last updated.
    """

    MeasurementValueQuality: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    MeasurementValueSource: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    sensorAccuracy: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PerCent",
        },
    )

    timeStamp: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "DateTime",
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
