"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindQcontrolModeKind(str, Enum):
    """
    General wind turbine Q control modes <i>M</i><i><sub>qG</sub></i><i>.</i>  # noqa: E501
    """

    voltage = "voltage"  # Voltage control (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qG&lt;/sub&gt;&lt;/i&gt; equals 0).  # noqa: E501
    reactivePower = "reactivePower"  # Reactive power control (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qG&lt;/sub&gt;&lt;/i&gt; equals 1).  # noqa: E501
    openLoopReactivePower = "openLoopReactivePower"  # Open loop reactive power control (only used with closed loop at plant level) (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qG&lt;/sub&gt;&lt;/i&gt;&lt;sub&gt; &lt;/sub&gt;equals 2).  # noqa: E501
    powerFactor = "powerFactor"  # Power factor control (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qG&lt;/sub&gt;&lt;/i&gt;&lt;sub&gt; &lt;/sub&gt;equals 3).  # noqa: E501
    openLooppowerFactor = "openLooppowerFactor"  # Open loop power factor control (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qG&lt;/sub&gt;&lt;/i&gt;&lt;sub&gt; &lt;/sub&gt;equals 4).  # noqa: E501
