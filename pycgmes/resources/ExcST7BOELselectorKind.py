"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class ExcST7BOELselectorKind(str, Enum):
    """
    Types of connections for the OEL input used for static excitation systems type 7B.
    """

    noOELinput = "noOELinput"  # No OEL input is used. Corresponds to <i>OELin</i> not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this <i>OELin</i> = 0.  # noqa: E501
    addVref = "addVref"  # The signal is added to <i>Vref</i>.  Corresponds to <i>OELin</i> = 1 on the ExcST7B diagram.  # noqa: E501
    inputLVgate = "inputLVgate"  # The signal is connected into the input <i>LVGate</i>. Corresponds to <i>OELin</i> = 2 on the ExcST7B diagram.  # noqa: E501
    outputLVgate = "outputLVgate"  # The signal is connected into the output <i>LVGate</i>.  Corresponds to <i>OELin</i> = 3 on the ExcST7B diagram.  # noqa: E501
