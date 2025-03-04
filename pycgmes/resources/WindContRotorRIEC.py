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
class WindContRotorRIEC(IdentifiedObject):
    """
    Rotor resistance control model. Reference: IEC 61400-27-1:2015, 5.6.5.3.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model.
    WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is
      associated.
    kirr: Integral gain in rotor resistance PI controller (KIrr). It is a type-dependent parameter.
    komegafilt: Filter gain for generator speed measurement (Komegafilt). It is a type-dependent parameter.
    kpfilt: Filter gain for power measurement (Kpfilt). It is a type-dependent parameter.
    kprr: Proportional gain in rotor resistance PI controller (KPrr). It is a type-dependent parameter.
    rmax: Maximum rotor resistance (rmax) (> WindContRotorRIEC.rmin). It is a type-dependent parameter.
    rmin: Minimum rotor resistance (rmin) (< WindContRotorRIEC.rmax). It is a type-dependent parameter.
    tomegafiltrr: Filter time constant for generator speed measurement (Tomegafiltrr) (>= 0). It is a type-dependent
      parameter.
    tpfiltrr: Filter time constant for power measurement (Tpfiltrr) (>= 0). It is a type-dependent parameter.
    """

    WindDynamicsLookupTable: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    WindGenTurbineType2IEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    kirr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    komegafilt: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    kpfilt: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    kprr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    rmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    rmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "PU",
        },
    )

    tomegafiltrr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    tpfiltrr: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Seconds",
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.DY
