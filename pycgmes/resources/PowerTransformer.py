"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ConductingEquipment import ConductingEquipment


@dataclass
class PowerTransformer(ConductingEquipment):
    """
    An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing
      mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active
      power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A
      power transformer can be modelled with or without tanks and is intended for use in both balanced and
      unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding),
      three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The
      association from TransformerEnd to BaseVoltage should be used instead.

    PowerTransformerEnd: The ends of this power transformer.
    beforeShCircuitHighestOperatingCurrent: The highest operating current (Ib in IEC 60909-0) before short circuit
      (depends on network configuration and relevant reliability
      philosophy). It is used for calculation of the impedance correction
      factor KT defined in IEC 60909-0.
    beforeShCircuitHighestOperatingVoltage: The highest operating voltage (Ub in IEC 60909-0) before short circuit. It
      is used for calculation of the impedance correction factor KT defined
      in IEC 60909-0. This is worst case voltage on the low side winding
      (3.7.1 of IEC 60909:2001). Used to define operating conditions.
    beforeShortCircuitAnglePf: The angle of power factor before short circuit (phib in IEC 60909-0). It is used for
      calculation of the impedance correction factor KT defined in IEC 60909-0. This is
      the worst case power factor. Used to define operating conditions.
    highSideMinOperatingU: The minimum operating voltage (uQmin in IEC 60909-0) at the high voltage side (Q side) of the
      unit transformer of the power station unit. A value well established from long-term
      operating experience of the system. It is used for calculation of the impedance
      correction factor KG defined in IEC 60909-0.
    isPartOfGeneratorUnit: Indicates whether the machine is part of a power station unit. Used for short circuit data
      exchange according to IEC 60909.  It has an impact on how the correction factors are
      calculated for transformers, since the transformer is not necessarily part of a
      synchronous machine and generating unit. It is not always possible to derive this
      information from the model. This is why the attribute is necessary.
    operationalValuesConsidered: It is used to define if the data (other attributes related to short circuit data
      exchange) defines long term operational conditions or not. Used for short circuit
      data exchange according to IEC 60909.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # PowerTransformerEnd : list = field(default_factory=list)  # Type M:0..n in CIM
    beforeShCircuitHighestOperatingCurrent: float = 0.0  # Type #CurrentFlow in CIM
    beforeShCircuitHighestOperatingVoltage: float = 0.0  # Type #Voltage in CIM
    beforeShortCircuitAnglePf: float = 0.0  # Type #AngleDegrees in CIM
    highSideMinOperatingU: float = 0.0  # Type #Voltage in CIM
    isPartOfGeneratorUnit: bool = False  # Type #Boolean in CIM
    operationalValuesConsidered: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PowerTransformer\n"
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
                self.profiles.EQ.value,
                self.profiles.SC.value,
            ],
            # Attributes
            "PowerTransformerEnd": [
                self.profiles.EQ.value,
            ],
            "beforeShCircuitHighestOperatingCurrent": [
                self.profiles.SC.value,
            ],
            "beforeShCircuitHighestOperatingVoltage": [
                self.profiles.SC.value,
            ],
            "beforeShortCircuitAnglePf": [
                self.profiles.SC.value,
            ],
            "highSideMinOperatingU": [
                self.profiles.SC.value,
            ],
            "isPartOfGeneratorUnit": [
                self.profiles.SC.value,
            ],
            "operationalValuesConsidered": [
                self.profiles.SC.value,
            ],
        }
