"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcBBC(ExcitationSystemDynamics):
    """
    Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation
      system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main
      generator directly.

    t1: Controller time constant (T1) (>= 0).  Typical value = 6.
    t2: Controller time constant (T2) (>= 0).  Typical value = 1.
    t3: Lead/lag time constant (T3) (>= 0).  If = 0, block is bypassed.  Typical value = 0,05.
    t4: Lead/lag time constant (T4) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.
    k: Steady state gain (K) (not = 0).  Typical value = 300.
    vrmin: Minimum control element output (Vrmin) (< ExcBBC.vrmax).  Typical value = -5.
    vrmax: Maximum control element output (Vrmax) (> ExcBBC.vrmin).  Typical value = 5.
    efdmin: Minimum open circuit exciter voltage (Efdmin) (< ExcBBC.efdmax).  Typical value = -5.
    efdmax: Maximum open circuit exciter voltage (Efdmax) (> ExcBBC.efdmin).  Typical value = 5.
    xe: Effective excitation transformer reactance (Xe) (>= 0).  Xe models the regulation of the transformer/rectifier
      unit.  Typical value = 0,05.
    switch: Supplementary signal routing selector (switch). true = Vs connected to 3rd summing point false =  Vs
      connected to 1st summing point (see diagram). Typical value = false.
    """

    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    xe: float = 0.0  # Type #PU in CIM
    switch: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcBBC"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "k": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "efdmin": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
            "xe": [
                Profile.DY.value,
            ],
            "switch": [
                Profile.DY.value,
            ],
        }
