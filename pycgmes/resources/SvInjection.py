"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class SvInjection(Base):
    """
    The SvInjection reports the calculated bus injection minus the sum of the terminal flows. The terminal flow is
      positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection
      may have the remainder after state estimation or slack after power flow calculation.

    pInjection: The active power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    qInjection: The reactive power mismatch between calculated injection and initial injection.  Positive sign means
      injection into the TopologicalNode (bus).
    TopologicalNode: The topological node associated with the flow injection state variable.
    """

    pInjection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    qInjection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    TopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }
