"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


@dataclass(config=DataclassConfig)
class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """
    The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit
      diagram for the direct- and quadrature- axes, with two equivalent rotor windings in each axis.   Equations for
      conversion between equivalent circuit and time constant reactance forms: Xs = Xm + Xl X' = Xl + Xm x Xlr1 /
      (Xm + Xlr1) X'' = Xl + Xm x Xlr1 x Xlr2 / (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2) T'o = (Xm + Xlr1) / (omega0 x
      Rr1) T''o = (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2) / (omega0 x Rr2 x (Xm + Xlr1) Same equations using CIM
      attributes from AsynchronousMachineTimeConstantReactance class on left of "=" and
      AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm +
      RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1
      / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 x xlr2 / (xm x xlr1 + xm x xlr2
      + xlr1 x xlr2) tpo = (xm + xlr1) / (2 x pi x nominal frequency x rr1) tppo = (xm x xlr1 + xm x xlr2 + xlr1 x
      xlr2) / (2 x pi x nominal frequency x rr2 x (xm + xlr1).

    xm: Magnetizing reactance.
    rr1: Damper 1 winding resistance.
    xlr1: Damper 1 winding leakage reactance.
    rr2: Damper 2 winding resistance.
    xlr2: Damper 2 winding leakage reactance.
    """

    xm: float = 0.0  # Type #PU in CIM
    rr1: float = 0.0  # Type #PU in CIM
    xlr1: float = 0.0  # Type #PU in CIM
    rr2: float = 0.0  # Type #PU in CIM
    xlr2: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=AsynchronousMachineEquivalentCircuit"]
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
            "xm": [
                Profile.DY.value,
            ],
            "rr1": [
                Profile.DY.value,
            ],
            "xlr1": [
                Profile.DY.value,
            ],
            "rr2": [
                Profile.DY.value,
            ],
            "xlr2": [
                Profile.DY.value,
            ],
        }
