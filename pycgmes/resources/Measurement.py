"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class Measurement(IdentifiedObject):
    """
    A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment
      may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a
      transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow
      measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is
      intended to capture this use of Measurement and is included in the naming hierarchy based on
      EquipmentContainer. The naming hierarchy typically has Measurements as leaves, e.g. Substation-VoltageLevel-
      Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the
      network, e.g. a voltage transformer (VT) or potential transformer (PT) at a busbar or a current transformer
      (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR -
      Measurement association. Instead it is captured by the Measurement - Terminal association that is used to
      define the sensing location in the network topology. The location is defined by the connection of the Terminal
      to ConductingEquipment.  If both a Terminal and PSR are associated, and the PSR is of type
      ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance. When the
      sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal
      association is never used alone.

    PowerSystemResource: The power system resource that contains the measurement.
    Terminal: One or more measurements may be associated with a terminal in the network.
    measurementType: Specifies the type of measurement.  For example, this specifies if the measurement represents an
      indoor temperature, outdoor temperature, bus voltage, line flow, etc. When the
      measurementType is set to `Specialization`, the type of Measurement is defined in more detail
      by the specialized class which inherits from Measurement.
    phases: Indicates to which phases the measurement applies and avoids the need to use `measurementType` to also
      encode phase information (which would explode the types). The phase information in Measurement, along
      with `measurementType` and `phases` uniquely defines a Measurement for a device, based on normal
      network phase. Their meaning will not change when the computed energizing phasing is changed due to
      jumpers or other reasons. If the attribute is missing three phases (ABC) shall be assumed.
    unitMultiplier: The unit multiplier of the measured quantity.
    unitSymbol: The unit of measure of the measured quantity.
    """

    PowerSystemResource: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    Terminal: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    measurementType: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    phases: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    unitMultiplier: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    unitSymbol: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
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
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
