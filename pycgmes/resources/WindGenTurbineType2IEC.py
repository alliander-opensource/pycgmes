"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


@dataclass
class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC type 2.  Reference: IEC 61400-27-1:2015, 5.5.3.

    WindContRotorRIEC: Wind control rotor resistance model associated with wind turbine type 2 model.
    WindPitchContPowerIEC: Pitch control power model associated with this wind turbine type 2 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindContRotorRIEC: Optional[str] = None  # Type M:1 in CIM
    WindPitchContPowerIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindGenTurbineType2IEC\n"
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
            "WindContRotorRIEC": [
                self.profiles.DY.value,
            ],
            "WindPitchContPowerIEC": [
                self.profiles.DY.value,
            ],
        }
