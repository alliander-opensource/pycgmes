# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .Sensor import Sensor


@dataclass(config=DataclassConfig)
class PotentialTransformer(Sensor):
    """
    Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that
      is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering,
      protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
