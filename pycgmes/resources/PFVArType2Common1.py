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
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass(config=DataclassConfig)
class PFVArType2Common1(PFVArControllerType2Dynamics):
    """
    Power factor / reactive power regulator. This model represents the power factor or reactive power controller such as
      the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and
      compares it with the operator's set point. [Footnote: Basler SCP-250 is an example of a suitable product
      available commercially. This information is given for the convenience of users of this document and does not
      constitute an endorsement by IEC of this product.]

    j: Selector (J). true = control mode for reactive power false = control mode for power factor.
    kp: Proportional gain (Kp).
    ki: Reset gain (Ki).
    max: Output limit (max).
    ref: Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This
      initialisation can override the value exchanged by this attribute to represent a plant operator`s change
      of the reference setting.
    """

    j: bool = Field(
        default=False,
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

    max: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ref: float = Field(
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
