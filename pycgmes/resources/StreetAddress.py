"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class StreetAddress(Base):
    """
    General purpose street and postal address information.

    streetDetail: Street detail.
    townDetail: Town detail.
    status: Status of this address.
    postalCode: Postal code for the address.
    poBox: Post office box.
    language: The language in which the address is specified, using ISO 639-1 two digit language code.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    streetDetail: float = 0.0  # Type #StreetDetail in CIM
    townDetail: float = 0.0  # Type #TownDetail in CIM
    status: float = 0.0  # Type #Status in CIM
    postalCode: str = ""  # Type #String in CIM
    poBox: str = ""  # Type #String in CIM
    language: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=StreetAddress\n"
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
            "streetDetail": [
                self.profiles.GL.value,
            ],
            "townDetail": [
                self.profiles.GL.value,
            ],
            "status": [
                self.profiles.GL.value,
            ],
            "postalCode": [
                self.profiles.GL.value,
            ],
            "poBox": [
                self.profiles.GL.value,
            ],
            "language": [
                self.profiles.GL.value,
            ],
        }
