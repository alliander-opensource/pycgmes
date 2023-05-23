"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContPType3IEC(IdentifiedObject):
    """
    P control model type 3. Reference: IEC 61400-27-1:2015, 5.6.5.4.

    dpmax: Maximum wind turbine power ramp rate (dpmax). It is a type-dependent parameter.
    dprefmax: Maximum ramp rate of wind turbine reference power (dprefmax). It is a project-dependent parameter.
    dprefmin: Minimum ramp rate of wind turbine reference power (dprefmin). It is a project-dependent parameter.
    dthetamax: Ramp limitation of torque, required in some grid codes (dtmax). It is a project-dependent parameter.
    dthetamaxuvrt: Limitation of torque rise rate during UVRT (dthetamaxUVRT). It is a project-dependent parameter.
    kdtd: Gain for active drive train damping (KDTD). It is a type-dependent parameter.
    kip: PI controller integration parameter (KIp). It is a type-dependent parameter.
    kpp: PI controller proportional gain (KPp). It is a type-dependent parameter.
    mpuvrt: Enable UVRT power control mode (MpUVRT).  It is a project-dependent parameter. true = voltage control (1 in
      the IEC model) false = reactive power control (0 in the IEC model).
    omegaoffset: Offset to reference value that limits controller action during rotor speed changes (omegaoffset). It is
      a case-dependent parameter.
    pdtdmax: Maximum active drive train damping power (pDTDmax). It is a type-dependent parameter.
    tdvs: Time delay after deep voltage sags (TDVS) (>= 0). It is a project-dependent parameter.
    thetaemin: Minimum electrical generator torque (temin). It is a type-dependent parameter.
    thetauscale: Voltage scaling factor of reset-torque (tuscale). It is a project-dependent parameter.
    tomegafiltp3: Filter time constant for generator speed measurement (Tomegafiltp3) (>= 0). It is a type-dependent
      parameter.
    tpfiltp3: Filter time constant for power measurement (Tpfiltp3) (>= 0). It is a type-dependent parameter.
    tpord: Time constant in power order lag (Tpord). It is a type-dependent parameter.
    tufiltp3: Filter time constant for voltage measurement (Tufiltp3) (>= 0). It is a type-dependent parameter.
    tomegaref: Time constant in speed reference filter (Tomega,ref) (>= 0). It is a type-dependent parameter.
    udvs: Voltage limit for hold UVRT status after deep voltage sags (uDVS). It is a project-dependent parameter.
    updip: Voltage dip threshold for P-control (uPdip).  Part of turbine control, often different (e.g 0.8) from
      converter thresholds. It is a project-dependent parameter.
    omegadtd: Active drive train damping frequency (omegaDTD). It can be calculated from two mass model parameters. It
      is a type-dependent parameter.
    zeta: Coefficient for active drive train damping (zeta). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind control P type 3 model is associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this P control type 3 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    dpmax: float = 0.0  # Type #PU in CIM
    dprefmax: float = 0.0  # Type #PU in CIM
    dprefmin: float = 0.0  # Type #PU in CIM
    dthetamax: float = 0.0  # Type #PU in CIM
    dthetamaxuvrt: float = 0.0  # Type #PU in CIM
    kdtd: float = 0.0  # Type #PU in CIM
    kip: float = 0.0  # Type #PU in CIM
    kpp: float = 0.0  # Type #PU in CIM
    mpuvrt: bool = False  # Type #Boolean in CIM
    omegaoffset: float = 0.0  # Type #PU in CIM
    pdtdmax: float = 0.0  # Type #PU in CIM
    tdvs: int = 0  # Type #Seconds in CIM
    thetaemin: float = 0.0  # Type #PU in CIM
    thetauscale: float = 0.0  # Type #PU in CIM
    tomegafiltp3: int = 0  # Type #Seconds in CIM
    tpfiltp3: int = 0  # Type #Seconds in CIM
    tpord: float = 0.0  # Type #PU in CIM
    tufiltp3: int = 0  # Type #Seconds in CIM
    tomegaref: int = 0  # Type #Seconds in CIM
    udvs: float = 0.0  # Type #PU in CIM
    updip: float = 0.0  # Type #PU in CIM
    omegadtd: float = 0.0  # Type #PU in CIM
    zeta: float = 0.0  # Type #Float in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContPType3IEC\n"
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
            "dpmax": [
                self.profiles.DY.value,
            ],
            "dprefmax": [
                self.profiles.DY.value,
            ],
            "dprefmin": [
                self.profiles.DY.value,
            ],
            "dthetamax": [
                self.profiles.DY.value,
            ],
            "dthetamaxuvrt": [
                self.profiles.DY.value,
            ],
            "kdtd": [
                self.profiles.DY.value,
            ],
            "kip": [
                self.profiles.DY.value,
            ],
            "kpp": [
                self.profiles.DY.value,
            ],
            "mpuvrt": [
                self.profiles.DY.value,
            ],
            "omegaoffset": [
                self.profiles.DY.value,
            ],
            "pdtdmax": [
                self.profiles.DY.value,
            ],
            "tdvs": [
                self.profiles.DY.value,
            ],
            "thetaemin": [
                self.profiles.DY.value,
            ],
            "thetauscale": [
                self.profiles.DY.value,
            ],
            "tomegafiltp3": [
                self.profiles.DY.value,
            ],
            "tpfiltp3": [
                self.profiles.DY.value,
            ],
            "tpord": [
                self.profiles.DY.value,
            ],
            "tufiltp3": [
                self.profiles.DY.value,
            ],
            "tomegaref": [
                self.profiles.DY.value,
            ],
            "udvs": [
                self.profiles.DY.value,
            ],
            "updip": [
                self.profiles.DY.value,
            ],
            "omegadtd": [
                self.profiles.DY.value,
            ],
            "zeta": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3IEC": [
                self.profiles.DY.value,
            ],
            "WindDynamicsLookupTable": [
                self.profiles.DY.value,
            ],
        }
