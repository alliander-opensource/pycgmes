"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class PetersenCoilModeKind(str, Enum):
    """
    The mode of operation for a Petersen coil.  # noqa: E501
    """

    fixed = "fixed"  # Fixed position.  # noqa: E501
    manual = "manual"  # Manual positioning.  # noqa: E501
    automaticPositioning = "automaticPositioning"  # Automatic positioning.  # noqa: E501
