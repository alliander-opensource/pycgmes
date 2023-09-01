# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

class TestInit:
    def test_version_given(self):
        # I just want to know that the version has been given.
        from pycgmes.resources import CGMES_VERSION
