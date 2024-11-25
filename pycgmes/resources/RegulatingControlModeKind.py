"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class RegulatingControlModeKind(str, Enum):
    """
    The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.  # noqa: E501
    """

    voltage = "voltage"  # Voltage is specified.  # noqa: E501
    activePower = "activePower"  # Active power is specified.  # noqa: E501
    reactivePower = "reactivePower"  # Reactive power is specified.  # noqa: E501
    currentFlow = "currentFlow"  # Current flow is specified.  # noqa: E501
    admittance = "admittance"  # Admittance is specified.  # noqa: E501
    timeScheduled = "timeScheduled"  # Control switches on/off by time of day. The times may change on the weekend, or in different seasons.  # noqa: E501
    temperature = "temperature"  # Control switches on/off based on the local temperature (i.e., a thermostat).  # noqa: E501
    powerFactor = "powerFactor"  # Power factor is specified.  # noqa: E501
