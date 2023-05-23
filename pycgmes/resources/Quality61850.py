"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    badReference: bool = False  # Type #Boolean in CIM
    estimatorReplaced: bool = False  # Type #Boolean in CIM
    failure: bool = False  # Type #Boolean in CIM
    oldData: bool = False  # Type #Boolean in CIM
    operatorBlocked: bool = False  # Type #Boolean in CIM
    oscillatory: bool = False  # Type #Boolean in CIM
    outOfRange: bool = False  # Type #Boolean in CIM
    overFlow: bool = False  # Type #Boolean in CIM
    source: Optional[str] = None  # Type M:0..1 in CIM
    suspect: bool = False  # Type #Boolean in CIM
    test: bool = False  # Type #Boolean in CIM
    validity: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Quality61850\n"
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
                self.profiles.OP.value,
            ],
            # Attributes
            "badReference": [
                self.profiles.OP.value,
            ],
            "estimatorReplaced": [
                self.profiles.OP.value,
            ],
            "failure": [
                self.profiles.OP.value,
            ],
            "oldData": [
                self.profiles.OP.value,
            ],
            "operatorBlocked": [
                self.profiles.OP.value,
            ],
            "oscillatory": [
                self.profiles.OP.value,
            ],
            "outOfRange": [
                self.profiles.OP.value,
            ],
            "overFlow": [
                self.profiles.OP.value,
            ],
            "source": [
                self.profiles.OP.value,
            ],
            "suspect": [
                self.profiles.OP.value,
            ],
            "test": [
                self.profiles.OP.value,
            ],
            "validity": [
                self.profiles.OP.value,
            ],
        }
