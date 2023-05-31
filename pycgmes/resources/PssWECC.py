"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssWECC(PowerSystemStabilizerDynamics):
    """
    Dual input power system stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western
      Electricity Coordinating Council, USA).

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than PssWECC.inputSignal2Type).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, busVoltageDerivative -
      shall be different than PssWECC.inputSignal1Type).  Typical value = busVoltageDerivative.
    k1: Input signal 1 gain (K1).  Typical value = 1,13.
    t1: Input signal 1 transducer time constant (T1) (>= 0).  Typical value = 0,037.
    k2: Input signal 2 gain (K2).  Typical value = 0,0.
    t2: Input signal 2 transducer time constant (T2) (>= 0).  Typical value = 0,0.
    t3: Stabilizer washout time constant (T3) (>= 0).  Typical value = 9,5.
    t4: Stabilizer washout time lag constant (T4) (>= 0).  Typical value = 9,5.
    t5: Lead time constant (T5) (>= 0).  Typical value = 1,7.
    t6: Lag time constant (T6) (>= 0).  Typical value = 1,5.
    t7: Lead time constant (T7) (>= 0).  Typical value = 1,7.
    t8: Lag time constant (T8) (>= 0).  Typical value = 1,5.
    t10: Lag time constant (T10) (>= 0).  Typical value = 0.
    t9: Lead time constant (T9) (>= 0).  Typical value = 0.
    vsmax: Maximum output signal (Vsmax) (> PssWECC.vsmin). Typical value = 0,05.
    vsmin: Minimum output signal (Vsmin) (< PssWECC.vsmax).  Typical value = -0,05.
    vcu: Maximum value for voltage compensator output (VCU). Typical value = 0.
    vcl: Minimum value for voltage compensator output (VCL). Typical value = 0.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    inputSignal1Type: Optional[str] = None  # Type M:1..1 in CIM
    inputSignal2Type: Optional[str] = None  # Type M:1..1 in CIM
    k1: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    k2: float = 0.0  # Type #PU in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    t10: int = 0  # Type #Seconds in CIM
    t9: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM
    vcu: float = 0.0  # Type #PU in CIM
    vcl: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssWECC\n"
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
            "inputSignal1Type": [
                self.profiles.DY.value,
            ],
            "inputSignal2Type": [
                self.profiles.DY.value,
            ],
            "k1": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "k2": [
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
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "t7": [
                self.profiles.DY.value,
            ],
            "t8": [
                self.profiles.DY.value,
            ],
            "t10": [
                self.profiles.DY.value,
            ],
            "t9": [
                self.profiles.DY.value,
            ],
            "vsmax": [
                self.profiles.DY.value,
            ],
            "vsmin": [
                self.profiles.DY.value,
            ],
            "vcu": [
                self.profiles.DY.value,
            ],
            "vcl": [
                self.profiles.DY.value,
            ],
        }
