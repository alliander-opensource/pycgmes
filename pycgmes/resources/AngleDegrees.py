"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


AngleDegrees = CIMDatatype(
    name="AngleDegrees",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.deg,
    profiles=[
        Profile.EQ,
        Profile.DL,
        Profile.DY,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
Measurement of angle in degrees.
"""
