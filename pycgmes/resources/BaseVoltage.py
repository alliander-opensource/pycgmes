"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    TopologicalNode: The topological nodes at the base voltage.
    nominalVoltage: The power system resource`s base voltage.  Shall be a positive value and not zero.
    VoltageLevel: The voltage levels having this base voltage.
    ConductingEquipment: All conducting equipment with this base voltage.  Use only when there is no voltage level
      container used and only one base voltage applies.  For example, not used for
      transformers.
    TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TopologicalNode : list = Field(default_factory=list, in_profiles = [Profile.TP, ])

    nominalVoltage: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # VoltageLevel : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ConductingEquipment : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TransformerEnds : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
        }
