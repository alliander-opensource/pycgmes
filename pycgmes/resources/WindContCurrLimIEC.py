"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContCurrLimIEC(IdentifiedObject):
    """
    Current limitation model.  The current limitation model combines the physical limits and the control limits.
      Reference: IEC 61400-27-1:2015, 5.6.5.8.

    imax: Maximum continuous current at the wind turbine terminals (imax). It is a type-dependent parameter.
    imaxdip: Maximum current during voltage dip at the wind turbine terminals (imaxdip). It is a project-dependent
      parameter.
    kpqu: Partial derivative of reactive current limit (Kpqu) versus voltage. It is a type-dependent parameter.
    mdfslim: Limitation of type 3 stator current (MDFSLim). MDFSLim = 1 for wind turbines type 4. It is a type-dependent
      parameter. false= total current limitation (0 in the IEC model) true=stator current limitation (1 in
      the IEC model).
    mqpri: Prioritisation of Q control during UVRT (Mqpri). It is a project-dependent parameter. true = reactive power
      priority (1 in the IEC model) false = active power priority (0 in the IEC model).
    tufiltcl: Voltage measurement filter time constant (Tufiltcl) (>= 0). It is a type-dependent parameter.
    upqumax: Wind turbine voltage in the operation point where zero reactive current can be delivered (upqumax). It is a
      type-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this wind control current limitation model is
      associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this current control limitation model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    imax: float = 0.0  # Type #PU in CIM
    imaxdip: float = 0.0  # Type #PU in CIM
    kpqu: float = 0.0  # Type #PU in CIM
    mdfslim: bool = False  # Type #Boolean in CIM
    mqpri: bool = False  # Type #Boolean in CIM
    tufiltcl: int = 0  # Type #Seconds in CIM
    upqumax: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # WindDynamicsLookupTable : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContCurrLimIEC\n"
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
            "imax": [
                self.profiles.DY.value,
            ],
            "imaxdip": [
                self.profiles.DY.value,
            ],
            "kpqu": [
                self.profiles.DY.value,
            ],
            "mdfslim": [
                self.profiles.DY.value,
            ],
            "mqpri": [
                self.profiles.DY.value,
            ],
            "tufiltcl": [
                self.profiles.DY.value,
            ],
            "upqumax": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                self.profiles.DY.value,
            ],
            "WindDynamicsLookupTable": [
                self.profiles.DY.value,
            ],
        }
