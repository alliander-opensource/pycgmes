<!--
SPDX-FileCopyrightText: 2023 Alliander

SPDX-License-Identifier: Apache-2.0
-->

# PyCGMES

<<<<<<< HEAD
- [PyCGMES](#pycgmes)
  - [About CGMES](#about-cgmes)
  - [Library usage](#library-usage)
  - [Custom attributes](#custom-attributes)
    - [Add to an existing profile](#add-to-an-existing-profile)
    - [Create a new profile](#create-a-new-profile)
    - [Implementation details](#implementation-details)
      - [Apparent class](#apparent-class)
      - [Namespace](#namespace)
        - [Class/Resource Namespace](#classresource-namespace)
        - [Attribute namespace](#attribute-namespace)
  - [Content of this repository](#content-of-this-repository)
    - [Schemas v3](#schemas-v3)
    - [SHACL files](#shacl-files)
    - [V3 source zip](#v3-source-zip)
    - [Dataclasses](#dataclasses)
  - [Library build, CI, CD...](#library-build-ci-cd)
    - [CI](#ci)
    - [CD](#cd)
  - [License](#license)
>>>>>>> 4384d02 (update docs with CGMES info)

Python dataclasses for CGMES 3 + RDF schema description + SHACL (validation) files.

## About CGMES

The Common Grid Model Exchange Specification, or CGMES, is provided by ENTSO-E (the European Network of TSOs for
Electricity) to facilitate the exchange of grid data between parties. It is based on CIM, the Common Information Model
for electric utilities, provided by the IEC (see also
[CIM on Wikipedia](https://en.wikipedia.org/wiki/Common_Information_Model_(electricity))).

CIM defines the vocabulary for electricity grids, meaning the names we use for different components and the way they
relate to each other. CGMES takes a subset of this vocabulary and provides RDF schema and SHACL validation files.

Further reading and all relevant CGMES (source) files are found on
[the CGMES page of the ENTSO-E website](https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/).

## Library usage

From Pypi.org, 2 packages are available (both from this repository):

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

##### Class/Resource Namespace

The default class (or resource) namespace is `http://iec.ch/TC57/CIM100#`.

You can override it when you create a custom resource by just redefining the property `namespace`:

##### Attribute namespace

In the serialisation, the namespace of all attributes is `http://iec.ch/TC57/CIM100#` by default.

The namespace of an attribute is the first value found:

- namespace defined in the Field (see `colour` below - it would be `custom`)
- namespace of the class (see `size` below - it would be `custom ns class`)
- namespace of the first parent defining one. The top parent (`Base`) defined  `cim`.

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

    size: str = Field(
        default="Big",
        in_profiles=[
            Profile.EQ, # Do not do this, see chapter "create a new profile"
        ],
    )

    @property
    def namesapce(self) -> str:
        return "custom ns class"

    @classmethod
    def apparent_name(cls):
        return "ACLineSegment"
```

It will be given when `cgmes_attributes_in_profile()` is called.

## Content of this repository

### Schemas v3

[schemas](./schemas) are rdf definitions of CGMES. They are used once, to generate dataclasses, and
can then happily be forgotten.

They are available on the [ENTSO-E site](https://www.entsoe.eu/data/cim/cim-conformity-and-interoperability/).
Look for CGMES Conformity Assessment Scheme v3
then [Application Profiles v3.0.1](https://www.entsoe.eu/Documents/CIM_documents/Grid_Model_CIM/IEC61970-600-2_CGMES_3_0_1_ApplicationProfiles.zip)

Older versions could be found on the [ENTSO-E site](https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/).

### SHACL files

[Shapes Constraint Language](https://en.wikipedia.org/wiki/SHACL) is used for validation of the actual content of the
CGMES files, not just XML validation. They can be found in [shacl](./pycgmes/shacl). This is the new validation
standard. OCL
is referenced, specially with older versions, but ENTSO-E is moving away from it.

To use them, there is another package `pycmges-shacl`, built from this repo as well.

### V3 source zip

From ENTSO-E, in [data](./data). This is one small-ish zip file, containing a bit more than just the SHACL and RDFS
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
