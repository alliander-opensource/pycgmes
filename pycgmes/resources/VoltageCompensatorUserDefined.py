"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass
class VoltageCompensatorUserDefined(VoltageCompensatorDynamics):
    """
    Voltage compensator function block whose dynamic behaviour is described by a user-defined model.

    proprietary: Behaviour is based on a proprietary model as opposed to a detailed model. true = user-defined model is
      proprietary with behaviour mutually understood by sending and receiving applications and
      parameters passed as general attributes false = user-defined model is explicitly defined in terms
      of control blocks and their input and output signals.
    ProprietaryParameterDynamics: Parameter of this proprietary user-defined model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    proprietary: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # ProprietaryParameterDynamics : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VoltageCompensatorUserDefined\n"
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
            "proprietary": [
                self.profiles.DY.value,
            ],
            "ProprietaryParameterDynamics": [
                self.profiles.DY.value,
            ],
        }
