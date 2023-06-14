import json

from pycgmes.resources import Base, VoltageLevel


class TestJsonification:
    def test_round_robin_json_class_json(self):
        # Validates that the given parameters (start) is in the dict of final class,
        # ignoring the other defaults params.
        start = json.loads('{"__class__":"VoltageLevel", "lowVoltageLimit":32.0}')
        complete = Base.parse_json_as(start).to_dict()

        assert start.items() <= complete.items()

    def test_round_robin_class_json_class(self):
        vl = VoltageLevel(lowVoltageLimit=32.0)
        after_rr = Base.parse_json_as(vl.to_dict())

        assert vl == after_rr
