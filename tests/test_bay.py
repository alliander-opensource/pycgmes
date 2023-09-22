# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

# Checking only one well known class, for its callable module shortcut.
# As they are generated, if one is correct, the others should be as well.
import textwrap

import pytest
from pydantic import ValidationError

from pycgmes.resources import Bay as ShortcutBay
from pycgmes.resources.Bay import Bay as RealBay
from pycgmes.resources.ConnectivityNodeContainer import ConnectivityNodeContainer
from pycgmes.resources.EquipmentContainer import EquipmentContainer
from pycgmes.resources.IdentifiedObject import IdentifiedObject
from pycgmes.resources.PowerSystemResource import PowerSystemResource
from pycgmes.utils.base import Base
from pycgmes.utils.profile import Profile


@pytest.mark.parametrize("bay_class", [ShortcutBay, RealBay])
class TestBayCallableModule:
    def test_load_bay(self, bay_class):
        b = bay_class()

    def test_bay_has_mrid(self, bay_class):
        b = bay_class()
        assert getattr(b, "mRID") is not None

    def test_bay_has_expected_parents(self, bay_class):
        parents = bay_class().__class__.__mro__[0:6]
        expected = (  # mro returns a tuple
            RealBay,
            EquipmentContainer,
            ConnectivityNodeContainer,
            PowerSystemResource,
            IdentifiedObject,
            Base,
        )
        assert expected == parents

    def test_bay_has_expected_str(self, bay_class):
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
        assert str(bay_class()) == expected

    def test_bay_has_expected_profiles(self, bay_class):
        expected = {Profile.EQBD, Profile.EQ}

        assert expected == bay_class().possible_profiles

    @pytest.mark.parametrize(
        "profile, attribute_names",
        [
            # Different profiles will have different attributes.
            ("EQ", {"description", "VoltageLevel", "energyIdentCodeEic", "shortName", "name"}),
            ("SV", {"name"}),
        ],
    )
    def test_bay_has_expected_attributes(self, bay_class, profile, attribute_names):
        assert attribute_names == {a.name for a in bay_class().cgmes_attribute_names_in_profile(Profile[profile])}

    def test_param_casting(self, bay_class):
        # An int is castable to string, and it happens.
        assert bay_class(VoltageLevel=42).VoltageLevel == "42"

    def test_param_validation(self, bay_class):
        # mRID is not allowed to be None
        with pytest.raises(ValidationError):
            bay_class(mRID=None)
