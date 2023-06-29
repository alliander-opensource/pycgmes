"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class PowerSystemResource(IdentifiedObject):
    """
    A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many
      individual items of equipment such as a substation, or an organisational entity such as sub-control area.
      Power system resources can have measurements associated.

    Location: Location of this power system resource.
    Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a
      synchronous machine or capacitor bank breaker actuator.
    Measurements: The measurements associated with this power system resource.
    """

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # Location : Optional[str] = Field(default=None, in_profiles = [Profile.GL, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Controls : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Measurements : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
