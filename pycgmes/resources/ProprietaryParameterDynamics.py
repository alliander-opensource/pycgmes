"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class ProprietaryParameterDynamics(Base, ModuleType):
    """
    Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined
      models.   This class does not inherit from IdentifiedObject since it is not intended that a single instance of
      it be referenced by more than one proprietary user-defined model instance.

    CSCUserDefined: Proprietary user-defined model with which this parameter is associated.
    SVCUserDefined: Proprietary user-defined model with which this parameter is associated.
    VSCUserDefined: Proprietary user-defined model with which this parameter is associated.
    WindPlantUserDefined: Proprietary user-defined model with which this parameter is associated.
    WindType1or2UserDefined: Proprietary user-defined model with which this parameter is associated.
    WindType3or4UserDefined: Proprietary user-defined model with which this parameter is associated.
    SynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated.
    AsynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated.
    TurbineGovernorUserDefined: Proprietary user-defined model with which this parameter is associated.
    TurbineLoadControllerUserDefined: Proprietary user-defined model with which this parameter is associated.
    MechanicalLoadUserDefined: Proprietary user-defined model with which this parameter is associated.
    ExcitationSystemUserDefined: Proprietary user-defined model with which this parameter is associated.
    OverexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated.
    UnderexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated.
    PowerSystemStabilizerUserDefined: Proprietary user-defined model with which this parameter is associated.
    DiscontinuousExcitationControlUserDefined: Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType1UserDefined: Proprietary user-defined model with which this parameter is associated.
    VoltageAdjusterUserDefined: Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType2UserDefined: Proprietary user-defined model with which this parameter is associated.
    VoltageCompensatorUserDefined: Proprietary user-defined model with which this parameter is associated.
    LoadUserDefined: Proprietary user-defined model with which this parameter is associated.
    parameterNumber: Sequence number of the parameter among the set of parameters associated with the related
      proprietary user-defined model.
    booleanParameterValue: Boolean parameter value. If this attribute is populated, integerParameterValue and
      floatParameterValue will not be.
    integerParameterValue: Integer parameter value.  If this attribute is populated, booleanParameterValue and
      floatParameterValue will not be.
    floatParameterValue: Floating point parameter value.  If this attribute is populated, booleanParameterValue and
      integerParameterValue will not be.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ProprietaryParameterDynamics(*args, **kwargs)

    CSCUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    SVCUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    VSCUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindPlantUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindType1or2UserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindType3or4UserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    SynchronousMachineUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    AsynchronousMachineUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    TurbineGovernorUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    TurbineLoadControllerUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    MechanicalLoadUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    ExcitationSystemUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    OverexcitationLimiterUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    UnderexcitationLimiterUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    PowerSystemStabilizerUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    DiscontinuousExcitationControlUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    PFVArControllerType1UserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    VoltageAdjusterUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    PFVArControllerType2UserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    VoltageCompensatorUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    LoadUserDefined: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    parameterNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    booleanParameterValue: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    integerParameterValue: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    floatParameterValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import ProprietaryParameterDynamics"
# work as well as
# "from ProprietaryParameterDynamics import ProprietaryParameterDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ProprietaryParameterDynamics
