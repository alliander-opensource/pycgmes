"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .EarthFaultCompensator import EarthFaultCompensator


@dataclass(config=DataclassConfig)
class PetersenCoil(EarthFaultCompensator, ModuleType):
    """
    A variable impedance device normally used to offset line charging during single line faults in an ungrounded section
      of network.

    mode: The mode of operation of the Petersen coil.
    nominalU: The nominal voltage for which the coil is designed.
    offsetCurrent: The offset current that the Petersen coil controller is operating from the resonant point.  This is
      normally a fixed amount for which the controller is configured and could be positive or
      negative.  Typically 0 to 60 A depending on voltage and resonance conditions.
    positionCurrent: The control current used to control the Petersen coil also known as the position current.
      Typically in the range of 20 mA to 200 mA.
    xGroundMax: The maximum reactance.
    xGroundMin: The minimum reactance.
    xGroundNominal: The nominal reactance.  This is the operating point (normally over compensation) that is defined
      based on the resonance point in the healthy network condition.  The impedance is calculated
      based on nominal voltage divided by position current.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PetersenCoil(*args, **kwargs)

    mode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
        ],
    )

    nominalU: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    offsetCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    positionCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    xGroundMax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    xGroundMin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    xGroundNominal: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
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
            Profile.SC,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import PetersenCoil"
# work as well as
# "from PetersenCoil import PetersenCoil".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PetersenCoil
