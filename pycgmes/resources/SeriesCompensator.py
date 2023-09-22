"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class SeriesCompensator(ConductingEquipment, ModuleType):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It
      is a two terminal device.

    r: Positive sequence resistance.
    x: Positive sequence reactance.
    r0: Zero sequence resistance.
    x0: Zero sequence reactance.
    varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured in parallel with
      the series compensator. It is used for short circuit calculations.
    varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration. It is used for
      short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is
      true. The attribute shall be a positive value.
    varistorVoltageThreshold: The dc voltage at which the varistor starts conducting. It is used for short circuit
      calculations and exchanged only if SeriesCompensator.varistorPresent is true.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SeriesCompensator(*args, **kwargs)

    r: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    x: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    r0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    varistorPresent: bool = Field(
        default=False,
        in_profiles=[
            Profile.SC,
        ],
    )

    varistorRatedCurrent: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    varistorVoltageThreshold: float = Field(
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
# "import SeriesCompensator"
# work as well as
# "from SeriesCompensator import SeriesCompensator".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SeriesCompensator
