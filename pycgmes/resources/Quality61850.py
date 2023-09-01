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
from .Base import Base


@dataclass(config=DataclassConfig)
class Quality61850(Base):
    """
    Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in
      this class for convenience.

    badReference: Measurement value may be incorrect due to a reference being out of calibration.
    estimatorReplaced: Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but
      has been put in this class for convenience.
    failure: This identifier indicates that a supervision function has detected an internal or external failure, e.g.
      communication failure.
    oldData: Measurement value is old and possibly invalid, as it has not been successfully updated during a specified
      time interval.
    operatorBlocked: Measurement value is blocked and hence unavailable for transmission.
    oscillatory: To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast
      changing) binary inputs. If a signal changes in a defined time twice in the same direction (from
      0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier
      `oscillatory` is set. If it is detected a configured numbers of transient changes could be passed
      by. In this time the validity status `questionable` is set. If after this defined numbers of
      changes the signal is still in the oscillating state the value shall be set either to the
      opposite state of the previous stable value or to a defined default value. In this case the
      validity status `questionable` is reset and `invalid` is set as long as the signal is
      oscillating. If it is configured such that no transient changes should be passed by then the
      validity status `invalid` is set immediately in addition to the detail quality identifier
      `oscillatory` (used for status information only).
    outOfRange: Measurement value is beyond a predefined range of value.
    overFlow: Measurement value is beyond the capability of being  represented properly. For example, a counter value
      overflows from maximum count back to a value of zero.
    source: Source gives information related to the origin of a value. The value may be acquired from the process,
      defaulted or substituted.
    suspect: A correlation function has detected that the value is not consistent with other values. Typically set by a
      network State Estimator.
    test: Measurement value is transmitted for test purposes.
    validity: Validity of the measurement value.
    """

    badReference: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    estimatorReplaced: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    failure: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    oldData: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    operatorBlocked: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    oscillatory: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    outOfRange: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    overFlow: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    source: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    suspect: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    test: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    validity: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
