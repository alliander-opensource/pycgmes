from pathlib import Path

import pytest
from shacl.pycgmes import shacl


class Testshacl:
    def test_shacl_data_path_is_correct(self):
        assert shacl.get_shacl_file_dir().samefile(
            Path(__file__).parent.parent / "shacl" / "pycgmes" / "shacl" / "datafiles"
        )
        assert shacl.get_shacl_file_dir().exists
        assert shacl.get_shacl_file_dir().is_dir()

    @pytest.mark.parametrize("format", ["rdf", "ttl"])
    def test_got_some_files(self, format):
        files = shacl.get_all_shacl_files(serialization=format)
        assert files  # not empty
        assert all([f.suffix == f".{format}" for f in files])  # All the expected format ...
        assert all([f.exists() for f in files])  # ... exist ...
        assert all([f.is_file() for f in files])  # ... and are actual files.

    def test_wrong_file_format(self):
        with pytest.raises(ValueError):
            shacl.get_all_shacl_files(serialization="cheese")
