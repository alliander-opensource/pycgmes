"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=RemoteInputSignal\n"
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
            "Terminal": [
                self.profiles.DY.value,
            ],
            "remoteSignalType": [
                self.profiles.DY.value,
            ],
            "DiscontinuousExcitationControlDynamics": [
                self.profiles.DY.value,
            ],
            "WindTurbineType1or2Dynamics": [
                self.profiles.DY.value,
            ],
            "PowerSystemStabilizerDynamics": [
                self.profiles.DY.value,
            ],
            "UnderexcitationLimiterDynamics": [
                self.profiles.DY.value,
            ],
            "PFVArControllerType1Dynamics": [
                self.profiles.DY.value,
            ],
            "VoltageCompensatorDynamics": [
                self.profiles.DY.value,
            ],
            "WindPlantDynamics": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3or4Dynamics": [
                self.profiles.DY.value,
            ],
        }
