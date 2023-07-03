This directory contains the SHACL files, and a specific pyproject.toml, only meant to build a second distribution package.
The CI & co happen in the main poetry/github files.

To build pycgmes-shacl with `poetry build`, you **need to** be in the SHACL directory. Using `-C` will not work
because of some relative paths.
