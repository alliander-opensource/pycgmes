"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass(config=DataclassConfig)
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modelling construct to provide a root class for containing equipment.

    Equipments: Contained equipment.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Equipments : list = Field(default_factory=list, in_profiles = [Profile.EQBD, Profile.EQ, ])

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
