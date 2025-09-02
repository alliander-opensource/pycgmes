"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


PerCent = CIMDatatype(
    name="PerCent",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.none,
    profiles=[
        Profile.EQ,
        Profile.OP,
        Profile.SC,
        Profile.SSH,
    ],
)

"""
Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.
"""
