"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .TransformerEnd import TransformerEnd


@dataclass
class PowerTransformerEnd(TransformerEnd):
    """
    A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0
      of a PowerTransformerEnd represents a star equivalent as follows. 1) for a two Terminal PowerTransformer the
      high voltage (TransformerEnd.endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while
      the low voltage (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0.
      Parameters are always provided, even if the PowerTransformerEnds have the same rated voltage.  In this case,
      the parameters are provided at the PowerTransformerEnd which has TransformerEnd.endNumber equal to 1. 2) for a
      three Terminal PowerTransformer the three PowerTransformerEnds represent a star equivalent with each leg in
      the star represented by r, r0, x, and x0 values. 3) For a three Terminal transformer each PowerTransformerEnd
      shall have g, g0, b and b0 values corresponding to the no load losses distributed on the three
      PowerTransformerEnds. The total no load loss shunt impedances may also be placed at one of the
      PowerTransformerEnds, preferably the end numbered 1, having the shunt values on end 1.  This is the preferred
      way. 4) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot
      be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
      Each PowerTransformerEnd must be contained by a PowerTransformer. Because a PowerTransformerEnd (or any other
      object) can not be contained by more than one parent, a PowerTransformerEnd can not have an association to an
      EquipmentContainer (Substation, VoltageLevel, etc).

    PowerTransformer: The power transformer of this power transformer end.
    b: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    b0: Zero sequence magnetizing branch susceptance.
    connectionKind: Kind of connection.
    g: Magnetizing branch conductance.
    g0: Zero sequence magnetizing branch conductance (star-model).
    phaseAngleClock: Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The
      valid values are 0 to 11. For example, for the secondary side end of a transformer with
      vector group code of `Dyn11`, specify the connection kind as wye with neutral and specify the
      phase angle of the clock as 11.  The clock value of the transformer end number specified as
      1, is assumed to be zero.  Note the transformer end number is not assumed to be the same as
      the terminal sequence number.
    r: Resistance (star-model) of the transformer end. The attribute shall be equal to or greater than zero for non-
      equivalent transformers.
    r0: Zero sequence series resistance (star-model) of the transformer end.
    ratedS: Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the
      values for the high and low voltage sides shall be identical.
    ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-
      phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is
      greater than or equal to ratedU for the lower voltage sides. The attribute shall be a positive value.
    x: Positive sequence series reactance (star-model) of the transformer end.
    x0: Zero sequence series reactance of the transformer end.
    """

    PowerTransformer: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    b: float = Field(
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

    b0: float = Field(
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

    connectionKind: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    g: float = Field(
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

    g0: float = Field(
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

    phaseAngleClock: int = Field(
        default=0,
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

    r: float = Field(
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

    r0: float = Field(
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

    ratedS: float = Field(
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

    ratedU: float = Field(
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

    x: float = Field(
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

    x0: float = Field(
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
