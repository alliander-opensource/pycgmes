"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Seconds = CIMDatatype(
    name="Seconds",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.s,
    profiles=[
        Profile.DY,
        Profile.EQ,
    ],
)

"""
Time, in seconds.
"""
