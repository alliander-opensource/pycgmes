"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EarthFaultCompensator import EarthFaultCompensator


@dataclass
class PetersenCoil(EarthFaultCompensator):
    """
    A variable impedance device normally used to offset line charging during single line faults in an ungrounded section
      of network.

    mode: The mode of operation of the Petersen coil.
    nominalU: The nominal voltage for which the coil is designed.
    offsetCurrent: The offset current that the Petersen coil controller is operating from the resonant point.  This is
      normally a fixed amount for which the controller is configured and could be positive or
      negative.  Typically 0 to 60 A depending on voltage and resonance conditions.
    positionCurrent: The control current used to control the Petersen coil also known as the position current.
      Typically in the range of 20 mA to 200 mA.
    xGroundMax: The maximum reactance.
    xGroundMin: The minimum reactance.
    xGroundNominal: The nominal reactance.  This is the operating point (normally over compensation) that is defined
      based on the resonance point in the healthy network condition.  The impedance is calculated
      based on nominal voltage divided by position current.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mode: Optional[str] = None  # Type M:1..1 in CIM
    nominalU: float = 0.0  # Type #Voltage in CIM
    offsetCurrent: float = 0.0  # Type #CurrentFlow in CIM
    positionCurrent: float = 0.0  # Type #CurrentFlow in CIM
    xGroundMax: float = 0.0  # Type #Reactance in CIM
    xGroundMin: float = 0.0  # Type #Reactance in CIM
    xGroundNominal: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PetersenCoil\n"
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
            "mode": [
                self.profiles.SC.value,
            ],
            "nominalU": [
                self.profiles.SC.value,
            ],
            "offsetCurrent": [
                self.profiles.SC.value,
            ],
            "positionCurrent": [
                self.profiles.SC.value,
            ],
            "xGroundMax": [
                self.profiles.SC.value,
            ],
            "xGroundMin": [
                self.profiles.SC.value,
            ],
            "xGroundNominal": [
                self.profiles.SC.value,
            ],
        }
