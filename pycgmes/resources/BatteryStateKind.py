"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class BatteryStateKind(str, Enum):
    """
    The state of the battery unit.
    """

    discharging = "discharging"  # Stored energy is decreasing.  # noqa: E501
    full = "full"  # Unable to charge, and not discharging.  # noqa: E501
    waiting = "waiting"  # Neither charging nor discharging, but able to do so.  # noqa: E501
    charging = "charging"  # Stored energy is increasing.  # noqa: E501
    empty = "empty"  # Unable to discharge, and not charging.  # noqa: E501
