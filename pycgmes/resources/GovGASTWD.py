"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovGASTWD(TurbineGovernorDynamics):
    """
    Woodward™ gas turbine governor.  [Footnote: Woodward gas turbines are an example of suitable products available
      commercially. This information is given for the convenience of users of this document and does not constitute
      an endorsement by IEC of these products.]

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    kdroop: (Kdroop) (>= 0).
    kp: PID proportional gain (Kp).
    ki: Isochronous Governor Gain (Ki).
    kd: Drop governor gain (Kd).
    etd: Turbine and exhaust delay (Etd) (>= 0).
    tcd: Compressor discharge time constant (Tcd) (>= 0).
    trate: Turbine rating (Trate).  Unit = MW.
    t: Fuel control time constant (T) (>= 0).
    tmax: Maximum Turbine limit (Tmax) (> GovGASTWD.tmin).
    tmin: Minimum turbine limit (Tmin) (< GovGASTWD.tmax).
    ecr: Combustion reaction time delay (Ecr) (>= 0).
    k3: Ratio of fuel adjustment (K3).
    a: Valve positioner (A).
    b: Valve positioner (B).
    c: Valve positioner (C).
    tf: Fuel system time constant (Tf) (>= 0).
    kf: Fuel system feedback (Kf).
    k5: Gain of radiation shield (K5).
    k4: Gain of radiation shield (K4).
    t3: Radiation shield time constant (T3) (>= 0).
    t4: Thermocouple time constant (T4) (>= 0).
    tt: Temperature controller integration rate (Tt) (>= 0).
    t5: Temperature control time constant (T5) (>= 0).
    af1: Exhaust temperature parameter (Af1).
    bf1: (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0,55 to 0,65 x Tr.
    af2: Coefficient equal to 0,5(1-speed) (Af2).
    bf2: Turbine torque coefficient Khhv (depends on heating value of fuel stream in combustion chamber) (Bf2).
    cf2: Coefficient defining fuel flow where power output is 0 % (Cf2).  Synchronous but no output.  Typically 0,23 x
      Khhv (23 % fuel flow).
    tr: Rated temperature (Tr).
    k6: Minimum fuel flow (K6).
    tc: Temperature control (Tc).
    td: Power transducer time constant (Td) (>= 0).
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    kdroop: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    etd: int = 0  # Type #Seconds in CIM
    tcd: int = 0  # Type #Seconds in CIM
    trate: float = 0.0  # Type #ActivePower in CIM
    t: int = 0  # Type #Seconds in CIM
    tmax: float = 0.0  # Type #PU in CIM
    tmin: float = 0.0  # Type #PU in CIM
    ecr: int = 0  # Type #Seconds in CIM
    k3: float = 0.0  # Type #PU in CIM
    a: float = 0.0  # Type #Float in CIM
    b: float = 0.0  # Type #Float in CIM
    c: float = 0.0  # Type #Float in CIM
    tf: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    k5: float = 0.0  # Type #PU in CIM
    k4: float = 0.0  # Type #PU in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    tt: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    af1: float = 0.0  # Type #PU in CIM
    bf1: float = 0.0  # Type #PU in CIM
    af2: float = 0.0  # Type #PU in CIM
    bf2: float = 0.0  # Type #PU in CIM
    cf2: float = 0.0  # Type #PU in CIM
    tr: float = 0.0  # Type #Temperature in CIM
    k6: float = 0.0  # Type #PU in CIM
    tc: float = 0.0  # Type #Temperature in CIM
    td: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovGASTWD"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mwbase": [
                Profile.DY.value,
            ],
            "kdroop": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "etd": [
                Profile.DY.value,
            ],
            "tcd": [
                Profile.DY.value,
            ],
            "trate": [
                Profile.DY.value,
            ],
            "t": [
                Profile.DY.value,
            ],
            "tmax": [
                Profile.DY.value,
            ],
            "tmin": [
                Profile.DY.value,
            ],
            "ecr": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "a": [
                Profile.DY.value,
            ],
            "b": [
                Profile.DY.value,
            ],
            "c": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "k5": [
                Profile.DY.value,
            ],
            "k4": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "tt": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "af1": [
                Profile.DY.value,
            ],
            "bf1": [
                Profile.DY.value,
            ],
            "af2": [
                Profile.DY.value,
            ],
            "bf2": [
                Profile.DY.value,
            ],
            "cf2": [
                Profile.DY.value,
            ],
            "tr": [
                Profile.DY.value,
            ],
            "k6": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
        }
