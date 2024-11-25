"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindUVRTQcontrolModeKind(str, Enum):
    """
    UVRT Q control modes <i>M</i><i><sub>qUVRT</sub></i><i>.</i>  # noqa: E501
    """

    mode0 = "mode0"  # Voltage-dependent reactive current injection (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qUVRT&lt;/sub&gt;&lt;/i&gt; &lt;sub&gt; &lt;/sub&gt;equals 0).  # noqa: E501
    mode1 = "mode1"  # Reactive current injection controlled as the pre-fault value plus an additional voltage dependent reactive current injection (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qUVRT&lt;/sub&gt;&lt;/i&gt; equals 1).  # noqa: E501
    mode2 = "mode2"  # Reactive current injection controlled as the pre-fault value plus an additional voltage-dependent reactive current injection during fault, and as the pre-fault value plus an additional constant reactive current injection post fault (&lt;i&gt;M&lt;/i&gt;&lt;i&gt;&lt;sub&gt;qUVRT&lt;/sub&gt;&lt;/i&gt;&lt;sub&gt;  &lt;/sub&gt;equals 2).  # noqa: E501
