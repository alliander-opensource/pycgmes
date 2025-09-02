"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Conductance = CIMDatatype(
    name="Conductance",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.S,
    profiles=[
        Profile.EQ,
        Profile.SC,
    ],
)

"""
Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
"""
