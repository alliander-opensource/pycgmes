"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


VolumeFlowRate = CIMDatatype(
    name="VolumeFlowRate",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.m3Pers,
    profiles=[
        Profile.DY,
    ],
)

"""
Volume per time.
"""
