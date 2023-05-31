"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Curve import Curve


@dataclass
class ReactiveCapabilityCurve(Curve):
    """
    Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring
      modes. For each active power value there is a corresponding high and low reactive power limit  value.
      Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis
      values represent reactive minimum and the Y2 axis values represent reactive maximum.

    EquivalentInjection: The equivalent injection using this reactive capability curve.
    InitiallyUsedBySynchronousMachines: Synchronous machines using this curve as default.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # EquivalentInjection : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # InitiallyUsedBySynchronousMachines : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ReactiveCapabilityCurve\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.EQ.value,
            ],
            # Attributes
            "EquivalentInjection": [
                self.profiles.EQ.value,
            ],
            "InitiallyUsedBySynchronousMachines": [
                self.profiles.EQ.value,
            ],
        }
