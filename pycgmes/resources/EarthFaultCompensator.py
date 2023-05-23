"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ConductingEquipment import ConductingEquipment


@dataclass
class EarthFaultCompensator(ConductingEquipment):
    """
    A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults.
      An earth fault compensator device modelled with a single terminal implies a second terminal solidly connected
      to ground.  If two terminals are modelled, the ground is not assumed and normal connection rules apply.

    r: Nominal resistance of device.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    r: float = 0.0  # Type #Resistance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=EarthFaultCompensator\n"
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
                self.profiles.EQ.value,
                self.profiles.SC.value,
            ],
            # Attributes
            "r": [
                self.profiles.SC.value,
            ],
        }
