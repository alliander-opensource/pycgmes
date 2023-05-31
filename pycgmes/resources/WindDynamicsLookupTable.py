"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindDynamicsLookupTable(IdentifiedObject):
    """
    Look up table for the purpose of wind standard models.

    WindContCurrLimIEC: The current control limitation model with which this wind dynamics lookup table is associated.
    WindContPType3IEC: The P control type 3 model with which this wind dynamics lookup table is associated.
    WindContQPQULimIEC: The QP and QU limitation model with which this wind dynamics lookup table is associated.
    WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated.
    input: Input value (x) for the lookup table function.
    lookupTableFunctionType: Type of the lookup table function.
    output: Output value (y) for the lookup table function.
    sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function.
    WindPlantFreqPcontrolIEC: The frequency and active power wind plant control model with which this wind dynamics
      lookup table is associated.
    WindProtectionIEC: The grid protection model with which this wind dynamics lookup table is associated.
    WindPlantReactiveControlIEC: The voltage and reactive power wind plant control model with which this wind dynamics
      lookup table is associated.
    WindGenType3bIEC: The generator type 3B model with which this wind dynamics lookup table is associated.
    WindPitchContPowerIEC: The pitch control power model with which this wind dynamics lookup table is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindContCurrLimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContPType3IEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContQPQULimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContRotorRIEC: Optional[str] = None  # Type M:0..1 in CIM
    input: float = 0.0  # Type #Float in CIM
    lookupTableFunctionType: Optional[str] = None  # Type M:1..1 in CIM
    output: float = 0.0  # Type #Float in CIM
    sequence: int = 0  # Type #Integer in CIM
    WindPlantFreqPcontrolIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindProtectionIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindPlantReactiveControlIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindGenType3bIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindPitchContPowerIEC: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindDynamicsLookupTable\n"
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
            "WindContCurrLimIEC": [
                self.profiles.DY.value,
            ],
            "WindContPType3IEC": [
                self.profiles.DY.value,
            ],
            "WindContQPQULimIEC": [
                self.profiles.DY.value,
            ],
            "WindContRotorRIEC": [
                self.profiles.DY.value,
            ],
            "input": [
                self.profiles.DY.value,
            ],
            "lookupTableFunctionType": [
                self.profiles.DY.value,
            ],
            "output": [
                self.profiles.DY.value,
            ],
            "sequence": [
                self.profiles.DY.value,
            ],
            "WindPlantFreqPcontrolIEC": [
                self.profiles.DY.value,
            ],
            "WindProtectionIEC": [
                self.profiles.DY.value,
            ],
            "WindPlantReactiveControlIEC": [
                self.profiles.DY.value,
            ],
            "WindGenType3bIEC": [
                self.profiles.DY.value,
            ],
            "WindPitchContPowerIEC": [
                self.profiles.DY.value,
            ],
        }
