"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from datetime import date, datetime, time
from ..utils.datatypes import Primitive
from ..utils.profile import Profile

Decimal = Primitive(
    name="Decimal",
    type=float,
    profiles=[
        Profile.EQ,
    ],
)

"""
Decimal is the base-10 notational system for representing real numbers.
"""
