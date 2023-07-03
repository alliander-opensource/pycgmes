from pathlib import Path


def get_shacl_file_dir() -> Path:
    return Path(__file__).parent / "datafiles"


def get_all_shacl_files(format="rdf") -> list[Path]:
    if format.lower() not in ["rdf", "ttl"]:
        raise ValueError(
            "Parameter 'format' of function 'get_all_shacl_files' must be one of "
            f"'rdf' or 'ttl'. Got '{format}' instead."
        )
    return list(get_shacl_file_dir().glob(f"**/*.{format.lower()}"))
