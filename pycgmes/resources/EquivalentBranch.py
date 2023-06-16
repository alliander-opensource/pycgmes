"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentBranch(EquivalentEquipment):
    """
    The class represents equivalent branches. In cases where a transformer phase shift is modelled and the
      EquivalentBranch is spanning the same nodes, the impedance quantities for the EquivalentBranch shall consider
      the needed phase shift.

    r: Positive sequence series resistance of the reduced branch.
    r21: Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is
      optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r
      is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch
      is a result of network reduction prior to the data exchange.
    x: Positive sequence series reactance of the reduced branch.
    x21: Reactance from terminal sequence 2 to terminal sequence 1. Used for steady state power flow. This attribute is
      optional and represents an unbalanced network such as off-nominal phase shifter. If only
      EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x. Usage
      rule: EquivalentBranch is a result of network reduction prior to the data exchange.
    negativeR12: Negative sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeR21: Negative sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeX12: Negative sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    negativeX21: Negative sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveR12: Positive sequence series resistance from terminal sequence  1 to terminal sequence 2 . Used for short
      circuit data exchange according to IEC 60909.  EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveR21: Positive sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveX12: Positive sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveX21: Positive sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    zeroR12: Zero sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the
      data exchange.
    zeroR21: Zero sequence series resistance from terminal sequence  2 to terminal sequence 1. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX12: Zero sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX21: Zero sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data
      exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to
      the data exchange.
    """

    r: float = 0.0  # Type #Resistance in CIM
    r21: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    x21: float = 0.0  # Type #Reactance in CIM
    negativeR12: float = 0.0  # Type #Resistance in CIM
    negativeR21: float = 0.0  # Type #Resistance in CIM
    negativeX12: float = 0.0  # Type #Reactance in CIM
    negativeX21: float = 0.0  # Type #Reactance in CIM
    positiveR12: float = 0.0  # Type #Resistance in CIM
    positiveR21: float = 0.0  # Type #Resistance in CIM
    positiveX12: float = 0.0  # Type #Reactance in CIM
    positiveX21: float = 0.0  # Type #Reactance in CIM
    zeroR12: float = 0.0  # Type #Resistance in CIM
    zeroR21: float = 0.0  # Type #Resistance in CIM
    zeroX12: float = 0.0  # Type #Reactance in CIM
    zeroX21: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EquivalentBranch"]
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
                Profile.SC.value,
            ],
            # Attributes
            "r": [
                Profile.EQ.value,
            ],
            "r21": [
                Profile.EQ.value,
            ],
            "x": [
                Profile.EQ.value,
            ],
            "x21": [
                Profile.EQ.value,
            ],
            "negativeR12": [
                Profile.SC.value,
            ],
            "negativeR21": [
                Profile.SC.value,
            ],
            "negativeX12": [
                Profile.SC.value,
            ],
            "negativeX21": [
                Profile.SC.value,
            ],
            "positiveR12": [
                Profile.SC.value,
            ],
            "positiveR21": [
                Profile.SC.value,
            ],
            "positiveX12": [
                Profile.SC.value,
            ],
            "positiveX21": [
                Profile.SC.value,
            ],
            "zeroR12": [
                Profile.SC.value,
            ],
            "zeroR21": [
                Profile.SC.value,
            ],
            "zeroX12": [
                Profile.SC.value,
            ],
            "zeroX21": [
                Profile.SC.value,
            ],
        }
