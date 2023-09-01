"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    EquipmentContainer: Container of this equipment.
    aggregate: The aggregate flag provides an alternative way of representing an aggregated (equivalent) element. It is
      applicable in cases when the dedicated classes for equivalent equipment do not have all of the
      attributes necessary to represent the required level of detail.  In case the flag is set to `true`
      the single instance of equipment represents multiple pieces of equipment that have been modelled
      together as an aggregate equivalent obtained by a network reduction procedure. Examples would be
      power transformers or synchronous machines operating in parallel modelled as a single aggregate
      power transformer or aggregate synchronous machine.   The attribute is not used for
      EquivalentBranch, EquivalentShunt and EquivalentInjection.
    normallyInService: Specifies the availability of the equipment under normal operating conditions. True means the
      equipment is available for topology processing, which determines if the equipment is
      energized or not. False means that the equipment is treated by network applications as if
      it is not in the model.
    OperationalLimitSet: The operational limit sets associated with this equipment.
    inService: Specifies the availability of the equipment. True means the equipment is available for topology
      processing, which determines if the equipment is energized or not. False means that the equipment
      is treated by network applications as if it is not in the model.
    """

    EquipmentContainer: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    aggregate: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    normallyInService: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # OperationalLimitSet : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    inService: bool = Field(
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
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        }
