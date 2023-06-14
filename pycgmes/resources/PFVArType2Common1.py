"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass(config=DataclassConfig)
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

    j: bool = False  # Type #Boolean in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    max: float = 0.0  # Type #PU in CIM
    ref: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PFVArType2Common1"]
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
            "j": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "max": [
                Profile.DY.value,
            ],
            "ref": [
                Profile.DY.value,
            ],
        }
