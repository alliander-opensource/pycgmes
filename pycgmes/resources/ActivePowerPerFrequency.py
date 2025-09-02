"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


ActivePowerPerFrequency = CIMDatatype(
    name="ActivePowerPerFrequency",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.WPers,
    profiles=[
        Profile.EQ,
    ],
)

"""
Active power variation with frequency.
"""
