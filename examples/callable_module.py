"""
All resources are importable in the usual way:
from pycgmes.resources.Bay import Bay
But they can be loaded as well directly:
from pycgmes.resources import Bay

This is provided for possible backward compatibility,
for laziness and because it was fun to research, but there
are a few limitations.
"""
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources import Bay
from pycgmes.utils.profile import Profile

# No problem
# print(Bay(description="Business as usual"))


@dataclass
# Note the instanciation and class as parent
class CustomBay(Bay().__class__):
    """Note the parent!"""

    colour: str = Field(
        default="Red",
        in_profiles=[Profile.EQ],
    )

    @classmethod
    def apparent_name(cls):
        return cls.__base__.__name__


print(CustomBay(description="A tad customised", colour="red"))
