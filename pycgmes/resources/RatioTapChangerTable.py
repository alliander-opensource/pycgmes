"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with the tap step.

    RatioTapChanger: The ratio tap changer of this tap ratio table.
    RatioTapChangerTablePoint: Points of this table.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RatioTapChanger : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # RatioTapChangerTablePoint : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
