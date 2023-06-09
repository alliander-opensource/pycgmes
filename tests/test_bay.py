import textwrap

from pycgmes.resources import (
    Base,
    Bay,
    ConnectivityNodeContainer,
    EquipmentContainer,
    IdentifiedObject,
    PowerSystemResource,
)


class TestBay:
    def test_load_bay(self):
        b = Bay()

    def test_bay_has_mrid(self):
        b = Bay()
        assert getattr(b, "mRID") is not None

    def test_bay_has_expected_parents(self):
        parents = Bay.__mro__[0:6]  # after that there's object.
        expected = (  # mro returns a tuple
            Bay,
            EquipmentContainer,
            ConnectivityNodeContainer,
            PowerSystemResource,
            IdentifiedObject,
            Base,
        )
        assert expected == parents

    def test_bay_has_expected_str(self):
        expected = textwrap.dedent(
            """
        class=Bay
        serializationProfile={}
        description=
        energyIdentCodeEic=
        mRID=
        name=
        shortName=
        VoltageLevel=None
        """
        )[
            1:-1
        ]  # The first and last characters are newlines, which are not in str()
        assert str(Bay()) == expected

    def test_bay_has_expected_profiles(self):
        profiles = Base().profiles
        expected = {
            "class": [
                profiles.EQBD.value,
                profiles.EQ.value,
            ],
            "VoltageLevel": [
                profiles.EQBD.value,
                profiles.EQ.value,
            ],
        }
        assert expected == Bay().possible_profiles
