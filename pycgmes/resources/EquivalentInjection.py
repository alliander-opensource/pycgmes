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
from .Base import DataclassConfig, Profile
from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentInjection(EquivalentEquipment):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point
      of connection.

    maxP: Maximum active power of the injection.
    maxQ: Maximum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for
      short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
    minP: Minimum active power of the injection.
    minQ: Minimum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for
      short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
    regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local
      voltage. If true the EquivalentInjection can regulate. If false the EquivalentInjection
      cannot regulate. ReactiveCapabilityCurve can only be associated with EquivalentInjection
      if the flag is true.
    ReactiveCapabilityCurve: The reactive capability curve used by this equivalent injection.
    r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    regulationStatus: Specifies the regulation status of the EquivalentInjection.  True is regulating.  False is not
      regulating.
    regulationTarget: The target voltage for voltage regulation. The attribute shall be a positive value.
    p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    """

    maxP: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    maxQ: float = Field(
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

    minQ: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    regulationCapability: bool = Field(
        default=False,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ReactiveCapabilityCurve: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    r: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    r0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    r2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    regulationStatus: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    regulationTarget: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        }
