"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class RegulatingControl(PowerSystemResource):
    """
    Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote
      bus voltage control is possible by specifying the controlled terminal located at some place remote from the
      controlling equipment. The specified terminal shall be associated with the connectivity node of the controlled
      point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the
      control, e.g. TapChangerControl for tap changers. For flow control, load sign convention is used, i.e.
      positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. The attribute
      minAllowedTargetValue and maxAllowedTargetValue are required in the following cases: - For a power generating
      module operated in power factor control mode to specify maximum and minimum power factor values; - Whenever it
      is necessary to have an off center target voltage for the tap changer regulator. For instance, due to long
      cables to off shore wind farms and the need to have a simpler setup at the off shore transformer platform, the
      voltage is controlled from the land at the connection point for the off shore wind farm. Since there usually
      is a voltage rise along the cable, there is typical and overvoltage of up 3-4 kV compared to the on shore
      station. Thus in normal operation the tap changer on the on shore station is operated with a target set point,
      which is in the lower parts of the dead band. The attributes minAllowedTargetValue and maxAllowedTargetValue
      are not related to the attribute targetDeadband and thus they are not treated as an alternative of the
      targetDeadband. They are needed due to limitations in the local substation controller. The attribute
      targetDeadband is used to prevent the power flow from move the tap position in circles (hunting) that is to be
      used regardless of the attributes minAllowedTargetValue and maxAllowedTargetValue.

    RegulationSchedule: Schedule for this regulating control.
    RegulatingCondEq: The equipment that participates in this regulating control scheme.
    mode: The regulating control mode presently available.  This specification allows for determining the kind of
      regulation without need for obtaining the units from a schedule.
    Terminal: The terminal associated with this regulating control.  The terminal is associated instead of a node, since
      the terminal could connect into either a topological node or a connectivity node.  Sometimes it is
      useful to model regulation at a terminal of a bus bar object.
    discrete: The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap
      changers and shunt compensators.
    enabled: The flag tells if regulation is enabled.
    targetDeadband: This is a deadband used with discrete control to avoid excessive update of controls like tap
      changers and shunt compensator banks while regulating.  The units of those appropriate for the
      mode. The attribute shall be a positive value or zero. If RegulatingControl.discrete is set to
      `false`, the RegulatingControl.targetDeadband is to be ignored. Note that for instance, if the
      targetValue is 100 kV and the targetDeadband is 2 kV the range is from 99 to 101 kV.
    targetValue: The target value specified for case input.   This value can be used for the target value without the
      use of schedules. The value has the units appropriate to the mode attribute.
    targetValueUnitMultiplier: Specify the multiplier for used for the targetValue.
    maxAllowedTargetValue: Maximum allowed target value (RegulatingControl.targetValue).
    minAllowedTargetValue: Minimum allowed target value (RegulatingControl.targetValue).
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RegulationSchedule : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RegulatingCondEq : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    mode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    discrete: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    enabled: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetDeadband: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetValueUnitMultiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SSH,
        ],
    )

    maxAllowedTargetValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    minAllowedTargetValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
