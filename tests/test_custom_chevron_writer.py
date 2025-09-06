# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

import textwrap
from functools import cached_property
from pathlib import Path

from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.base import Base
from pycgmes.utils.chevron_writer import ChevronWriter
from pycgmes.utils.profile import BaseProfile, Profile


class CustomProfile(BaseProfile):
    CUS = "Tom"
    FRO = "Mage"

    @cached_property
    def uris(self) -> list[str]:
        profile_uris = {"CUS": ["http://custom"], "FRO": ["http://fromage"]}  # NOSONAR
        return profile_uris[self.name]


@dataclass
class CustomBayAttr(Bay):
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.CUS,
            ],
            "is_used": True,
            "namespace": "custom",
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
    )

    @classmethod
    def apparent_name(cls) -> str:
        return "Bay"

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        return {CustomProfile.CUS}

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return CustomProfile.CUS


@dataclass
class CustomBayClass(Bay):
    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        return {CustomProfile.CUS}

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return CustomProfile.CUS


@dataclass
class CustomBase(Base):
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.FRO,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "String",
        },
        # No namespace defined, it will use the class namespace.
    )

    @classmethod
    def apparent_name(cls) -> str:
        return "Cheese"

    @cached_property
    def namespace(self) -> str:
        return "cheesy namespace"

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return CustomProfile.FRO


class TestChevronWriter:
    def test_is_class_matching_profile(self):
        assert ChevronWriter.is_class_matching_profile(CustomBayAttr(), CustomProfile.CUS)
        assert ChevronWriter.is_class_matching_profile(CustomBayAttr(), Profile.EQ)
        assert ChevronWriter.is_class_matching_profile(CustomBayClass(), CustomProfile.CUS)
        assert ChevronWriter.is_class_matching_profile(CustomBayClass(), Profile.EQ)
        assert ChevronWriter.is_class_matching_profile(CustomBase(), CustomProfile.FRO)
        assert not ChevronWriter.is_class_matching_profile(CustomBase(), Profile.EQ)

    def test_get_class_profile(self):
        assert ChevronWriter.get_class_profile(CustomBayAttr()) == CustomProfile.CUS
        assert ChevronWriter.get_class_profile(CustomBayClass()) == CustomProfile.CUS
        assert ChevronWriter.get_class_profile(CustomBase()) == CustomProfile.FRO

    def test_get_class_profile_map(self):
        class_profile_map = ChevronWriter.get_class_profile_map([CustomBayAttr(), CustomBayClass(), CustomBase()])
        expected = {"Bay": CustomProfile.CUS, "CustomBayClass": CustomProfile.CUS, "Cheese": CustomProfile.FRO}
        assert class_profile_map == expected

    def test_get_attribute_profile(self):
        custom_bay_attr = CustomBayAttr()
        class_profile = ChevronWriter.get_class_profile(custom_bay_attr)
        assert ChevronWriter.get_attribute_profile(custom_bay_attr, "colour", class_profile) == CustomProfile.CUS
        assert ChevronWriter.get_attribute_profile(custom_bay_attr, "name", class_profile) == Profile.EQ

        custom_bay_class = CustomBayClass()
        class_profile = ChevronWriter.get_class_profile(custom_bay_class)
        assert ChevronWriter.get_attribute_profile(custom_bay_class, "name", class_profile) == Profile.EQ

        custom_base = CustomBase()
        class_profile = ChevronWriter.get_class_profile(custom_base)
        assert ChevronWriter.get_attribute_profile(custom_base, "colour", class_profile) == CustomProfile.FRO

    def test_get_attribute_infos(self):
        infos = ChevronWriter.get_attribute_infos(CustomBayAttr(name="CBA", colour="Blue"))
        assert len(infos) == 7
        assert infos["colour"]["attr_name"] == "Bay.colour"
        assert infos["colour"]["value"] == "Blue"
        assert infos["name"]["attr_name"] == "IdentifiedObject.name"
        assert infos["name"]["value"] == "CBA"

    def test_generate_custom(self):
        writer = ChevronWriter(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(CustomProfile.CUS, "model" + "_" + CustomProfile.CUS.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:ns0="custom">
              <md:FullModel rdf:about="model_Tom">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://custom</md:Model.profile>
              </md:FullModel>
              <cim:Bay rdf:ID="CBA">
                <ns0:Bay.colour>Blue</ns0:Bay.colour>
              </cim:Bay>
              <cim:CustomBayClass rdf:ID="CBC">
              </cim:CustomBayClass>
            </rdf:RDF>
            """  # noqa: E501
        )
        assert xml == expected

    def test_generate_about(self):
        writer = ChevronWriter(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.EQ, "model" + "_" + Profile.EQ.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" xmlns:cim="http://iec.ch/TC57/CIM100#">
              <md:FullModel rdf:about="model_CoreEquipment">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:Bay rdf:about="#CBA">
                <cim:IdentifiedObject.name>CBA</cim:IdentifiedObject.name>
              </cim:Bay>
              <cim:CustomBayClass rdf:about="#CBC">
                <cim:IdentifiedObject.name>CBC</cim:IdentifiedObject.name>
              </cim:CustomBayClass>
            </rdf:RDF>
            """  # noqa: E501
        )
        assert xml == expected

    def test_write(self, tmp_path):
        writer = ChevronWriter(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        profile_file_map = writer.write(str(tmp_path / "model"), "model", class_profile_map)
        assert len(profile_file_map) == 3
        assert profile_file_map[CustomProfile.CUS] == str(tmp_path / "model_Tom.xml")
        assert profile_file_map[CustomProfile.FRO] == str(tmp_path / "model_Mage.xml")
        assert profile_file_map[Profile.EQ] == str(tmp_path / "model_CoreEquipment.xml")

        xml = Path(profile_file_map[CustomProfile.FRO]).read_text()
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#" xmlns:ns0="cheesy namespace">
              <md:FullModel rdf:about="model_Mage">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://fromage</md:Model.profile>
              </md:FullModel>
              <ns0:Cheese rdf:ID="CB">
                <ns0:Cheese.colour>Red</ns0:Cheese.colour>
              </ns0:Cheese>
            </rdf:RDF>
            """  # noqa: E501
        )
        assert xml == expected
