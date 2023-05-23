"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass
class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is common to all
      excitation system models described in the IEEE Standard.  Parameter details:  If Rc and Xc are set to zero,
      the load compensation is not employed and the behaviour is as a simple sensing circuit.   If all parameters
      (Rc, Xc and Tr) are set to zero, the standard model VCompIEEEType1 is bypassed.  Reference: IEEE 421.5-2005 4.

    rc: Resistive component of compensation of a generator (Rc) (>= 0).
    xc: Reactive component of compensation of a generator (Xc) (>= 0).
    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    rc: float = 0.0  # Type #PU in CIM
    xc: float = 0.0  # Type #PU in CIM
    tr: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VCompIEEEType1\n"
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
            "rc": [
                self.profiles.DY.value,
            ],
            "xc": [
                self.profiles.DY.value,
            ],
            "tr": [
                self.profiles.DY.value,
            ],
        }
