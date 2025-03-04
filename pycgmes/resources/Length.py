"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Length = CIMDatatype(
    name="Length",
    type=float,
    multiplier=UnitMultiplier.k,
    unit=UnitSymbol.m,
    profiles=[
        Profile.DY,
        Profile.EQ,
        Profile.SC,
    ],
)

"""
Unit of length. It shall be a positive value or zero.
"""
