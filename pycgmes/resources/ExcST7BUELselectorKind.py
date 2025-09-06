"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcST7BUELselectorKind(str, Enum):
    """
    Types of connections for the UEL input used for static excitation systems type 7B.
    """

    noUELinput = "noUELinput"  # No UEL input is used.  Corresponds to <i>UELin</i> not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this <i>UELin</i> = 0.  # noqa: E501
    addVref = "addVref"  # The signal is added to <i>Vref</i>. Corresponds to <i>UELin</i> = 1 on the ExcST7B diagram.  # noqa: E501
    inputHVgate = "inputHVgate"  # The signal is connected into the input <i>HVGate</i>.  Corresponds to <i>UELin</i> = 2 on the ExcST7B diagram.  # noqa: E501
    outputHVgate = "outputHVgate"  # The signal is connected into the output <i>HVGate</i>.  Corresponds to <i>UELin</i> = 3 on the ExcST7B diagram.  # noqa: E501
