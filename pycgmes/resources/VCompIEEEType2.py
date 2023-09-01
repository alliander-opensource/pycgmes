"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass(config=DataclassConfig)
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:2..n in CIM  # pylint: disable-next=line-too-long
    # GenICompensationForGenJ : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
