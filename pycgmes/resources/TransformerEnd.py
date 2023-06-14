"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class TransformerEnd(IdentifiedObject):
    """
    A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In
      earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible
      because it associates to terminal but is not a specialization of ConductingEquipment.

    BaseVoltage: Base voltage of the transformer end.  This is essential for PU calculation.
    PhaseTapChanger: Phase tap changer associated with this transformer end.
    RatioTapChanger: Ratio tap changer associated with this transformer end.
    Terminal: Terminal of the power transformer to which this transformer end belongs.
    endNumber: Number for this transformer end, corresponding to the end`s order in the power transformer vector group
      or phase angle clock number.  Highest voltage winding should be 1.  Each end within a power
      transformer should have a unique subsequent end number.   Note the transformer end number need not
      match the terminal sequence number.
    rground: (for Yn and Zn connections) Resistance part of neutral impedance where `grounded` is true.
    grounded: (for Yn and Zn connections) True if the neutral is solidly grounded.
    xground: (for Yn and Zn connections) Reactive part of neutral impedance where `grounded` is true.
    """

    BaseVoltage: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # PhaseTapChanger : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # RatioTapChanger : Optional[str] = None  # Type M:0..1 in CIM
    Terminal: Optional[str] = None  # Type M:1..1 in CIM
    endNumber: int = 0  # Type #Integer in CIM
    rground: float = 0.0  # Type #Resistance in CIM
    grounded: bool = False  # Type #Boolean in CIM
    xground: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TransformerEnd"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "BaseVoltage": [
                Profile.EQ.value,
            ],
            "PhaseTapChanger": [
                Profile.EQ.value,
            ],
            "RatioTapChanger": [
                Profile.EQ.value,
            ],
            "Terminal": [
                Profile.EQ.value,
            ],
            "endNumber": [
                Profile.EQ.value,
            ],
            "rground": [
                Profile.SC.value,
            ],
            "grounded": [
                Profile.SC.value,
            ],
            "xground": [
                Profile.SC.value,
            ],
        }
