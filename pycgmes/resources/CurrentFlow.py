"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


CurrentFlow = CIMDatatype(
    name="CurrentFlow",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.A,
    profiles=[
        Profile.EQ,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity
      node. Can be both AC and DC.
"""
