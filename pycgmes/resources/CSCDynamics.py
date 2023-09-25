"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .HVDCDynamics import HVDCDynamics


@dataclass(config=DataclassConfig)
class CSCDynamics(HVDCDynamics):
    """
    CSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined
      model.

    CSConverter: Current source converter to which current source converter dynamics model applies.
    """

    CSConverter: Optional[str] = Field(
        default=None,
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
