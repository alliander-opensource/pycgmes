"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IOPoint import IOPoint


@dataclass
class MeasurementValue(IOPoint):
    """
    The current state for a measurement. A state value is an instance of a measurement from a specific source.
      Measurements can be associated with many state values, each representing a different source for the
      measurement.

    timeStamp: The time when the value was last updated.
    sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the
      sensor is used under  reference conditions.
    MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink,
      manual, etc. User conventions for the names of sources are contained in the
      introduction to IEC 61970-301.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    timeStamp: str = ""  # Type #DateTime in CIM
    sensorAccuracy: float = 0.0  # Type #PerCent in CIM
    # *Association not used*
    # MeasurementValueQuality : Optional[str] = None  # Type M:0..1 in CIM
    MeasurementValueSource: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=MeasurementValue\n"
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
                self.profiles.OP.value,
            ],
            # Attributes
            "timeStamp": [
                self.profiles.OP.value,
            ],
            "sensorAccuracy": [
                self.profiles.OP.value,
            ],
            "MeasurementValueQuality": [
                self.profiles.OP.value,
            ],
            "MeasurementValueSource": [
                self.profiles.OP.value,
            ],
        }
