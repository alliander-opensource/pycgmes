"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Equipment import Equipment


@dataclass
class GeneratingUnit(Equipment):
    """
    A single or set of synchronous machines for converting mechanical power into alternating-current power. For example,
      individual machines within a set may be defined for scheduling purposes while a single control signal is
      derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional
      GeneratingUnit corresponding to the set.

    ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
    genControlSource: The source of controls for a generating unit.  Defines the control status of the generating unit.
    governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in
      frequency normalized by the nominal power of the generator and the nominal frequency and
      expressed in percent and negated. A positive value of speed change droop provides additional
      generator output upon a drop in frequency.
    longPF: Generating unit long term economic participation factor.
    maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered
      greater than this value regardless of the current operating point.
    maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit.
    minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit.
    nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes
      such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive
      value equal to or less than RotatingMachine.ratedS.
    ratedGrossMaxP: The unit`s gross rated maximum capacity (book value). The attribute shall be a positive value.
    ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power
      to the transmission grid. The attribute shall be a positive value.
    ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the
      internal plant machinery from the rated gross maximum capacity. The attribute shall be a
      positive value.
    shortPF: Generating unit short term economic participation factor.
    startupCost: The initial startup cost incurred for each start of the GeneratingUnit.
    variableCost: The variable cost component of production per unit of ActivePower.
    startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied.
    totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy.
    GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing
      the losses and auxiliary power requirements of the unit.
    RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
    normalPF: Generating unit economic participation factor.  The sum of the participation factors across generating
      units does not have to sum to one.  It is used for representing distributed slack participation
      factor. The attribute shall be a positive value or zero.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # ControlAreaGeneratingUnit : list = field(default_factory=list)  # Type M:0..n in CIM
    genControlSource: Optional[str] = None  # Type M:0..1 in CIM
    governorSCD: float = 0.0  # Type #PerCent in CIM
    longPF: float = 0.0  # Type #Float in CIM
    maximumAllowableSpinningReserve: float = 0.0  # Type #ActivePower in CIM
    maxOperatingP: float = 0.0  # Type #ActivePower in CIM
    minOperatingP: float = 0.0  # Type #ActivePower in CIM
    nominalP: float = 0.0  # Type #ActivePower in CIM
    ratedGrossMaxP: float = 0.0  # Type #ActivePower in CIM
    ratedGrossMinP: float = 0.0  # Type #ActivePower in CIM
    ratedNetMaxP: float = 0.0  # Type #ActivePower in CIM
    shortPF: float = 0.0  # Type #Float in CIM
    startupCost: float = 0.0  # Type #Money in CIM
    variableCost: float = 0.0  # Type #Money in CIM
    startupTime: int = 0  # Type #Seconds in CIM
    totalEfficiency: float = 0.0  # Type #PerCent in CIM
    # *Association not used*
    # GrossToNetActivePowerCurves : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # RotatingMachine : list = field(default_factory=list)  # Type M:1..n in CIM
    normalPF: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GeneratingUnit\n"
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
            ],
            # Attributes
            "ControlAreaGeneratingUnit": [
                self.profiles.EQ.value,
            ],
            "genControlSource": [
                self.profiles.EQ.value,
            ],
            "governorSCD": [
                self.profiles.EQ.value,
            ],
            "longPF": [
                self.profiles.EQ.value,
            ],
            "maximumAllowableSpinningReserve": [
                self.profiles.EQ.value,
            ],
            "maxOperatingP": [
                self.profiles.EQ.value,
            ],
            "minOperatingP": [
                self.profiles.EQ.value,
            ],
            "nominalP": [
                self.profiles.EQ.value,
            ],
            "ratedGrossMaxP": [
                self.profiles.EQ.value,
            ],
            "ratedGrossMinP": [
                self.profiles.EQ.value,
            ],
            "ratedNetMaxP": [
                self.profiles.EQ.value,
            ],
            "shortPF": [
                self.profiles.EQ.value,
            ],
            "startupCost": [
                self.profiles.EQ.value,
            ],
            "variableCost": [
                self.profiles.EQ.value,
            ],
            "startupTime": [
                self.profiles.EQ.value,
            ],
            "totalEfficiency": [
                self.profiles.EQ.value,
            ],
            "GrossToNetActivePowerCurves": [
                self.profiles.EQ.value,
            ],
            "RotatingMachine": [
                self.profiles.EQ.value,
            ],
            "normalPF": [
                self.profiles.SSH.value,
            ],
        }
