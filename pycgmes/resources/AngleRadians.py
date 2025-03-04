"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


AngleRadians = CIMDatatype(
    name="AngleRadians",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.rad,
    profiles=[
        Profile.SSH,
    ],
)

"""
Phase angle in radians.
"""
