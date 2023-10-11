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
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker
      position.

    DiscreteValues: The values connected to this measurement.
    ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DiscreteValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    ValueAliasSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
