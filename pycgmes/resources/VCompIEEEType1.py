"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics
from .PU import PU
from .Seconds import Seconds


@dataclass
class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is common to all
      excitation system models described in the IEEE Standard.  Parameter details:  If Rc and Xc are set to zero,
      the load compensation is not employed and the behaviour is as a simple sensing circuit.   If all parameters
      (Rc, Xc and Tr) are set to zero, the standard model VCompIEEEType1 is bypassed.  Reference: IEEE 421.5-2005 4.

    rc: Resistive component of compensation of a generator (Rc) (>= 0).
    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    xc: Reactive component of compensation of a generator (Xc) (>= 0).
    """

    rc: float = Field(
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

    tr: float = Field(
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

    xc: float = Field(
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
