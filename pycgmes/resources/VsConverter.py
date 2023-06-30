"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ACDCConverter import ACDCConverter


@dataclass(config=DataclassConfig)
class VsConverter(ACDCConverter):
    """
    DC side of the voltage source converter (VSC).

    CapabilityCurve: Capability curve of this converter.
    maxModulationIndex: The maximum quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor
      typically less than 1. It is converter`s configuration data used in power flow.
    delta: Angle between VsConverter.uv and ACDCConverter.uc. It is converter`s state variable used in power flow. The
      attribute shall be a positive value or zero.
    uv: Line-to-line voltage on the valve side of the converter transformer. It is converter`s state variable, result
      from power flow. The attribute shall be a positive value.
    droop: Droop constant. The pu value is obtained as D [kV/MW] x Sb / Ubdc. The attribute shall be a positive value.
    droopCompensation: Compensation constant. Used to compensate for voltage drop when controlling voltage at a distant
      bus. The attribute shall be a positive value.
    pPccControl: Kind of control of real power and/or DC voltage.
    qPccControl: Kind of reactive power control.
    qShare: Reactive power sharing factor among parallel converters on Uac control. The attribute shall be a positive
      value or zero.
    targetQpcc: Reactive power injection target in AC grid, at point of common coupling.  Load sign convention is used,
      i.e. positive sign means flow out from a node.
    targetUpcc: Voltage target in AC grid, at point of common coupling. The attribute shall be a positive value.
    targetPowerFactorPcc: Power factor target at the AC side, at point of common coupling. The attribute shall be a
      positive value.
    targetPhasePcc: Phase target at AC side, at point of common coupling. The attribute shall be a positive value.
    targetPWMfactor: Magnitude of pulse-modulation factor. The attribute shall be a positive value.
    VSCDynamics: Voltage source converter dynamics model used to describe dynamic behaviour of this converter.
    """

    CapabilityCurve: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maxModulationIndex: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    delta: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    uv: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    droop: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    droopCompensation: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    pPccControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SSH,
        ],
    )

    qPccControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SSH,
        ],
    )

    qShare: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetQpcc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetUpcc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetPowerFactorPcc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetPhasePcc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetPWMfactor: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # VSCDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
        }
