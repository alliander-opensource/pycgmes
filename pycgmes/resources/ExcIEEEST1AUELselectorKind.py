"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcIEEEST1AUELselectorKind(str, Enum):
    """
    Types of connections for the UEL input used in ExcIEEEST1A.  # noqa: E501
    """

    ignoreUELsignal = "ignoreUELsignal"  # Ignore UEL signal.  # noqa: E501
    inputHVgateVoltageOutput = "inputHVgateVoltageOutput"  # UEL input HV gate with voltage regulator output.  # noqa: E501
    inputHVgateErrorSignal = "inputHVgateErrorSignal"  # UEL input HV gate with error signal.  # noqa: E501
    inputAddedToErrorSignal = "inputAddedToErrorSignal"  # UEL input added to error signal.  # noqa: E501
