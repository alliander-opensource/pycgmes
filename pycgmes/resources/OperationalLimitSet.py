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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class OperationalLimitSet(IdentifiedObject, ModuleType):
    """
    A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for
      example. A set of limits may contain different severities of limit levels that would apply to the same
      equipment. The set may contain limits of different types such as apparent power and current limits or high and
      low voltage limits  that are logically applied together as a set.

    Terminal: The terminal where the operational limit set apply.
    Equipment: The equipment to which the limit set applies.
    OperationalLimitValue: Values of equipment limits.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return OperationalLimitSet(*args, **kwargs)

    Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Equipment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # OperationalLimitValue : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import OperationalLimitSet"
# work as well as
# "from OperationalLimitSet import OperationalLimitSet".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = OperationalLimitSet
