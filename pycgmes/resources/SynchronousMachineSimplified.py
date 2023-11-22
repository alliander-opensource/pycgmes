# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .SynchronousMachineDynamics import SynchronousMachineDynamics


@dataclass
class SynchronousMachineSimplified(SynchronousMachineDynamics):
    """
    The simplified model represents a synchronous generator as a constant internal voltage behind an impedance (Rs +
      jXp) as shown in the Simplified diagram. Since internal voltage is held constant, there is no Efd input and
      any excitation system model will be ignored.  There is also no Ifd output. This model should not be used for
      representing a real generator except, perhaps, small generators whose response is insignificant.   The
      parameters used for the simplified model include: - RotatingMachineDynamics.damping (D); -
      RotatingMachineDynamics.inertia (H); - RotatingMachineDynamics.statorLeakageReactance (used to exchange jXp
      for SynchronousMachineSimplified); - RotatingMachineDynamics.statorResistance (Rs).

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
