"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class PetersenCoilModeKind(str, Enum):
    """
    The mode of operation for a Petersen coil.
    """

    fixed = "fixed"  # Fixed position.  # noqa: E501, E741, RUF003
    manual = "manual"  # Manual positioning.  # noqa: E501, E741, RUF003
    automaticPositioning = "automaticPositioning"  # Automatic positioning.  # noqa: E501, E741, RUF003
