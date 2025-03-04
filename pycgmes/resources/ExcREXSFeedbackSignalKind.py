"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcREXSFeedbackSignalKind(str, Enum):
    """
    Types of rate feedback signals.
    """

    fieldVoltage = "fieldVoltage"  # The voltage regulator output voltage is used. It is the same as exciter field voltage.  # noqa: E501, E741, RUF003
    fieldCurrent = "fieldCurrent"  # The exciter field current is used.  # noqa: E501, E741, RUF003
    outputVoltage = "outputVoltage"  # The output voltage of the exciter is used.  # noqa: E501, E741, RUF003
