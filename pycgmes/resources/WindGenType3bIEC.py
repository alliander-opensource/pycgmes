"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindGenType3IEC import WindGenType3IEC


@dataclass(config=DataclassConfig)
class WindGenType3bIEC(WindGenType3IEC):
    """
    IEC type 3B generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.3.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this generator type 3B model.
    mwtcwp: Crowbar control mode (MWTcwp). It is a case-dependent parameter. true = 1 in the IEC model false = 0 in the
      IEC model.
    tg: Current generation time constant (Tg) (>= 0). It is a type-dependent parameter.
    two: Time constant for crowbar washout filter (Two) (>= 0). It is a case-dependent parameter.
    """

    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    mwtcwp: bool = False  # Type #Boolean in CIM
    tg: int = 0  # Type #Seconds in CIM
    two: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindGenType3bIEC"]
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
            "WindDynamicsLookupTable": [
                Profile.DY.value,
            ],
            "mwtcwp": [
                Profile.DY.value,
            ],
            "tg": [
                Profile.DY.value,
            ],
            "two": [
                Profile.DY.value,
            ],
        }
