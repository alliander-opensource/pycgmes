"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContQPQULimIEC(IdentifiedObject):
    """
    QP and QU limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.10.

    tpfiltql: Power measurement filter time constant for Q capacity (Tpfiltql) (>= 0). It is a type-dependent parameter.
    tufiltql: Voltage measurement filter time constant for Q capacity (Tufiltql) (>= 0). It is a type-dependent
      parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this QP and QU limitation model is
      associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this QP and QU limitation model.
    """

    tpfiltql: int = 0  # Type #Seconds in CIM
    tufiltql: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindContQPQULimIEC"]
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
            "tpfiltql": [
                Profile.DY.value,
            ],
            "tufiltql": [
                Profile.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                Profile.DY.value,
            ],
            "WindDynamicsLookupTable": [
                Profile.DY.value,
            ],
        }
