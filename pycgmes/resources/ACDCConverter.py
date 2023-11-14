# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching
      devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    baseS: Base apparent power of the converter pole. The attribute shall be a positive value.
    idleLoss: Active power loss in pole at no power transfer. It is converter`s configuration data used in power flow.
      The attribute shall be a positive value.
    maxUdc: The maximum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    minUdc: The minimum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    numberOfValves: Number of valves in the converter. Used in loss calculations.
    ratedUdc: Rated converter DC voltage, also called UdN. The attribute shall be a positive value. It is converter`s
      configuration data used in power flow. For instance a bipolar HVDC link with value  200 kV has a
      400kV difference between the dc lines.
    resistiveLoss: It is converter`s configuration data used in power flow. Refer to poleLossP. The attribute shall be a
      positive value.
    switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. The attribute
      shall be a positive value.
    valveU0: Valve threshold voltage, also called Uvalve. Forward voltage drop when the valve is conducting. Used in
      loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0.
    maxP: Maximum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    minP: Minimum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    PccTerminal: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power
      transformer (or switch) closest to the AC network.
    DCTerminals: A DC converter have DC converter terminals. A converter has two DC converter terminals.
    idc: Converter DC current, also called Id. It is converter`s state variable, result from power flow.
    poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2. For lossless
      operation Pdc=Pac. For rectifier operation with losses Pdc=Pac-lossP. For inverter operation with
      losses Pdc=Pac+lossP. It is converter`s state variable used in power flow. The attribute shall be a
      positive value.
    uc: Line-to-line converter voltage, the voltage at the AC side of the valve. It is converter`s state variable,
      result from power flow. The attribute shall be a positive value.
    udc: Converter voltage at the DC side, also called Ud. It is converter`s state variable, result from power flow. The
      attribute shall be a positive value.
    p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    targetPpcc: Real power injection target in AC grid, at point of common coupling.  Load sign convention is used, i.e.
      positive sign means flow out from a node.
    targetUdc: Target value for DC voltage magnitude. The attribute shall be a positive value.
    """

    baseS: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    idleLoss: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maxUdc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    minUdc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    numberOfValves: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedUdc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    resistiveLoss: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    switchingLoss: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    valveU0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maxP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    minP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    PccTerminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTerminals : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    idc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    poleLossP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    uc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    udc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetPpcc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    targetUdc: float = Field(
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
            Profile.SV,
            Profile.SSH,
            Profile.DY,
        }
