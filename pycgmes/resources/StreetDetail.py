"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class StreetDetail(Base):
    """
    Street details, in the context of address.

    number: Designator of the specific location on the street.
    name: Name of the street.
    suffix: Suffix to the street name. For example: North, South, East, West.
    prefix: Prefix to the street name. For example: North, South, East, West.
    type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
    code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner`s
      department or surveyor general`s mapping system, that allocate global reference codes to streets.
    buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct
      point of entry from the street, but may be located inside a larger structure such as a building,
      complex, office block, apartment, etc.
    suiteNumber: Number of the apartment or suite.
    addressGeneral: First line of a free form address or some additional address information (for example a mail stop).
    addressGeneral2: (if applicable) Second line of a free form address.
    addressGeneral3: (if applicable) Third line of a free form address.
    withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default).
    floorIdentification: The identification by name or number, expressed as text, of the floor in the building as part
      of this address.
    """

    number: str = ""  # Type #String in CIM
    name: str = ""  # Type #String in CIM
    suffix: str = ""  # Type #String in CIM
    prefix: str = ""  # Type #String in CIM
    type: str = ""  # Type #String in CIM
    code: str = ""  # Type #String in CIM
    buildingName: str = ""  # Type #String in CIM
    suiteNumber: str = ""  # Type #String in CIM
    addressGeneral: str = ""  # Type #String in CIM
    addressGeneral2: str = ""  # Type #String in CIM
    addressGeneral3: str = ""  # Type #String in CIM
    withinTownLimits: bool = False  # Type #Boolean in CIM
    floorIdentification: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=StreetDetail"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "number": [
                Profile.GL.value,
            ],
            "name": [
                Profile.GL.value,
            ],
            "suffix": [
                Profile.GL.value,
            ],
            "prefix": [
                Profile.GL.value,
            ],
            "type": [
                Profile.GL.value,
            ],
            "code": [
                Profile.GL.value,
            ],
            "buildingName": [
                Profile.GL.value,
            ],
            "suiteNumber": [
                Profile.GL.value,
            ],
            "addressGeneral": [
                Profile.GL.value,
            ],
            "addressGeneral2": [
                Profile.GL.value,
            ],
            "addressGeneral3": [
                Profile.GL.value,
            ],
            "withinTownLimits": [
                Profile.GL.value,
            ],
            "floorIdentification": [
                Profile.GL.value,
            ],
        }
