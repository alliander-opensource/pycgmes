"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindPlantDynamics import WindPlantDynamics


@dataclass
class WindPlantIEC(WindPlantDynamics):
    """
    Simplified IEC type plant level model.  Reference: IEC 61400-27-1:2015, Annex D.

    WindPlantFreqPcontrolIEC: Wind plant frequency and active power control model associated with this wind plant.
    WindPlantReactiveControlIEC: Wind plant model with which this wind reactive control is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindPlantFreqPcontrolIEC: Optional[str] = None  # Type M:1 in CIM
    WindPlantReactiveControlIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindPlantIEC\n"
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
            "WindPlantFreqPcontrolIEC": [
                self.profiles.DY.value,
            ],
            "WindPlantReactiveControlIEC": [
                self.profiles.DY.value,
            ],
        }
