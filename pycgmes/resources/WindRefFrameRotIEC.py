"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindRefFrameRotIEC(IdentifiedObject):
    """
    Reference frame rotation model. Reference: IEC 61400-27-1:2015, 5.6.3.5.

    tpll: Time constant for PLL first order filter model (TPLL) (>= 0). It is a type-dependent parameter.
    upll1: Voltage below which the angle of the voltage is filtered and possibly also frozen (uPLL1). It is a type-
      dependent parameter.
    upll2: Voltage (uPLL2) below which the angle of the voltage is frozen if uPLL2 is smaller or equal to uPLL1 . It is
      a type-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reference frame rotation model is
      associated.
    """

    tpll: int = 0  # Type #Seconds in CIM
    upll1: float = 0.0  # Type #PU in CIM
    upll2: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindRefFrameRotIEC"]
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
            "tpll": [
                Profile.DY.value,
            ],
            "upll1": [
                Profile.DY.value,
            ],
            "upll2": [
                Profile.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                Profile.DY.value,
            ],
        }
