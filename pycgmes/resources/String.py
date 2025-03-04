"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

String = Primitive(
    name="String",
    type=str,
    profiles=[
        Profile.DL,
        Profile.DY,
        Profile.EQ,
        Profile.EQBD,
        Profile.GL,
        Profile.OP,
        Profile.SC,
        Profile.SSH,
        Profile.SV,
        Profile.TP,
    ],
)

"""
A string consisting of a sequence of characters. The character encoding is UTF-8. The string length is unspecified
      and unlimited.
"""
