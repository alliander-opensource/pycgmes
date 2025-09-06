"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

Date = Primitive(
    name="Date",
    type=date,
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
        Profile.TP,
    ],
)

"""
Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ". A local timezone
      relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".
"""
