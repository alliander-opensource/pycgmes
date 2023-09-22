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

from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentBranch(EquivalentEquipment, ModuleType):
    """
    The class represents equivalent branches. In cases where a transformer phase shift is modelled and the
      EquivalentBranch is spanning the same nodes, the impedance quantities for the EquivalentBranch shall consider
      the needed phase shift.

    r: Positive sequence series resistance of the reduced branch.
    r21: Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is
      optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r
      is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch
      is a result of network reduction prior to the data exchange.
    x: Positive sequence series reactance of the reduced branch.
    x21: Reactance from terminal sequence 2 to terminal sequence 1. Used for steady state power flow. This attribute is
      optional and represents an unbalanced network such as off-nominal phase shifter. If only
      EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x. Usage
      rule: EquivalentBranch is a result of network reduction prior to the data exchange.
    negativeR12: Negative sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeR21: Negative sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeX12: Negative sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    negativeX21: Negative sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveR12: Positive sequence series resistance from terminal sequence  1 to terminal sequence 2 . Used for short
      circuit data exchange according to IEC 60909.  EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveR21: Positive sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveX12: Positive sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveX21: Positive sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    zeroR12: Zero sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the
      data exchange.
    zeroR21: Zero sequence series resistance from terminal sequence  2 to terminal sequence 1. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX12: Zero sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX21: Zero sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data
      exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to
      the data exchange.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return EquivalentBranch(*args, **kwargs)

    r: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    r21: float = Field(
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

    x21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    negativeR12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    negativeR21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    negativeX12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    negativeX21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    positiveR12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    positiveR21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    positiveX12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    positiveX21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    zeroR12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    zeroR21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    zeroX12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    zeroX21: float = Field(
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
# "import EquivalentBranch"
# work as well as
# "from EquivalentBranch import EquivalentBranch".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = EquivalentBranch
