"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ExcBBC\n"
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
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "t4": [
                self.profiles.DY.value,
            ],
            "k": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "efdmin": [
                self.profiles.DY.value,
            ],
            "efdmax": [
                self.profiles.DY.value,
            ],
            "xe": [
                self.profiles.DY.value,
            ],
            "switch": [
                self.profiles.DY.value,
            ],
        }
