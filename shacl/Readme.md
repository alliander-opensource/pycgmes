# Why this directory

It contains the SHACL build files, only meant to build a second distribution package.
The CI & co happen in the main poetry/github files.

The main `pycgmes` package does not have the SHACL files.

# Actual Shacl files

They are in the [main tree](../pycgmes/shacl/).

# Build

To be able to build multiple pacakges based om the same source, things need to be a bit different, because:

- poetry does not allow another name for `pyproject.toml`
- you cannot by default include files outside the directory of the `pyproject.toml`

This is neatly worked around via a plugin, written by one of the maintainer of poetry, so it feels safe enough.

```bash
poetry self add poetry-multiproject-plugin
poetry build-project --with-top-namespace pycgmes
```

Note that to build pycgmes-shacl, you **need to** be in the shacl directory. Using `-C` will not work
because of some relative paths.
