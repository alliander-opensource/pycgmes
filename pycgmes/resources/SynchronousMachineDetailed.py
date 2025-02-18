"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .SynchronousMachineDynamics import SynchronousMachineDynamics


@dataclass
class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The
      several variations differ in the following ways: - the number of  equivalent windings that are included; - the
      way in which saturation is incorporated into the model; - whether or not "subtransient saliency" (X''q not =
      X''d) is represented. It is not necessary for each simulation tool to have separate models for each of the
      model types.  The same model can often be used for several types by alternative logic within the model.  Also,
      differences in saturation representation might not result in significant model performance differences so
      model substitutions are often acceptable.

    efdBaseRatio: Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical
      value = 1.
    ifdBaseType: Excitation base system mode. It should be equal to the value of WLMDV given by the user. WLMDV is the
      PU ratio between the field voltage and the excitation current: Efd = WLMDV x Ifd. Typical value =
      ifag.
    saturationFactor120QAxis: Quadrature-axis saturation factor at 120% of rated terminal voltage (S12q) (>=
      SynchonousMachineDetailed.saturationFactorQAxis).  Typical value = 0,12.
    saturationFactorQAxis: Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value =
      0,02.
    """

    efdBaseRatio: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    ifdBaseType: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    saturationFactor120QAxis: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    saturationFactorQAxis: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.DY
