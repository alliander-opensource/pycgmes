"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum
from functools import cached_property


class BaseProfile(str, Enum):
    """
    Profile parent. Use it if you need your own profiles.

    All pycgmes objects requiring a Profile are actually asking for a `BaseProfile`. As
    Enum with fields cannot be inherited or composed, just create your own CustomProfile without
    trying to extend Profile. It will work.
    """

    @cached_property
    def long_name(self) -> str:
        """Return the long name of the profile."""
        return self.value

    @cached_property
    def uris(self) -> list[str]:
        """Return the list of uris of the profile."""
        raise NotImplementedError("Method has to be implemented in subclass.")

    def __lt__(self, other):
        """Provide a strict ordering of the enum values of this class and of all subclasses.

        The enum values within a class are not sorted alphabetically, but in the order in which they were defined.
        Enum values from different classes should not be mixed up. All values of one class come first, then all values
        of the other class, whereby the order of the classes is alphabetical.
        """
        if not isinstance(other, self.__class__):
            return str(self.__class__) < str(other.__class__)
        order = list(self.__class__)
        return order.index(self) < order.index(other)

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


class Profile(BaseProfile):
    """
    Enum containing all CGMES profiles and their export priority.
    """

    EQ = "CoreEquipment"
    DL = "DiagramLayout"
    DY = "Dynamics"
    EQBD = "EquipmentBoundary"
    GL = "GeographicalLocation"
    OP = "Operation"
    SC = "ShortCircuit"
    SSH = "SteadyStateHypothesis"
    SV = "StateVariables"
    TP = "Topology"

    @cached_property
    def uris(self) -> list[str]:
        """Return the list of uris of the profile."""
        return profile_uris[self.name]


profile_uris: dict[str, list[str]] = {  # Those are strings, not real addresses, hence the NOSONAR.
    "EQ": [
        "http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0",  # NOSONAR
    ],
    "DL": [
        "http://iec.ch/TC57/ns/CIM/DiagramLayout-EU/3.0",  # NOSONAR
    ],
    "DY": [
        "http://iec.ch/TC57/ns/CIM/Dynamics-EU/1.0",  # NOSONAR
    ],
    "EQBD": [
        "http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU/3.0",  # NOSONAR
    ],
    "GL": [
        "http://iec.ch/TC57/ns/CIM/GeographicalLocation-EU/3.0",  # NOSONAR
    ],
    "OP": [
        "http://iec.ch/TC57/ns/CIM/Operation-EU/3.0",  # NOSONAR
    ],
    "SC": [
        "http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0",  # NOSONAR
    ],
    "SSH": [
        "http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU/3.0",  # NOSONAR
    ],
    "SV": [
        "http://iec.ch/TC57/ns/CIM/StateVariables-EU/3.0",  # NOSONAR
    ],
    "TP": [
        "http://iec.ch/TC57/ns/CIM/Topology-EU/3.0",  # NOSONAR
    ],
}
