"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .ActivePower import ActivePower
from .PU import PU
from .Seconds import Seconds


@dataclass
class GovGAST(TurbineGovernorDynamics):
    """
    Single shaft gas turbine.

    at: Ambient temperature load limit (Load Limit).  Typical value = 1.
    dturb: Turbine damping factor (Dturb).  Typical value = 0,18.
    kt: Temperature limiter gain (Kt).  Typical value = 3.
    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R) (>0). Typical value = 0,04.
    t1: Governor mechanism time constant (T1) (>= 0).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5.
    t2: Turbine power time constant (T2) (>= 0).  T2 represents delay due to internal energy storage of the gas turbine
      engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the
      compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power
      turbine of an aero-derivative unit, for example.  Typical value = 0,5.
    t3: Turbine exhaust temperature time constant (T3) (>= 0).  Typical value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax) (> GovGAST.vmin).  Typical value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin) (< GovGAST.vmax).  Typical value = 0.
    """

    at: float = Field(
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
            "attribute_class": PU,
        },
    )

    dturb: float = Field(
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
            "attribute_class": PU,
        },
    )

    kt: float = Field(
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
            "attribute_class": PU,
        },
    )

    mwbase: float = Field(
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
            "attribute_class": ActivePower,
        },
    )

    r: float = Field(
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
            "attribute_class": PU,
        },
    )

    t1: float = Field(
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
            "attribute_class": Seconds,
        },
    )

    t2: float = Field(
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
            "attribute_class": Seconds,
        },
    )

    t3: float = Field(
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
            "attribute_class": Seconds,
        },
    )

    vmax: float = Field(
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
            "attribute_class": PU,
        },
    )

    vmin: float = Field(
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
            "attribute_class": PU,
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
