"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass
class PowerTransformer(ConductingEquipment):
    """
    An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing
      mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active
      power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A
      power transformer can be modelled with or without tanks and is intended for use in both balanced and
      unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding),
      three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The
      association from TransformerEnd to BaseVoltage should be used instead.

    PowerTransformerEnd: The ends of this power transformer.
    beforeShCircuitHighestOperatingCurrent: The highest operating current (Ib in IEC 60909-0) before short circuit
      (depends on network configuration and relevant reliability
      philosophy). It is used for calculation of the impedance correction
      factor KT defined in IEC 60909-0.
    beforeShCircuitHighestOperatingVoltage: The highest operating voltage (Ub in IEC 60909-0) before short circuit. It
      is used for calculation of the impedance correction factor KT defined
      in IEC 60909-0. This is worst case voltage on the low side winding
      (3.7.1 of IEC 60909:2001). Used to define operating conditions.
    beforeShortCircuitAnglePf: The angle of power factor before short circuit (phib in IEC 60909-0). It is used for
      calculation of the impedance correction factor KT defined in IEC 60909-0. This is
      the worst case power factor. Used to define operating conditions.
    highSideMinOperatingU: The minimum operating voltage (uQmin in IEC 60909-0) at the high voltage side (Q side) of the
      unit transformer of the power station unit. A value well established from long-term
      operating experience of the system. It is used for calculation of the impedance
      correction factor KG defined in IEC 60909-0.
    isPartOfGeneratorUnit: Indicates whether the machine is part of a power station unit. Used for short circuit data
      exchange according to IEC 60909.  It has an impact on how the correction factors are
      calculated for transformers, since the transformer is not necessarily part of a
      synchronous machine and generating unit. It is not always possible to derive this
      information from the model. This is why the attribute is necessary.
    operationalValuesConsidered: It is used to define if the data (other attributes related to short circuit data
      exchange) defines long term operational conditions or not. Used for short circuit
      data exchange according to IEC 60909.
    """

    PowerTransformerEnd: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    beforeShCircuitHighestOperatingCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "CurrentFlow",
        },
    )

    beforeShCircuitHighestOperatingVoltage: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Voltage",
        },
    )

    beforeShortCircuitAnglePf: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "AngleDegrees",
        },
    )

    highSideMinOperatingU: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Voltage",
        },
    )

    isPartOfGeneratorUnit: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
        },
    )

    operationalValuesConsidered: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
