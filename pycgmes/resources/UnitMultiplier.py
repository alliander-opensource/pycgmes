"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class UnitMultiplier(str, Enum):
    """
    The unit multipliers defined for the CIM.  When applied to unit symbols, the unit symbol is treated as a derived unit. Regardless of the contents of the unit symbol text, the unit symbol shall be treated as if it were a single-character unit symbol. Unit symbols should not contain multipliers, and it should be left to the multiplier to define the multiple for an entire data type.   For example, if a unit symbol is "m2Pers" and the multiplier is "k", then the value is k(m**2/s), and the multiplier applies to the entire final value, not to any individual part of the value. This can be conceptualized by substituting a derived unit symbol for the unit type. If one imagines that the symbol "Þ" represents the derived unit "m2Pers", then applying the multiplier "k" can be conceptualized simply as "kÞ".  For example, the SI unit for mass is "kg" and not "g".  If the unit symbol is defined as "kg", then the multiplier is applied to "kg" as a whole and does not replace the "k" in front of the "g". In this case, the multiplier of "m" would be used with the unit symbol of "kg" to represent one gram.  As a text string, this violates the instructions in IEC 80000-1. However, because the unit symbol in CIM is treated as a derived unit instead of as an SI unit, it makes more sense to conceptualize the "kg" as if it were replaced by one of the proposed replacements for the SI mass symbol. If one imagines that the "kg" were replaced by a symbol "Þ", then it is easier to conceptualize the multiplier "m" as creating the proper unit "mÞ", and not the forbidden unit "mkg".  # noqa: E501
    """  # noqa: E501

    y = "y"  # Yocto 10**-24.  # noqa: E501
    z = "z"  # Zepto 10**-21.  # noqa: E501
    a = "a"  # Atto 10**-18.  # noqa: E501
    f = "f"  # Femto 10**-15.  # noqa: E501
    p = "p"  # Pico 10**-12.  # noqa: E501
    n = "n"  # Nano 10**-9.  # noqa: E501
    micro = "micro"  # Micro 10**-6.  # noqa: E501
    m = "m"  # Milli 10**-3.  # noqa: E501
    c = "c"  # Centi 10**-2.  # noqa: E501
    d = "d"  # Deci 10**-1.  # noqa: E501
    none = "none"  # No multiplier or equivalently multiply by 1.  # noqa: E501
    da = "da"  # Deca 10**1.  # noqa: E501
    h = "h"  # Hecto 10**2.  # noqa: E501
    k = "k"  # Kilo 10**3.  # noqa: E501
    M = "M"  # Mega 10**6.  # noqa: E501
    G = "G"  # Giga 10**9.  # noqa: E501
    T = "T"  # Tera 10**12.  # noqa: E501
    P = "P"  # Peta 10**15.  # noqa: E501
    E = "E"  # Exa 10**18.  # noqa: E501
    Z = "Z"  # Zetta 10**21.  # noqa: E501
    Y = "Y"  # Yotta 10**24.  # noqa: E501
