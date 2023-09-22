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

from .IOPoint import IOPoint


@dataclass(config=DataclassConfig)
class Control(IOPoint, ModuleType):
    """
    Control is used for supervisory/device control. It represents control outputs that are used to change the state in a
      process, e.g. close or open breaker, a set point value or a raise lower command.

    controlType: Specifies the type of Control. For example, this specifies if the Control represents BreakerOpen,
      BreakerClose, GeneratorVoltageSetPoint, GeneratorRaise, GeneratorLower, etc.
    operationInProgress: Indicates that a client is currently sending control commands that has not completed.
    timeStamp: The last time a control output was sent.
    unitMultiplier: The unit multiplier of the controlled quantity.
    unitSymbol: The unit of measure of the controlled quantity.
    PowerSystemResource: Regulating device governed by this control output.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Control(*args, **kwargs)

    controlType: str = Field(
        default="",
        in_profiles=[
            Profile.OP,
        ],
    )

    operationInProgress: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    timeStamp: str = Field(
        default="",
        in_profiles=[
            Profile.OP,
        ],
    )

    unitMultiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    unitSymbol: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    PowerSystemResource: Optional[str] = Field(
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
# "import Control"
# work as well as
# "from Control import Control".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Control
