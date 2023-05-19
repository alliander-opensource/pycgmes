# cgmes-python

- [cgmes-python](#cgmes-python)
  - [Content](#content)
    - [Schemas v3](#schemas-v3)
    - [Shacl files](#shacl-files)
    - [V3 source](#v3-source)
    - [Dataclasses](#dataclasses)

Python dataclasses for CGMES 3 + rdf schema description + SHACL files

## Content

### Schemas v3

[schemas](./schemas/) are rdf definitions of CGMES. They are used once, to generate dataclasses, and
can then happily be forgotten.

They have been given by Entsoe, via the data office.

Older versions could be found on the [Entsoe site](https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/).

### Shacl files

[Shapes constraint Language](https://en.wikipedia.org/wiki/SHACL) is used for validation of the actual content of the
CGMES files, not just XML validation. They can be found in [SHACL](./SHACL/). This is the new validation standard. OCL
is referenced, specially with older versions, but Entsoe is moving away from it.

### V3 source

From Entsoe, in [data](./data/). This is one small-ish zip file, containing a bit more than just the shacl and rdfs
files (those extracted and emtioned above) but is usually not needed.

### Dataclasses

Generated from our [fork](https://github.com/Alliander/uno-cimgen/) of [cimgen](https://github.com/sogno-platform/cimgen), with as goal to push back our changes upstream.

The main differences between our version and upstream are:

- handle CGMES v3
- generate dataclasses instead of classes
- typing
- more comments
- independent of [cimpy](https://github.com/sogno-platform/cimpy)
