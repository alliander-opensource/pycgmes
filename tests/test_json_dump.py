import json

from pycgmes.resources import Base, VoltageLevel


class TestJsonification:
    def test_round_robin_json_class_json(self):
        start = json.loads('{"__class__":"VoltageLevel", "lowVoltageLimit":32.0}')
        complete = Base.parse_json_as(start).to_dict()

        # Validates that the given parameters (start) is in the dict of final class,
        # ignoring the other defaults params.
        # items() is actuallly a set view, and sets can be compared with <=. This line
        # thus means: make sure that start is a subset of complete.
        assert start.items() <= complete.items()

    def test_round_robin_class_json_class(self):
        vl = VoltageLevel(lowVoltageLimit=32.0)
        after_rr = Base.parse_json_as(vl.to_dict())

        assert vl == after_rr
