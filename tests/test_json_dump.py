import json

from pycgmes.resources import Bay


class TestJsonification:
    def test_load_bay(self):
        b = Bay(mRID="42", description="Cheese", name="fromage", shortName="from")
        assert (
            json.dumps(b, default=Bay.json_encoder) == '{"serializationProfile": {}, "description": "Cheese", '
            '"energyIdentCodeEic": "", "mRID": "42", "name": "fromage", "shortName": "from", "VoltageLevel": null}'
        )
