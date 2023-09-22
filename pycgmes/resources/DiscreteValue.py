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

from .MeasurementValue import MeasurementValue


@dataclass(config=DataclassConfig)
class DiscreteValue(MeasurementValue, ModuleType):
    """
    DiscreteValue represents a discrete MeasurementValue.

    Command: The Control variable associated with the MeasurementValue.
    Discrete: Measurement to which this value is connected.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DiscreteValue(*args, **kwargs)

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # Command : Optional[str] = Field(default=None, in_profiles = [Profile.OP, ])

    Discrete: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DiscreteValue"
# work as well as
# "from DiscreteValue import DiscreteValue".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DiscreteValue
