"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcST7BUELselectorKind(str, Enum):
    """
    Types of connections for the UEL input used for static excitation systems type 7B.
    """

    noUELinput = "noUELinput"  # No UEL input is used.  Corresponds to &lt;i&gt;UELin&lt;/i&gt; not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this &lt;i&gt;UELin&lt;/i&gt; = 0.  # noqa: E501
    addVref = "addVref"  # The signal is added to &lt;i&gt;Vref&lt;/i&gt;. Corresponds to &lt;i&gt;UELin&lt;/i&gt; = 1 on the ExcST7B diagram.  # noqa: E501
    inputHVgate = "inputHVgate"  # The signal is connected into the input &lt;i&gt;HVGate&lt;/i&gt;.  Corresponds to &lt;i&gt;UELin&lt;/i&gt; = 2 on the ExcST7B diagram.  # noqa: E501
    outputHVgate = "outputHVgate"  # The signal is connected into the output &lt;i&gt;HVGate&lt;/i&gt;.  Corresponds to &lt;i&gt;UELin&lt;/i&gt; = 3 on the ExcST7B diagram.  # noqa: E501
