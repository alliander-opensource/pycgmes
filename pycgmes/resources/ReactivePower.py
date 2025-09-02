"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


ReactivePower = CIMDatatype(
    name="ReactivePower",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.VAr,
    profiles=[
        Profile.EQ,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
Product of RMS value of the voltage and the RMS value of the quadrature component of the current.
"""
