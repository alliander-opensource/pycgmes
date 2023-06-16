"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal
      devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be
      considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant.

    normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a
      status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen.
    ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and
      construction. The attribute shall be a positive value.
    retained: Branch is retained in the topological solution.  The flow through retained switches will normally be
      calculated in power flow.
    SwitchSchedules: A Switch can be associated with SwitchSchedules.
    SvSwitch: The switch state associated with the switch.
    open: The attribute tells if the switch is considered open when used as input to topology processing.
    locked: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open
      attributes as follows:  locked=true and Switch.open=true. The resulting state is open and locked;
      locked=false and Switch.open=true. The resulting state is open; locked=false and Switch.open=false.
      The resulting state is closed.
    """

    normalOpen: bool = False  # Type #Boolean in CIM
    ratedCurrent: float = 0.0  # Type #CurrentFlow in CIM
    retained: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # SwitchSchedules : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # SvSwitch : list = field(default_factory=list)  # Type M:0..n in CIM
    open: bool = False  # Type #Boolean in CIM
    locked: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Switch"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SV.value,
                Profile.SSH.value,
            ],
            # Attributes
            "normalOpen": [
                Profile.EQ.value,
            ],
            "ratedCurrent": [
                Profile.EQ.value,
            ],
            "retained": [
                Profile.EQ.value,
            ],
            "SwitchSchedules": [
                Profile.EQ.value,
            ],
            "SvSwitch": [
                Profile.SV.value,
            ],
            "open": [
                Profile.SSH.value,
            ],
            "locked": [
                Profile.SSH.value,
            ],
        }
