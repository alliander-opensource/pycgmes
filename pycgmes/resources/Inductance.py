"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from ..utils.datatypes import CIMDatatype
from ..utils.profile import Profile
from .UnitMultiplier import UnitMultiplier
from .UnitSymbol import UnitSymbol


Inductance = CIMDatatype(
    name="Inductance",
    type=float,
    multiplier=UnitMultiplier.none,
    unit=UnitSymbol.H,
    profiles=[
        Profile.EQ,
    ],
)

"""
Inductive part of reactance (imaginary part of impedance), at rated frequency.
"""
