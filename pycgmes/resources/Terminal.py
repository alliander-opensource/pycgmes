"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ACDCTerminal import ACDCTerminal


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=Terminal\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.TP.value,
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SV.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
                self.profiles.OP.value,
            ],
            # Attributes
            "TopologicalNode": [
                self.profiles.TP.value,
            ],
            "ConductingEquipment": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.DY.value,
            ],
            "ConnectivityNode": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "ConverterDCSides": [
                self.profiles.EQ.value,
            ],
            "AuxiliaryEquipment": [
                self.profiles.EQ.value,
            ],
            "RegulatingControl": [
                self.profiles.EQ.value,
            ],
            "phases": [
                self.profiles.EQ.value,
            ],
            "TransformerEnd": [
                self.profiles.EQ.value,
            ],
            "TieFlow": [
                self.profiles.EQ.value,
            ],
            "HasSecondMutualCoupling": [
                self.profiles.SC.value,
            ],
            "HasFirstMutualCoupling": [
                self.profiles.SC.value,
            ],
            "SvPowerFlow": [
                self.profiles.SV.value,
            ],
            "RemoteInputSignal": [
                self.profiles.DY.value,
            ],
        }
