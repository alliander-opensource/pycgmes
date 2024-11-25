"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


VoltagePerReactivePower = CIMDatatype(
    name="VoltagePerReactivePower",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.VPerVAr,
    profiles=[
        Profile.EQ,
    ],
)

"""
Voltage variation with reactive power.
"""
