"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ACDCTerminal import ACDCTerminal


@dataclass
class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection
      points called connectivity nodes.

    AuxiliaryEquipment: The auxiliary equipment connected to the terminal.
    ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be
      connected to other conducting equipment terminals via connectivity nodes or topological
      nodes.
    ConnectivityNode: The connectivity node to which this terminal connects with zero impedance.
    ConverterDCSides: All converters` DC sides linked to this point of common coupling terminal.
    HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch.
    HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch.
    RegulatingControl: The controls regulating this terminal.
    RemoteInputSignal: Input signal coming from this terminal.
    SvPowerFlow: The power flow state variable associated with the terminal.
    TieFlow: The control area tie flows to which this terminal associates.
    TopologicalNode: The topological node associated with the terminal.   This can be used as an alternative to the
      connectivity node path to topological node, thus making it unnecessary to model connectivity
      nodes in some cases.   Note that the if connectivity nodes are in the model, this association
      would probably not be used as an input specification.
    TransformerEnd: All transformer ends connected at this terminal.
    phases: Represents the normal network phasing condition. If the attribute is missing, three phases (ABC) shall be
      assumed, except for terminals of grounding classes (specializations of EarthFaultCompensator,
      GroundDisconnector, and Ground) which will be assumed to be N. Therefore, phase code ABCN is
      explicitly declared when needed, e.g. for star point grounding equipment. The phase code on terminals
      connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two
      terminals shall be consistent.
    """

    AuxiliaryEquipment: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    ConductingEquipment: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    ConnectivityNode: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    ConverterDCSides: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    HasFirstMutualCoupling: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    HasSecondMutualCoupling: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    RegulatingControl: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    RemoteInputSignal: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    SvPowerFlow: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    TieFlow: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    TopologicalNode: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.TP,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    TransformerEnd: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    phases: str = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
            Profile.EQ,
            Profile.EQBD,
            Profile.OP,
            Profile.SC,
            Profile.SSH,
            Profile.SV,
            Profile.TP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
