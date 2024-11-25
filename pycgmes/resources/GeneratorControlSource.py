"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class GeneratorControlSource(str, Enum):
    """
    The source of controls for a generating unit.  # noqa: E501
    """

    unavailable = "unavailable"  # Not available.  # noqa: E501
    offAGC = "offAGC"  # Off of automatic generation control (AGC).  # noqa: E501
    onAGC = "onAGC"  # On automatic generation control (AGC).  # noqa: E501
    plantControl = "plantControl"  # Plant is controlling.  # noqa: E501
