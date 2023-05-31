"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=StreetDetail\n"
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
            "number": [
                self.profiles.GL.value,
            ],
            "name": [
                self.profiles.GL.value,
            ],
            "suffix": [
                self.profiles.GL.value,
            ],
            "prefix": [
                self.profiles.GL.value,
            ],
            "type": [
                self.profiles.GL.value,
            ],
            "code": [
                self.profiles.GL.value,
            ],
            "buildingName": [
                self.profiles.GL.value,
            ],
            "suiteNumber": [
                self.profiles.GL.value,
            ],
            "addressGeneral": [
                self.profiles.GL.value,
            ],
            "addressGeneral2": [
                self.profiles.GL.value,
            ],
            "addressGeneral3": [
                self.profiles.GL.value,
            ],
            "withinTownLimits": [
                self.profiles.GL.value,
            ],
            "floorIdentification": [
                self.profiles.GL.value,
            ],
        }
