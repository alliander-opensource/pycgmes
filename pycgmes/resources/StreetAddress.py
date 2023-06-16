"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
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

    streetDetail: float = 0.0  # Type #StreetDetail in CIM
    townDetail: float = 0.0  # Type #TownDetail in CIM
    status: float = 0.0  # Type #Status in CIM
    postalCode: str = ""  # Type #String in CIM
    poBox: str = ""  # Type #String in CIM
    language: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=StreetAddress"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.GL.value,
            ],
            # Attributes
            "streetDetail": [
                Profile.GL.value,
            ],
            "townDetail": [
                Profile.GL.value,
            ],
            "status": [
                Profile.GL.value,
            ],
            "postalCode": [
                Profile.GL.value,
            ],
            "poBox": [
                Profile.GL.value,
            ],
            "language": [
                Profile.GL.value,
            ],
        }
