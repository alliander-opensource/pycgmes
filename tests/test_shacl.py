from pathlib import Path

import pytest
import SHACL


class TestShacl:
    def test_shacl_data_path_is_correct(self):
        assert SHACL.get_shacl_file_dir().samefile(Path(__file__).parent.parent / "SHACL" / "datafiles")

    @pytest.mark.parametrize("format", ["rdf", "ttl"])
    def test_got_some_files(self, format):
        files = SHACL.get_all_shacl_files(format=format)
        assert files  # not empty
        assert all([f.suffix == f".{format}" for f in files])  # All the expected format ...
        assert all([f.exists() for f in files])  # ... exist ...
        assert all([f.is_file() for f in files])  # ... and are actual files.

    def test_wrong_file_format(self):
        with pytest.raises(ValueError):
            SHACL.get_all_shacl_files(format="cheese")
