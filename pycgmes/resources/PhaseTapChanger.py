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
from .TapChanger import TapChanger


@dataclass(config=DataclassConfig)
class PhaseTapChanger(TapChanger):
    """
    A transformer phase shifting tap model that controls the phase angle difference across the power transformer and
      potentially the active power flow through the power transformer.  This phase tap model may also impact the
      voltage magnitude.

    TransformerEnd: Transformer end to which this phase tap changer belongs.
    """

    TransformerEnd: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
