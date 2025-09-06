"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    SvTapStep: The tap step state associated with the tap changer.
    TapChangerControl: The regulating control scheme in which this tap changer participates.
    TapSchedules: A TapChanger can have TapSchedules.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep.
    lowStep: Lowest possible tap step position, retard from neutral.
    ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities.
    neutralStep: The neutral tap step position for this winding. The attribute shall be equal to or greater than lowStep
      and equal or less than highStep. It is the step position where the voltage is neutralU when the
      other terminals of the transformer are at the ratedU.  If there are other tap changers on the
      transformer those taps are kept constant at their neutralStep.
    neutralU: Voltage at which the winding operates at the neutral tap setting. It is the voltage at the terminal of the
      PowerTransformerEnd associated with the tap changer when all tap changers on the transformer are at
      their neutralStep position.  Normally neutralU of the tap changer is the same as ratedU of the
      PowerTransformerEnd, but it can differ in special cases such as when the tapping mechanism is
      separate from the winding more common on lower voltage transformers. This attribute is not relevant
      for PhaseTapChangerAsymmetrical, PhaseTapChangerSymmetrical and PhaseTapChangerLinear.
    normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer
      indicates the current physical tap setting. The attribute shall be equal to or greater than
      lowStep and equal to or less than highStep.
    step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support
      continuous tap variables. The reasons for continuous value are to support study cases where no discrete
      tap changer has yet been designed, a solution where a narrow voltage band forces the tap step to
      oscillate or to accommodate for a continuous solution as input. The attribute shall be equal to or
      greater than lowStep and equal to or less than highStep.
    """

    SvTapStep: Optional[str] = Field(
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

    TapChangerControl: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
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

    TapSchedules: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    controlEnabled: bool = Field(
        default=False,
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
            "attribute_class": "Boolean",
        },
    )

    highStep: int = Field(
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

    lowStep: int = Field(
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

    ltcFlag: bool = Field(
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

    neutralStep: int = Field(
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

    neutralU: float = Field(
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

    normalStep: int = Field(
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

    step: float = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
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
