# cgmes-python

- [cgmes-python](#cgmes-python)
  - [Library usage](#library-usage)
  - [Custom attributes](#custom-attributes)
    - [Apparent class](#apparent-class)
    - [Namespace](#namespace)
  - [Content](#content)
    - [Schemas v3](#schemas-v3)
    - [Shacl files](#shacl-files)
    - [V3 source zip](#v3-source-zip)
    - [Dataclasses](#dataclasses)
  - [Library build, CI, CD...](#library-build-ci-cd)
    - [CI](#ci)
    - [CD](#cd)
  - [TODOs](#todos)

Python dataclasses for CGMES 3 + rdf schema description + SHACL files

## Library usage

From the internal Alliander nexus repo, 2 packages are available:

- https://nexus.appx.cloud/#browse/browse:uno-pypi:pycgmes
- https://nexus.appx.cloud/#browse/browse:uno-pypi:pycgmes-shacl

They can be installed by pip once `https://nexus.appx.cloud/repository/uno-pypi/simple` is added as pip extra url or Poetry dependency.

## Custom attributes

### Apparent class

If you need to add your own attributes (example: cable colour), you can do that by subclassing the relevant class.

If this is a leaf node (for instance `ACLineSegment`), it "just works". If you want to add an extr attribute to a
class higher in the hierarchy (for instance `Equipment`) there is a lot more work to do.

By default, an attribute is fully qualified. `bch` in `ACLineSegment` will appear as `ACLineSegment.bch` in the serialisation.
For a custom attribute, you might not want to see  `ACLineSegmentCustom.bch`. To prevent this, you can override the `apparent_name`
of your custom class:

```python
from pydantic.dataclasses import dataclass

from pycgmes.resources.Base import Base, DataclassConfig, Profile

@dataclass(config=DataclassConfig)
class ACLineSegmentCustom(ACLineSegment)
    @classmethod
    def apparent_name(self):
        return "ACLineSegment"
```

### Namespace

In the serialisation, the namespace of all attributes is `cim` (`"http://iec.ch/TC57/2013/CIM-schema-cim16#"`) by default.
The serialisation is not done by PyCGMES (yet), but if you want a custom namespace for an attribute,
you can give a hint to the serialiser by adding some metadata to your custom attributes:

```python
from pydantic.dataclasses import dataclass
from pydantic import Field

from pycgmes.resources.Base import Base, DataclassConfig, Profile

@dataclass(config=DataclassConfig)
class ACLineSegmentCustom(ACLineSegment)

    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(self):
        return "ACLineSegment"
```

It will be given when `cgmes_attributes_in_profile()` is called.

## Content

### Schemas v3

[schemas](./schemas/) are rdf definitions of CGMES. They are used once, to generate dataclasses, and
can then happily be forgotten.

They have been given by Entsoe, via the data office.

Older versions could be found on the [Entsoe site](https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/).

### Shacl files

[Shapes constraint Language](https://en.wikipedia.org/wiki/SHACL) is used for validation of the actual content of the
CGMES files, not just XML validation. They can be found in [shacl](./pycgmes/shacl). This is the new validation standard. OCL
is referenced, specially with older versions, but Entsoe is moving away from it.

To use them, there is another package `pycmges-shacl`, built from this repo as well.

### V3 source zip

From Entsoe, in [data](./data/). This is one small-ish zip file, containing a bit more than just the shacl and rdfs
files (those extracted and mentioned above) but is usually not needed.

### Dataclasses

Generated from our [fork](https://github.com/Alliander/uno-cimgen/) of [cimgen](https://github.com/sogno-platform/cimgen), with as goal to push back our changes upstream.

The main differences between our version and upstream are:

- handle CGMES v3
- generate dataclasses instead of classes
- typing
- more comments
- independent of [cimpy](https://github.com/sogno-platform/cimpy)

## Library build, CI, CD...

### CI

The CI happens in GitHub actions.

The standard black/mypy/autoflake/isort/pylint/ruff/mypy are run there, via scons.

### CD

Deployment happens to the internal [Alliander Nexus](https://nexus.appx.cloud/#browse/browse:uno-pypi:pycgmes) for now, via the standard poetry commands `poetry build`, `poetry publish`.

This is managed by Team Uno, which has the nexus credentials in their own keeper and as action secrets in GitHub.

## TODOs

- open source it?
- build the library with different versions possible, to eventually use it with eg. `pip install pycgmes["3.0.0"]` for CGMES version 3 or `pip install pycgmes["2.4.5"]` for another version.
- buid cimexport in ?
- Sort out proper versioning. Currently pypi will prevent reupload, but maybe we can be smarter than that, inclusive github artifacts & co.