"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class InputSignalKind(str, Enum):
    """
    Types of input signals.  In dynamics modelling, commonly represented by the j parameter.
    """

    rotorSpeed = "rotorSpeed"  # Input signal is rotor or shaft speed (angular frequency).  # noqa: E501, E741, RUF003
    rotorAngularFrequencyDeviation = "rotorAngularFrequencyDeviation"  # Input signal is rotor or shaft angular frequency deviation.  # noqa: E501, E741, RUF003
    busFrequency = "busFrequency"  # Input signal is bus voltage fr&lt;font color=&quot;#0f0f0f&quot;&gt;equency.  This could be a terminal frequency or remote frequency.&lt;/font&gt;  # noqa: E501, E741, RUF003
    busFrequencyDeviation = "busFrequencyDeviation"  # Input signal is deviation of bus voltage frequ&lt;font color=&quot;#0f0f0f&quot;&gt;ency.  This could be a terminal frequency deviation or remote frequency deviation.&lt;/font&gt;  # noqa: E501, E741, RUF003
    generatorElectricalPower = "generatorElectricalPower"  # Input signal is generator electrical power on rated &lt;i&gt;S&lt;/i&gt;.  # noqa: E501, E741, RUF003
    generatorAcceleratingPower = "generatorAcceleratingPower"  # Input signal is generator accelerating power.  # noqa: E501, E741, RUF003
    busVoltage = "busVoltage"  # Input signal &lt;font color=&quot;#0f0f0f&quot;&gt;is bus voltage.  This could be a terminal voltage or remote voltage.&lt;/font&gt;  # noqa: E501, E741, RUF003
    busVoltageDerivative = "busVoltageDerivative"  # Input signal is derivative of bus voltag&lt;font color=&quot;#0f0f0f&quot;&gt;e.  This could be a terminal voltage derivative or remote voltage derivative.&lt;/font&gt;  # noqa: E501, E741, RUF003
    branchCurrent = "branchCurrent"  # Input signal is amplitude of remote branch current.  # noqa: E501, E741, RUF003
    fieldCurrent = "fieldCurrent"  # Input signal is generator field current.  # noqa: E501, E741, RUF003
    generatorMechanicalPower = "generatorMechanicalPower"  # Input signal is generator mechanical power.  # noqa: E501, E741, RUF003
