"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EquivalentEquipment import EquivalentEquipment


@dataclass
class EquivalentInjection(EquivalentEquipment):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point
      of connection.

    maxP: Maximum active power of the injection.
    maxQ: Maximum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for
      short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
    minP: Minimum active power of the injection.
    minQ: Minimum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for
      short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
    regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local
      voltage. If true the EquivalentInjection can regulate. If false the EquivalentInjection
      cannot regulate. ReactiveCapabilityCurve can only be associated with EquivalentInjection
      if the flag is true.
    ReactiveCapabilityCurve: The reactive capability curve used by this equivalent injection.
    r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    regulationStatus: Specifies the regulation status of the EquivalentInjection.  True is regulating.  False is not
      regulating.
    regulationTarget: The target voltage for voltage regulation. The attribute shall be a positive value.
    p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    maxP: float = 0.0  # Type #ActivePower in CIM
    maxQ: float = 0.0  # Type #ReactivePower in CIM
    minP: float = 0.0  # Type #ActivePower in CIM
    minQ: float = 0.0  # Type #ReactivePower in CIM
    regulationCapability: bool = False  # Type #Boolean in CIM
    ReactiveCapabilityCurve: Optional[str] = None  # Type M:0..1 in CIM
    r: float = 0.0  # Type #Resistance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    r2: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    x0: float = 0.0  # Type #Reactance in CIM
    x2: float = 0.0  # Type #Reactance in CIM
    regulationStatus: bool = False  # Type #Boolean in CIM
    regulationTarget: float = 0.0  # Type #Voltage in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EquivalentInjection\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "maxP": [
                self.profiles.EQ.value,
            ],
            "maxQ": [
                self.profiles.EQ.value,
            ],
            "minP": [
                self.profiles.EQ.value,
            ],
            "minQ": [
                self.profiles.EQ.value,
            ],
            "regulationCapability": [
                self.profiles.EQ.value,
            ],
            "ReactiveCapabilityCurve": [
                self.profiles.EQ.value,
            ],
            "r": [
                self.profiles.SC.value,
            ],
            "r0": [
                self.profiles.SC.value,
            ],
            "r2": [
                self.profiles.SC.value,
            ],
            "x": [
                self.profiles.SC.value,
            ],
            "x0": [
                self.profiles.SC.value,
            ],
            "x2": [
                self.profiles.SC.value,
            ],
            "regulationStatus": [
                self.profiles.SSH.value,
            ],
            "regulationTarget": [
                self.profiles.SSH.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
        }
