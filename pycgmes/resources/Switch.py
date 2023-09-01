"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal
      devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be
      considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant.

    normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a
      status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen.
    ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and
      construction. The attribute shall be a positive value.
    retained: Branch is retained in the topological solution.  The flow through retained switches will normally be
      calculated in power flow.
    SwitchSchedules: A Switch can be associated with SwitchSchedules.
    SvSwitch: The switch state associated with the switch.
    open: The attribute tells if the switch is considered open when used as input to topology processing.
    locked: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open
      attributes as follows:  locked=true and Switch.open=true. The resulting state is open and locked;
      locked=false and Switch.open=true. The resulting state is open; locked=false and Switch.open=false.
      The resulting state is closed.
    """

    normalOpen: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    retained: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # SwitchSchedules : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # SvSwitch : list = Field(default_factory=list, in_profiles = [Profile.SV, ])

    open: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    locked: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
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
            Profile.SV,
            Profile.SSH,
        }
