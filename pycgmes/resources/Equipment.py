"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerSystemResource import PowerSystemResource


@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    EquipmentContainer: Container of this equipment.
    aggregate: The aggregate flag provides an alternative way of representing an aggregated (equivalent) element. It is
      applicable in cases when the dedicated classes for equivalent equipment do not have all of the
      attributes necessary to represent the required level of detail.  In case the flag is set to `true`
      the single instance of equipment represents multiple pieces of equipment that have been modelled
      together as an aggregate equivalent obtained by a network reduction procedure. Examples would be
      power transformers or synchronous machines operating in parallel modelled as a single aggregate
      power transformer or aggregate synchronous machine.   The attribute is not used for
      EquivalentBranch, EquivalentShunt and EquivalentInjection.
    normallyInService: Specifies the availability of the equipment under normal operating conditions. True means the
      equipment is available for topology processing, which determines if the equipment is
      energized or not. False means that the equipment is treated by network applications as if
      it is not in the model.
    OperationalLimitSet: The operational limit sets associated with this equipment.
    inService: Specifies the availability of the equipment. True means the equipment is available for topology
      processing, which determines if the equipment is energized or not. False means that the equipment
      is treated by network applications as if it is not in the model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    EquipmentContainer: Optional[str] = None  # Type M:0..1 in CIM
    aggregate: bool = False  # Type #Boolean in CIM
    normallyInService: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # OperationalLimitSet : list = field(default_factory=list)  # Type M:0..n in CIM
    inService: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Equipment\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "EquipmentContainer": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "aggregate": [
                self.profiles.EQ.value,
            ],
            "normallyInService": [
                self.profiles.EQ.value,
            ],
            "OperationalLimitSet": [
                self.profiles.EQ.value,
            ],
            "inService": [
                self.profiles.SSH.value,
            ],
        }
