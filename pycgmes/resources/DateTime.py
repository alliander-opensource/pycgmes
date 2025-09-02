"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

DateTime = Primitive(
    name="DateTime",
    type=datetime,
    profiles=[
        Profile.EQ,
        Profile.GL,
        Profile.OP,
    ],
)

"""
Date and time as "yyyy-mm-ddThh:mm:ss.sss", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-
      ddThh:mm:ss.sssZ". A local timezone relative UTC is specified as "yyyy-mm-ddThh:mm:ss.sss-hh:mm". The second
      component (shown here as "ss.sss") could have any number of digits in its fractional part to allow any kind of
      precision beyond seconds.
"""
