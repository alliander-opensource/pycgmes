# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.base import Base
from pycgmes.utils.constants import NAMESPACES
from pycgmes.utils.dataclassconfig import DataclassConfig
from pycgmes.utils.profile import Profile


@dataclass(config=DataclassConfig)
class CustomBay(Bay):
    # Extends Bay. Has a lot of inherited fields.
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(cls):
        return "Bay"


@dataclass(config=DataclassConfig)
class CustomBase(Base):
    # Extends Base. Has no inherited fields. Says its Bay.
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(cls):
        return "Bay"


@dataclass(config=DataclassConfig)
class CustomButNotmuch(Base):
    # Extends Base. No inherited fields. Not namespace defined anywhere.
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        # no namespace
    )

    # no apparent_name()


@dataclass(config=DataclassConfig)
class CustomNS(Base):
    # Extends Base. No inherited fields. NS only defined at class level, but will be
    # used by the attribute.
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        # no namespace
    )

    @property
    def namespace(self):
        return "cheesy namespace"

    # no apparent_name()


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
