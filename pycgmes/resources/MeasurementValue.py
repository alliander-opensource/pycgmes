# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IOPoint import IOPoint


@dataclass(config=DataclassConfig)
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

    timeStamp: str = Field(
        default="",
        in_profiles=[
            Profile.OP,
        ],
    )

    sensorAccuracy: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # MeasurementValueQuality : Optional[str] = Field(default=None, in_profiles = [Profile.OP, ])

    MeasurementValueSource: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
