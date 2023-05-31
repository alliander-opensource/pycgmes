"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RotatingMachine import RotatingMachine


@dataclass
class SynchronousMachine(RotatingMachine):
    """
    An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine
      operating either as a generator or synchronous condenser or pump.

    InitialReactiveCapabilityCurve: The default reactive capability curve for use by a synchronous machine.
    maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    minQ: Minimum reactive power limit for the unit.
    qPercent: Part of the coordinated reactive control that comes from this machine. The attribute is used as a
      participation factor not necessarily summing up to 100% for the participating devices in the
      control.
    type: Modes that this synchronous machine can operate in.
    earthing: Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC
      60909.
    earthingStarPointR: Generator star point earthing resistance (Re). Used for short circuit data exchange according to
      IEC 60909.
    earthingStarPointX: Generator star point earthing reactance (Xe). Used for short circuit data exchange according to
      IEC 60909.
    ikk: Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase
      short circuit. - Ikk=0: Generator with no compound excitation. - Ikk<>0: Generator with compound
      excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with
      compound excitation. (4.6.1.2 in IEC 60909-0:2001). Used only for single fed short circuit on a
      generator. (4.3.4.2. in IEC 60909-0:2001).
    mu: Factor to calculate the breaking current (Section 4.5.2.1 in IEC 60909-0). Used only for single fed short
      circuit on a generator (Section 4.3.4.2. in IEC 60909-0).
    x0: Zero sequence reactance of the synchronous machine.
    r0: Zero sequence resistance of the synchronous machine.
    x2: Negative sequence reactance.
    r2: Negative sequence resistance.
    r: Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the
      calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909.
    satDirectSubtransX: Direct-axis subtransient reactance saturated, also known as Xd`sat.
    satDirectSyncX: Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for
      short circuit data exchange, only for single fed short circuit on a generator. (4.3.4.2. in
      IEC 60909-0:2001).
    satDirectTransX: Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit
      calculations according to ANSI.
    shortCircuitRotorType: Type of rotor, used by short circuit applications, only for single fed short circuit
      according to IEC 60909.
    voltageRegulationRange: Range of generator voltage regulation (PG in IEC 60909-0) used for calculation of the
      impedance correction factor KG defined in IEC 60909-0. This attribute is used to
      describe the operating voltage of the generating unit.
    operatingMode: Current mode of operation.
    referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care
      (default) 1 = highest priority. 2 is less than 1 and so on.
    SynchronousMachineDynamics: Synchronous machine dynamics model used to describe dynamic behaviour of this
      synchronous machine.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    InitialReactiveCapabilityCurve: Optional[str] = None  # Type M:0..1 in CIM
    maxQ: float = 0.0  # Type #ReactivePower in CIM
    minQ: float = 0.0  # Type #ReactivePower in CIM
    qPercent: float = 0.0  # Type #PerCent in CIM
    type: Optional[str] = None  # Type M:1..1 in CIM
    earthing: bool = False  # Type #Boolean in CIM
    earthingStarPointR: float = 0.0  # Type #Resistance in CIM
    earthingStarPointX: float = 0.0  # Type #Reactance in CIM
    ikk: float = 0.0  # Type #CurrentFlow in CIM
    mu: float = 0.0  # Type #Float in CIM
    x0: float = 0.0  # Type #Reactance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    x2: float = 0.0  # Type #Reactance in CIM
    r2: float = 0.0  # Type #Resistance in CIM
    r: float = 0.0  # Type #Resistance in CIM
    satDirectSubtransX: float = 0.0  # Type #PU in CIM
    satDirectSyncX: float = 0.0  # Type #PU in CIM
    satDirectTransX: float = 0.0  # Type #PU in CIM
    shortCircuitRotorType: Optional[str] = None  # Type M:0..1 in CIM
    voltageRegulationRange: float = 0.0  # Type #PerCent in CIM
    operatingMode: Optional[str] = None  # Type M:1..1 in CIM
    referencePriority: int = 0  # Type #Integer in CIM
    # *Association not used*
    # SynchronousMachineDynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SynchronousMachine\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "InitialReactiveCapabilityCurve": [
                self.profiles.EQ.value,
            ],
            "maxQ": [
                self.profiles.EQ.value,
            ],
            "minQ": [
                self.profiles.EQ.value,
            ],
            "qPercent": [
                self.profiles.EQ.value,
            ],
            "type": [
                self.profiles.EQ.value,
            ],
            "earthing": [
                self.profiles.SC.value,
            ],
            "earthingStarPointR": [
                self.profiles.SC.value,
            ],
            "earthingStarPointX": [
                self.profiles.SC.value,
            ],
            "ikk": [
                self.profiles.SC.value,
            ],
            "mu": [
                self.profiles.SC.value,
            ],
            "x0": [
                self.profiles.SC.value,
            ],
            "r0": [
                self.profiles.SC.value,
            ],
            "x2": [
                self.profiles.SC.value,
            ],
            "r2": [
                self.profiles.SC.value,
            ],
            "r": [
                self.profiles.SC.value,
            ],
            "satDirectSubtransX": [
                self.profiles.SC.value,
            ],
            "satDirectSyncX": [
                self.profiles.SC.value,
            ],
            "satDirectTransX": [
                self.profiles.SC.value,
            ],
            "shortCircuitRotorType": [
                self.profiles.SC.value,
            ],
            "voltageRegulationRange": [
                self.profiles.SC.value,
            ],
            "operatingMode": [
                self.profiles.SSH.value,
            ],
            "referencePriority": [
                self.profiles.SSH.value,
            ],
            "SynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
        }
