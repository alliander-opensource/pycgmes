# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .LoadDynamics import LoadDynamics


@dataclass(config=DataclassConfig)
class LoadAggregate(LoadDynamics):
    """
    Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static
      (power flow) data. This load is usually the aggregation of many individual load devices and the load model is
      an approximate representation of the aggregate response of the load devices to system disturbances. Standard
      aggregate load model comprised of static and/or dynamic components.  A static load model represents the
      sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus
      voltage. A dynamic load model can be used to represent the aggregate response of the motor components of the
      load.

    LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load.
    LoadStatic: Aggregate static load associated with this aggregate load.
    """

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # LoadMotor : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # LoadStatic : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
