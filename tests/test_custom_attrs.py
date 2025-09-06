# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

from functools import cached_property

import pytest
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.base import Base
from pycgmes.utils.constants import NAMESPACES
from pycgmes.utils.profile import BaseProfile, Profile


@dataclass
class CustomBay(Bay):
    # Extends Bay. Has a lot of inherited fields.
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
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
class CustomBase(Base):
    # Extends Base. Has no inherited fields. Says its Bay.
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
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

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return Profile.EQ


@dataclass
class CustomButNotmuch(Base):
    # Extends Base. No inherited fields. Not namespace defined anywhere.
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
        # no namespace
    )

    # no apparent_name()

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return Profile.EQ


@dataclass
class CustomNS(Base):
    # Extends Base. No inherited fields. NS only defined at class level, but will be
    # used by the attribute.
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
        # no namespace
    )

    @cached_property
    def namespace(self) -> str:
        return "cheesy namespace"

    # no apparent_name()

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return Profile.EQ


class TestCustom:
    @pytest.mark.parametrize(
        ("klass", "num_attrs", "apparent", "ns"),
        [
            (CustomBay, 6, "Bay", "custom"),
            (CustomBase, 1, "Bay", "custom"),
            (CustomButNotmuch, 1, "CustomButNotmuch", NAMESPACES["cim"]),
            (CustomNS, 1, "CustomNS", "cheesy namespace"),
        ],
    )
    def test_customisation(self, klass, num_attrs, apparent, ns):
        # Test different variations of class with a 'colour' attribute.
        colour = "cheese"
        cust = klass(colour=colour)
        attrs = cust.cgmes_attributes_in_profile(None)
        assert len(attrs) == num_attrs
        assert f"{apparent}.colour" in attrs
        assert attrs[f"{apparent}.colour"]["value"] == colour
        assert attrs[f"{apparent}.colour"]["namespace"] == ns
