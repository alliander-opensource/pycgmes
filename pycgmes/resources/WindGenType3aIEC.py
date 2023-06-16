"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindGenType3IEC import WindGenType3IEC


@dataclass(config=DataclassConfig)
class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC type 3A generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.2.

    kpc: Current PI controller proportional gain (KPc). It is a type-dependent parameter.
    tic: Current PI controller integration time constant (TIc) (>= 0). It is a type-dependent parameter.
    WindTurbineType4IEC: Wind turbine type 4 model with which this wind generator type 3A model is associated.
    """

    kpc: float = 0.0  # Type #Float in CIM
    tic: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType4IEC : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindGenType3aIEC"]
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
            "kpc": [
                Profile.DY.value,
            ],
            "tic": [
                Profile.DY.value,
            ],
            "WindTurbineType4IEC": [
                Profile.DY.value,
            ],
        }
