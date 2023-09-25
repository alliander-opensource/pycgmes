"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .RegulatingCondEq import RegulatingCondEq


@dataclass(config=DataclassConfig)
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

    aVRDelay: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    grounded: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maximumSections: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    nomU: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    normalSections: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    voltageSensitivity: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # SvShuntCompensatorSections : Optional[str] = Field(default=None, in_profiles = [Profile.SV, ])

    sections: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
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
            Profile.SV,
            Profile.SSH,
        }
