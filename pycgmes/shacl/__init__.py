from pathlib import Path


def get_shacl_file_dir() -> Path:
    return Path(__file__).parent / "datafiles"


def get_all_shacl_files(serialization="rdf") -> list[Path]:
    if serialization.lower() not in ["rdf", "ttl"]:
        raise ValueError(
            "Parameter 'format' of function 'get_all_shacl_files' must be one of "
            f"'rdf' or 'ttl'. Got '{serialization}' instead."
        )
    return list(get_shacl_file_dir().glob(f"**/*.{serialization.lower()}"))
