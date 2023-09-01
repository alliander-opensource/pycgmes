"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class GenICompensationForGenJ(IdentifiedObject):
    """
    Resistive and reactive components of compensation for generator associated with IEEE type 2 voltage compensator for
      current flow out of another generator in the interconnection.

    SynchronousMachineDynamics: Standard synchronous machine out of which current flow is being compensated for.
    VcompIEEEType2: The standard IEEE type 2 voltage compensator of this compensation.
    rcij: Resistive component of compensation of generator associated with this IEEE type 2 voltage compensator for
      current flow out of another generator (Rcij).
    xcij: Reactive component of compensation of generator associated with this IEEE type 2 voltage compensator for
      current flow out of another generator (Xcij).
    """

    SynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    VcompIEEEType2: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    rcij: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xcij: float = Field(
        default=0.0,
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
