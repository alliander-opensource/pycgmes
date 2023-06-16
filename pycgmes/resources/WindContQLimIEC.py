"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContQLimIEC(IdentifiedObject):
    """
    Constant Q limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.9.

    qmax: Maximum reactive power (qmax) (> WindContQLimIEC.qmin). It is a type-dependent parameter.
    qmin: Minimum reactive power (qmin) (< WindContQLimIEC.qmax). It is a type-dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this constant Q limitation model is
      associated.
    """

    qmax: float = 0.0  # Type #PU in CIM
    qmin: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindContQLimIEC"]
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
            "qmax": [
                Profile.DY.value,
            ],
            "qmin": [
                Profile.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                Profile.DY.value,
            ],
        }
