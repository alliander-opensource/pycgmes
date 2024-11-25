"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcST7BOELselectorKind(str, Enum):
    """
    Types of connections for the OEL input used for static excitation systems type 7B.  # noqa: E501
    """

    noOELinput = "noOELinput"  # No OEL input is used. Corresponds to &lt;i&gt;OELin&lt;/i&gt; not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this &lt;i&gt;OELin&lt;/i&gt; = 0.  # noqa: E501
    addVref = "addVref"  # The signal is added to &lt;i&gt;Vref&lt;/i&gt;.  Corresponds to &lt;i&gt;OELin&lt;/i&gt; = 1 on the ExcST7B diagram.  # noqa: E501
    inputLVgate = "inputLVgate"  # The signal is connected into the input &lt;i&gt;LVGate&lt;/i&gt;. Corresponds to &lt;i&gt;OELin&lt;/i&gt; = 2 on the ExcST7B diagram.  # noqa: E501
    outputLVgate = "outputLVgate"  # The signal is connected into the output &lt;i&gt;LVGate&lt;/i&gt;.  Corresponds to &lt;i&gt;OELin&lt;/i&gt; = 3 on the ExcST7B diagram.  # noqa: E501
