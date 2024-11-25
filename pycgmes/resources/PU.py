"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


PU = CIMDatatype(
    name="PU",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.none,
    profiles=[
        Profile.DY,
        Profile.SC,
        Profile.SSH,
    ],
)

"""
Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.
"""
