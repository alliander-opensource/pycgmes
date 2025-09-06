"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


ApparentPower = CIMDatatype(
    name="ApparentPower",
    type=float,
    multiplier=UnitMultiplier.M,
    unit=UnitSymbol.VA,
    profiles=[
        Profile.EQ,
        Profile.DY,
        Profile.SSH,
    ],
)

"""
Product of the RMS value of the voltage and the RMS value of the current.
"""
