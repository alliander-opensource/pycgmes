"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Area = CIMDatatype(
    name="Area",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.m2,
    profiles=[
        Profile.DY,
    ],
)

"""
Area.
"""
