"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=WindPlantFreqPcontrolIEC\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "WindDynamicsLookupTable": [
                self.profiles.DY.value,
            ],
            "dprefmax": [
                self.profiles.DY.value,
            ],
            "dprefmin": [
                self.profiles.DY.value,
            ],
            "dpwprefmax": [
                self.profiles.DY.value,
            ],
            "dpwprefmin": [
                self.profiles.DY.value,
            ],
            "prefmax": [
                self.profiles.DY.value,
            ],
            "prefmin": [
                self.profiles.DY.value,
            ],
            "kiwpp": [
                self.profiles.DY.value,
            ],
            "kiwppmax": [
                self.profiles.DY.value,
            ],
            "kiwppmin": [
                self.profiles.DY.value,
            ],
            "kpwpp": [
                self.profiles.DY.value,
            ],
            "kwppref": [
                self.profiles.DY.value,
            ],
            "tpft": [
                self.profiles.DY.value,
            ],
            "tpfv": [
                self.profiles.DY.value,
            ],
            "twpffiltp": [
                self.profiles.DY.value,
            ],
            "twppfiltp": [
                self.profiles.DY.value,
            ],
            "WindPlantIEC": [
                self.profiles.DY.value,
            ],
        }
