"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


RotationSpeed = CIMDatatype(
    name="RotationSpeed",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.Hz,
    profiles=[
        Profile.EQ,
    ],
)

"""
Number of revolutions per second.
"""
