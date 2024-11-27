"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class DCPolarityKind(str, Enum):
    """
    Polarity for DC circuits.
    """

    positive = "positive"  # Positive pole. The converter terminal is intended to operate at a positive voltage relative the midpoint or negative terminal.  # noqa: E501, E741, RUF003
    middle = "middle"  # Middle pole. The converter terminal is the midpoint in a bipolar or symmetric monopole configuration. The midpoint can be grounded and/or have a metallic return.  # noqa: E501, E741, RUF003
    negative = "negative"  # Negative pole. The converter terminal is intended to operate at a negative voltage relative the midpoint or positive terminal.  # noqa: E501, E741, RUF003
