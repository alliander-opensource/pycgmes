"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class Status(Base):
    """
    Current status information relevant to an entity.

    value: Status value at `dateTime`; prior status changes may have been kept in instances of activity records
      associated with the object to which this status applies.
    dateTime: Date and time for which status `value` applies.
    remark: Pertinent information regarding the current `value`, as free form text.
    reason: Reason code or explanation for why an object went to the current status `value`.
    """

    value: str = ""  # Type #String in CIM
    dateTime: str = ""  # Type #DateTime in CIM
    remark: str = ""  # Type #String in CIM
    reason: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Status"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "value": [
                Profile.GL.value,
            ],
            "dateTime": [
                Profile.GL.value,
            ],
            "remark": [
                Profile.GL.value,
            ],
            "reason": [
                Profile.GL.value,
            ],
        }
