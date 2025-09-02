"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class DCConverterOperatingModeKind(str, Enum):
    """
    The operating mode of an HVDC bipole.
    """

    bipolar = "bipolar"  # Bipolar operation.  # noqa: E501, E741, RUF003
    monopolarMetallicReturn = "monopolarMetallicReturn"  # Monopolar operation with metallic return.  # noqa: E501, E741, RUF003
    monopolarGroundReturn = "monopolarGroundReturn"  # Monopolar operation with ground return.  # noqa: E501, E741, RUF003
