"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class StaticLoadModelKind(str, Enum):
    """
    Type of static load model.  # noqa: E501
    """

    exponential = "exponential"  # This model is an exponential representation of the load. Exponential equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kpf, ep1, ep2, ep3 kq1, kq2, kq3, kqf, eq1, eq2, eq3.  # noqa: E501
    zIP1 = "zIP1"  # This model integrates the frequency-dependent load (primarily motors).  ZIP1 equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kpf kq1, kq2, kq3, kqf.  # noqa: E501
    zIP2 = "zIP2"  # This model separates the frequency-dependent load (primarily motors) from other load.  ZIP2 equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kq4, kpf kq1, kq2, kq3, kq4, kqf.  # noqa: E501
    constantZ = "constantZ"  # The load is represented as a constant impedance.  ConstantZ equations are used  for active and reactive power and no attributes are required.  # noqa: E501
