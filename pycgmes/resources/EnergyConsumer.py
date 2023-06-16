"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class EnergyConsumer(EnergyConnection):
    """
    Generic user of energy - a  point of consumption on the power system model. EnergyConsumer.pfixed, .qfixed,
      .pfixedPct and .qfixedPct have meaning only if there is no LoadResponseCharacteristic associated with
      EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to False.

    pfixed: Active power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    pfixedPct: Fixed active power as a percentage of load group fixed active power. Used to represent the time-varying
      components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    qfixed: Reactive power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    qfixedPct: Fixed reactive power as a percentage of load group fixed reactive power. Used to represent the time-
      varying components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power.
    p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    LoadDynamics: Load dynamics model used to describe dynamic behaviour of this energy consumer.
    """

    pfixed: float = 0.0  # Type #ActivePower in CIM
    pfixedPct: float = 0.0  # Type #PerCent in CIM
    qfixed: float = 0.0  # Type #ReactivePower in CIM
    qfixedPct: float = 0.0  # Type #PerCent in CIM
    LoadResponse: Optional[str] = None  # Type M:0..1 in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM
    LoadDynamics: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EnergyConsumer"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "pfixed": [
                Profile.EQ.value,
            ],
            "pfixedPct": [
                Profile.EQ.value,
            ],
            "qfixed": [
                Profile.EQ.value,
            ],
            "qfixedPct": [
                Profile.EQ.value,
            ],
            "LoadResponse": [
                Profile.EQ.value,
            ],
            "p": [
                Profile.SSH.value,
            ],
            "q": [
                Profile.SSH.value,
            ],
            "LoadDynamics": [
                Profile.DY.value,
            ],
        }
