"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .RegulatingCondEq import RegulatingCondEq


@dataclass
class ShuntCompensator(RegulatingCondEq):
    """
    A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is
      an individual capacitor or reactor. A negative value for bPerSection indicates that the compensator is a
      reactor. ShuntCompensator is a single terminal device.  Ground is implied.

    SvShuntCompensatorSections: The state for the number of shunt compensator sections in service.
    aVRDelay: An automatic voltage regulation delay (AVRDelay) which is the time delay from a change in voltage to when
      the capacitor is allowed to change state. This filters out temporary changes in voltage.
    grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded.
    maximumSections: The maximum number of sections that may be switched in.
    nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the
      voltage at which the capacitor is connected to the network.
    normalSections: The normal number of sections switched in. The value shall be between zero and
      ShuntCompensator.maximumSections.
    sections: Shunt compensator sections in use. Starting value for steady state solution. The attribute shall be a
      positive value or zero. Non integer values are allowed to support continuous variables. The reasons
      for continuous value are to support study cases where no discrete shunt compensators has yet been
      designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for
      a continuous solution as input.  For LinearShuntConpensator the value shall be between zero and
      ShuntCompensator.maximumSections. At value zero the shunt compensator conductance and admittance is
      zero. Linear interpolation of conductance and admittance between the previous and next integer
      section is applied in case of non-integer values. For NonlinearShuntCompensator-s shall only be set
      to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no interpolation between
      NonlinearShuntCompenstorPoint-s.
    voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive
      power.
    """

    SvShuntCompensatorSections: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": False,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    aVRDelay: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    grounded: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
        },
    )

    maximumSections: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Integer",
        },
    )

    nomU: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Voltage",
        },
    )

    normalSections: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Integer",
        },
    )

    sections: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    voltageSensitivity: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "VoltagePerReactivePower",
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
            Profile.SC,
            Profile.SSH,
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
