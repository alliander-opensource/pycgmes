"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """
    The non-linear phase tap changer describes the non-linear behaviour of a phase tap changer. This is a base class for
      the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in IEC
      61970-301.

    voltageStepIncrement: The voltage step increment on the out of phase winding (the PowerTransformerEnd where the
      TapChanger is located) specified in percent of rated voltage of the PowerTransformerEnd.
      A positive value means a positive voltage variation from the Terminal at the
      PowerTransformerEnd, where the TapChanger is located, into the transformer. When the
      increment is negative, the voltage decreases when the tap step increases.
    xMax: The reactance depends on the tap position according to a `u` shaped curve. The maximum reactance (xMax)
      appears at the low and high tap positions. Depending on the `u` curve the attribute can be either higher
      or lower than PowerTransformerEnd.x.
    xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear
      at the mid tap position.   PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and
      PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used.
    """

    voltageStepIncrement: float = Field(
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
            "attribute_class": "PerCent",
        },
    )

    xMax: float = Field(
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
            "attribute_class": "Reactance",
        },
    )

    xMin: float = Field(
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
            "attribute_class": "Reactance",
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
