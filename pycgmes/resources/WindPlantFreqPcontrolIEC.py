"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """
    Frequency and active power controller model. Reference: IEC 61400-27-1:2015, Annex D.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this frequency and active power wind plant
      model.
    dprefmax: Maximum ramp rate of pWTref request from the plant controller to the wind turbines (dprefmax) (>
      WindPlantFreqPcontrolIEC.dprefmin). It is a case-dependent parameter.
    dprefmin: Minimum (negative) ramp rate of pWTref request from the plant controller to the wind turbines (dprefmin)
      (< WindPlantFreqPcontrolIEC.dprefmax). It is a project-dependent parameter.
    dpwprefmax: Maximum positive ramp rate for wind plant power reference (dpWPrefmax) (>
      WindPlantFreqPcontrolIEC.dpwprefmin). It is a project-dependent parameter.
    dpwprefmin: Maximum negative ramp rate for wind plant power reference (dpWPrefmin) (<
      WindPlantFreqPcontrolIEC.dpwprefmax). It is a project-dependent parameter.
    prefmax: Maximum pWTref request from the plant controller to the wind turbines (prefmax) (>
      WindPlantFreqPcontrolIEC.prefmin). It is a project-dependent parameter.
    prefmin: Minimum pWTref request from the plant controller to the wind turbines (prefmin) (<
      WindPlantFreqPcontrolIEC.prefmax). It is a project-dependent parameter.
    kiwpp: Plant P controller integral gain (KIWPp). It is a project-dependent parameter.
    kiwppmax: Maximum PI integrator term (KIWPpmax) (> WindPlantFreqPcontrolIEC.kiwppmin). It is a project-dependent
      parameter.
    kiwppmin: Minimum PI integrator term (KIWPpmin) (< WindPlantFreqPcontrolIEC.kiwppmax). It is a project-dependent
      parameter.
    kpwpp: Plant P controller proportional gain (KPWPp). It is a project-dependent parameter.
    kwppref: Power reference gain (KWPpref). It is a project-dependent parameter.
    tpft: Lead time constant in reference value transfer function (Tpft) (>= 0). It is a project-dependent parameter.
    tpfv: Lag time constant in reference value transfer function (Tpfv) (>= 0). It is a project-dependent parameter.
    twpffiltp: Filter time constant for frequency measurement (TWPffiltp) (>= 0). It is a project-dependent parameter.
    twppfiltp: Filter time constant for active power measurement (TWPpfiltp) (>= 0). It is a project-dependent
      parameter.
    WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated.
    """

    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    dprefmax: float = 0.0  # Type #PU in CIM
    dprefmin: float = 0.0  # Type #PU in CIM
    dpwprefmax: float = 0.0  # Type #PU in CIM
    dpwprefmin: float = 0.0  # Type #PU in CIM
    prefmax: float = 0.0  # Type #PU in CIM
    prefmin: float = 0.0  # Type #PU in CIM
    kiwpp: float = 0.0  # Type #Float in CIM
    kiwppmax: float = 0.0  # Type #PU in CIM
    kiwppmin: float = 0.0  # Type #PU in CIM
    kpwpp: float = 0.0  # Type #Float in CIM
    kwppref: float = 0.0  # Type #PU in CIM
    tpft: int = 0  # Type #Seconds in CIM
    tpfv: int = 0  # Type #Seconds in CIM
    twpffiltp: int = 0  # Type #Seconds in CIM
    twppfiltp: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindPlantIEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindPlantFreqPcontrolIEC"]
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
            "WindDynamicsLookupTable": [
                Profile.DY.value,
            ],
            "dprefmax": [
                Profile.DY.value,
            ],
            "dprefmin": [
                Profile.DY.value,
            ],
            "dpwprefmax": [
                Profile.DY.value,
            ],
            "dpwprefmin": [
                Profile.DY.value,
            ],
            "prefmax": [
                Profile.DY.value,
            ],
            "prefmin": [
                Profile.DY.value,
            ],
            "kiwpp": [
                Profile.DY.value,
            ],
            "kiwppmax": [
                Profile.DY.value,
            ],
            "kiwppmin": [
                Profile.DY.value,
            ],
            "kpwpp": [
                Profile.DY.value,
            ],
            "kwppref": [
                Profile.DY.value,
            ],
            "tpft": [
                Profile.DY.value,
            ],
            "tpfv": [
                Profile.DY.value,
            ],
            "twpffiltp": [
                Profile.DY.value,
            ],
            "twppfiltp": [
                Profile.DY.value,
            ],
            "WindPlantIEC": [
                Profile.DY.value,
            ],
        }
