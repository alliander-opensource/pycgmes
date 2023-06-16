"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadDynamics import LoadDynamics


@dataclass(config=DataclassConfig)
class LoadComposite(LoadDynamics):
    """
    Combined static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the
      induction machine equations.

    epvs: Active load-voltage dependence index (static) (Epvs).  Typical value = 0,7.
    epfs: Active load-frequency dependence index (static) (Epfs).  Typical value = 1,5.
    eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical value = 2.
    eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical value = 0.
    epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical value = 0,7.
    epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical value = 1,5.
    eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical value = 2.
    eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical value = 0.
    lfac: Loading factor (Lfac). The ratio of initial P to motor MVA base.  Typical value = 0,8.
    h: Inertia constant (H) (>= 0).  Typical value = 2,5.
    pfrac: Fraction of constant-power load to be represented by this motor model (PFRAC) (>= 0,0 and <= 1,0).  Typical
      value = 0,5.
    """

    epvs: float = 0.0  # Type #Float in CIM
    epfs: float = 0.0  # Type #Float in CIM
    eqvs: float = 0.0  # Type #Float in CIM
    eqfs: float = 0.0  # Type #Float in CIM
    epvd: float = 0.0  # Type #Float in CIM
    epfd: float = 0.0  # Type #Float in CIM
    eqvd: float = 0.0  # Type #Float in CIM
    eqfd: float = 0.0  # Type #Float in CIM
    lfac: float = 0.0  # Type #Float in CIM
    h: int = 0  # Type #Seconds in CIM
    pfrac: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadComposite"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "epvs": [
                Profile.DY.value,
            ],
            "epfs": [
                Profile.DY.value,
            ],
            "eqvs": [
                Profile.DY.value,
            ],
            "eqfs": [
                Profile.DY.value,
            ],
            "epvd": [
                Profile.DY.value,
            ],
            "epfd": [
                Profile.DY.value,
            ],
            "eqvd": [
                Profile.DY.value,
            ],
            "eqfd": [
                Profile.DY.value,
            ],
            "lfac": [
                Profile.DY.value,
            ],
            "h": [
                Profile.DY.value,
            ],
            "pfrac": [
                Profile.DY.value,
            ],
        }
