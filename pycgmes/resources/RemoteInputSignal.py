"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    Terminal: Optional[str] = None  # Type M:1 in CIM
    remoteSignalType: Optional[str] = None  # Type M:1..1 in CIM
    DiscontinuousExcitationControlDynamics: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType1or2Dynamics : Optional[str] = None  # Type M:0..1 in CIM
    PowerSystemStabilizerDynamics: Optional[str] = None  # Type M:0..1 in CIM
    UnderexcitationLimiterDynamics: Optional[str] = None  # Type M:0..1 in CIM
    PFVArControllerType1Dynamics: Optional[str] = None  # Type M:0..1 in CIM
    VoltageCompensatorDynamics: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindPlantDynamics : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType3or4Dynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=RemoteInputSignal"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "Terminal": [
                Profile.DY.value,
            ],
            "remoteSignalType": [
                Profile.DY.value,
            ],
            "DiscontinuousExcitationControlDynamics": [
                Profile.DY.value,
            ],
            "WindTurbineType1or2Dynamics": [
                Profile.DY.value,
            ],
            "PowerSystemStabilizerDynamics": [
                Profile.DY.value,
            ],
            "UnderexcitationLimiterDynamics": [
                Profile.DY.value,
            ],
            "PFVArControllerType1Dynamics": [
                Profile.DY.value,
            ],
            "VoltageCompensatorDynamics": [
                Profile.DY.value,
            ],
            "WindPlantDynamics": [
                Profile.DY.value,
            ],
            "WindTurbineType3or4Dynamics": [
                Profile.DY.value,
            ],
        }
