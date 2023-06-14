"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class UnitSymbol(Base):
    """
    The derived units defined for usage in the CIM. In some cases, the derived unit is equal to an SI unit. Whenever
      possible, the standard derived symbol is used instead of the formula for the derived unit. For example, the
      unit symbol Farad is defined as "F" instead of "CPerV". In cases where a standard symbol does not exist for a
      derived unit, the formula for the unit is used as the unit symbol. For example, density does not have a
      standard symbol and so it is represented as "kgPerm3". With the exception of the "kg", which is an SI unit,
      the unit symbols do not contain multipliers and therefore represent the base derived unit to which a
      multiplier can be applied as a whole.  Every unit symbol is treated as an unparseable text as if it were a
      single-letter symbol. The meaning of each unit symbol is defined by the accompanying descriptive text and not
      by the text contents of the unit symbol. To allow the widest possible range of serializations without
      requiring special character handling, several substitutions are made which deviate from the format described
      in IEC 80000-1. The division symbol "/" is replaced by the letters "Per". Exponents are written in plain text
      after the unit as "m3" instead of being formatted as "m" with a superscript of 3  or introducing a symbol as
      in "m^3". The degree symbol "[SYMBOL REMOVED]" is replaced with the letters "deg". Any clarification of the
      meaning for a substitution is included in the description for the unit symbol. Non-SI units are included in
      list of unit symbols to allow sources of data to be correctly labelled with their non-SI units (for example, a
      GPS sensor that is reporting numbers that represent feet instead of meters). This allows software to use the
      unit symbol information correctly convert and scale the raw data of those sources into SI-based units.  The
      integer values are used for harmonization with IEC 61850.

    """

    # No attributes defined for this class.

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=UnitSymbol"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DL.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            # Attributes
        }
