"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

MonthDay = Primitive(
    name="MonthDay",
    type=str,
    profiles=[
        Profile.EQ,
    ],
)

"""
MonthDay format as "--mm-dd", which conforms with XSD data type gMonthDay.
"""
