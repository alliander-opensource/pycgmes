"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


@dataclass(config=DataclassConfig)
class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """
    Parameter details:  If X'' = X', a single cage (one equivalent rotor winding per axis) is modelled. The "p" in the
      attribute names is a substitution for a "prime" in the usual parameter notation, e.g. tpo refers to T'o.  The
      parameters used for models expressed in time constant reactance form include: - RotatingMachine.ratedS
      (MVAbase); - RotatingMachineDynamics.damping (D); - RotatingMachineDynamics.inertia (H); -
      RotatingMachineDynamics.saturationFactor (S1); - RotatingMachineDynamics.saturationFactor120 (S12); -
      RotatingMachineDynamics.statorLeakageReactance (Xl); - RotatingMachineDynamics.statorResistance (Rs); - .xs
      (Xs); - .xp (X'); - .xpp (X''); - .tpo (T'o); - .tppo (T''o).

    xs: Synchronous reactance (Xs) (>= AsynchronousMachineTimeConstantReactance.xp).  Typical value = 1,8.
    xp: Transient reactance (unsaturated) (X`) (>= AsynchronousMachineTimeConstantReactance.xpp).  Typical value = 0,5.
    xpp: Subtransient reactance (unsaturated) (X``) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value =
      0,2.
    tpo: Transient rotor time constant (T`o) (> AsynchronousMachineTimeConstantReactance.tppo).  Typical value = 5.
    tppo: Subtransient rotor time constant (T``o) (> 0).  Typical value = 0,03.
    """

    xs: float = 0.0  # Type #PU in CIM
    xp: float = 0.0  # Type #PU in CIM
    xpp: float = 0.0  # Type #PU in CIM
    tpo: int = 0  # Type #Seconds in CIM
    tppo: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AsynchronousMachineTimeConstantReactance"]
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
            "xs": [
                Profile.DY.value,
            ],
            "xp": [
                Profile.DY.value,
            ],
            "xpp": [
                Profile.DY.value,
            ],
            "tpo": [
                Profile.DY.value,
            ],
            "tppo": [
                Profile.DY.value,
            ],
        }
