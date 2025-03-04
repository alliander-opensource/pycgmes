"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Susceptance = CIMDatatype(
    name="Susceptance",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.S,
    profiles=[
        Profile.EQ,
        Profile.SC,
    ],
)

"""
Imaginary part of admittance.
"""
