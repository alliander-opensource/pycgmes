"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    BaseVoltage: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Bays : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

    Substation: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    highVoltageLimit: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    lowVoltageLimit: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQBD,
            Profile.EQ,
        }
