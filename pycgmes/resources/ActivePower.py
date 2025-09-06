"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


ActivePower = CIMDatatype(
    name="ActivePower",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.W,
    profiles=[
        Profile.EQ,
        Profile.DY,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
Product of RMS value of the voltage and the RMS value of the in-phase component of the current.
"""
