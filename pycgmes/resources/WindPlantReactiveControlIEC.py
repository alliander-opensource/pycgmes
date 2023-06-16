"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindPlantReactiveControlIEC(IdentifiedObject):
    """
    Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.
      Reference: IEC 61400-27-1:2015, Annex D.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this voltage and reactive power wind plant
      model.
    WindPlantIEC: Wind plant reactive control model associated with this wind plant.
    dxrefmax: Maximum positive ramp rate for wind turbine reactive power/voltage reference (dxrefmax) (>
      WindPlantReactiveControlIEC.dxrefmin). It is a project-dependent parameter.
    dxrefmin: Maximum negative ramp rate for wind turbine reactive power/voltage reference (dxrefmin) (<
      WindPlantReactiveControlIEC.dxrefmax). It is a project-dependent parameter.
    kiwpx: Plant Q controller integral gain (KIWPx). It is a project-dependent parameter.
    kiwpxmax: Maximum reactive power/voltage reference from integration (KIWPxmax) (>
      WindPlantReactiveControlIEC.kiwpxmin). It is a project-dependent parameter.
    kiwpxmin: Minimum reactive power/voltage reference from integration (KIWPxmin) (<
      WindPlantReactiveControlIEC.kiwpxmax). It is a project-dependent parameter.
    kpwpx: Plant Q controller proportional gain (KPWPx). It is a project-dependent parameter.
    kwpqref: Reactive power reference gain (KWPqref). It is a project-dependent parameter.
    kwpqu: Plant voltage control droop (KWPqu). It is a project-dependent parameter.
    tuqfilt: Filter time constant for voltage-dependent reactive power (Tuqfilt) (>= 0). It is a project-dependent
      parameter.
    twppfiltq: Filter time constant for active power measurement (TWPpfiltq) (>= 0). It is a project-dependent
      parameter.
    twpqfiltq: Filter time constant for reactive power measurement (TWPqfiltq) (>= 0). It is a project-dependent
      parameter.
    twpufiltq: Filter time constant for voltage measurement (TWPufiltq) (>= 0). It is a project-dependent parameter.
    txft: Lead time constant in reference value transfer function (Txft) (>= 0). It is a project-dependent parameter.
    txfv: Lag time constant in reference value transfer function (Txfv) (>= 0). It is a project-dependent parameter.
    uwpqdip: Voltage threshold for UVRT detection in Q control (uWPqdip). It is a project-dependent parameter.
    windPlantQcontrolModesType: Reactive power/voltage controller mode (MWPqmode). It is a case-dependent parameter.
    xrefmax: Maximum xWTref (qWTref or delta uWTref) request from the plant controller (xrefmax) (>
      WindPlantReactiveControlIEC.xrefmin). It is a case-dependent parameter.
    xrefmin: Minimum xWTref (qWTref or delta uWTref) request from the plant controller (xrefmin) (<
      WindPlantReactiveControlIEC.xrefmax). It is a project-dependent parameter.
    """

    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # WindPlantIEC : Optional[str] = None  # Type M:1 in CIM
    dxrefmax: float = 0.0  # Type #PU in CIM
    dxrefmin: float = 0.0  # Type #PU in CIM
    kiwpx: float = 0.0  # Type #Float in CIM
    kiwpxmax: float = 0.0  # Type #PU in CIM
    kiwpxmin: float = 0.0  # Type #PU in CIM
    kpwpx: float = 0.0  # Type #Float in CIM
    kwpqref: float = 0.0  # Type #PU in CIM
    kwpqu: float = 0.0  # Type #PU in CIM
    tuqfilt: int = 0  # Type #Seconds in CIM
    twppfiltq: int = 0  # Type #Seconds in CIM
    twpqfiltq: int = 0  # Type #Seconds in CIM
    twpufiltq: int = 0  # Type #Seconds in CIM
    txft: int = 0  # Type #Seconds in CIM
    txfv: int = 0  # Type #Seconds in CIM
    uwpqdip: float = 0.0  # Type #PU in CIM
    windPlantQcontrolModesType: Optional[str] = None  # Type M:1..1 in CIM
    xrefmax: float = 0.0  # Type #PU in CIM
    xrefmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindPlantReactiveControlIEC"]
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
            "WindPlantIEC": [
                Profile.DY.value,
            ],
            "dxrefmax": [
                Profile.DY.value,
            ],
            "dxrefmin": [
                Profile.DY.value,
            ],
            "kiwpx": [
                Profile.DY.value,
            ],
            "kiwpxmax": [
                Profile.DY.value,
            ],
            "kiwpxmin": [
                Profile.DY.value,
            ],
            "kpwpx": [
                Profile.DY.value,
            ],
            "kwpqref": [
                Profile.DY.value,
            ],
            "kwpqu": [
                Profile.DY.value,
            ],
            "tuqfilt": [
                Profile.DY.value,
            ],
            "twppfiltq": [
                Profile.DY.value,
            ],
            "twpqfiltq": [
                Profile.DY.value,
            ],
            "twpufiltq": [
                Profile.DY.value,
            ],
            "txft": [
                Profile.DY.value,
            ],
            "txfv": [
                Profile.DY.value,
            ],
            "uwpqdip": [
                Profile.DY.value,
            ],
            "windPlantQcontrolModesType": [
                Profile.DY.value,
            ],
            "xrefmax": [
                Profile.DY.value,
            ],
            "xrefmin": [
                Profile.DY.value,
            ],
        }
