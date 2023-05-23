"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class TapChangerTablePoint(Base):
    """
    Describes each tap step in the tabular curve.

    b: The magnetizing branch susceptance deviation as a percentage of nominal value. The actual susceptance is
      calculated as follows: calculated magnetizing susceptance = b(nominal) * (1 + b(from this class)/100).
      The b(nominal) is defined as the static magnetizing susceptance on the associated power transformer end or
      ends.  This model assumes the star impedance (pi model) form.
    g: The magnetizing branch conductance deviation as a percentage of nominal value. The actual conductance is
      calculated as follows: calculated magnetizing conductance = g(nominal) * (1 + g(from this class)/100).
      The g(nominal) is defined as the static magnetizing conductance on the associated power transformer end or
      ends.  This model assumes the star impedance (pi model) form.
    r: The resistance deviation as a percentage of nominal value. The actual reactance is calculated as follows:
      calculated resistance = r(nominal) * (1 + r(from this class)/100).   The r(nominal) is defined as the
      static resistance on the associated power transformer end or ends.  This model assumes the star impedance
      (pi model) form.
    ratio: The voltage at the tap step divided by rated voltage of the transformer end having the tap changer. Hence
      this is a value close to one. For example, if the ratio at step 1 is 1.01, and the rated voltage of the
      transformer end is 110kV, then the voltage obtained by setting the tap changer to step 1 to is 111.1kV.
    step: The tap step.
    x: The series reactance deviation as a percentage of nominal value. The actual reactance is calculated as follows:
      calculated reactance = x(nominal) * (1 + x(from this class)/100).   The x(nominal) is defined as the static
      series reactance on the associated power transformer end or ends.  This model assumes the star impedance
      (pi model) form.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    b: float = 0.0  # Type #PerCent in CIM
    g: float = 0.0  # Type #PerCent in CIM
    r: float = 0.0  # Type #PerCent in CIM
    ratio: float = 0.0  # Type #Float in CIM
    step: int = 0  # Type #Integer in CIM
    x: float = 0.0  # Type #PerCent in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=TapChangerTablePoint\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "b": [
                self.profiles.EQ.value,
            ],
            "g": [
                self.profiles.EQ.value,
            ],
            "r": [
                self.profiles.EQ.value,
            ],
            "ratio": [
                self.profiles.EQ.value,
            ],
            "step": [
                self.profiles.EQ.value,
            ],
            "x": [
                self.profiles.EQ.value,
            ],
        }
