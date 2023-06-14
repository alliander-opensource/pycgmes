"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LimitSet(IdentifiedObject):
    """
    Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets
      corresponding to seasonal or other changing conditions. The condition is captured in the name and description
      attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used
      this way.

    isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for
      Measurements and Controls.
    """

    isPercentageLimits: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LimitSet"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.OP.value,
            ],
            # Attributes
            "isPercentageLimits": [
                Profile.OP.value,
            ],
        }
