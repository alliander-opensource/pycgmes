"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .SynchronousMachineDetailed import SynchronousMachineDetailed


@dataclass
class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    """
    The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit
      diagram for the direct- and quadrature- axes. Equations for conversion between equivalent circuit and time
      constant reactance forms: Xd = Xad + Xl X'd = Xl + Xad x Xfd / (Xad + Xfd) X"d = Xl + Xad x Xfd x X1d / (Xad x
      Xfd + Xad x X1d + Xfd x X1d) Xq = Xaq + Xl X'q = Xl + Xaq x X1q / (Xaq + X1q) X"q = Xl + Xaq x X1q x X2q /
      (Xaq x X1q + Xaq x X2q + X1q x X2q) T'do = (Xad + Xfd) / (omega0 x Rfd) T"do = (Xad x Xfd + Xad x X1d + Xfd x
      X1d) / (omega0 x R1d x (Xad + Xfd) T'qo = (Xaq + X1q) / (omega0 x R1q) T"qo = (Xaq x X1q + Xaq x X2q + X1q x
      X2q) / (omega0 x R2q x (Xaq + X1q) Same equations using CIM attributes from
      SynchronousMachineTimeConstantReactance class on left of "=" and SynchronousMachineEquivalentCircuit class on
      right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans =
      RotatingMachineDynamics.statorLeakageReactance + xad x xfd / (xad + xfd) xDirectSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xad x xfd x x1d / (xad x xfd + xad x x1d + xfd x x1d)
      xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq x x1q / (xaq+ x1q) xQuadSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq x x1q x x2q / (xaq x x1q + xaq x x2q + x1q x x2q)  tpdo =
      (xad + xfd) / (2 x pi x nominal frequency x rfd) tppdo = (xad x xfd + xad x x1d + xfd x x1d) / (2 x pi x
      nominal frequency x r1d x (xad + xfd) tpqo = (xaq + x1q) / (2 x pi x nominal frequency x r1q) tppqo = (xaq x
      x1q + xaq x x2q + x1q x x2q) / (2 x pi x nominal frequency x r2q x (xaq + x1q) These are only valid for a
      simplified model where "Canay" reactance is zero.

    xad: Direct-axis mutual reactance.
    rfd: Field winding resistance.
    xfd: Field winding leakage reactance.
    r1d: Direct-axis damper 1 winding resistance.
    x1d: Direct-axis damper 1 winding leakage reactance.
    xf1d: Differential mutual (`Canay`) reactance.
    xaq: Quadrature-axis mutual reactance.
    r1q: Quadrature-axis damper 1 winding resistance.
    x1q: Quadrature-axis damper 1 winding leakage reactance.
    r2q: Quadrature-axis damper 2 winding resistance.
    x2q: Quadrature-axis damper 2 winding leakage reactance.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    xad: float = 0.0  # Type #PU in CIM
    rfd: float = 0.0  # Type #PU in CIM
    xfd: float = 0.0  # Type #PU in CIM
    r1d: float = 0.0  # Type #PU in CIM
    x1d: float = 0.0  # Type #PU in CIM
    xf1d: float = 0.0  # Type #PU in CIM
    xaq: float = 0.0  # Type #PU in CIM
    r1q: float = 0.0  # Type #PU in CIM
    x1q: float = 0.0  # Type #PU in CIM
    r2q: float = 0.0  # Type #PU in CIM
    x2q: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SynchronousMachineEquivalentCircuit\n"
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
            "xad": [
                self.profiles.DY.value,
            ],
            "rfd": [
                self.profiles.DY.value,
            ],
            "xfd": [
                self.profiles.DY.value,
            ],
            "r1d": [
                self.profiles.DY.value,
            ],
            "x1d": [
                self.profiles.DY.value,
            ],
            "xf1d": [
                self.profiles.DY.value,
            ],
            "xaq": [
                self.profiles.DY.value,
            ],
            "r1q": [
                self.profiles.DY.value,
            ],
            "x1q": [
                self.profiles.DY.value,
            ],
            "r2q": [
                self.profiles.DY.value,
            ],
            "x2q": [
                self.profiles.DY.value,
            ],
        }
