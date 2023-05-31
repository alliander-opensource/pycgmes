"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .LoadDynamics import LoadDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # LoadMotor : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # LoadStatic : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=LoadAggregate\n"
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
            "LoadMotor": [
                self.profiles.DY.value,
            ],
            "LoadStatic": [
                self.profiles.DY.value,
            ],
        }
