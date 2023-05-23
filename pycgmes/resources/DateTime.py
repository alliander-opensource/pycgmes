"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class DateTime(Base):
    """
    Date and time as "yyyy-mm-ddThh:mm:ss.sss", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-
      ddThh:mm:ss.sssZ". A local timezone relative UTC is specified as "yyyy-mm-ddThh:mm:ss.sss-hh:mm". The second
      component (shown here as "ss.sss") could have any number of digits in its fractional part to allow any kind of
      precision beyond seconds.

    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DateTime\n"
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
                self.profiles.GL.value,
                self.profiles.EQ.value,
                self.profiles.OP.value,
            ],
            # Attributes
        }
