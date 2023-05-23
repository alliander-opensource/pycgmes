"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass
class PFVArType2Common1(PFVArControllerType2Dynamics):
    """
    Power factor / reactive power regulator. This model represents the power factor or reactive power controller such as
      the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and
      compares it with the operator's set point. [Footnote: Basler SCP-250 is an example of a suitable product
      available commercially. This information is given for the convenience of users of this document and does not
      constitute an endorsement by IEC of this product.]

    j: Selector (J). true = control mode for reactive power false = control mode for power factor.
    kp: Proportional gain (Kp).
    ki: Reset gain (Ki).
    max: Output limit (max).
    ref: Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This
      initialisation can override the value exchanged by this attribute to represent a plant operator`s change
      of the reference setting.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    j: bool = False  # Type #Boolean in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    max: float = 0.0  # Type #PU in CIM
    ref: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PFVArType2Common1\n"
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
            "j": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "max": [
                self.profiles.DY.value,
            ],
            "ref": [
                self.profiles.DY.value,
            ],
        }
