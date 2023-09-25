# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.base import Base
from pycgmes.utils.dataclassconfig import DataclassConfig
from pycgmes.utils.profile import Profile


@dataclass(config=DataclassConfig)
class CustomBay(Bay):
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
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        # no namespace
    )

    # no apparent_name()


class TestCustom:
    @pytest.mark.parametrize(
        "klass, num_attrs, apparent, ns",
        [
            (CustomBay, 6, "Bay", "custom"),
            (CustomBase, 1, "Bay", "custom"),
            (CustomButNotmuch, 1, "CustomButNotmuch", None),
        ],
    )
    def test_customisation(self, klass, num_attrs, apparent, ns):
        colour = "cheese"
        cust = klass(colour=colour)
        attrs = cust.cgmes_attributes_in_profile(None)
        assert len(attrs) == num_attrs
        assert f"{apparent}.colour" in attrs
        assert attrs[f"{apparent}.colour"]["value"] == colour
        assert attrs[f"{apparent}.colour"]["namespace"] == ns
