# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

import pytest

from pycgmes.utils.profile import BaseProfile, Profile, profile_uris


class TestProfile:
    @pytest.mark.parametrize("profile", list(Profile))
    def test_long_name(self, profile):
        expected = profile.value
        assert expected == profile.long_name

    @pytest.mark.parametrize("profile", list(Profile))
    def test_uris(self, profile):
        expected = profile_uris[profile.name]
        assert len(profile.uris) >= 1
        assert expected == profile.uris

    def test_order(self):
        """The enum values within a class are sorted in the order in which they were defined."""
        assert Profile.EQ < Profile.DY
        assert Profile.DY <= Profile.TP
        assert Profile.TP > Profile.SV
        assert Profile.TP >= Profile.TP
        assert sorted(Profile) == list(Profile)

    def test_order_between_profiles(self):
        """Enum values from different classes should not be mixed up. The order of the classes is alphabetical."""

        class CustomProfile(BaseProfile):
            CUS = "Tom"
            FRO = "Mage"

        class TestProfile(BaseProfile):
            XYZ = "xyz"
            ABC = "abc"

        assert CustomProfile.CUS < CustomProfile.FRO
        assert CustomProfile.FRO <= Profile.EQ
        assert Profile.TP < TestProfile.ABC
        assert TestProfile.ABC >= TestProfile.XYZ
