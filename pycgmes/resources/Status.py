"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class Status(Base):
    """
    Current status information relevant to an entity.

    value: Status value at `dateTime`; prior status changes may have been kept in instances of activity records
      associated with the object to which this status applies.
    dateTime: Date and time for which status `value` applies.
    remark: Pertinent information regarding the current `value`, as free form text.
    reason: Reason code or explanation for why an object went to the current status `value`.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    value: str = ""  # Type #String in CIM
    dateTime: str = ""  # Type #DateTime in CIM
    remark: str = ""  # Type #String in CIM
    reason: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Status\n"
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
            "value": [
                self.profiles.GL.value,
            ],
            "dateTime": [
                self.profiles.GL.value,
            ],
            "remark": [
                self.profiles.GL.value,
            ],
            "reason": [
                self.profiles.GL.value,
            ],
        }
