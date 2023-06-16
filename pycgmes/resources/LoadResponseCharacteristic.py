"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
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
    # EnergyConsumer : list = field(default_factory=list)  # Type M:0..n in CIM
    exponentModel: bool = False  # Type #Boolean in CIM
    pConstantCurrent: float = 0.0  # Type #Float in CIM
    pConstantImpedance: float = 0.0  # Type #Float in CIM
    pConstantPower: float = 0.0  # Type #Float in CIM
    pFrequencyExponent: float = 0.0  # Type #Float in CIM
    pVoltageExponent: float = 0.0  # Type #Float in CIM
    qConstantCurrent: float = 0.0  # Type #Float in CIM
    qConstantImpedance: float = 0.0  # Type #Float in CIM
    qConstantPower: float = 0.0  # Type #Float in CIM
    qFrequencyExponent: float = 0.0  # Type #Float in CIM
    qVoltageExponent: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadResponseCharacteristic"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.EQ.value,
            ],
            # Attributes
            "EnergyConsumer": [
                Profile.EQ.value,
            ],
            "exponentModel": [
                Profile.EQ.value,
            ],
            "pConstantCurrent": [
                Profile.EQ.value,
            ],
            "pConstantImpedance": [
                Profile.EQ.value,
            ],
            "pConstantPower": [
                Profile.EQ.value,
            ],
            "pFrequencyExponent": [
                Profile.EQ.value,
            ],
            "pVoltageExponent": [
                Profile.EQ.value,
            ],
            "qConstantCurrent": [
                Profile.EQ.value,
            ],
            "qConstantImpedance": [
                Profile.EQ.value,
            ],
            "qConstantPower": [
                Profile.EQ.value,
            ],
            "qFrequencyExponent": [
                Profile.EQ.value,
            ],
            "qVoltageExponent": [
                Profile.EQ.value,
            ],
        }
