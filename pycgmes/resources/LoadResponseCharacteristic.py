"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # EnergyConsumer : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    exponentModel: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pConstantCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pConstantImpedance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pConstantPower: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pFrequencyExponent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pVoltageExponent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qConstantCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qConstantImpedance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qConstantPower: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qFrequencyExponent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qVoltageExponent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
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
