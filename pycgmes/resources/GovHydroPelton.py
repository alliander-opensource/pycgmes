"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydroPelton(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and
      surge chamber. The DetailedHydroModelHydraulicSystem diagram, located under the GovHydroFrancis class,
      provides a schematic of the hydraulic system of detailed hydro unit models, such as Francis and Pelton.

    av0: Area of the surge tank (AV0). Unit = m2. Typical value = 30.
    av1: Area of the compensation tank (AV1). Unit = m2. Typical value = 700.
    bp: Droop (bp).  Typical value = 0,05.
    db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical value = 0.
    db2: Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical value = 0,01.
    h1: Head of compensation chamber water level with respect to the level of penstock (H1).  Unit = km.  Typical value
      = 0,004.
    h2: Head of surge tank water level with respect to the level of penstock (H2).  Unit = km.  Typical value = 0,040.
    hn: Rated hydraulic head (Hn).  Unit = km.  Typical value = 0,250.
    kc: Penstock loss coefficient (due to friction) (Kc).  Typical value = 0,025.
    kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical value = 0,025.
    qc0: No-load turbine flow at nominal head (Qc0).  Typical value = 0,05.
    qn: Rated flow (Qn). Unit = m3/s. Typical value = 250.
    simplifiedPelton: Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation
      false = enable of complete Pelton model simulation (non-linear gain). Typical value = true.
    staticCompensating: Static compensating characteristic (Cflag). It should be true if simplifiedPelton = false. true
      = enable of static compensating characteristic  false = inhibit of static compensating
      characteristic. Typical value = false.
    ta: Derivative gain (accelerometer time constant) (Ta) (>= 0).  Typical value = 3.
    ts: Gate servo time constant (Ts) (>= 0).  Typical value = 0,15.
    tv: Servomotor integrator time constant (Tv) (>= 0).  Typical value = 0,3.
    twnc: Water inertia time constant (Twnc) (>= 0).  Typical value = 1.
    twng: Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.
    tx: Electronic integrator time constant (Tx) (>= 0).  Typical value = 0,5.
    va: Maximum gate opening velocity (Va).  Unit = PU / s.  Typical value = 0,06.
    valvmax: Maximum gate opening (ValvMax) (> GovHydroPelton.valvmin).  Typical value = 1,1.
    valvmin: Minimum gate opening (ValvMin) (< GovHydroPelton.valvmax).  Typical value = 0.
    vav: Maximum servomotor valve opening velocity (Vav).  Typical value = 0,1.
    vc: Maximum gate closing velocity (Vc).  Unit = PU / s.  Typical value = -0,06.
    vcv: Maximum servomotor valve closing velocity (Vcv).  Typical value = -0,1.
    waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel
      and surge chamber simulation false = inhibit of water tunnel and surge
      chamber simulation. Typical value = false.
    zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = km.  Typical value = 0,025.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    av0: float = 0.0  # Type #Area in CIM
    av1: float = 0.0  # Type #Area in CIM
    bp: float = 0.0  # Type #PU in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    db2: float = 0.0  # Type #Frequency in CIM
    h1: float = 0.0  # Type #Length in CIM
    h2: float = 0.0  # Type #Length in CIM
    hn: float = 0.0  # Type #Length in CIM
    kc: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    qc0: float = 0.0  # Type #PU in CIM
    qn: float = 0.0  # Type #VolumeFlowRate in CIM
    simplifiedPelton: bool = False  # Type #Boolean in CIM
    staticCompensating: bool = False  # Type #Boolean in CIM
    ta: int = 0  # Type #Seconds in CIM
    ts: int = 0  # Type #Seconds in CIM
    tv: int = 0  # Type #Seconds in CIM
    twnc: int = 0  # Type #Seconds in CIM
    twng: int = 0  # Type #Seconds in CIM
    tx: int = 0  # Type #Seconds in CIM
    va: float = 0.0  # Type #Float in CIM
    valvmax: float = 0.0  # Type #PU in CIM
    valvmin: float = 0.0  # Type #PU in CIM
    vav: float = 0.0  # Type #PU in CIM
    vc: float = 0.0  # Type #Float in CIM
    vcv: float = 0.0  # Type #PU in CIM
    waterTunnelSurgeChamberSimulation: bool = False  # Type #Boolean in CIM
    zsfc: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovHydroPelton\n"
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
            "av0": [
                self.profiles.DY.value,
            ],
            "av1": [
                self.profiles.DY.value,
            ],
            "bp": [
                self.profiles.DY.value,
            ],
            "db1": [
                self.profiles.DY.value,
            ],
            "db2": [
                self.profiles.DY.value,
            ],
            "h1": [
                self.profiles.DY.value,
            ],
            "h2": [
                self.profiles.DY.value,
            ],
            "hn": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "kg": [
                self.profiles.DY.value,
            ],
            "qc0": [
                self.profiles.DY.value,
            ],
            "qn": [
                self.profiles.DY.value,
            ],
            "simplifiedPelton": [
                self.profiles.DY.value,
            ],
            "staticCompensating": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "ts": [
                self.profiles.DY.value,
            ],
            "tv": [
                self.profiles.DY.value,
            ],
            "twnc": [
                self.profiles.DY.value,
            ],
            "twng": [
                self.profiles.DY.value,
            ],
            "tx": [
                self.profiles.DY.value,
            ],
            "va": [
                self.profiles.DY.value,
            ],
            "valvmax": [
                self.profiles.DY.value,
            ],
            "valvmin": [
                self.profiles.DY.value,
            ],
            "vav": [
                self.profiles.DY.value,
            ],
            "vc": [
                self.profiles.DY.value,
            ],
            "vcv": [
                self.profiles.DY.value,
            ],
            "waterTunnelSurgeChamberSimulation": [
                self.profiles.DY.value,
            ],
            "zsfc": [
                self.profiles.DY.value,
            ],
        }
