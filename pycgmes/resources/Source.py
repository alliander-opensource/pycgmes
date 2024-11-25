"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class Source(str, Enum):
    """
    Source gives information related to the origin of a value.  # noqa: E501
    """

    PROCESS = "PROCESS"  # The value is provided by input from the process I/O or being calculated from some function.  # noqa: E501
    DEFAULTED = "DEFAULTED"  # The value contains a default value.  # noqa: E501
    SUBSTITUTED = "SUBSTITUTED"  # The value is provided by input of an operator or by an automatic source.  # noqa: E501
