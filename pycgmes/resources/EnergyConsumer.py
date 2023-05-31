"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyConnection import EnergyConnection


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=EnergyConsumer\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.EQ.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "pfixed": [
                self.profiles.EQ.value,
            ],
            "pfixedPct": [
                self.profiles.EQ.value,
            ],
            "qfixed": [
                self.profiles.EQ.value,
            ],
            "qfixedPct": [
                self.profiles.EQ.value,
            ],
            "LoadResponse": [
                self.profiles.EQ.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
            "LoadDynamics": [
                self.profiles.DY.value,
            ],
        }
