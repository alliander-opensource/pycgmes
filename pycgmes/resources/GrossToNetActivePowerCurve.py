"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Curve import Curve


@dataclass(config=DataclassConfig)
class GrossToNetActivePowerCurve(Curve):
    """
    Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the
      machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined
      measurements at the power station). Station service loads, when modelled, should be treated as non-conforming
      bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.

    GeneratingUnit: A generating unit may have a gross active power to net active power curve, describing the losses and
      auxiliary power requirements of the unit.
    """

    GeneratingUnit: Optional[str] = Field(
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
