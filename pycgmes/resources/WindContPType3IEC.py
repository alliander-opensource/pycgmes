"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=WindContPType3IEC"]
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
            "dpmax": [
                Profile.DY.value,
            ],
            "dprefmax": [
                Profile.DY.value,
            ],
            "dprefmin": [
                Profile.DY.value,
            ],
            "dthetamax": [
                Profile.DY.value,
            ],
            "dthetamaxuvrt": [
                Profile.DY.value,
            ],
            "kdtd": [
                Profile.DY.value,
            ],
            "kip": [
                Profile.DY.value,
            ],
            "kpp": [
                Profile.DY.value,
            ],
            "mpuvrt": [
                Profile.DY.value,
            ],
            "omegaoffset": [
                Profile.DY.value,
            ],
            "pdtdmax": [
                Profile.DY.value,
            ],
            "tdvs": [
                Profile.DY.value,
            ],
            "thetaemin": [
                Profile.DY.value,
            ],
            "thetauscale": [
                Profile.DY.value,
            ],
            "tomegafiltp3": [
                Profile.DY.value,
            ],
            "tpfiltp3": [
                Profile.DY.value,
            ],
            "tpord": [
                Profile.DY.value,
            ],
            "tufiltp3": [
                Profile.DY.value,
            ],
            "tomegaref": [
                Profile.DY.value,
            ],
            "udvs": [
                Profile.DY.value,
            ],
            "updip": [
                Profile.DY.value,
            ],
            "omegadtd": [
                Profile.DY.value,
            ],
            "zeta": [
                Profile.DY.value,
            ],
            "WindTurbineType3IEC": [
                Profile.DY.value,
            ],
            "WindDynamicsLookupTable": [
                Profile.DY.value,
            ],
        }
