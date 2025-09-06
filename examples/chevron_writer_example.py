# SPDX-FileCopyrightText: 2024 Thomas Guenther <tom@toms-cafe.de>
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from pycgmes.resources.Analog import Analog
from pycgmes.resources.AnalogValue import AnalogValue
from pycgmes.resources.BaseVoltage import BaseVoltage
from pycgmes.resources.Terminal import Terminal
from pycgmes.resources.TopologicalIsland import TopologicalIsland
from pycgmes.resources.TopologicalNode import TopologicalNode
from pycgmes.resources.VoltageLevel import VoltageLevel
from pycgmes.utils.base import Base
from pycgmes.utils.chevron_writer import ChevronWriter
from pycgmes.utils.profile import Profile

_curr_dir = Path(__file__).resolve().parent


def main() -> None:
    output_dir = _curr_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    objects = {
        "BaseVoltage.20": BaseVoltage(mRID="BaseVoltage.20", nominalVoltage=20.0),
        "VoltageLevel.98": VoltageLevel(mRID="VoltageLevel.98", name="98", BaseVoltage="BaseVoltage.20"),
        "VoltageLevel.99": VoltageLevel(mRID="VoltageLevel.99", name="99", BaseVoltage="BaseVoltage.20"),
        "N0": TopologicalNode(mRID="N0", name="N0", ConnectivityNodeContainer="VoltageLevel.98"),
        "N1": TopologicalNode(mRID="N1", name="N1", ConnectivityNodeContainer="VoltageLevel.99"),
        "N": TopologicalIsland(mRID="N", name="N", TopologicalNodes=["N0", "N1"]),
        "Terminal.N0": Terminal(mRID="Terminal.N0", name="Terminal at N0", TopologicalNode="N0", connected=True),
        "Analog.N0.Voltage": Analog(
            mRID="Analog.N0.Voltage",
            name="Voltage Magnitude Measurement at N0",
            shortName="N0",
            Terminal="Terminal.N0",
            measurementType="Voltage",
            unitMultiplier="UnitMultiplier.k",
            unitSymbol="UnitSymbol.V",
        ),
        "AnalogValue.N0.Voltage": AnalogValue(mRID="AnalogValue.N0.Voltage", Analog="Analog.N0.Voltage"),
    }
    write(output_dir / "Example_Model", "Example_Model", objects)


def write(outputfile: Path, model_id: str, objects: dict[str, Base]) -> None:
    writer = ChevronWriter(objects)
    class_profile_map = ChevronWriter.get_class_profile_map(writer.objects.values())
    class_profile_map["Terminal"] = Profile.TP  # override recommended profile
    profile_file_map = writer.write(str(outputfile), model_id, class_profile_map)
    for idx, (profile, file) in enumerate(profile_file_map.items()):
        print(f"CIM outputfile {idx + 1} for {profile}: {file}")


if __name__ == "__main__":
    main()
