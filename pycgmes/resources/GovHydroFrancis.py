"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    am: float = 0.0  # Type #PU in CIM
    av0: float = 0.0  # Type #Area in CIM
    av1: float = 0.0  # Type #Area in CIM
    bp: float = 0.0  # Type #PU in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    etamax: float = 0.0  # Type #PU in CIM
    governorControl: Optional[str] = None  # Type M:1..1 in CIM
    h1: float = 0.0  # Type #Length in CIM
    h2: float = 0.0  # Type #Length in CIM
    hn: float = 0.0  # Type #Length in CIM
    kc: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    kt: float = 0.0  # Type #PU in CIM
    qc0: float = 0.0  # Type #PU in CIM
    qn: float = 0.0  # Type #VolumeFlowRate in CIM
    ta: int = 0  # Type #Seconds in CIM
    td: int = 0  # Type #Seconds in CIM
    ts: int = 0  # Type #Seconds in CIM
    twnc: int = 0  # Type #Seconds in CIM
    twng: int = 0  # Type #Seconds in CIM
    tx: int = 0  # Type #Seconds in CIM
    va: float = 0.0  # Type #Float in CIM
    valvmax: float = 0.0  # Type #PU in CIM
    valvmin: float = 0.0  # Type #PU in CIM
    vc: float = 0.0  # Type #Float in CIM
    waterTunnelSurgeChamberSimulation: bool = False  # Type #Boolean in CIM
    zsfc: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroFrancis"]
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
            "am": [
                Profile.DY.value,
            ],
            "av0": [
                Profile.DY.value,
            ],
            "av1": [
                Profile.DY.value,
            ],
            "bp": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "etamax": [
                Profile.DY.value,
            ],
            "governorControl": [
                Profile.DY.value,
            ],
            "h1": [
                Profile.DY.value,
            ],
            "h2": [
                Profile.DY.value,
            ],
            "hn": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "kt": [
                Profile.DY.value,
            ],
            "qc0": [
                Profile.DY.value,
            ],
            "qn": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
            "ts": [
                Profile.DY.value,
            ],
            "twnc": [
                Profile.DY.value,
            ],
            "twng": [
                Profile.DY.value,
            ],
            "tx": [
                Profile.DY.value,
            ],
            "va": [
                Profile.DY.value,
            ],
            "valvmax": [
                Profile.DY.value,
            ],
            "valvmin": [
                Profile.DY.value,
            ],
            "vc": [
                Profile.DY.value,
            ],
            "waterTunnelSurgeChamberSimulation": [
                Profile.DY.value,
            ],
            "zsfc": [
                Profile.DY.value,
            ],
        }
