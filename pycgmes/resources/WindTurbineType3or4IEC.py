"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


@dataclass(config=DataclassConfig)
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 3 and type 4 including their control models.

    WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or type 4 model.
    WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or type 4 model.
    WindContQLimIEC: Constant Q limitation model associated with this wind generator type 3 or type 4 model.
    WindContQPQULimIEC: QP and QU limitation model associated with this wind generator type 3 or type 4 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or type 4 model.
    WindRefFrameRotIEC: Reference frame rotation model associated with this wind turbine type 3 or type 4 model.
    """

    WindContCurrLimIEC: Optional[str] = None  # Type M:1 in CIM
    WIndContQIEC: Optional[str] = None  # Type M:1 in CIM
    WindContQLimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContQPQULimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindProtectionIEC: Optional[str] = None  # Type M:1 in CIM
    WindRefFrameRotIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindTurbineType3or4IEC"]
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
            "WIndContQIEC": [
                Profile.DY.value,
            ],
            "WindContQLimIEC": [
                Profile.DY.value,
            ],
            "WindContQPQULimIEC": [
                Profile.DY.value,
            ],
            "WindProtectionIEC": [
                Profile.DY.value,
            ],
            "WindRefFrameRotIEC": [
                Profile.DY.value,
            ],
        }
