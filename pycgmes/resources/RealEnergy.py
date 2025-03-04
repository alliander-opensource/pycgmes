"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


RealEnergy = CIMDatatype(
    name="RealEnergy",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.Wh,
    profiles=[
        Profile.EQ,
        Profile.SSH,
    ],
)

"""
Real electrical energy.
"""
