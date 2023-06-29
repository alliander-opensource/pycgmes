"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .HVDCDynamics import HVDCDynamics


@dataclass(config=DataclassConfig)
class VSCDynamics(HVDCDynamics):
    """
    VSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined
      model.

    VsConverter: Voltage source converter to which voltage source converter dynamics model applies.
    """

    VsConverter: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
