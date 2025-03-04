# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

import textwrap
from pathlib import Path

from pycgmes.resources.Analog import Analog
from pycgmes.resources.AnalogValue import AnalogValue
from pycgmes.resources.BaseVoltage import BaseVoltage
from pycgmes.resources.Location import Location
from pycgmes.resources.Season import Season
from pycgmes.resources.Status import Status
from pycgmes.resources.StreetAddress import StreetAddress
from pycgmes.resources.StreetDetail import StreetDetail
from pycgmes.resources.Terminal import Terminal
from pycgmes.resources.TopologicalIsland import TopologicalIsland
from pycgmes.resources.TopologicalNode import TopologicalNode
from pycgmes.resources.TownDetail import TownDetail
from pycgmes.resources.VoltageLevel import VoltageLevel
from pycgmes.utils.chevron_writer import ChevronWriter
from pycgmes.utils.profile import Profile


class TestChevronWriter:
    def test_is_class_matching_profile(self):
        assert ChevronWriter.is_class_matching_profile(TopologicalNode(), Profile.TP)
        assert ChevronWriter.is_class_matching_profile(TopologicalNode(), Profile.SV)
        assert ChevronWriter.is_class_matching_profile(TopologicalNode(), Profile.EQ)

    def test_get_class_profile(self):
        assert ChevronWriter.get_class_profile(BaseVoltage()) == Profile.EQ
        assert ChevronWriter.get_class_profile(TopologicalNode()) == Profile.TP
        assert ChevronWriter.get_class_profile(TopologicalIsland()) == Profile.SV

    def test_get_class_profile_map(self):
        class_profile_map = ChevronWriter.get_class_profile_map([BaseVoltage(), TopologicalNode(), BaseVoltage()])
        expected = {"BaseVoltage": Profile.EQ, "TopologicalNode": Profile.TP}
        assert class_profile_map == expected

    def test_get_attribute_profile(self):
        base_voltage = BaseVoltage()
        class_profile = ChevronWriter.get_class_profile(base_voltage)
        assert ChevronWriter.get_attribute_profile(base_voltage, "nominalVoltage", class_profile) == Profile.EQ
        assert ChevronWriter.get_attribute_profile(base_voltage, "name", class_profile) == Profile.EQ
        assert ChevronWriter.get_attribute_profile(base_voltage, "shortName", class_profile) == Profile.EQ
        assert ChevronWriter.get_attribute_profile(base_voltage, "description", class_profile) == Profile.EQ

        topological_node = TopologicalNode()
        class_profile = ChevronWriter.get_class_profile(topological_node)
        assert ChevronWriter.get_attribute_profile(topological_node, "BaseVoltage", class_profile) == Profile.TP
        assert ChevronWriter.get_attribute_profile(topological_node, "name", class_profile) == Profile.TP
        assert ChevronWriter.get_attribute_profile(topological_node, "shortName", class_profile) == Profile.TP
        assert ChevronWriter.get_attribute_profile(topological_node, "description", class_profile) == Profile.TP

        topological_island = TopologicalIsland()
        class_profile = ChevronWriter.get_class_profile(topological_island)
        assert ChevronWriter.get_attribute_profile(topological_island, "TopologicalNodes", class_profile) == Profile.SV
        assert ChevronWriter.get_attribute_profile(topological_island, "name", class_profile) == Profile.SV
        assert ChevronWriter.get_attribute_profile(topological_island, "shortName", class_profile) == Profile.EQ
        assert ChevronWriter.get_attribute_profile(topological_island, "description", class_profile) == Profile.EQ

    def test_get_attribute_infos(self):
        infos = ChevronWriter.get_attribute_infos(BaseVoltage(name="20", nominalVoltage=20.0))
        assert len(infos) == 6
        assert infos["nominalVoltage"]["attr_name"] == "BaseVoltage.nominalVoltage"
        assert infos["nominalVoltage"]["value"] == 20.0
        assert infos["name"]["attr_name"] == "IdentifiedObject.name"
        assert infos["name"]["value"] == "20"

    def test_generate_primitive(self):
        writer = ChevronWriter(
            {
                "BaseVoltage.20": BaseVoltage(mRID="BaseVoltage.20", nominalVoltage=20.0),
                "VoltageLevel.98": VoltageLevel(mRID="VoltageLevel.98", name="98", BaseVoltage="BaseVoltage.20"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.EQ, "model" + "_" + Profile.EQ.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_CoreEquipment">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:BaseVoltage rdf:ID="BaseVoltage.20">
                <cim:BaseVoltage.nominalVoltage>20.0</cim:BaseVoltage.nominalVoltage>
              </cim:BaseVoltage>
              <cim:VoltageLevel rdf:ID="VoltageLevel.98">
                <cim:IdentifiedObject.name>98</cim:IdentifiedObject.name>
                <cim:VoltageLevel.BaseVoltage rdf:resource="#BaseVoltage.20" />
              </cim:VoltageLevel>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_enum(self):
        writer = ChevronWriter(
            {
                "Analog.N0": Analog(mRID="Analog.N0", unitMultiplier="UnitMultiplier.k", unitSymbol="UnitSymbol.V"),
                "AnalogValue.N0": AnalogValue(mRID="AnalogValue.N0", Analog="Analog.N0.Voltage"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.OP, "model" + "_" + Profile.OP.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_Operation">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/Operation-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:Analog rdf:ID="Analog.N0">
                <cim:Measurement.unitMultiplier rdf:resource="http://iec.ch/TC57/CIM100#UnitMultiplier.k" />
                <cim:Measurement.unitSymbol rdf:resource="http://iec.ch/TC57/CIM100#UnitSymbol.V" />
                <cim:Analog.positiveFlowIn>false</cim:Analog.positiveFlowIn>
              </cim:Analog>
              <cim:AnalogValue rdf:ID="AnalogValue.N0">
                <cim:AnalogValue.Analog rdf:resource="#Analog.N0.Voltage" />
              </cim:AnalogValue>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_class_list(self):
        writer = ChevronWriter(
            {
                "N0": TopologicalNode(mRID="N0", name="N0"),
                "N1": TopologicalNode(mRID="N1", name="N1"),
                "TopologicalIsland.N": TopologicalIsland(mRID="N", name="N", TopologicalNodes=["N0", "N1"]),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.SV, "model" + "_" + Profile.SV.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_StateVariables">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/StateVariables-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:TopologicalIsland rdf:ID="TopologicalIsland.N">
                <cim:IdentifiedObject.name>N</cim:IdentifiedObject.name>
                <cim:TopologicalIsland.TopologicalNodes rdf:resource="#N0" />
                <cim:TopologicalIsland.TopologicalNodes rdf:resource="#N1" />
              </cim:TopologicalIsland>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_about(self):
        writer = ChevronWriter(
            {
                "N0": TopologicalNode(mRID="N0"),
                "Terminal.N0": Terminal(mRID="Terminal.N0", TopologicalNode="N0"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.TP, "model" + "_" + Profile.TP.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_Topology">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/Topology-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:TopologicalNode rdf:ID="N0">
              </cim:TopologicalNode>
              <cim:Terminal rdf:about="#Terminal.N0">
                <cim:Terminal.TopologicalNode rdf:resource="#N0" />
              </cim:Terminal>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_write(self, tmp_path):
        writer = ChevronWriter(
            {
                "Analog.N0.Voltage": Analog(
                    mRID="Analog.N0.Voltage",
                    name="Voltage Magnitude Measurement at N0",
                    shortName="N0",
                    measurementType="Voltage",
                    unitMultiplier="UnitMultiplier.k",
                    unitSymbol="UnitSymbol.V",
                ),
                "AnalogValue.N0.Voltage": AnalogValue(mRID="AnalogValue.N0.Voltage", Analog="Analog.N0.Voltage"),
                "BaseVoltage.20": BaseVoltage(mRID="BaseVoltage.20", nominalVoltage=20.0),
                "VoltageLevel.98": VoltageLevel(mRID="VoltageLevel.98", name="98", BaseVoltage="BaseVoltage.20"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        profile_file_map = writer.write(str(tmp_path / "model"), "model", class_profile_map)
        assert len(profile_file_map) == 2
        assert profile_file_map[Profile.EQ] == str(tmp_path / "model_CoreEquipment.xml")
        assert profile_file_map[Profile.OP] == str(tmp_path / "model_Operation.xml")

        xml = Path(profile_file_map[Profile.EQ]).read_text()
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_CoreEquipment">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:BaseVoltage rdf:ID="BaseVoltage.20">
                <cim:BaseVoltage.nominalVoltage>20.0</cim:BaseVoltage.nominalVoltage>
              </cim:BaseVoltage>
              <cim:VoltageLevel rdf:ID="VoltageLevel.98">
                <cim:IdentifiedObject.name>98</cim:IdentifiedObject.name>
                <cim:VoltageLevel.BaseVoltage rdf:resource="#BaseVoltage.20" />
              </cim:VoltageLevel>
              <cim:Analog rdf:about="#Analog.N0.Voltage">
                <cim:IdentifiedObject.shortName>N0</cim:IdentifiedObject.shortName>
              </cim:Analog>
            </rdf:RDF>
            """
        )
        assert xml == expected

        xml = Path(profile_file_map[Profile.OP]).read_text()
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_Operation">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/Operation-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:Analog rdf:ID="Analog.N0.Voltage">
                <cim:IdentifiedObject.name>Voltage Magnitude Measurement at N0</cim:IdentifiedObject.name>
                <cim:Measurement.measurementType>Voltage</cim:Measurement.measurementType>
                <cim:Measurement.unitMultiplier rdf:resource="http://iec.ch/TC57/CIM100#UnitMultiplier.k" />
                <cim:Measurement.unitSymbol rdf:resource="http://iec.ch/TC57/CIM100#UnitSymbol.V" />
                <cim:Analog.positiveFlowIn>false</cim:Analog.positiveFlowIn>
              </cim:Analog>
              <cim:AnalogValue rdf:ID="AnalogValue.N0.Voltage">
                <cim:AnalogValue.Analog rdf:resource="#Analog.N0.Voltage" />
              </cim:AnalogValue>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_location(self):
        writer = ChevronWriter(
            {
                "_Location": Location(mRID="_Location", mainAddress="_Address"),
                "_Address": StreetAddress(status="_Status", streetDetail="_Street", townDetail="_Town"),
                "_Status": Status(dateTime="2024-10-13 19:17:22 +0200", value="verified"),
                "_Street": StreetDetail(name="Ku'damm", number="33", withinTownLimits=True),
                "_Town": TownDetail(name="Berlin", country="Germany"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.GL, "model" + "_" + Profile.GL.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_GeographicalLocation">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/GeographicalLocation-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:Location rdf:ID="_Location">
                <cim:Location.mainAddress rdf:resource="#_Address" />
              </cim:Location>
              <cim:StreetAddress rdf:ID="_Address">
                <cim:StreetAddress.status rdf:resource="#_Status" />
                <cim:StreetAddress.streetDetail rdf:resource="#_Street" />
                <cim:StreetAddress.townDetail rdf:resource="#_Town" />
              </cim:StreetAddress>
              <cim:Status rdf:ID="_Status">
                <cim:Status.dateTime>2024-10-13 19:17:22 +0200</cim:Status.dateTime>
                <cim:Status.value>verified</cim:Status.value>
              </cim:Status>
              <cim:StreetDetail rdf:ID="_Street">
                <cim:StreetDetail.name>Ku'damm</cim:StreetDetail.name>
                <cim:StreetDetail.number>33</cim:StreetDetail.number>
                <cim:StreetDetail.withinTownLimits>true</cim:StreetDetail.withinTownLimits>
              </cim:StreetDetail>
              <cim:TownDetail rdf:ID="_Town">
                <cim:TownDetail.country>Germany</cim:TownDetail.country>
                <cim:TownDetail.name>Berlin</cim:TownDetail.name>
              </cim:TownDetail>
            </rdf:RDF>
            """
        )
        assert xml == expected

    def test_generate_season(self):
        writer = ChevronWriter(
            {
                "_Season": Season(mRID="_Season", startDate="--10-13", endDate="--10-31"),
            }
        )
        class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
        xml = writer.generate(Profile.EQ, "model" + "_" + Profile.EQ.long_name, class_profile_map)
        expected = textwrap.dedent(
            """\
            <?xml version="1.0" encoding="utf-8" ?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#">
              <md:FullModel rdf:about="model_CoreEquipment">
                <md:Model.modelingAuthoritySet>www.sogno.energy</md:Model.modelingAuthoritySet>
                <md:Model.profile>http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0</md:Model.profile>
              </md:FullModel>
              <cim:Season rdf:ID="_Season">
                <cim:Season.endDate>--10-31</cim:Season.endDate>
                <cim:Season.startDate>--10-13</cim:Season.startDate>
              </cim:Season>
            </rdf:RDF>
            """
        )
        assert xml == expected
