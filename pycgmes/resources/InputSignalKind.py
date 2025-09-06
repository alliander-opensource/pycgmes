"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class InputSignalKind(str, Enum):
    """
    Types of input signals.  In dynamics modelling, commonly represented by the j parameter.
    """

    rotorSpeed = "rotorSpeed"  # Input signal is rotor or shaft speed (angular frequency).  # noqa: E501
    rotorAngularFrequencyDeviation = "rotorAngularFrequencyDeviation"  # Input signal is rotor or shaft angular frequency deviation.  # noqa: E501
    busFrequency = "busFrequency"  # Input signal is bus voltage fr<font color="#0f0f0f">equency.  This could be a terminal frequency or remote frequency.</font>  # noqa: E501
    busFrequencyDeviation = "busFrequencyDeviation"  # Input signal is deviation of bus voltage frequ<font color="#0f0f0f">ency.  This could be a terminal frequency deviation or remote frequency deviation.</font>  # noqa: E501
    generatorElectricalPower = "generatorElectricalPower"  # Input signal is generator electrical power on rated <i>S</i>.  # noqa: E501
    generatorAcceleratingPower = "generatorAcceleratingPower"  # Input signal is generator accelerating power.  # noqa: E501
    busVoltage = "busVoltage"  # Input signal <font color="#0f0f0f">is bus voltage.  This could be a terminal voltage or remote voltage.</font>  # noqa: E501
    busVoltageDerivative = "busVoltageDerivative"  # Input signal is derivative of bus voltag<font color="#0f0f0f">e.  This could be a terminal voltage derivative or remote voltage derivative.</font>  # noqa: E501
    branchCurrent = "branchCurrent"  # Input signal is amplitude of remote branch current.  # noqa: E501
    fieldCurrent = "fieldCurrent"  # Input signal is generator field current.  # noqa: E501
    generatorMechanicalPower = "generatorMechanicalPower"  # Input signal is generator mechanical power.  # noqa: E501
