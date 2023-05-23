"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindProtectionIEC(IdentifiedObject):
    """
    The grid protection model includes protection against over- and under-voltage, and against over- and under-
      frequency. Reference: IEC 61400-27-1:2015, 5.6.6.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this grid protection model.
    dfimax: Maximum rate of change of frequency (dFmax). It is a type-dependent parameter.
    fover: Wind turbine over frequency protection activation threshold (fover). It is a project-dependent parameter.
    funder: Wind turbine under frequency protection activation threshold (funder). It is a project-dependent parameter.
    mzc: Zero crossing measurement mode (Mzc).  It is a type-dependent parameter.  true = WT protection system uses zero
      crossings to detect frequency (1 in the IEC model) false = WT protection system does not use zero
      crossings to detect frequency (0 in the IEC model).
    tfma: Time interval of moving average window (TfMA) (>= 0).  It is a type-dependent parameter.
    uover: Wind turbine over voltage protection activation threshold (uover). It is a project-dependent parameter.
    uunder: Wind turbine under voltage protection activation threshold (uunder). It is a project-dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this wind turbine protection model is
      associated.
    WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind turbine protection model is
      associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    dfimax: float = 0.0  # Type #PU in CIM
    fover: float = 0.0  # Type #PU in CIM
    funder: float = 0.0  # Type #PU in CIM
    mzc: bool = False  # Type #Boolean in CIM
    tfma: int = 0  # Type #Seconds in CIM
    uover: float = 0.0  # Type #PU in CIM
    uunder: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindTurbineType1or2IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindProtectionIEC\n"
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
            "dfimax": [
                self.profiles.DY.value,
            ],
            "fover": [
                self.profiles.DY.value,
            ],
            "funder": [
                self.profiles.DY.value,
            ],
            "mzc": [
                self.profiles.DY.value,
            ],
            "tfma": [
                self.profiles.DY.value,
            ],
            "uover": [
                self.profiles.DY.value,
            ],
            "uunder": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                self.profiles.DY.value,
            ],
            "WindTurbineType1or2IEC": [
                self.profiles.DY.value,
            ],
        }
