"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class VsPpccControlKind(str, Enum):
    """
    Types applicable to the control of real power and/or DC voltage by voltage source converter.  # noqa: E501
    """

    pPcc = "pPcc"  # Control is real power at point of common coupling. The target value is provided by ACDCConverter.targetPpcc.  # noqa: E501
    udc = "udc"  # Control is DC voltage  with target value provided by ACDCConverter.targetUdc.  # noqa: E501
    pPccAndUdcDroop = "pPccAndUdcDroop"  # Control is active power at point of common coupling and local DC voltage, with the droop. Target values are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc and VsConverter.droop.  # noqa: E501
    pPccAndUdcDroopWithCompensation = "pPccAndUdcDroopWithCompensation"  # Control is active power at point of common coupling and compensated DC voltage, with the droop. Compensation factor is the resistance, as an approximation of the DC voltage of a common (real or virtual) node in the DC network. Targets are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc, VsConverter.droop and VsConverter.droopCompensation.  # noqa: E501
    pPccAndUdcDroopPilot = "pPccAndUdcDroopPilot"  # Control is active power at point of common coupling and the pilot DC voltage, with the droop. The mode is used for Multi Terminal High Voltage DC (MTDC) systems where multiple HVDC Substations are connected to the HVDC transmission lines. The pilot voltage is then used to coordinate the control the DC voltage across the HVDC substations. Targets are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc and  VsConverter.droop.  # noqa: E501
    phasePcc = "phasePcc"  # Control is phase at point of common coupling. Target is provided by VsConverter.targetPhasePcc.  # noqa: E501
