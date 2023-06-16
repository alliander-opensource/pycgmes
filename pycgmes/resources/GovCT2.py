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
class GovCT2(TurbineGovernorDynamics):
    """
    General governor with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1 model in
      order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R).  Typical value = 0,05.
    rselect: Feedback signal for droop (Rselect).  Typical value = electricalPower.
    tpelec: Electrical power transducer time constant (Tpelec) (>= 0).  Typical value = 2,5.
    maxerr: Maximum value for speed error signal (Maxerr) (> GovCT2.minerr).  Typical value = 1.
    minerr: Minimum value for speed error signal (Minerr) (< GovCT2.maxerr).  Typical value = -1.
    kpgov: Governor proportional gain (Kpgov).  Typical value = 4.
    kigov: Governor integral gain (Kigov).  Typical value = 0,45.
    kdgov: Governor derivative gain (Kdgov).  Typical value = 0.
    tdgov: Governor derivative controller time constant (Tdgov) (>= 0).  Typical value = 1.
    vmax: Maximum valve position limit (Vmax) (> GovCT2.vmin).  Typical value = 1.
    vmin: Minimum valve position limit (Vmin) (< GovCT2.vmax).  Typical value = 0,175.
    tact: Actuator time constant (Tact) (>= 0).  Typical value = 0,4.
    kturb: Turbine gain (Kturb).  Typical value = 1,9168.
    wfnl: No load fuel flow (Wfnl).  Typical value = 0,187.
    tb: Turbine lag time constant (Tb) (>= 0).  Typical value = 0,1.
    tc: Turbine lead time constant (Tc) (>= 0).  Typical value = 0.
    wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be
      proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and
      diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow
      independent of engine speed. Typical value = false.
    teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but
      measurable transport delay between a change in fuel flow setting and the development of torque (Teng)
      (>= 0).  Teng should be zero in all but special cases where this transport delay is of particular
      concern.  Typical value = 0.
    tfload: Load limiter time constant (Tfload) (>= 0).  Typical value = 3.
    kpload: Load limiter proportional gain for PI controller (Kpload).  Typical value = 1.
    kiload: Load limiter integral gain for PI controller (Kiload).  Typical value = 1.
    ldref: Load limiter reference value (Ldref).  Typical value = 1.
    dm: Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft
      speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the
      falling slope of the engine speed verses power characteristic as speed increases. A slightly falling
      characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative
      the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is
      taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to
      exhaust temperature limits.  Typical value = 0.
    ropen: Maximum valve opening rate (Ropen).  Unit = PU / s.  Typical value = 99.
    rclose: Minimum valve closing rate (Rclose).  Unit = PU / s.  Typical value = -99.
    kimw: Power controller (reset) gain (Kimw).  The default value of 0,01 corresponds to a reset time of 100 seconds.
      A value of 0,001 corresponds to a relatively slow-acting load controller.  Typical value = 0.
    aset: Acceleration limiter setpoint (Aset).  Unit = PU / s.  Typical value = 10.
    ka: Acceleration limiter gain (Ka).  Typical value = 10.
    ta: Acceleration limiter time constant (Ta) (>= 0).  Typical value = 1.
    db: Speed governor deadband in PU speed (db).  In the majority of applications, it is recommended that this value be
      set to zero.  Typical value = 0.
    tsa: Temperature detection lead time constant (Tsa) (>= 0).  Typical value = 0.
    tsb: Temperature detection lag time constant (Tsb) (>= 0).  Typical value = 50.
    rup: Maximum rate of load limit increase (Rup).  Typical value = 99.
    rdown: Maximum rate of load limit decrease (Rdown).  Typical value = -99.
    prate: Ramp rate for frequency-dependent power limit (Prate).  Typical value = 0,017.
    flim1: Frequency threshold 1 (Flim1).  Unit = Hz.  Typical value = 59.
    plim1: Power limit 1 (Plim1).  Typical value = 0,8325.
    flim2: Frequency threshold 2 (Flim2).  Unit = Hz.  Typical value = 0.
    plim2: Power limit 2 (Plim2).  Typical value = 0.
    flim3: Frequency threshold 3 (Flim3).  Unit = Hz.  Typical value = 0.
    plim3: Power limit 3 (Plim3).  Typical value = 0.
    flim4: Frequency threshold 4 (Flim4).  Unit = Hz.  Typical value = 0.
    plim4: Power limit 4 (Plim4).  Typical value = 0.
    flim5: Frequency threshold 5 (Flim5).  Unit = Hz.  Typical value = 0.
    plim5: Power limit 5 (Plim5).  Typical value = 0.
    flim6: Frequency threshold 6 (Flim6).  Unit = Hz.  Typical value = 0.
    plim6: Power limit 6 (Plim6).  Typical value = 0.
    flim7: Frequency threshold 7 (Flim7).  Unit = Hz.  Typical value = 0.
    plim7: Power limit 7 (Plim7).  Typical value = 0.
    flim8: Frequency threshold 8 (Flim8).  Unit = Hz.  Typical value = 0.
    plim8: Power limit 8 (Plim8).  Typical value = 0.
    flim9: Frequency threshold 9 (Flim9).  Unit = Hz.  Typical value = 0.
    plim9: Power Limit 9 (Plim9).  Typical value = 0.
    flim10: Frequency threshold 10 (Flim10).  Unit = Hz.  Typical value = 0.
    plim10: Power limit 10 (Plim10).  Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    r: float = 0.0  # Type #PU in CIM
    rselect: Optional[str] = None  # Type M:1..1 in CIM
    tpelec: int = 0  # Type #Seconds in CIM
    maxerr: float = 0.0  # Type #PU in CIM
    minerr: float = 0.0  # Type #PU in CIM
    kpgov: float = 0.0  # Type #PU in CIM
    kigov: float = 0.0  # Type #PU in CIM
    kdgov: float = 0.0  # Type #PU in CIM
    tdgov: int = 0  # Type #Seconds in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    tact: int = 0  # Type #Seconds in CIM
    kturb: float = 0.0  # Type #PU in CIM
    wfnl: float = 0.0  # Type #PU in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    wfspd: bool = False  # Type #Boolean in CIM
    teng: int = 0  # Type #Seconds in CIM
    tfload: int = 0  # Type #Seconds in CIM
    kpload: float = 0.0  # Type #PU in CIM
    kiload: float = 0.0  # Type #PU in CIM
    ldref: float = 0.0  # Type #PU in CIM
    dm: float = 0.0  # Type #PU in CIM
    ropen: float = 0.0  # Type #Float in CIM
    rclose: float = 0.0  # Type #Float in CIM
    kimw: float = 0.0  # Type #PU in CIM
    aset: float = 0.0  # Type #Float in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    db: float = 0.0  # Type #PU in CIM
    tsa: int = 0  # Type #Seconds in CIM
    tsb: int = 0  # Type #Seconds in CIM
    rup: float = 0.0  # Type #PU in CIM
    rdown: float = 0.0  # Type #PU in CIM
    prate: float = 0.0  # Type #PU in CIM
    flim1: float = 0.0  # Type #Frequency in CIM
    plim1: float = 0.0  # Type #PU in CIM
    flim2: float = 0.0  # Type #Frequency in CIM
    plim2: float = 0.0  # Type #PU in CIM
    flim3: float = 0.0  # Type #Frequency in CIM
    plim3: float = 0.0  # Type #PU in CIM
    flim4: float = 0.0  # Type #Frequency in CIM
    plim4: float = 0.0  # Type #PU in CIM
    flim5: float = 0.0  # Type #Frequency in CIM
    plim5: float = 0.0  # Type #PU in CIM
    flim6: float = 0.0  # Type #Frequency in CIM
    plim6: float = 0.0  # Type #PU in CIM
    flim7: float = 0.0  # Type #Frequency in CIM
    plim7: float = 0.0  # Type #PU in CIM
    flim8: float = 0.0  # Type #Frequency in CIM
    plim8: float = 0.0  # Type #PU in CIM
    flim9: float = 0.0  # Type #Frequency in CIM
    plim9: float = 0.0  # Type #PU in CIM
    flim10: float = 0.0  # Type #Frequency in CIM
    plim10: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovCT2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mwbase": [
                Profile.DY.value,
            ],
            "r": [
                Profile.DY.value,
            ],
            "rselect": [
                Profile.DY.value,
            ],
            "tpelec": [
                Profile.DY.value,
            ],
            "maxerr": [
                Profile.DY.value,
            ],
            "minerr": [
                Profile.DY.value,
            ],
            "kpgov": [
                Profile.DY.value,
            ],
            "kigov": [
                Profile.DY.value,
            ],
            "kdgov": [
                Profile.DY.value,
            ],
            "tdgov": [
                Profile.DY.value,
            ],
            "vmax": [
                Profile.DY.value,
            ],
            "vmin": [
                Profile.DY.value,
            ],
            "tact": [
                Profile.DY.value,
            ],
            "kturb": [
                Profile.DY.value,
            ],
            "wfnl": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "wfspd": [
                Profile.DY.value,
            ],
            "teng": [
                Profile.DY.value,
            ],
            "tfload": [
                Profile.DY.value,
            ],
            "kpload": [
                Profile.DY.value,
            ],
            "kiload": [
                Profile.DY.value,
            ],
            "ldref": [
                Profile.DY.value,
            ],
            "dm": [
                Profile.DY.value,
            ],
            "ropen": [
                Profile.DY.value,
            ],
            "rclose": [
                Profile.DY.value,
            ],
            "kimw": [
                Profile.DY.value,
            ],
            "aset": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "db": [
                Profile.DY.value,
            ],
            "tsa": [
                Profile.DY.value,
            ],
            "tsb": [
                Profile.DY.value,
            ],
            "rup": [
                Profile.DY.value,
            ],
            "rdown": [
                Profile.DY.value,
            ],
            "prate": [
                Profile.DY.value,
            ],
            "flim1": [
                Profile.DY.value,
            ],
            "plim1": [
                Profile.DY.value,
            ],
            "flim2": [
                Profile.DY.value,
            ],
            "plim2": [
                Profile.DY.value,
            ],
            "flim3": [
                Profile.DY.value,
            ],
            "plim3": [
                Profile.DY.value,
            ],
            "flim4": [
                Profile.DY.value,
            ],
            "plim4": [
                Profile.DY.value,
            ],
            "flim5": [
                Profile.DY.value,
            ],
            "plim5": [
                Profile.DY.value,
            ],
            "flim6": [
                Profile.DY.value,
            ],
            "plim6": [
                Profile.DY.value,
            ],
            "flim7": [
                Profile.DY.value,
            ],
            "plim7": [
                Profile.DY.value,
            ],
            "flim8": [
                Profile.DY.value,
            ],
            "plim8": [
                Profile.DY.value,
            ],
            "flim9": [
                Profile.DY.value,
            ],
            "plim9": [
                Profile.DY.value,
            ],
            "flim10": [
                Profile.DY.value,
            ],
            "plim10": [
                Profile.DY.value,
            ],
        }
