# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

from functools import cached_property

import pytest
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.profile import BaseProfile


class CustomProfile(BaseProfile):
    CUS = "Tom"
    FRO = "Mage"


@dataclass
class CustomBayAttr(Bay):
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.CUS,
            ],
            "is_used": True,
            "namespace": "custom",
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    @classmethod
    def apparent_name(cls) -> str:
        return "Bay"


@dataclass
class CustomBayClass(Bay):
    @classmethod
    def apparent_name(cls) -> str:
        return "Cheese"

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        return {CustomProfile.CUS}

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return CustomProfile.CUS


class TestCustom:
    def test_custom_profile_in_attrs(self):
        colour = "cheese"
        apparent = "Bay"
        cust = CustomBayAttr(colour=colour)
        mine_attrs = cust.cgmes_attributes_in_profile(CustomProfile.CUS)
        none_attrs = cust.cgmes_attributes_in_profile(CustomProfile.FRO)
        all_attrs = cust.cgmes_attributes_in_profile(None)
        assert len(mine_attrs) == 1
        assert len(all_attrs) == 6
        assert len(none_attrs) == 0

        assert f"{apparent}.colour" in mine_attrs
        assert mine_attrs[f"{apparent}.colour"]["value"] == colour
        assert mine_attrs[f"{apparent}.colour"]["namespace"] == "custom"

    def test_custom_class(self):
        cust = CustomBayClass()
        assert cust.possible_profiles == {CustomProfile.CUS}
        assert cust.recommended_profile == CustomProfile.CUS

    def test_custom_class_uris(self):
        profile = CustomProfile.CUS
        with pytest.raises(NotImplementedError):
            assert profile.uris
