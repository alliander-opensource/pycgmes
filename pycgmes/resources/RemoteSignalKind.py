"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class RemoteSignalKind(str, Enum):
    """
    Type of input signal coming from remote bus.
    """

    remoteBusVoltageFrequency = "remoteBusVoltageFrequency"  # Input is voltage frequency from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusVoltageFrequencyDeviation = "remoteBusVoltageFrequencyDeviation"  # Input is voltage frequency deviation from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusFrequency = "remoteBusFrequency"  # Input is frequency from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusFrequencyDeviation = "remoteBusFrequencyDeviation"  # Input is frequency deviation from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusVoltageAmplitude = "remoteBusVoltageAmplitude"  # Input is voltage amplitude from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusVoltage = "remoteBusVoltage"  # Input is voltage from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBranchCurrentAmplitude = "remoteBranchCurrentAmplitude"  # Input is branch current amplitude from remote terminal bus.  # noqa: E501, E741, RUF003
    remoteBusVoltageAmplitudeDerivative = "remoteBusVoltageAmplitudeDerivative"  # Input is branch current amplitude derivative from remote terminal bus.  # noqa: E501, E741, RUF003
    remotePuBusVoltageDerivative = "remotePuBusVoltageDerivative"  # Input is PU voltage derivative from remote terminal bus.  # noqa: E501, E741, RUF003
