"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Voltage = CIMDatatype(
    name="Voltage",
    type=float,
    multiplier=UnitMultiplier.k,
    unit=UnitSymbol.V,
    profiles=[
        Profile.EQ,
        Profile.EQBD,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
Electrical voltage, can be both AC and DC.
"""
