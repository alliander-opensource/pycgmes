"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class RemoteInputSignal(IdentifiedObject):
    """
    Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is
      coming.

    Terminal: Remote terminal with which this input signal is associated.
    remoteSignalType: Type of input signal.
    DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal.
    WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model using this remote input signal.
    PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal.
    UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal.
    PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model using this remote input signal.
    VoltageCompensatorDynamics: Voltage compensator model using this remote input signal.
    WindPlantDynamics: The wind plant using the remote signal.
    WindTurbineType3or4Dynamics: Wind turbine type 3 or type 4 models using this remote input signal.
    """

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    remoteSignalType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    DiscontinuousExcitationControlDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType1or2Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    PowerSystemStabilizerDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    UnderexcitationLimiterDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    PFVArControllerType1Dynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    VoltageCompensatorDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindPlantDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
