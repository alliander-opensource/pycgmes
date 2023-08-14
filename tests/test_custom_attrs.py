import pytest
from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Base import Base, DataclassConfig, Profile
from resources import ACLineSegment


@dataclass(config=DataclassConfig)
class CustomACLineSegment(ACLineSegment):
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(cls):
        return "ACLineSegment"


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
        return "ACLineSegment"


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
            (CustomACLineSegment, 20, "ACLineSegment", "custom"),
            (CustomBase, 1, "ACLineSegment", "custom"),
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
