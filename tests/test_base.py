# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

import pytest

from pycgmes.utils.base import Base


class TestBase:
    def test_possible_profiles_not_implemented(self):
        base = Base()
        with pytest.raises(NotImplementedError):
            assert base.possible_profiles

    def test_recommended_profile_not_implemented(self):
        base = Base()
        with pytest.raises(NotImplementedError):
            assert base.recommended_profile

    def test_resource_name(self):
        expected = "Base"
        assert expected == Base().resource_name

    def test_possible_attribute_profiles(self):
        attr_profiles_map = Base().possible_attribute_profiles
        assert attr_profiles_map == {}
