<!--
SPDX-FileCopyrightText: 2023 Alliander

SPDX-License-Identifier: Apache-2.0
-->

# cgmes-python

- [cgmes-python](#cgmes-python)
  - [Library usage](#library-usage)
  - [Custom attributes](#custom-attributes)
    - [Add to an existing profile](#add-to-an-existing-profile)
    - [Create a new profile](#create-a-new-profile)
    - [Implementation details](#implementation-details)
      - [Apparent class](#apparent-class)
      - [Namespace](#namespace)
  - [Content of this repository](#content-of-this-repository)
    - [Schemas v3](#schemas-v3)
    - [Shacl files](#shacl-files)
    - [V3 source zip](#v3-source-zip)
    - [Dataclasses](#dataclasses)
  - [Library build, CI, CD...](#library-build-ci-cd)
    - [CI](#ci)
    - [CD](#cd)
  - [License](#license)

Python dataclasses for CGMES 3 + rdf schema description + SHACL files.

## Library usage

From Pypi.org, 2 packages are available:

- [https://pypi.org/project/pycgmes/](https://pypi.org/project/pycgmes/)
- [https://pypi.org/project/pycgmes-shacl/](https://pypi.org/project/pycgmes-shacl/)

They can easily be installed via pip: `pip install pycgmes` or `pip install pycgmes-shacl`.

## Custom attributes

You might want to add extra attributes. For instance, the color of a cable (ACLineSegment). This is possible in 2 ways:

- Adding the attribute to a custom class in an existing profile.
- Define a new profile including a custom class where the attribute is defined.

You can look at the [examples](./examples/custom_attributes.py)

### Add to an existing profile

If you need to add your own attributes (example: cable colour), you can do that by subclassing the relevant class, and
add one or more new atributes there.

If this is a leaf node (for instance `ACLineSegment`), it "just works". If you want to add an extra attribute to a
class higher in the hierarchy (for instance `Equipment`) there is a lot more work to do.

```python
@dataclass(config=DataclassConfig)
class CustomBay(Bay):
    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ,
        ],
    )
```

### Create a new profile

This approach is cleaner and more standard compliant: the official CGMES profiles stay untouched, while a new additional profile contains your customisations.

You can do this by extending the `BaseProfile`` Enum in [profile.py](./pycgmes/utils/profile.py).

While in Python it is not possible to extend or compose Enums which already have fields, you can create your own:

```python
from pycgmes.utils.profile import BaseProfile

class CustomProfile(BaseProfile):
    CUS="Tom"
    FRO="Mage"
```

And use it everywhere you would use a profile:

```python
from pycgmes.utils.dataclassconfig import DataclassConfig

@dataclass(config=DataclassConfig)
class CustomBayAttr(Bay):
    colour: str = Field(
        default="Red",
        in_profiles=[
            CustomProfile.CUS,
        ],
    )

# And for instance:
custom_attrs = CustomBayAttr(colour="purple").cgmes_attributes_in_profile(CustomProfile.CUS)
```

### Implementation details

#### Apparent class

By default, an attribute is fully qualified. A standard `attribute` in `ACLineSegment` will appear as `ACLineSegment.attribute` in the serialisation.
In the case of a custom attribute defined via a sub class, the result would be: `ACLineSegmentCustom.customAttribute`. To preserve the original class name (i.e. serialise your attribute as `ACLineSegment.customAttribute`), you need to override the `apparent_name` of your custom class:

```python
from pydantic.dataclasses import dataclass

from pycgmes.resources.ACLineSegment import ACLineSegment
from pycgmes.utils.dataclassconfig import DataclassConfig

@dataclass(config=DataclassConfig)
class ACLineSegmentCustom(ACLineSegment):
    @classmethod
    def apparent_name(cls):
        return "ACLineSegment"
```

#### Namespace

In the serialisation, the namespace of all attributes is `cim` (`"http://iec.ch/TC57/2013/CIM-schema-cim16#"`) by default.
The serialisation is not done by PyCGMES (yet), but if you want a custom namespace for an attribute,
you can give a hint to the serialiser by adding some metadata to your custom attributes:

```python
from pydantic.dataclasses import dataclass
from pydantic import Field

from pycgmes.resources import ACLineSegment
from pycgmes.resources.Base import DataclassConfig, Profile

@dataclass(config=DataclassConfig)
class ACLineSegmentCustom(ACLineSegment):

    colour: str = Field(
        default="Red",
        in_profiles=[
            Profile.EQ, # Do not do this, see chapter "create a new profile"
        ],
        namespace="custom",
    )

    @classmethod
    def apparent_name(cls):
        return "ACLineSegment"
```

It will be given when `cgmes_attributes_in_profile()` is called.

## Content of this repository

### Schemas v3

[schemas](./schemas/) are rdf definitions of CGMES. They are used once, to generate dataclasses, and
can then happily be forgotten.

They are available on the [ENTSO-E site](https://www.entsoe.eu/data/cim/cim-conformity-and-interoperability/).
Look for CGMES Conformity Assessment Scheme v3 then [Application Profiles v3.0.1](https://www.entsoe.eu/Documents/CIM_documents/Grid_Model_CIM/IEC61970-600-2_CGMES_3_0_1_ApplicationProfiles.zip)

Older versions could be found on the [ENTSO-E site](https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/).

### Shacl files

[Shapes constraint Language](https://en.wikipedia.org/wiki/SHACL) is used for validation of the actual content of the
CGMES files, not just XML validation. They can be found in [shacl](./pycgmes/shacl). This is the new validation standard. OCL
is referenced, specially with older versions, but Entsoe is moving away from it.

To use them, there is another package `pycmges-shacl`, built from this repo as well.

### V3 source zip

From Entsoe, in [data](./data/). This is one small-ish zip file, containing a bit more than just the shacl and rdfs
files (those extracted and mentioned above) but is usually not needed.

### Dataclasses

Generated from the modernpython serialisation of [cimgen](https://github.com/sogno-platform/cimgen).

## Library build, CI, CD...

### CI

The CI happens in GitHub actions.

The standard black/mypy/autoflake/isort/pylint/ruff/mypy are run there, via scons.

### CD

Deployment happens to pypi.org, via the standard poetry commands `poetry build`, `poetry publish`.

## License

This project is licensed under the Apache 2.0 license - see [LICENSE](./LICENSE) for details.
