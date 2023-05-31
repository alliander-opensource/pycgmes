"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .EquivalentEquipment import EquivalentEquipment


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=EquivalentBranch\n"
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
                self.profiles.SC.value,
            ],
            # Attributes
            "r": [
                self.profiles.EQ.value,
            ],
            "r21": [
                self.profiles.EQ.value,
            ],
            "x": [
                self.profiles.EQ.value,
            ],
            "x21": [
                self.profiles.EQ.value,
            ],
            "negativeR12": [
                self.profiles.SC.value,
            ],
            "negativeR21": [
                self.profiles.SC.value,
            ],
            "negativeX12": [
                self.profiles.SC.value,
            ],
            "negativeX21": [
                self.profiles.SC.value,
            ],
            "positiveR12": [
                self.profiles.SC.value,
            ],
            "positiveR21": [
                self.profiles.SC.value,
            ],
            "positiveX12": [
                self.profiles.SC.value,
            ],
            "positiveX21": [
                self.profiles.SC.value,
            ],
            "zeroR12": [
                self.profiles.SC.value,
            ],
            "zeroR21": [
                self.profiles.SC.value,
            ],
            "zeroX12": [
                self.profiles.SC.value,
            ],
            "zeroX21": [
                self.profiles.SC.value,
            ],
        }
