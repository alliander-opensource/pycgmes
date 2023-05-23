"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindPitchContPowerIEC(IdentifiedObject):
    """
    Pitch control power model. Reference: IEC 61400-27-1:2015, 5.6.5.1.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this pitch control power model.
    WindGenTurbineType1bIEC: Wind turbine type 1B model with which this pitch control power model is associated.
    WindGenTurbineType2IEC: Wind turbine type 2 model with which this pitch control power model is associated.
    dpmax: Rate limit for increasing power (dpmax) (> WindPitchContPowerIEC.dpmin). It is a type-dependent parameter.
    dpmin: Rate limit for decreasing power (dpmin) (< WindPitchContPowerIEC.dpmax). It is a type-dependent parameter.
    pmin: Minimum power setting (pmin). It is a type-dependent parameter.
    pset: If pinit < pset then power will be ramped down to pmin. It is (pset) in the IEC 61400-27-1:2015. It is a type-
      dependent parameter.
    t1: Lag time constant (T1) (>= 0). It is a type-dependent parameter.
    tr: Voltage measurement time constant (Tr) (>= 0). It is a type-dependent parameter.
    uuvrt: Dip detection threshold (uUVRT). It is a type-dependent parameter.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # WindGenTurbineType1bIEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindGenTurbineType2IEC : Optional[str] = None  # Type M:0..1 in CIM
    dpmax: float = 0.0  # Type #PU in CIM
    dpmin: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    pset: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    tr: int = 0  # Type #Seconds in CIM
    uuvrt: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindPitchContPowerIEC\n"
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
            "WindDynamicsLookupTable": [
                self.profiles.DY.value,
            ],
            "WindGenTurbineType1bIEC": [
                self.profiles.DY.value,
            ],
            "WindGenTurbineType2IEC": [
                self.profiles.DY.value,
            ],
            "dpmax": [
                self.profiles.DY.value,
            ],
            "dpmin": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "pset": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "tr": [
                self.profiles.DY.value,
            ],
            "uuvrt": [
                self.profiles.DY.value,
            ],
        }
