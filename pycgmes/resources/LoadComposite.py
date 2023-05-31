"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .LoadDynamics import LoadDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=LoadComposite\n"
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
            "epvs": [
                self.profiles.DY.value,
            ],
            "epfs": [
                self.profiles.DY.value,
            ],
            "eqvs": [
                self.profiles.DY.value,
            ],
            "eqfs": [
                self.profiles.DY.value,
            ],
            "epvd": [
                self.profiles.DY.value,
            ],
            "epfd": [
                self.profiles.DY.value,
            ],
            "eqvd": [
                self.profiles.DY.value,
            ],
            "eqfd": [
                self.profiles.DY.value,
            ],
            "lfac": [
                self.profiles.DY.value,
            ],
            "h": [
                self.profiles.DY.value,
            ],
            "pfrac": [
                self.profiles.DY.value,
            ],
        }
