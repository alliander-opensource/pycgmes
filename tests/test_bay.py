import textwrap

import pytest
from pydantic import ValidationError

from pycgmes.resources import (
    Base,
    Bay,
    ConnectivityNodeContainer,
    EquipmentContainer,
    IdentifiedObject,
    PowerSystemResource,
)
from pycgmes.resources.Base import Profile


class TestBay:
    def test_load_bay(self):
        b = Bay()

    def test_bay_has_mrid(self):
        b = Bay()
        assert getattr(b, "mRID") is not None

    def test_bay_has_expected_parents(self):
        parents = Bay.__mro__[0:6]  # after that there's object.
        expected = (  # mro returns a tuple
            Bay,
            EquipmentContainer,
            ConnectivityNodeContainer,
            PowerSystemResource,
            IdentifiedObject,
            Base,
        )
        assert expected == parents

    def test_bay_has_expected_str(self):
        expected = textwrap.dedent(
            """
        description=
        energyIdentCodeEic=
        mRID=
        name=
        shortName=
        VoltageLevel=None
        __class__=Bay
        """
        )[
            1:-1  # The first and last characters are newlines, which are not in str()
        ]
        assert str(Bay()) == expected

    def test_bay_has_expected_profiles(self):
        expected = {Profile.EQBD, Profile.EQ}

        assert expected == Bay().possible_profiles

    @pytest.mark.parametrize(
        "profile, attribute_names",
        [
            # Different profiles will have different attributes.
            ("EQ", {"description", "VoltageLevel", "energyIdentCodeEic", "shortName", "name"}),
            ("SV", {"name"}),
        ],
    )
    def test_bay_has_expected_attributes(self, profile, attribute_names):
        assert attribute_names == {a.name for a in Bay().cgmes_attribute_names_in_profile(Profile[profile])}

    def test_param_casting(self):
        # An int is castable to string, and it happens.
        assert Bay(VoltageLevel=42).VoltageLevel == "42"

    def test_param_validation(self):
        # mRID is not allowed to be None
        with pytest.raises(ValidationError):
            Bay(mRID=None)
