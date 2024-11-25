"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .EnergyConnection import EnergyConnection
from .ActivePower import ActivePower
from .PerCent import PerCent
from .ReactivePower import ReactivePower


@dataclass
class EnergyConsumer(EnergyConnection):
    """
    Generic user of energy - a  point of consumption on the power system model. EnergyConsumer.pfixed, .qfixed,
      .pfixedPct and .qfixedPct have meaning only if there is no LoadResponseCharacteristic associated with
      EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to False.

    LoadDynamics: Load dynamics model used to describe dynamic behaviour of this energy consumer.
    LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power.
    p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    pfixed: Active power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    pfixedPct: Fixed active power as a percentage of load group fixed active power. Used to represent the time-varying
      components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    qfixed: Reactive power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    qfixedPct: Fixed reactive power as a percentage of load group fixed reactive power. Used to represent the time-
      varying components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    """

    LoadDynamics: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    LoadResponse: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    p: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
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

    pfixed: float = Field(
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
            "attribute_class": ActivePower,
        },
    )

    pfixedPct: float = Field(
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
            "attribute_class": PerCent,
        },
    )

    q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": ReactivePower,
        },
    )

    qfixed: float = Field(
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
            "attribute_class": ReactivePower,
        },
    )

    qfixedPct: float = Field(
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
            "attribute_class": PerCent,
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
