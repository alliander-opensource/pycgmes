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
from pycgmes.utils.profile import BaseProfile, Profile
from pycgmes.utils.writer import Writer


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
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "namespace": "custom",
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
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    @classmethod
    def apparent_name(cls) -> str:
        return "Cheese"

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        return {CustomProfile.FRO}

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        return CustomProfile.FRO


class TestWriter:
    def test_is_class_matching_profile(self):
        assert Writer.is_class_matching_profile(CustomBayAttr(), CustomProfile.CUS)
        assert Writer.is_class_matching_profile(CustomBayAttr(), Profile.EQ)
        assert Writer.is_class_matching_profile(CustomBayClass(), CustomProfile.CUS)
        assert Writer.is_class_matching_profile(CustomBayClass(), Profile.EQ)
        assert Writer.is_class_matching_profile(CustomBase(), CustomProfile.FRO)
        assert not Writer.is_class_matching_profile(CustomBase(), Profile.EQ)

    def test_get_class_profile(self):
        assert Writer.get_class_profile(CustomBayAttr()) == CustomProfile.CUS
        assert Writer.get_class_profile(CustomBayClass()) == CustomProfile.CUS
        assert Writer.get_class_profile(CustomBase()) == CustomProfile.FRO

    def test_get_class_profile_map(self):
        class_profile_map = Writer.get_class_profile_map([CustomBayAttr(), CustomBayClass(), CustomBase()])
        expected = {"Bay": CustomProfile.CUS, "CustomBayClass": CustomProfile.CUS, "Cheese": CustomProfile.FRO}
        assert class_profile_map == expected

    def test_get_attribute_profile(self):
        custom_bay_attr = CustomBayAttr()
        class_profile = Writer.get_class_profile(custom_bay_attr)
        assert Writer.get_attribute_profile(custom_bay_attr, "colour", class_profile) == CustomProfile.CUS
        assert Writer.get_attribute_profile(custom_bay_attr, "name", class_profile) == Profile.EQ

        custom_bay_class = CustomBayClass()
        class_profile = Writer.get_class_profile(custom_bay_class)
        assert Writer.get_attribute_profile(custom_bay_class, "name", class_profile) == Profile.EQ

        custom_base = CustomBase()
        class_profile = Writer.get_class_profile(custom_base)
        assert Writer.get_attribute_profile(custom_base, "colour", class_profile) == CustomProfile.FRO

    def test_get_attribute_infos(self):
        infos = Writer.get_attribute_infos(CustomBayAttr(name="CBA", colour="Blue"))
        assert len(infos) == 7
        assert infos["colour"]["attr_name"] == "Bay.colour"
        assert infos["colour"]["value"] == "Blue"
        assert infos["name"]["attr_name"] == "IdentifiedObject.name"
        assert infos["name"]["value"] == "CBA"

    def test_generate_custom(self):
        writer = Writer(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = Writer.get_class_profile_map(writer.objects.values())
        xml = writer.generate(CustomProfile.CUS, "model" + "_" + CustomProfile.CUS.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_Tom">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://custom</md:Model.profile>
              </md:FullModel>
              <cim:Bay rdf:ID="CBA">
                <cim:Bay.colour>Blue</cim:Bay.colour>
              </cim:Bay>
              <cim:CustomBayClass rdf:ID="CBC">
              </cim:CustomBayClass>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_about(self):
        writer = Writer(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = Writer.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.EQ, "model" + "_" + Profile.EQ.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
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
            """
        )
        assert xml == expected

    def test_write(self, tmp_path):
        writer = Writer(
            {
                "CBA": CustomBayAttr(mRID="CBA", name="CBA", colour="Blue"),
                "CBC": CustomBayClass(mRID="CBC", name="CBC"),
                "CB": CustomBase(),
            }
        )
        class_profile_map = Writer.get_class_profile_map(writer.objects.values())
        profile_file_map = writer.write(str(tmp_path / "model"), "model", class_profile_map)
        assert len(profile_file_map) == 3
        assert profile_file_map[CustomProfile.CUS] == str(tmp_path / "model_Tom.xml")
        assert profile_file_map[CustomProfile.FRO] == str(tmp_path / "model_Mage.xml")
        assert profile_file_map[Profile.EQ] == str(tmp_path / "model_CoreEquipment.xml")

        xml = Path(profile_file_map[CustomProfile.FRO]).read_text()
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_Mage">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://fromage</md:Model.profile>
              </md:FullModel>
              <cim:Cheese rdf:ID="CB">
                <cim:Cheese.colour>Red</cim:Cheese.colour>
              </cim:Cheese>
            </rdf:RDF>
            """
        )
        assert xml == expected
