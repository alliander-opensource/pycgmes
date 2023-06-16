"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcELIN1(ExcitationSystemDynamics):
    """
    Static PI transformer fed excitation system ELIN (VATECH) - simplified model.  This model represents an all-static
      excitation system. A PI voltage controller establishes a desired field current set point for a proportional
      current controller. The integrator of the PI controller has a follow-up input to match its signal to the
      present field current.  A power system stabilizer with power input is included in the model.

    tfi: Current transducer time constant (Tfi) (>= 0).  Typical value = 0.
    tnu: Controller reset time constant (Tnu) (>= 0).  Typical value = 2.
    vpu: Voltage controller proportional gain (Vpu).  Typical value = 34,5.
    vpi: Current controller gain (Vpi).  Typical value = 12,45.
    vpnf: Controller follow up gain (Vpnf).  Typical value = 2.
    dpnf: Controller follow up deadband (Dpnf).  Typical value = 0.
    tsw: Stabilizer parameters (Tsw) (>= 0).  Typical value = 3.
    efmin: Minimum open circuit excitation voltage (Efmin) (< ExcELIN1.efmax).  Typical value = -5.
    efmax: Maximum open circuit excitation voltage (Efmax) (> ExcELIN1.efmin).  Typical value = 5.
    xe: Excitation transformer effective reactance (Xe) (>= 0).  Xe represents the regulation of the
      transformer/rectifier unit.  Typical value = 0,06.
    ks1: Stabilizer gain 1 (Ks1).  Typical value = 0.
    ks2: Stabilizer gain 2 (Ks2).  Typical value = 0.
    ts1: Stabilizer phase lag time constant (Ts1) (>= 0).  Typical value = 1.
    ts2: Stabilizer filter time constant (Ts2) (>= 0).  Typical value = 1.
    smax: Stabilizer limit output (smax).  Typical value = 0,1.
    """

    tfi: int = 0  # Type #Seconds in CIM
    tnu: int = 0  # Type #Seconds in CIM
    vpu: float = 0.0  # Type #PU in CIM
    vpi: float = 0.0  # Type #PU in CIM
    vpnf: float = 0.0  # Type #PU in CIM
    dpnf: float = 0.0  # Type #PU in CIM
    tsw: int = 0  # Type #Seconds in CIM
    efmin: float = 0.0  # Type #PU in CIM
    efmax: float = 0.0  # Type #PU in CIM
    xe: float = 0.0  # Type #PU in CIM
    ks1: float = 0.0  # Type #PU in CIM
    ks2: float = 0.0  # Type #PU in CIM
    ts1: int = 0  # Type #Seconds in CIM
    ts2: int = 0  # Type #Seconds in CIM
    smax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcELIN1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tfi": [
                Profile.DY.value,
            ],
            "tnu": [
                Profile.DY.value,
            ],
            "vpu": [
                Profile.DY.value,
            ],
            "vpi": [
                Profile.DY.value,
            ],
            "vpnf": [
                Profile.DY.value,
            ],
            "dpnf": [
                Profile.DY.value,
            ],
            "tsw": [
                Profile.DY.value,
            ],
            "efmin": [
                Profile.DY.value,
            ],
            "efmax": [
                Profile.DY.value,
            ],
            "xe": [
                Profile.DY.value,
            ],
            "ks1": [
                Profile.DY.value,
            ],
            "ks2": [
                Profile.DY.value,
            ],
            "ts1": [
                Profile.DY.value,
            ],
            "ts2": [
                Profile.DY.value,
            ],
            "smax": [
                Profile.DY.value,
            ],
        }
