"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Resistance = CIMDatatype(
    name="Resistance",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.ohm,
    profiles=[
        Profile.EQ,
        Profile.SC,
        Profile.SSH,
    ],
)

"""
Resistance (real part of impedance).
"""
