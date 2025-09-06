"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindUVRTQcontrolModeKind(str, Enum):
    """
    UVRT Q control modes MqUVRT.
    """

    mode0 = "mode0"  # Voltage-dependent reactive current injection (<i>M</i><i><sub>qUVRT</sub></i> <sub> </sub>equals 0).  # noqa: E501
    mode1 = "mode1"  # Reactive current injection controlled as the pre-fault value plus an additional voltage dependent reactive current injection (<i>M</i><i><sub>qUVRT</sub></i> equals 1).  # noqa: E501
    mode2 = "mode2"  # Reactive current injection controlled as the pre-fault value plus an additional voltage-dependent reactive current injection during fault, and as the pre-fault value plus an additional constant reactive current injection post fault (<i>M</i><i><sub>qUVRT</sub></i><sub>  </sub>equals 2).  # noqa: E501
