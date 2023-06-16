"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class SeriesCompensator(ConductingEquipment):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It
      is a two terminal device.

    r: Positive sequence resistance.
    x: Positive sequence reactance.
    r0: Zero sequence resistance.
    x0: Zero sequence reactance.
    varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured in parallel with
      the series compensator. It is used for short circuit calculations.
    varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration. It is used for
      short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is
      true. The attribute shall be a positive value.
    varistorVoltageThreshold: The dc voltage at which the varistor starts conducting. It is used for short circuit
      calculations and exchanged only if SeriesCompensator.varistorPresent is true.
    """

    r: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    x0: float = 0.0  # Type #Reactance in CIM
    varistorPresent: bool = False  # Type #Boolean in CIM
    varistorRatedCurrent: float = 0.0  # Type #CurrentFlow in CIM
    varistorVoltageThreshold: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SeriesCompensator"]
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
            "x": [
                Profile.EQ.value,
            ],
            "r0": [
                Profile.SC.value,
            ],
            "x0": [
                Profile.SC.value,
            ],
            "varistorPresent": [
                Profile.SC.value,
            ],
            "varistorRatedCurrent": [
                Profile.SC.value,
            ],
            "varistorVoltageThreshold": [
                Profile.SC.value,
            ],
        }
