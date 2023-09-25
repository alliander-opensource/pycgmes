"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Curve import Curve


@dataclass(config=DataclassConfig)
class ReactiveCapabilityCurve(Curve):
    """
    Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring
      modes. For each active power value there is a corresponding high and low reactive power limit  value.
      Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis
      values represent reactive minimum and the Y2 axis values represent reactive maximum.

    EquivalentInjection: The equivalent injection using this reactive capability curve.
    InitiallyUsedBySynchronousMachines: Synchronous machines using this curve as default.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # EquivalentInjection : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # InitiallyUsedBySynchronousMachines : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
