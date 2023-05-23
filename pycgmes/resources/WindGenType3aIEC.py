"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .WindGenType3IEC import WindGenType3IEC


@dataclass
class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC type 3A generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.2.

    kpc: Current PI controller proportional gain (KPc). It is a type-dependent parameter.
    tic: Current PI controller integration time constant (TIc) (>= 0). It is a type-dependent parameter.
    WindTurbineType4IEC: Wind turbine type 4 model with which this wind generator type 3A model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kpc: float = 0.0  # Type #Float in CIM
    tic: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindGenType3aIEC\n"
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
            "kpc": [
                self.profiles.DY.value,
            ],
            "tic": [
                self.profiles.DY.value,
            ],
            "WindTurbineType4IEC": [
                self.profiles.DY.value,
            ],
        }
