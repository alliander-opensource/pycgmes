# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


@dataclass(config=DataclassConfig)
class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """
    The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit
      diagram for the direct- and quadrature- axes, with two equivalent rotor windings in each axis.   Equations for
      conversion between equivalent circuit and time constant reactance forms: Xs = Xm + Xl X' = Xl + Xm x Xlr1 /
      (Xm + Xlr1) X'' = Xl + Xm x Xlr1 x Xlr2 / (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2) T'o = (Xm + Xlr1) / (omega0 x
      Rr1) T''o = (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2) / (omega0 x Rr2 x (Xm + Xlr1) Same equations using CIM
      attributes from AsynchronousMachineTimeConstantReactance class on left of "=" and
      AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm +
      RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1
      / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 x xlr2 / (xm x xlr1 + xm x xlr2
      + xlr1 x xlr2) tpo = (xm + xlr1) / (2 x pi x nominal frequency x rr1) tppo = (xm x xlr1 + xm x xlr2 + xlr1 x
      xlr2) / (2 x pi x nominal frequency x rr2 x (xm + xlr1).

    xm: Magnetizing reactance.
    rr1: Damper 1 winding resistance.
    xlr1: Damper 1 winding leakage reactance.
    rr2: Damper 2 winding resistance.
    xlr2: Damper 2 winding leakage reactance.
    """

    xm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rr1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xlr1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rr2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xlr2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
