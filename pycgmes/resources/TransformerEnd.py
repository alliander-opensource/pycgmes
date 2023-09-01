"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
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

    BaseVoltage: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # PhaseTapChanger : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # RatioTapChanger : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    endNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    rground: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    grounded: bool = Field(
        default=False,
        in_profiles=[
            Profile.SC,
        ],
    )

    xground: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
        }
