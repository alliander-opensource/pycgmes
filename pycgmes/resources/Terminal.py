"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ACDCTerminal import ACDCTerminal


@dataclass(config=DataclassConfig)
class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection
      points called connectivity nodes.

    TopologicalNode: The topological node associated with the terminal.   This can be used as an alternative to the
      connectivity node path to topological node, thus making it unnecessary to model connectivity
      nodes in some cases.   Note that the if connectivity nodes are in the model, this association
      would probably not be used as an input specification.
    ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be
      connected to other conducting equipment terminals via connectivity nodes or topological
      nodes.
    ConnectivityNode: The connectivity node to which this terminal connects with zero impedance.
    ConverterDCSides: All converters` DC sides linked to this point of common coupling terminal.
    AuxiliaryEquipment: The auxiliary equipment connected to the terminal.
    RegulatingControl: The controls regulating this terminal.
    phases: Represents the normal network phasing condition. If the attribute is missing, three phases (ABC) shall be
      assumed, except for terminals of grounding classes (specializations of EarthFaultCompensator,
      GroundDisconnector, and Ground) which will be assumed to be N. Therefore, phase code ABCN is
      explicitly declared when needed, e.g. for star point grounding equipment. The phase code on terminals
      connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two
      terminals shall be consistent.
    TransformerEnd: All transformer ends connected at this terminal.
    TieFlow: The control area tie flows to which this terminal associates.
    HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch.
    HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch.
    SvPowerFlow: The power flow state variable associated with the terminal.
    RemoteInputSignal: Input signal coming from this terminal.
    """

    TopologicalNode: Optional[str] = None  # Type M:0..1 in CIM
    ConductingEquipment: Optional[str] = None  # Type M:1 in CIM
    ConnectivityNode: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # ConverterDCSides : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # AuxiliaryEquipment : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # RegulatingControl : list = field(default_factory=list)  # Type M:0..n in CIM
    phases: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # TransformerEnd : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # TieFlow : list = field(default_factory=list)  # Type M:0..2 in CIM
    # *Association not used*
    # HasSecondMutualCoupling : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # HasFirstMutualCoupling : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # SvPowerFlow : Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # RemoteInputSignal : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Terminal"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.TP.value,
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
                Profile.OP.value,
            ],
            # Attributes
            "TopologicalNode": [
                Profile.TP.value,
            ],
            "ConductingEquipment": [
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.DY.value,
            ],
            "ConnectivityNode": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "ConverterDCSides": [
                Profile.EQ.value,
            ],
            "AuxiliaryEquipment": [
                Profile.EQ.value,
            ],
            "RegulatingControl": [
                Profile.EQ.value,
            ],
            "phases": [
                Profile.EQ.value,
            ],
            "TransformerEnd": [
                Profile.EQ.value,
            ],
            "TieFlow": [
                Profile.EQ.value,
            ],
            "HasSecondMutualCoupling": [
                Profile.SC.value,
            ],
            "HasFirstMutualCoupling": [
                Profile.SC.value,
            ],
            "SvPowerFlow": [
                Profile.SV.value,
            ],
            "RemoteInputSignal": [
                Profile.DY.value,
            ],
        }
