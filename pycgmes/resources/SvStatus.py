"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class SvStatus(Base):
    """
    State variable for status.

    ConductingEquipment: The conducting equipment associated with the status state variable.
    inService: The in service status as a result of topology processing.  It indicates if the equipment is considered as
      energized by the power flow. It reflects if the equipment is connected within a solvable island.
      It does not necessarily reflect whether or not the island was solved by the power flow.
    """

    ConductingEquipment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    inService: bool = Field(
        default=False,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }
