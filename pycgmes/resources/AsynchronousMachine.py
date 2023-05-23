"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RotatingMachine import RotatingMachine


@dataclass
class AsynchronousMachine(RotatingMachine):
    """
    A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine
      with no external connection to the rotor windings, e.g. squirrel-cage induction machine.

    nominalFrequency: Nameplate data indicates if the machine is 50 Hz or 60 Hz.
    nominalSpeed: Nameplate data.  Depends on the slip and number of pole pairs.
    converterFedDrive: Indicates whether the machine is a converter fed drive. Used for short circuit data exchange
      according to IEC 60909.
    efficiency: Efficiency of the asynchronous machine at nominal operation as a percentage. Indicator for converter
      drive motors. Used for short circuit data exchange according to IEC 60909.
    iaIrRatio: Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data
      exchange according to IEC 60909.
    polePairNumber: Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909.
    ratedMechanicalPower: Rated mechanical power (Pr in IEC 60909-0). Used for short circuit data exchange according to
      IEC 60909.
    reversible: Indicates for converter drive motors if the power can be reversible. Used for short circuit data
      exchange according to IEC 60909.
    rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909.
    asynchronousMachineType: Indicates the type of Asynchronous Machine (motor or generator).
    AsynchronousMachineDynamics: Asynchronous machine dynamics model used to describe dynamic behaviour of this
      asynchronous machine.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    nominalFrequency: float = 0.0  # Type #Frequency in CIM
    nominalSpeed: float = 0.0  # Type #RotationSpeed in CIM
    converterFedDrive: bool = False  # Type #Boolean in CIM
    efficiency: float = 0.0  # Type #PerCent in CIM
    iaIrRatio: float = 0.0  # Type #Float in CIM
    polePairNumber: int = 0  # Type #Integer in CIM
    ratedMechanicalPower: float = 0.0  # Type #ActivePower in CIM
    reversible: bool = False  # Type #Boolean in CIM
    rxLockedRotorRatio: float = 0.0  # Type #Float in CIM
    asynchronousMachineType: Optional[str] = None  # Type M:1..1 in CIM
    # *Association not used*
    # AsynchronousMachineDynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AsynchronousMachine\n"
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
            "nominalFrequency": [
                self.profiles.EQ.value,
            ],
            "nominalSpeed": [
                self.profiles.EQ.value,
            ],
            "converterFedDrive": [
                self.profiles.SC.value,
            ],
            "efficiency": [
                self.profiles.SC.value,
            ],
            "iaIrRatio": [
                self.profiles.SC.value,
            ],
            "polePairNumber": [
                self.profiles.SC.value,
            ],
            "ratedMechanicalPower": [
                self.profiles.SC.value,
            ],
            "reversible": [
                self.profiles.SC.value,
            ],
            "rxLockedRotorRatio": [
                self.profiles.SC.value,
            ],
            "asynchronousMachineType": [
                self.profiles.SSH.value,
            ],
            "AsynchronousMachineDynamics": [
                self.profiles.DY.value,
            ],
        }
