"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroFrancis(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of
      the hydraulic system of detailed hydro unit models, such as Francis and Pelton, is provided in the
      DetailedHydroModelHydraulicSystem diagram.

    am: Opening section SEFF at the maximum efficiency (Am).  Typical value = 0,7.
    av0: Area of the surge tank (AV0). Unit = m2. Typical value = 30.
    av1: Area of the compensation tank (AV1). Unit = m2. Typical value = 700.
    bp: Droop (Bp).  Typical value = 0,05.
    db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical value = 0.
    etamax: Maximum efficiency (EtaMax).  Typical value = 1,05.
    governorControl: Governor control flag (Cflag).  Typical value = mechanicHydrolicTachoAccelerator.
    h1: Head of compensation chamber water level with respect to the level of penstock (H1).  Unit = km.  Typical value
      = 0,004.
    h2: Head of surge tank water level with respect to the level of penstock (H2).  Unit = km.  Typical value = 0,040.
    hn: Rated hydraulic head (Hn).  Unit = km.  Typical value = 0,250.
    kc: Penstock loss coefficient (due to friction) (Kc).  Typical value = 0,025.
    kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical value = 0,025.
    kt: Washout gain (Kt).  Typical value = 0,25.
    qc0: No-load turbine flow at nominal head (Qc0).  Typical value = 0,1.
    qn: Rated flow (Qn). Unit = m3/s. Typical value = 250.
    ta: Derivative gain (Ta) (>= 0).  Typical value = 3.
    td: Washout time constant (Td) (>= 0).  Typical value = 6.
    ts: Gate servo time constant (Ts) (>= 0).  Typical value = 0,5.
    twnc: Water inertia time constant (Twnc) (>= 0).  Typical value = 1.
    twng: Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.
    tx: Derivative feedback gain (Tx) (>= 0).  Typical value = 1.
    va: Maximum gate opening velocity (Va).  Unit = PU / s.  Typical value = 0,06.
    valvmax: Maximum gate opening (ValvMax) (> GovHydroFrancis.valvmin).  Typical value = 1,1.
    valvmin: Minimum gate opening (ValvMin) (< GovHydroFrancis.valvmax).  Typical value = 0.
    vc: Maximum gate closing velocity (Vc).  Unit = PU / s.  Typical value = -0,06.
    waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel
      and surge chamber simulation false = inhibit of water tunnel and surge
      chamber simulation. Typical value = false.
    zsfc: Head of upper water level with respect to the level of penstock (Zsfc). Unit = km.  Typical value = 0,025.
    """

    am: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    av0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    av1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    bp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    db1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    etamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    governorControl: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    h1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    h2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    hn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kg: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qc0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ts: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    twnc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    twng: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tx: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    va: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    valvmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    valvmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    waterTunnelSurgeChamberSimulation: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    zsfc: float = Field(
        default=0.0,
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
