"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC2A model for discontinuous excitation control. This system provides transient excitation boosting via
      an open-loop control as initiated by a trigger signal generated remotely. Reference: IEEE 421.5-2005 12.3.

    vk: Discontinuous controller input reference (VK).
    td1: Discontinuous controller time constant (TD1) (>= 0).
    td2: Discontinuous controller washout time constant (TD2) (>= 0).
    vdmin: Limiter (VDMIN) (< DiscExcContIEEEDEC2A.vdmax).
    vdmax: Limiter (VDMAX) (> DiscExcContIEEEDEC2A.vdmin).
    """

    vk: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vdmax: float = Field(
        default=0.0,
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
