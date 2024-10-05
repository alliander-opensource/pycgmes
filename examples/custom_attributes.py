# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import json
from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.ACLineSegment import ACLineSegment
from pycgmes.utils.profile import BaseProfile


class CustomProfile(BaseProfile):
    MYOWN = 100


@dataclass
class CustomAttribute(ACLineSegment):
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.MYOWN,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "namespace": "custom for colour",
        },
    )

    structure: str = Field(
        default="chewy",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.MYOWN,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
        # No namespace defined, it will use the class namespace.
    )

    @classmethod
    def apparent_name(cls) -> str:
        return cls.__base__.apparent_name()

    @cached_property
    def namespace(self) -> str:
        return "custom from class"


if __name__ == "__main__":
    my_resource = CustomAttribute(colour="red")

    print("Attributes in profile MYOWN:")
    print(
        json.dumps(
            {qualname: attr for qualname, attr in my_resource.cgmes_attributes_in_profile(CustomProfile.MYOWN).items()},
            indent=2,
        )
    )
