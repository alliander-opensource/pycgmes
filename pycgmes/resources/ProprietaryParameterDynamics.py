"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class ProprietaryParameterDynamics(Base):
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    CSCUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    SVCUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    VSCUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    WindPlantUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    WindType1or2UserDefined: Optional[str] = None  # Type M:0..1 in CIM
    WindType3or4UserDefined: Optional[str] = None  # Type M:0..1 in CIM
    SynchronousMachineUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    AsynchronousMachineUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    TurbineGovernorUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    TurbineLoadControllerUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    MechanicalLoadUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    ExcitationSystemUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    OverexcitationLimiterUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    UnderexcitationLimiterUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    PowerSystemStabilizerUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    DiscontinuousExcitationControlUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    PFVArControllerType1UserDefined: Optional[str] = None  # Type M:0..1 in CIM
    VoltageAdjusterUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    PFVArControllerType2UserDefined: Optional[str] = None  # Type M:0..1 in CIM
    VoltageCompensatorUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    LoadUserDefined: Optional[str] = None  # Type M:0..1 in CIM
    parameterNumber: int = 0  # Type #Integer in CIM
    booleanParameterValue: bool = False  # Type #Boolean in CIM
    integerParameterValue: int = 0  # Type #Integer in CIM
    floatParameterValue: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ProprietaryParameterDynamics\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "CSCUserDefined": [
                self.profiles.DY.value,
            ],
            "SVCUserDefined": [
                self.profiles.DY.value,
            ],
            "VSCUserDefined": [
                self.profiles.DY.value,
            ],
            "WindPlantUserDefined": [
                self.profiles.DY.value,
            ],
            "WindType1or2UserDefined": [
                self.profiles.DY.value,
            ],
            "WindType3or4UserDefined": [
                self.profiles.DY.value,
            ],
            "SynchronousMachineUserDefined": [
                self.profiles.DY.value,
            ],
            "AsynchronousMachineUserDefined": [
                self.profiles.DY.value,
            ],
            "TurbineGovernorUserDefined": [
                self.profiles.DY.value,
            ],
            "TurbineLoadControllerUserDefined": [
                self.profiles.DY.value,
            ],
            "MechanicalLoadUserDefined": [
                self.profiles.DY.value,
            ],
            "ExcitationSystemUserDefined": [
                self.profiles.DY.value,
            ],
            "OverexcitationLimiterUserDefined": [
                self.profiles.DY.value,
            ],
            "UnderexcitationLimiterUserDefined": [
                self.profiles.DY.value,
            ],
            "PowerSystemStabilizerUserDefined": [
                self.profiles.DY.value,
            ],
            "DiscontinuousExcitationControlUserDefined": [
                self.profiles.DY.value,
            ],
            "PFVArControllerType1UserDefined": [
                self.profiles.DY.value,
            ],
            "VoltageAdjusterUserDefined": [
                self.profiles.DY.value,
            ],
            "PFVArControllerType2UserDefined": [
                self.profiles.DY.value,
            ],
            "VoltageCompensatorUserDefined": [
                self.profiles.DY.value,
            ],
            "LoadUserDefined": [
                self.profiles.DY.value,
            ],
            "parameterNumber": [
                self.profiles.DY.value,
            ],
            "booleanParameterValue": [
                self.profiles.DY.value,
            ],
            "integerParameterValue": [
                self.profiles.DY.value,
            ],
            "floatParameterValue": [
                self.profiles.DY.value,
            ],
        }
