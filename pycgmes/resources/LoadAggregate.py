"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadDynamics import LoadDynamics


@dataclass(config=DataclassConfig)
class LoadAggregate(LoadDynamics):
    """
    Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static
      (power flow) data. This load is usually the aggregation of many individual load devices and the load model is
      an approximate representation of the aggregate response of the load devices to system disturbances. Standard
      aggregate load model comprised of static and/or dynamic components.  A static load model represents the
      sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus
      voltage. A dynamic load model can be used to represent the aggregate response of the motor components of the
      load.

    LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load.
    LoadStatic: Aggregate static load associated with this aggregate load.
    """

    # *Association not used*
    # LoadMotor : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # LoadStatic : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadAggregate"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "LoadMotor": [
                Profile.DY.value,
            ],
            "LoadStatic": [
                Profile.DY.value,
            ],
        }
