# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroPID2(TurbineGovernorDynamics):
    """
    Hydro turbine and governor. Represents plants with straightforward penstock configurations and "three term" electro-
      hydraulic governors (i.e. WoodwardTM electronic). [Footnote: Woodward electronic governors are an example of
      suitable products available commercially. This information is given for the convenience of users of this
      document and does not constitute an endorsement by IEC of these products.]

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    treg: Speed detector time constant (Treg) (>= 0).  Typical value = 0.
    rperm: Permanent drop (Rperm).  Typical value = 0.
    kp: Proportional gain (Kp).  Typical value = 0.
    ki: Reset gain (Ki).  Unit = PU/s.  Typical value = 0.
    kd: Derivative gain (Kd).  Typical value = 0.
    ta: Controller time constant (Ta) (>= 0).  Typical value = 0.
    tb: Gate servo time constant (Tb) (> 0).
    velmax: Maximum gate opening velocity (Velmax) (< GovHydroPID2.velmin).  Unit = PU / s.  Typical value = 0.
    velmin: Maximum gate closing velocity (Velmin) (> GovHydroPID2.velmax).  Unit = PU / s.  Typical value = 0.
    gmax: Maximum gate opening (Gmax) (> GovHydroPID2.gmin).  Typical value = 0.
    gmin: Minimum gate opening (Gmin) (> GovHydroPID2.gmax).  Typical value = 0.
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 0.
    d: Turbine damping factor (D).  Unit = delta P / delta speed.  Typical value = 0.
    g0: Gate opening at speed no load (G0).  Typical value = 0.
    g1: Intermediate gate opening (G1).  Typical value = 0.
    p1: Power at gate opening G1 (P1).  Typical value = 0.
    g2: Intermediate gate opening (G2).  Typical value = 0.
    p2: Power at gate opening G2 (P2).  Typical value = 0.
    p3: Power at full opened gate (P3).  Typical value = 0.
    atw: Factor multiplying Tw (Atw).  Typical value = 0.
    feedbackSignal: Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe.
    """

    mwbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    treg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rperm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    velmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    gmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    g0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    g1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    g2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    atw: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    feedbackSignal: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
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
