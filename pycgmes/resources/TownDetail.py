"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class TownDetail(Base):
    """
    Town details, in the context of address.

    code: Town code.
    section: Town section. For example, it is common for there to be 36 sections per township.
    name: Town name.
    stateOrProvince: Name of the state or province.
    country: Name of the country.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    code: str = ""  # Type #String in CIM
    section: str = ""  # Type #String in CIM
    name: str = ""  # Type #String in CIM
    stateOrProvince: str = ""  # Type #String in CIM
    country: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TownDetail\n"
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
            ],
            # Attributes
            "code": [
                self.profiles.GL.value,
            ],
            "section": [
                self.profiles.GL.value,
            ],
            "name": [
                self.profiles.GL.value,
            ],
            "stateOrProvince": [
                self.profiles.GL.value,
            ],
            "country": [
                self.profiles.GL.value,
            ],
        }
