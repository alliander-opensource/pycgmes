"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

Float = Primitive(
    name="Float",
    type=float,
    profiles=[
        Profile.EQ,
        Profile.DL,
        Profile.DY,
        Profile.EQBD,
        Profile.OP,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
A floating point number. The range is unspecified and not limited.
"""
