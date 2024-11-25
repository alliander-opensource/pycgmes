"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


ActivePowerPerCurrentFlow = CIMDatatype(
    name="ActivePowerPerCurrentFlow",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.WPerA,
    profiles=[
        Profile.EQ,
    ],
)

"""
Active power variation with current flow.
"""
