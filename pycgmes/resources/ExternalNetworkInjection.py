"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .RegulatingCondEq import RegulatingCondEq


@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """
    This class represents the external network and it is used for IEC 60909 calculations.

    governorSCD: Power Frequency Bias. This is the change in power injection divided by the change in frequency and
      negated.  A positive value of the power frequency bias provides additional power injection upon a
      drop in frequency.
    maxP: Maximum active power of the injection.
    maxQ: Maximum reactive power limit. It is used for modelling of infeed for load flow exchange and not for short
      circuit modelling.
    minP: Minimum active power of the injection.
    minQ: Minimum reactive power limit. It is used for modelling of infeed for load flow exchange and not for short
      circuit modelling.
    ikSecond: Indicates whether initial symmetrical short-circuit current and power have been calculated according to
      IEC (Ik`).  Used only if short circuit calculations are done according to superposition method.
    maxInitialSymShCCurrent: Maximum initial symmetrical short-circuit currents (Ik` max) in A (Ik` = Sk`/(SQRT(3) Un)).
      Used for short circuit data exchange according to IEC 60909.
    maxR0ToX0Ratio: Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance
      (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909.
    maxR1ToX1Ratio: Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance
      (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909.
    maxZ0ToZ1Ratio: Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used
      for short circuit data exchange according to IEC 60909.
    minInitialSymShCCurrent: Minimum initial symmetrical short-circuit currents (Ik` min) in A (Ik` = Sk`/(SQRT(3) Un)).
      Used for short circuit data exchange according to IEC 60909.
    minR0ToX0Ratio: Indicates whether initial symmetrical short-circuit current and power have been calculated according
      to IEC (Ik`). Used for short circuit data exchange according to IEC 6090.
    minR1ToX1Ratio: Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance
      (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909.
    minZ0ToZ1Ratio: Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used
      for short circuit data exchange according to IEC 60909.
    voltageFactor: Voltage factor in pu, which was used to calculate short-circuit current Ik` and power Sk`.  Used only
      if short circuit calculations are done according to superposition method.
    referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care
      (default) 1 = highest priority. 2 is less than 1 and so on.
    p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for steady state solutions.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for steady state solutions.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    governorSCD: float = 0.0  # Type #ActivePowerPerFrequency in CIM
    maxP: float = 0.0  # Type #ActivePower in CIM
    maxQ: float = 0.0  # Type #ReactivePower in CIM
    minP: float = 0.0  # Type #ActivePower in CIM
    minQ: float = 0.0  # Type #ReactivePower in CIM
    ikSecond: bool = False  # Type #Boolean in CIM
    maxInitialSymShCCurrent: float = 0.0  # Type #CurrentFlow in CIM
    maxR0ToX0Ratio: float = 0.0  # Type #Float in CIM
    maxR1ToX1Ratio: float = 0.0  # Type #Float in CIM
    maxZ0ToZ1Ratio: float = 0.0  # Type #Float in CIM
    minInitialSymShCCurrent: float = 0.0  # Type #CurrentFlow in CIM
    minR0ToX0Ratio: float = 0.0  # Type #Float in CIM
    minR1ToX1Ratio: float = 0.0  # Type #Float in CIM
    minZ0ToZ1Ratio: float = 0.0  # Type #Float in CIM
    voltageFactor: float = 0.0  # Type #PU in CIM
    referencePriority: int = 0  # Type #Integer in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExternalNetworkInjection\n"
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
            "governorSCD": [
                self.profiles.EQ.value,
            ],
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
            "ikSecond": [
                self.profiles.SC.value,
            ],
            "maxInitialSymShCCurrent": [
                self.profiles.SC.value,
            ],
            "maxR0ToX0Ratio": [
                self.profiles.SC.value,
            ],
            "maxR1ToX1Ratio": [
                self.profiles.SC.value,
            ],
            "maxZ0ToZ1Ratio": [
                self.profiles.SC.value,
            ],
            "minInitialSymShCCurrent": [
                self.profiles.SC.value,
            ],
            "minR0ToX0Ratio": [
                self.profiles.SC.value,
            ],
            "minR1ToX1Ratio": [
                self.profiles.SC.value,
            ],
            "minZ0ToZ1Ratio": [
                self.profiles.SC.value,
            ],
            "voltageFactor": [
                self.profiles.SC.value,
            ],
            "referencePriority": [
                self.profiles.SSH.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
        }
