"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContRotorRIEC(IdentifiedObject):
    """
    Rotor resistance control model. Reference: IEC 61400-27-1:2015, 5.6.5.3.

    kirr: Integral gain in rotor resistance PI controller (KIrr). It is a type-dependent parameter.
    komegafilt: Filter gain for generator speed measurement (Komegafilt). It is a type-dependent parameter.
    kpfilt: Filter gain for power measurement (Kpfilt). It is a type-dependent parameter.
    kprr: Proportional gain in rotor resistance PI controller (KPrr). It is a type-dependent parameter.
    rmax: Maximum rotor resistance (rmax) (> WindContRotorRIEC.rmin). It is a type-dependent parameter.
    rmin: Minimum rotor resistance (rmin) (< WindContRotorRIEC.rmax). It is a type-dependent parameter.
    tomegafiltrr: Filter time constant for generator speed measurement (Tomegafiltrr) (>= 0). It is a type-dependent
      parameter.
    tpfiltrr: Filter time constant for power measurement (Tpfiltrr) (>= 0). It is a type-dependent parameter.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model.
    WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is
      associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kirr: float = 0.0  # Type #PU in CIM
    komegafilt: float = 0.0  # Type #Float in CIM
    kpfilt: float = 0.0  # Type #Float in CIM
    kprr: float = 0.0  # Type #PU in CIM
    rmax: float = 0.0  # Type #PU in CIM
    rmin: float = 0.0  # Type #PU in CIM
    tomegafiltrr: int = 0  # Type #Seconds in CIM
    tpfiltrr: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # WindGenTurbineType2IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContRotorRIEC\n"
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
            "kirr": [
                self.profiles.DY.value,
            ],
            "komegafilt": [
                self.profiles.DY.value,
            ],
            "kpfilt": [
                self.profiles.DY.value,
            ],
            "kprr": [
                self.profiles.DY.value,
            ],
            "rmax": [
                self.profiles.DY.value,
            ],
            "rmin": [
                self.profiles.DY.value,
            ],
            "tomegafiltrr": [
                self.profiles.DY.value,
            ],
            "tpfiltrr": [
                self.profiles.DY.value,
            ],
            "WindDynamicsLookupTable": [
                self.profiles.DY.value,
            ],
            "WindGenTurbineType2IEC": [
                self.profiles.DY.value,
            ],
        }
