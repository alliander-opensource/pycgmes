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
class LoadMotor(IdentifiedObject):
    """
    Aggregate induction motor load. This model is used to represent a fraction of an ordinary load as "induction motor
      load".  It allows a load that is treated as an ordinary constant power in power flow analysis to be
      represented by an induction motor in dynamic simulation. This model is intended for representation of
      aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no
      information on the characteristics of individual motors. Either a "one-cage" or "two-cage" model of the
      induction machine can be modelled. Magnetic saturation is not modelled. This model treats a fraction of the
      constant power part of a load as a motor. During initialisation, the initial power drawn by the motor is set
      equal to Pfrac times the constant P part of the static load.  The remainder of the load is left as a static
      load. The reactive power demand of the motor is calculated during initialisation as a function of voltage at
      the load bus. This reactive power demand can be less than or greater than the constant Q component of the
      load.  If the motor's reactive demand is greater than the constant Q component of the load, the model inserts
      a shunt capacitor at the terminal of the motor to bring its reactive demand down to equal the constant Q
      reactive load.   If an induction motor load model and a static load model are both present for a load, the
      motor Pfrac is assumed to be subtracted from the power flow constant P load before the static load model is
      applied.  The remainder of the load, if any, is then represented by the static load model.

    LoadAggregate: Aggregate load to which this aggregate motor (dynamic) load belongs.
    pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>= 0,0 and <= 1,0).  Typical
      value = 0,3.
    lfac: Loading factor (Lfac). The ratio of initial P to motor MVA base.  Typical value = 0,8.
    ls: Synchronous reactance (Ls).  Typical value = 3,2.
    lp: Transient reactance (Lp).  Typical value = 0,15.
    lpp: Subtransient reactance (Lpp).  Typical value = 0,15.
    ra: Stator resistance (Ra).  Typical value = 0.
    tpo: Transient rotor time constant (Tpo) (>= 0).  Typical value = 1.
    tppo: Subtransient rotor time constant (Tppo) (>= 0).  Typical value = 0,02.
    h: Inertia constant (H) (>= 0).  Typical value = 0,4.
    d: Damping factor (D).  Unit = delta P/delta speed.  Typical value = 2.
    vt: Voltage threshold for tripping (Vt).  Typical value = 0,7.
    tv: Voltage trip pickup time (Tv) (>= 0).  Typical value = 0,1.
    tbkr: Circuit breaker operating time (Tbkr) (>= 0).  Typical value = 0,08.
    """

    LoadAggregate: Optional[str] = None  # Type M:1 in CIM
    pfrac: float = 0.0  # Type #Float in CIM
    lfac: float = 0.0  # Type #Float in CIM
    ls: float = 0.0  # Type #PU in CIM
    lp: float = 0.0  # Type #PU in CIM
    lpp: float = 0.0  # Type #PU in CIM
    ra: float = 0.0  # Type #PU in CIM
    tpo: int = 0  # Type #Seconds in CIM
    tppo: int = 0  # Type #Seconds in CIM
    h: int = 0  # Type #Seconds in CIM
    d: float = 0.0  # Type #Float in CIM
    vt: float = 0.0  # Type #PU in CIM
    tv: int = 0  # Type #Seconds in CIM
    tbkr: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadMotor"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "LoadAggregate": [
                Profile.DY.value,
            ],
            "pfrac": [
                Profile.DY.value,
            ],
            "lfac": [
                Profile.DY.value,
            ],
            "ls": [
                Profile.DY.value,
            ],
            "lp": [
                Profile.DY.value,
            ],
            "lpp": [
                Profile.DY.value,
            ],
            "ra": [
                Profile.DY.value,
            ],
            "tpo": [
                Profile.DY.value,
            ],
            "tppo": [
                Profile.DY.value,
            ],
            "h": [
                Profile.DY.value,
            ],
            "d": [
                Profile.DY.value,
            ],
            "vt": [
                Profile.DY.value,
            ],
            "tv": [
                Profile.DY.value,
            ],
            "tbkr": [
                Profile.DY.value,
            ],
        }
