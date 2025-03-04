"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier


Money = CIMDatatype(
    name="Money",
    type=float,
    multiplier=UnitMultiplier.none,
    profiles=[
        Profile.EQ,
    ],
)

"""
Amount of money.
"""
