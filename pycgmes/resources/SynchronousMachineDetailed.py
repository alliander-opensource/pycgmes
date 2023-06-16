"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .SynchronousMachineDynamics import SynchronousMachineDynamics


@dataclass(config=DataclassConfig)
class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The
      several variations differ in the following ways: - the number of  equivalent windings that are included; - the
      way in which saturation is incorporated into the model; - whether or not "subtransient saliency" (X''q not =
      X''d) is represented. It is not necessary for each simulation tool to have separate models for each of the
      model types.  The same model can often be used for several types by alternative logic within the model.  Also,
      differences in saturation representation might not result in significant model performance differences so
      model substitutions are often acceptable.

    saturationFactorQAxis: Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value =
      0,02.
    saturationFactor120QAxis: Quadrature-axis saturation factor at 120% of rated terminal voltage (S12q) (>=
      SynchonousMachineDetailed.saturationFactorQAxis).  Typical value = 0,12.
    efdBaseRatio: Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical
      value = 1.
    ifdBaseType: Excitation base system mode. It should be equal to the value of WLMDV given by the user. WLMDV is the
      PU ratio between the field voltage and the excitation current: Efd = WLMDV x Ifd. Typical value =
      ifag.
    """

    saturationFactorQAxis: float = 0.0  # Type #Float in CIM
    saturationFactor120QAxis: float = 0.0  # Type #Float in CIM
    efdBaseRatio: float = 0.0  # Type #Float in CIM
    ifdBaseType: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SynchronousMachineDetailed"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "saturationFactorQAxis": [
                Profile.DY.value,
            ],
            "saturationFactor120QAxis": [
                Profile.DY.value,
            ],
            "efdBaseRatio": [
                Profile.DY.value,
            ],
            "ifdBaseType": [
                Profile.DY.value,
            ],
        }
