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

from .Control import Control


@dataclass(config=DataclassConfig)
class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    AnalogValue: The MeasurementValue that is controlled.
    """

    maxValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    minValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    AnalogValue: Optional[str] = Field(
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
