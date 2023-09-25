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

from .ProtectedSwitch import ProtectedSwitch


@dataclass(config=DataclassConfig)
class Breaker(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and
      also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions
      e.g.  those of short circuit.

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
            Profile.SSH,
        }
