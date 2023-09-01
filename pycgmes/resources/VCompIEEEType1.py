"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass(config=DataclassConfig)
class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is common to all
      excitation system models described in the IEEE Standard.  Parameter details:  If Rc and Xc are set to zero,
      the load compensation is not employed and the behaviour is as a simple sensing circuit.   If all parameters
      (Rc, Xc and Tr) are set to zero, the standard model VCompIEEEType1 is bypassed.  Reference: IEEE 421.5-2005 4.

    rc: Resistive component of compensation of a generator (Rc) (>= 0).
    xc: Reactive component of compensation of a generator (Xc) (>= 0).
    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    """

    rc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
