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
class LoadResponseCharacteristic(IdentifiedObject):
    """
    Models the characteristic response of the load demand due to changes in system conditions such as voltage and
      frequency. It is not related to demand response. If LoadResponseCharacteristic.exponentModel is True, the
      exponential voltage or frequency dependent models are specified and used as to calculate active and reactive
      power components of the load model. The equations to calculate active and reactive power components of the
      load model are internal to the power flow calculation, hence they use different quantities depending on the
      use case of the data exchange.  The equations for exponential voltage dependent load model injected power are:
      pInjection= Pnominal* (Voltage/cim:BaseVoltage.nominalVoltage) **
      cim:LoadResponseCharacteristic.pVoltageExponent qInjection= Qnominal* (Voltage/cim:BaseVoltage.nominalVoltage)
      ** cim:LoadResponseCharacteristic.qVoltageExponent Where:  1) * means "multiply" and ** is "raised to power
      of"; 2) Pnominal and Qnominal represent the active power and reactive power at nominal voltage as any load
      described by the voltage exponential model shall be given at nominal voltage.  This means that
      EnergyConsumer.p and EnergyConsumer.q  are at nominal voltage. 3) After power flow is solved:  -pInjection and
      qInjection correspond to SvPowerflow.p and SvPowerflow.q respectively.   - Voltage corresponds to SvVoltage.v
      at the TopologicalNode where the load is connected.

    EnergyConsumer: The set of loads that have the response characteristics.
    exponentModel: Indicates the exponential voltage dependency model is to be used. If false, the coefficient model is
      to be used. The exponential voltage dependency model consist of the attributes: -
      pVoltageExponent - qVoltageExponent - pFrequencyExponent - qFrequencyExponent. The coefficient
      model consist of the attributes: - pConstantImpedance - pConstantCurrent - pConstantPower -
      qConstantImpedance - qConstantCurrent - qConstantPower. The sum of pConstantImpedance,
      pConstantCurrent and pConstantPower shall equal 1. The sum of qConstantImpedance,
      qConstantCurrent and qConstantPower shall equal 1.
    pConstantCurrent: Portion of active power load modelled as constant current.
    pConstantImpedance: Portion of active power load modelled as constant impedance.
    pConstantPower: Portion of active power load modelled as constant power.
    pFrequencyExponent: Exponent of per unit frequency effecting active power.
    pVoltageExponent: Exponent of per unit voltage effecting real power.
    qConstantCurrent: Portion of reactive power load modelled as constant current.
    qConstantImpedance: Portion of reactive power load modelled as constant impedance.
    qConstantPower: Portion of reactive power load modelled as constant power.
    qFrequencyExponent: Exponent of per unit frequency effecting reactive power.
    qVoltageExponent: Exponent of per unit voltage effecting reactive power.
    """

    EnergyConsumer: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    exponentModel: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    pConstantCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    pConstantImpedance: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    pConstantPower: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    pFrequencyExponent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    pVoltageExponent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    qConstantCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    qConstantImpedance: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    qConstantPower: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    qFrequencyExponent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    qVoltageExponent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
