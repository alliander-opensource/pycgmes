# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .AuxiliaryEquipment import AuxiliaryEquipment


@dataclass
class FaultIndicator(AuxiliaryEquipment):
    """
    A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of
      equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and
      Restoration) purposes, assisting with the dispatch of crews to "most likely" part of the network (i.e. assists
      with determining circuit section where the fault most likely happened).

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
