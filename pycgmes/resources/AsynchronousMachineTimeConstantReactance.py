"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    xs: float = 0.0  # Type #PU in CIM
    xp: float = 0.0  # Type #PU in CIM
    xpp: float = 0.0  # Type #PU in CIM
    tpo: int = 0  # Type #Seconds in CIM
    tppo: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=AsynchronousMachineTimeConstantReactance\n"
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
            "xs": [
                self.profiles.DY.value,
            ],
            "xp": [
                self.profiles.DY.value,
            ],
            "xpp": [
                self.profiles.DY.value,
            ],
            "tpo": [
                self.profiles.DY.value,
            ],
            "tppo": [
                self.profiles.DY.value,
            ],
        }
