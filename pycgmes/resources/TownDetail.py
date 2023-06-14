"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class TownDetail(Base):
    """
    Town details, in the context of address.

    code: Town code.
    section: Town section. For example, it is common for there to be 36 sections per township.
    name: Town name.
    stateOrProvince: Name of the state or province.
    country: Name of the country.
    """

    code: str = ""  # Type #String in CIM
    section: str = ""  # Type #String in CIM
    name: str = ""  # Type #String in CIM
    stateOrProvince: str = ""  # Type #String in CIM
    country: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=TownDetail"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "code": [
                Profile.GL.value,
            ],
            "section": [
                Profile.GL.value,
            ],
            "name": [
                Profile.GL.value,
            ],
            "stateOrProvince": [
                Profile.GL.value,
            ],
            "country": [
                Profile.GL.value,
            ],
        }
