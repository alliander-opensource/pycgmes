"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=WindDynamicsLookupTable"]
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
            "WindContCurrLimIEC": [
                Profile.DY.value,
            ],
            "WindContPType3IEC": [
                Profile.DY.value,
            ],
            "WindContQPQULimIEC": [
                Profile.DY.value,
            ],
            "WindContRotorRIEC": [
                Profile.DY.value,
            ],
            "input": [
                Profile.DY.value,
            ],
            "lookupTableFunctionType": [
                Profile.DY.value,
            ],
            "output": [
                Profile.DY.value,
            ],
            "sequence": [
                Profile.DY.value,
            ],
            "WindPlantFreqPcontrolIEC": [
                Profile.DY.value,
            ],
            "WindProtectionIEC": [
                Profile.DY.value,
            ],
            "WindPlantReactiveControlIEC": [
                Profile.DY.value,
            ],
            "WindGenType3bIEC": [
                Profile.DY.value,
            ],
            "WindPitchContPowerIEC": [
                Profile.DY.value,
            ],
        }
