"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class GeneratorControlSource(str, Enum):
    """
    The source of controls for a generating unit.
    """

    unavailable = "unavailable"  # Not available.  # noqa: E501, E741, RUF003
    offAGC = "offAGC"  # Off of automatic generation control (AGC).  # noqa: E501, E741, RUF003
    onAGC = "onAGC"  # On automatic generation control (AGC).  # noqa: E501, E741, RUF003
    plantControl = "plantControl"  # Plant is controlling.  # noqa: E501, E741, RUF003
