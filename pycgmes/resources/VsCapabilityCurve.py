"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Curve import Curve


@dataclass(config=DataclassConfig)
class VsCapabilityCurve(Curve):
    """
    The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and Qmax on Y1-axis and Y2-axis.

    VsConverterDCSides: All converters with this capability curve.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # VsConverterDCSides : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
