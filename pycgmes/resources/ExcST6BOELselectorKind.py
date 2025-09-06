"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcST6BOELselectorKind(str, Enum):
    """
    Types of connections for the OEL input used for static excitation systems type 6B.
    """

    noOELinput = "noOELinput"  # No OEL input is used. Corresponds to &lt;i&gt;OELin&lt;/i&gt; not = 1 and not = 2 on the ExcST6B diagram. Original ExcST6B model would have called this &lt;i&gt;OELin&lt;/i&gt; = 0.  # noqa: E501
    beforeUEL = "beforeUEL"  # The connection is before UEL. Corresponds to &lt;i&gt;OELin&lt;/i&gt; = 1 on the ExcST6B diagram.  # noqa: E501
    afterUEL = "afterUEL"  # The connection is after UEL. Corresponds to &lt;i&gt;OELin&lt;/i&gt; = 2 on the ExcST6B diagram.  # noqa: E501
