"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EarthFaultCompensator import EarthFaultCompensator


@dataclass(config=DataclassConfig)
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

    mode: Optional[str] = None  # Type M:1..1 in CIM
    nominalU: float = 0.0  # Type #Voltage in CIM
    offsetCurrent: float = 0.0  # Type #CurrentFlow in CIM
    positionCurrent: float = 0.0  # Type #CurrentFlow in CIM
    xGroundMax: float = 0.0  # Type #Reactance in CIM
    xGroundMin: float = 0.0  # Type #Reactance in CIM
    xGroundNominal: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PetersenCoil"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mode": [
                Profile.SC.value,
            ],
            "nominalU": [
                Profile.SC.value,
            ],
            "offsetCurrent": [
                Profile.SC.value,
            ],
            "positionCurrent": [
                Profile.SC.value,
            ],
            "xGroundMax": [
                Profile.SC.value,
            ],
            "xGroundMin": [
                Profile.SC.value,
            ],
            "xGroundNominal": [
                Profile.SC.value,
            ],
        }
