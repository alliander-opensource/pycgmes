"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindAeroTwoDimIEC(IdentifiedObject):
    """
    Two-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.3.

    dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (dpomega). It is a type-
      dependent parameter.
    dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (dptheta). It is a type-
      dependent parameter.
    dpv1: Partial derivative (dpv1). It is a type-dependent parameter.
    omegazero: Rotor speed if the wind turbine is not derated (omega0). It is a type-dependent parameter.
    pavail: Available aerodynamic power (pavail). It is a case-dependent parameter.
    thetazero: Pitch angle if the wind turbine is not derated (theta0). It is a case-dependent parameter.
    thetav2: Blade angle at twice rated wind speed (thetav2). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    dpomega: float = 0.0  # Type #PU in CIM
    dptheta: float = 0.0  # Type #PU in CIM
    dpv1: float = 0.0  # Type #PU in CIM
    omegazero: float = 0.0  # Type #PU in CIM
    pavail: float = 0.0  # Type #PU in CIM
    thetazero: float = 0.0  # Type #AngleDegrees in CIM
    thetav2: float = 0.0  # Type #AngleDegrees in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindAeroTwoDimIEC\n"
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
            "dpomega": [
                self.profiles.DY.value,
            ],
            "dptheta": [
                self.profiles.DY.value,
            ],
            "dpv1": [
                self.profiles.DY.value,
            ],
            "omegazero": [
                self.profiles.DY.value,
            ],
            "pavail": [
                self.profiles.DY.value,
            ],
            "thetazero": [
                self.profiles.DY.value,
            ],
            "thetav2": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3IEC": [
                self.profiles.DY.value,
            ],
        }
