"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC4A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied controlled-rectifier excitation
      system which is quite different from the other types of AC systems. This high initial response excitation
      system utilizes a full thyristor bridge in the exciter output circuit.  The voltage regulator controls the
      firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its
      output voltage to a constant value. These effects are not modelled; however, transient loading effects on the
      exciter alternator are included. Reference: IEEE 421.5-2005, 6.4.

    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -10.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 200.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,015.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5,64.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -4,53.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0.
    """

    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    tc: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEAC4A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
        }
