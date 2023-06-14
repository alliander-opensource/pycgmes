"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .SynchronousMachineDynamics import SynchronousMachineDynamics


@dataclass(config=DataclassConfig)
class SynchronousMachineSimplified(SynchronousMachineDynamics):
    """
    The simplified model represents a synchronous generator as a constant internal voltage behind an impedance (Rs +
      jXp) as shown in the Simplified diagram. Since internal voltage is held constant, there is no Efd input and
      any excitation system model will be ignored.  There is also no Ifd output. This model should not be used for
      representing a real generator except, perhaps, small generators whose response is insignificant.   The
      parameters used for the simplified model include: - RotatingMachineDynamics.damping (D); -
      RotatingMachineDynamics.inertia (H); - RotatingMachineDynamics.statorLeakageReactance (used to exchange jXp
      for SynchronousMachineSimplified); - RotatingMachineDynamics.statorResistance (Rs).

    """

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SynchronousMachineSimplified"]
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
        }
