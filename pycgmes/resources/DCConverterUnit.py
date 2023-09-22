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

from .DCEquipmentContainer import DCEquipmentContainer


@dataclass(config=DataclassConfig)
class DCConverterUnit(DCEquipmentContainer, ModuleType):
    """
    Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the
      point of common coupling - DC side, essentially one or more converters, together with one or more converter
      transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any,
      used for conversion.

    operationMode: The operating mode of an HVDC bipole (bipolar, monopolar metallic return, etc).
    Substation: The containing substation of the DC converter unit.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCConverterUnit(*args, **kwargs)

    operationMode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Substation: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
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
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCConverterUnit"
# work as well as
# "from DCConverterUnit import DCConverterUnit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCConverterUnit
