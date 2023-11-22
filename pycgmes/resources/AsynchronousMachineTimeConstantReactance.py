# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


@dataclass
class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """
    Parameter details:  If X'' = X', a single cage (one equivalent rotor winding per axis) is modelled. The "p" in the
      attribute names is a substitution for a "prime" in the usual parameter notation, e.g. tpo refers to T'o.  The
      parameters used for models expressed in time constant reactance form include: - RotatingMachine.ratedS
      (MVAbase); - RotatingMachineDynamics.damping (D); - RotatingMachineDynamics.inertia (H); -
      RotatingMachineDynamics.saturationFactor (S1); - RotatingMachineDynamics.saturationFactor120 (S12); -
      RotatingMachineDynamics.statorLeakageReactance (Xl); - RotatingMachineDynamics.statorResistance (Rs); - .xs
      (Xs); - .xp (X'); - .xpp (X''); - .tpo (T'o); - .tppo (T''o).

    xs: Synchronous reactance (Xs) (>= AsynchronousMachineTimeConstantReactance.xp).  Typical value = 1,8.
    xp: Transient reactance (unsaturated) (X`) (>= AsynchronousMachineTimeConstantReactance.xpp).  Typical value = 0,5.
    xpp: Subtransient reactance (unsaturated) (X``) (> RotatingMachineDynamics.statorLeakageReactance).  Typical value =
      0,2.
    tpo: Transient rotor time constant (T`o) (> AsynchronousMachineTimeConstantReactance.tppo).  Typical value = 5.
    tppo: Subtransient rotor time constant (T``o) (> 0).  Typical value = 0,03.
    """

    xs: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    xp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    xpp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tpo: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tppo: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
