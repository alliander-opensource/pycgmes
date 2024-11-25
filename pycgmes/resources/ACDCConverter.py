"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ConductingEquipment import ConductingEquipment
from .ActivePower import ActivePower
from .ActivePowerPerCurrentFlow import ActivePowerPerCurrentFlow
from .ApparentPower import ApparentPower
from .CurrentFlow import CurrentFlow
from .Integer import Integer
from .ReactivePower import ReactivePower
from .Resistance import Resistance
from .Voltage import Voltage


@dataclass
class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching
      devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    DCTerminals: A DC converter have DC converter terminals. A converter has two DC converter terminals.
    PccTerminal: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power
      transformer (or switch) closest to the AC network.
    baseS: Base apparent power of the converter pole. The attribute shall be a positive value.
    idc: Converter DC current, also called Id. It is converter`s state variable, result from power flow.
    idleLoss: Active power loss in pole at no power transfer. It is converter`s configuration data used in power flow.
      The attribute shall be a positive value.
    maxP: Maximum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    maxUdc: The maximum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    minP: Minimum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    minUdc: The minimum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    numberOfValves: Number of valves in the converter. Used in loss calculations.
    p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2. For lossless
      operation Pdc=Pac. For rectifier operation with losses Pdc=Pac-lossP. For inverter operation with
      losses Pdc=Pac+lossP. It is converter`s state variable used in power flow. The attribute shall be a
      positive value.
    q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    ratedUdc: Rated converter DC voltage, also called UdN. The attribute shall be a positive value. It is converter`s
      configuration data used in power flow. For instance a bipolar HVDC link with value  200 kV has a
      400kV difference between the dc lines.
    resistiveLoss: It is converter`s configuration data used in power flow. Refer to poleLossP. The attribute shall be a
      positive value.
    switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. The attribute
      shall be a positive value.
    targetPpcc: Real power injection target in AC grid, at point of common coupling.  Load sign convention is used, i.e.
      positive sign means flow out from a node.
    targetUdc: Target value for DC voltage magnitude. The attribute shall be a positive value.
    uc: Line-to-line converter voltage, the voltage at the AC side of the valve. It is converter`s state variable,
      result from power flow. The attribute shall be a positive value.
    udc: Converter voltage at the DC side, also called Ud. It is converter`s state variable, result from power flow. The
      attribute shall be a positive value.
    valveU0: Valve threshold voltage, also called Uvalve. Forward voltage drop when the valve is conducting. Used in
      loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0.
    """

    DCTerminals: list = Field(
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

    PccTerminal: Optional[str] = Field(
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

    baseS: float = Field(
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
            "attribute_class": ApparentPower,
        },
    )

    idc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": CurrentFlow,
        },
    )

    idleLoss: float = Field(
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

    maxP: float = Field(
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

    maxUdc: float = Field(
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
            "attribute_class": Voltage,
        },
    )

    minP: float = Field(
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

    minUdc: float = Field(
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
            "attribute_class": Voltage,
        },
    )

    numberOfValves: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Integer,
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

    poleLossP: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
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

    ratedUdc: float = Field(
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
            "attribute_class": Voltage,
        },
    )

    resistiveLoss: float = Field(
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
            "attribute_class": Resistance,
        },
    )

    switchingLoss: float = Field(
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
            "attribute_class": ActivePowerPerCurrentFlow,
        },
    )

    targetPpcc: float = Field(
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

    targetUdc: float = Field(
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
            "attribute_class": Voltage,
        },
    )

    uc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": Voltage,
        },
    )

    udc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": Voltage,
        },
    )

    valveU0: float = Field(
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
            "attribute_class": Voltage,
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
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
