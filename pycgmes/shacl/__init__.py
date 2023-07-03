from pathlib import Path


def get_shacl_file_dir() -> Path:
    """
    Returns the directory where all shacls files are to be found.
    """
    return Path(__file__).parent / "datafiles"


def get_all_shacl_files(serialization="rdf") -> list[Path]:
    """
    Returns a list of all shacl files for one serialization format.
    """
    if serialization.lower() not in ["rdf", "ttl"]:
        raise ValueError(
            "Parameter 'serialization' of function 'get_all_shacl_files' must be one of "
            f"'rdf' or 'ttl'. Got '{serialization}' instead."
        )
    return list(get_shacl_file_dir().glob(f"**/*.{serialization.lower()}"))
