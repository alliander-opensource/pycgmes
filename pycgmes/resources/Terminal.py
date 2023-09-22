"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ACDCTerminal import ACDCTerminal


@dataclass(config=DataclassConfig)
class Terminal(ACDCTerminal, ModuleType):
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

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Terminal(*args, **kwargs)

    TopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.TP,
        ],
    )

    ConductingEquipment: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
            Profile.DY,
        ],
    )

    ConnectivityNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQBD,
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # ConverterDCSides : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # AuxiliaryEquipment : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RegulatingControl : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    phases: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # TransformerEnd : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..2 in CIM  # pylint: disable-next=line-too-long
    # TieFlow : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HasSecondMutualCoupling : list = Field(default_factory=list, in_profiles = [Profile.SC, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HasFirstMutualCoupling : list = Field(default_factory=list, in_profiles = [Profile.SC, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # SvPowerFlow : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RemoteInputSignal : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Terminal"
# work as well as
# "from Terminal import Terminal".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Terminal
