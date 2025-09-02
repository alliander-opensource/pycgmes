"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindingConnection(str, Enum):
    """
    Winding connection type.
    """

    D = "D"  # Delta.  # noqa: E501, E741, RUF003
    Y = "Y"  # Wye.  # noqa: E501, E741, RUF003
    Z = "Z"  # ZigZag.  # noqa: E501, E741, RUF003
    Yn = "Yn"  # Wye, with neutral brought out for grounding.  # noqa: E501, E741, RUF003
    Zn = "Zn"  # ZigZag, with neutral brought out for grounding.  # noqa: E501, E741, RUF003
    A = "A"  # Autotransformer common winding.  # noqa: E501, E741, RUF003
    I = "I"  # Independent winding, for single-phase connections.  # noqa: E501, E741, RUF003
