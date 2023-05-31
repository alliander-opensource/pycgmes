"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .RegulatingCondEq import RegulatingCondEq


@dataclass
class ShuntCompensator(RegulatingCondEq):
    """
    A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is
      an individual capacitor or reactor. A negative value for bPerSection indicates that the compensator is a
      reactor. ShuntCompensator is a single terminal device.  Ground is implied.

    aVRDelay: An automatic voltage regulation delay (AVRDelay) which is the time delay from a change in voltage to when
      the capacitor is allowed to change state. This filters out temporary changes in voltage.
    grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded.
    maximumSections: The maximum number of sections that may be switched in.
    nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the
      voltage at which the capacitor is connected to the network.
    normalSections: The normal number of sections switched in. The value shall be between zero and
      ShuntCompensator.maximumSections.
    voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive
      power.
    SvShuntCompensatorSections: The state for the number of shunt compensator sections in service.
    sections: Shunt compensator sections in use. Starting value for steady state solution. The attribute shall be a
      positive value or zero. Non integer values are allowed to support continuous variables. The reasons
      for continuous value are to support study cases where no discrete shunt compensators has yet been
      designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for
      a continuous solution as input.  For LinearShuntConpensator the value shall be between zero and
      ShuntCompensator.maximumSections. At value zero the shunt compensator conductance and admittance is
      zero. Linear interpolation of conductance and admittance between the previous and next integer
      section is applied in case of non-integer values. For NonlinearShuntCompensator-s shall only be set
      to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no interpolation between
      NonlinearShuntCompenstorPoint-s.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    aVRDelay: int = 0  # Type #Seconds in CIM
    grounded: bool = False  # Type #Boolean in CIM
    maximumSections: int = 0  # Type #Integer in CIM
    nomU: float = 0.0  # Type #Voltage in CIM
    normalSections: int = 0  # Type #Integer in CIM
    voltageSensitivity: float = 0.0  # Type #VoltagePerReactivePower in CIM
    # *Association not used*
    # SvShuntCompensatorSections : Optional[str] = None  # Type M:0..1 in CIM
    sections: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ShuntCompensator\n"
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
                self.profiles.SV.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "aVRDelay": [
                self.profiles.EQ.value,
            ],
            "grounded": [
                self.profiles.EQ.value,
            ],
            "maximumSections": [
                self.profiles.EQ.value,
            ],
            "nomU": [
                self.profiles.EQ.value,
            ],
            "normalSections": [
                self.profiles.EQ.value,
            ],
            "voltageSensitivity": [
                self.profiles.EQ.value,
            ],
            "SvShuntCompensatorSections": [
                self.profiles.SV.value,
            ],
            "sections": [
                self.profiles.SSH.value,
            ],
        }
