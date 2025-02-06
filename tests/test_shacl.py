# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest

from pycgmes import shacl


class Testshacl:
    def test_shacl_data_path_is_correct(self):
        assert shacl.get_shacl_file_dir().samefile(Path(__file__).parent.parent / "pycgmes" / "shacl" / "datafiles")
        assert shacl.get_shacl_file_dir().exists
        assert shacl.get_shacl_file_dir().is_dir()

    @pytest.mark.parametrize("serialization_type", ["rdf", "ttl"])
    def test_got_some_files(self, serialization_type):
        files = shacl.get_all_shacl_files(serialization=serialization_type)
        assert files  # not empty
        assert all(f.suffix == f".{serialization_type}" for f in files)  # All the expected format ...
        assert all(f.exists() for f in files)  # ... exist ...
        assert all(f.is_file() for f in files)  # ... and are actual files.

    def test_wrong_file_format(self):
        with pytest.raises(ValueError, match="^Parameter .* must be one of 'rdf' or 'ttl'"):
            shacl.get_all_shacl_files(serialization="cheese")
