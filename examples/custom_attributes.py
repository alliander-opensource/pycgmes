from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.ACLineSegment import ACLineSegment
from pycgmes.utils.profile import BaseProfile, Profile


class CustomProfile(BaseProfile):
    MYOWN = 100


@dataclass
class CustomAttribute(ACLineSegment):
    colour: str = Field(
        default="Red",
        in_profiles=[
            CustomProfile.MYOWN,
        ],
        namespace="custom",
    )

    structure: str = Field(
        default="chewy",
        in_profiles=[
            Profile.EQ,
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(cls):
        return cls.__base__.__name__


if __name__ == "__main__":
    my_resource = CustomAttribute(colour="red")

    print(my_resource.cgmes_attribute_names_in_profile(CustomProfile.MYOWN))
    print(my_resource.cgmes_attribute_names_in_profile(Profile.EQ))
