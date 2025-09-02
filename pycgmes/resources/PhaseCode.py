"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class PhaseCode(str, Enum):
    """
    An unordered enumeration of phase identifiers.  Allows designation of phases for both transmission and distribution
      equipment, circuits and loads.   The enumeration, by itself, does not describe how the phases are connected
      together or connected to ground.  Ground is not explicitly denoted as a phase. Residential and small
      commercial loads are often served from single-phase, or split-phase, secondary circuits. For the example of
      s12N, phases 1 and 2 refer to hot wires that are 180 degrees out of phase, while N refers to the neutral wire.
      Through single-phase transformer connections, these secondary circuits may be served from one or two of the
      primary phases A, B, and C. For three-phase loads, use the A, B, C phase codes instead of s12N. The integer
      values are from IEC 61968-9 to support revenue metering applications.
    """

    ABCN = "ABCN"  # Phases A, B, C, and N.  # noqa: E501, E741, RUF003
    ABC = "ABC"  # Phases A, B, and C.  # noqa: E501, E741, RUF003
    ABN = "ABN"  # Phases A, B, and neutral.  # noqa: E501, E741, RUF003
    ACN = "ACN"  # Phases A, C and neutral.  # noqa: E501, E741, RUF003
    BCN = "BCN"  # Phases B, C, and neutral.  # noqa: E501, E741, RUF003
    AB = "AB"  # Phases A and B.  # noqa: E501, E741, RUF003
    AC = "AC"  # Phases A and C.  # noqa: E501, E741, RUF003
    BC = "BC"  # Phases B and C.  # noqa: E501, E741, RUF003
    AN = "AN"  # Phases A and neutral.  # noqa: E501, E741, RUF003
    BN = "BN"  # Phases B and neutral.  # noqa: E501, E741, RUF003
    CN = "CN"  # Phases C and neutral.  # noqa: E501, E741, RUF003
    A = "A"  # Phase A.  # noqa: E501, E741, RUF003
    B = "B"  # Phase B.  # noqa: E501, E741, RUF003
    C = "C"  # Phase C.  # noqa: E501, E741, RUF003
    N = "N"  # Neutral phase.  # noqa: E501, E741, RUF003
    s1N = "s1N"  # Secondary phase 1 and neutral.  # noqa: E501, E741, RUF003
    s2N = "s2N"  # Secondary phase 2 and neutral.  # noqa: E501, E741, RUF003
    s12N = "s12N"  # Secondary phases 1, 2, and neutral.  # noqa: E501, E741, RUF003
    s1 = "s1"  # Secondary phase 1.  # noqa: E501, E741, RUF003
    s2 = "s2"  # Secondary phase 2.  # noqa: E501, E741, RUF003
    s12 = "s12"  # Secondary phase 1 and 2.  # noqa: E501, E741, RUF003
    none = "none"  # No phases specified.  # noqa: E501, E741, RUF003
    X = "X"  # Unknown non-neutral phase.  # noqa: E501, E741, RUF003
    XY = "XY"  # Two unknown non-neutral phases.  # noqa: E501, E741, RUF003
    XN = "XN"  # Unknown non-neutral phase plus neutral.  # noqa: E501, E741, RUF003
    XYN = "XYN"  # Two unknown non-neutral phases plus neutral.  # noqa: E501, E741, RUF003
