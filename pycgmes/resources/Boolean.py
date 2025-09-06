"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

Boolean = Primitive(
    name="Boolean",
    type=bool,
    profiles=[
        Profile.EQ,
        Profile.DL,
        Profile.DY,
        Profile.EQBD,
        Profile.GL,
        Profile.OP,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
    ],
)

"""
A type with the value space "true" and "false".
"""
