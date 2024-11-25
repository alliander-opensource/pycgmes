"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class OrientationKind(str, Enum):
    """
    The orientation of the coordinate system with respect to top, left, and the coordinate number system.  # noqa: E501
    """

    positive = "positive"  # For 2D diagrams, a positive orientation will result in X values increasing from left to right and Y values increasing from bottom to top.  This is also known as a right hand orientation.  # noqa: E501
    negative = "negative"  # For 2D diagrams, a negative orientation gives the left-hand orientation (favoured by computer graphics displays) with X values increasing from left to right and Y values increasing from top to bottom.   This is also known as a left hand orientation.  # noqa: E501
