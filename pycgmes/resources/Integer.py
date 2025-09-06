"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

Integer = Primitive(
    name="Integer",
    type=int,
    profiles=[
        Profile.EQ,
        Profile.DL,
        Profile.DY,
        Profile.GL,
        Profile.OP,
        Profile.SC,
        Profile.SSH,
    ],
)

"""
An integer number. The range is unspecified and not limited.
"""
