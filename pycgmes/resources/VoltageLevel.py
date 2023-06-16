"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquipmentContainer import EquipmentContainer


@dataclass(config=DataclassConfig)
class VoltageLevel(EquipmentContainer):
    """
    A collection of equipment at one common system voltage forming a switchgear. The equipment typically consists of
      breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all
      these.

    BaseVoltage: The base voltage used for all equipment within the voltage level.
    Bays: The bays within this voltage level.
    Substation: The substation of the voltage level.
    highVoltageLimit: The bus bar`s high voltage limit. The limit applies to all equipment and nodes contained in a
      given VoltageLevel. It is not required that it is exchanged in pair with lowVoltageLimit. It
      is preferable to use operational VoltageLimit, which prevails, if present.
    lowVoltageLimit: The bus bar`s low voltage limit. The limit applies to all equipment and nodes contained in a given
      VoltageLevel. It is not required that it is exchanged in pair with highVoltageLimit. It is
      preferable to use operational VoltageLimit, which prevails, if present.
    """

    BaseVoltage: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # Bays : list = field(default_factory=list)  # Type M:0..n in CIM
    Substation: Optional[str] = None  # Type M:1 in CIM
    highVoltageLimit: float = 0.0  # Type #Voltage in CIM
    lowVoltageLimit: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=VoltageLevel"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            # Attributes
            "BaseVoltage": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "Bays": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "Substation": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "highVoltageLimit": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "lowVoltageLimit": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
        }
