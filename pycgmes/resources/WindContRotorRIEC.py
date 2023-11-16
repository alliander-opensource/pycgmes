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
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContRotorRIEC(IdentifiedObject):
    """
    Rotor resistance control model. Reference: IEC 61400-27-1:2015, 5.6.5.3.

    kirr: Integral gain in rotor resistance PI controller (KIrr). It is a type-dependent parameter.
    komegafilt: Filter gain for generator speed measurement (Komegafilt). It is a type-dependent parameter.
    kpfilt: Filter gain for power measurement (Kpfilt). It is a type-dependent parameter.
    kprr: Proportional gain in rotor resistance PI controller (KPrr). It is a type-dependent parameter.
    rmax: Maximum rotor resistance (rmax) (> WindContRotorRIEC.rmin). It is a type-dependent parameter.
    rmin: Minimum rotor resistance (rmin) (< WindContRotorRIEC.rmax). It is a type-dependent parameter.
    tomegafiltrr: Filter time constant for generator speed measurement (Tomegafiltrr) (>= 0). It is a type-dependent
      parameter.
    tpfiltrr: Filter time constant for power measurement (Tpfiltrr) (>= 0). It is a type-dependent parameter.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model.
    WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is
      associated.
    """

    kirr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    komegafilt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpfilt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kprr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    rmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tomegafiltrr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpfiltrr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # WindDynamicsLookupTable : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindGenTurbineType2IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
