"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class Date(Base):
    """
    Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ". A local timezone
      relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".

    """

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Date"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.TP.value,
                Profile.GL.value,
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            # Attributes
        }
