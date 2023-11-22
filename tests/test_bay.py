# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

# Checking only one well known class, for its callable module shortcut.
# As they are generated, if one is correct, the others should be as well.
import textwrap

import pytest
from pydantic import ValidationError

from pycgmes.resources.Bay import Bay
from pycgmes.resources.ConnectivityNodeContainer import ConnectivityNodeContainer
from pycgmes.resources.EquipmentContainer import EquipmentContainer
from pycgmes.resources.IdentifiedObject import IdentifiedObject
from pycgmes.resources.PowerSystemResource import PowerSystemResource
from pycgmes.utils.base import Base
from pycgmes.utils.profile import Profile


class TestBay:
    def test_load_bay(self):
        Bay()

    def test_bay_has_mrid(self):
        b = Bay()
        assert b.mRID is not None

    def test_bay_has_expected_parents(self):
        parents = Bay.__mro__[0:6]
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
        VoltageLevel=None
        __class__=Bay
        description=
        energyIdentCodeEic=
        mRID=
        name=
        shortName=
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

    def test_param_validation(self):
        # mRID is not allowed to be None
        with pytest.raises(ValidationError):
            Bay(mRID=None)

    def test_extra_filed_forbidden(self):
        # Extra fields are not allowed
        with pytest.raises(ValidationError):
            Bay(somefield="should not exist")
