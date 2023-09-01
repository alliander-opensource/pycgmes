"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
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

    number: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    name: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    suffix: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    prefix: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    type: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    code: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    buildingName: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    suiteNumber: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    addressGeneral: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    addressGeneral2: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    addressGeneral3: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    withinTownLimits: bool = Field(
        default=False,
        in_profiles=[
            Profile.GL,
        ],
    )

    floorIdentification: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
