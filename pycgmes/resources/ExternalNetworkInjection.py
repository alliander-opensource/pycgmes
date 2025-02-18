"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .RegulatingCondEq import RegulatingCondEq


@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """
    This class represents the external network and it is used for IEC 60909 calculations.

    governorSCD: Power Frequency Bias. This is the change in power injection divided by the change in frequency and
      negated.  A positive value of the power frequency bias provides additional power injection upon a
      drop in frequency.
    ikSecond: Indicates whether initial symmetrical short-circuit current and power have been calculated according to
      IEC (Ik`).  Used only if short circuit calculations are done according to superposition method.
    maxInitialSymShCCurrent: Maximum initial symmetrical short-circuit currents (Ik` max) in A (Ik` = Sk`/(SQRT(3) Un)).
      Used for short circuit data exchange according to IEC 60909.
    maxP: Maximum active power of the injection.
    maxQ: Maximum reactive power limit. It is used for modelling of infeed for load flow exchange and not for short
      circuit modelling.
    maxR0ToX0Ratio: Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance
      (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909.
    maxR1ToX1Ratio: Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance
      (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909.
    maxZ0ToZ1Ratio: Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used
      for short circuit data exchange according to IEC 60909.
    minInitialSymShCCurrent: Minimum initial symmetrical short-circuit currents (Ik` min) in A (Ik` = Sk`/(SQRT(3) Un)).
      Used for short circuit data exchange according to IEC 60909.
    minP: Minimum active power of the injection.
    minQ: Minimum reactive power limit. It is used for modelling of infeed for load flow exchange and not for short
      circuit modelling.
    minR0ToX0Ratio: Indicates whether initial symmetrical short-circuit current and power have been calculated according
      to IEC (Ik`). Used for short circuit data exchange according to IEC 6090.
    minR1ToX1Ratio: Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance
      (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909.
    minZ0ToZ1Ratio: Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used
      for short circuit data exchange according to IEC 60909.
    p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for steady state solutions.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for steady state solutions.
    referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care
      (default) 1 = highest priority. 2 is less than 1 and so on.
    voltageFactor: Voltage factor in pu, which was used to calculate short-circuit current Ik` and power Sk`.  Used only
      if short circuit calculations are done according to superposition method.
    """

    governorSCD: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    ikSecond: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxInitialSymShCCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxP: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxQ: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxR0ToX0Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxR1ToX1Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxZ0ToZ1Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minInitialSymShCCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minP: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minQ: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minR0ToX0Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minR1ToX1Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minZ0ToZ1Ratio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    p: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    q: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    referencePriority: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    voltageFactor: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
