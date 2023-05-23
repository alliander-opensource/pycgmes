"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ACDCConverter import ACDCConverter


@dataclass
class CsConverter(ACDCConverter):
    """
    DC side of the current source converter (CSC). The firing angle controls the dc voltage at the converter, both for
      rectifier and inverter. The difference between the dc voltages of the rectifier and inverter determines the dc
      current. The extinction angle is used to limit the dc voltage at the inverter, if needed, and is not used in
      active power control. The firing angle, transformer tap position and number of connected filters are the
      primary means to control a current source dc line. Higher level controls are built on top, e.g. dc voltage, dc
      current and active power. From a steady state perspective it is sufficient to specify the wanted active power
      transfer (ACDCConverter.targetPpcc) and the control functions will set the dc voltage, dc current, firing
      angle, transformer tap position and number of connected filters to meet this. Therefore attributes targetAlpha
      and targetGamma are not applicable in this case. The reactive power consumed by the converter is a function of
      the firing angle, transformer tap position and number of connected filter, which can be approximated with half
      of the active power. The losses is a function of the dc voltage and dc current. The attributes minAlpha and
      maxAlpha define the range of firing angles for rectifier operation between which no discrete tap changer
      action takes place. The range is typically 10-18 degrees. The attributes minGamma and maxGamma define the
      range of extinction angles for inverter operation between which no discrete tap changer action takes place.
      The range is typically 17-20 degrees.

    maxAlpha: Maximum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a
      positive value.
    maxGamma: Maximum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be
      a positive value.
    maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. It is converter`s
      configuration data use in power flow. The attribute shall be a positive value.
    minAlpha: Minimum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a
      positive value.
    minGamma: Minimum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be
      a positive value.
    minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. It is converter`s
      configuration data used in power flow. The attribute shall be a positive value.
    ratedIdc: Rated converter DC current, also called IdN. The attribute shall be a positive value. It is converter`s
      configuration data used in power flow.
    alpha: Firing angle that determines the dc voltage at the converter dc terminal. Typical value between 10 degrees
      and 18 degrees for a rectifier. It is converter`s state variable, result from power flow. The attribute
      shall be a positive value.
    gamma: Extinction angle. It is used to limit the dc voltage at the inverter if needed. Typical value between 17
      degrees and 20 degrees for an inverter. It is converter`s state variable, result from power flow. The
      attribute shall be a positive value.
    operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. It is converter`s
      control variable used in power flow.
    pPccControl: Kind of active power control.
    targetAlpha: Target firing angle. It is converter`s control variable used in power flow. It is only applicable for
      rectifier if continuous tap changer control is used. Allowed values are within the range
      minAlpha<=targetAlpha<=maxAlpha. The attribute shall be a positive value.
    targetGamma: Target extinction angle. It is converter`s control variable used in power flow. It is only applicable
      for inverter if continuous tap changer control is used. Allowed values are within the range
      minGamma<=targetGamma<=maxGamma. The attribute shall be a positive value.
    targetIdc: DC current target value. It is converter`s control variable used in power flow. The attribute shall be a
      positive value.
    CSCDynamics: Current source converter dynamics model used to describe dynamic behaviour of this converter.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    maxAlpha: float = 0.0  # Type #AngleDegrees in CIM
    maxGamma: float = 0.0  # Type #AngleDegrees in CIM
    maxIdc: float = 0.0  # Type #CurrentFlow in CIM
    minAlpha: float = 0.0  # Type #AngleDegrees in CIM
    minGamma: float = 0.0  # Type #AngleDegrees in CIM
    minIdc: float = 0.0  # Type #CurrentFlow in CIM
    ratedIdc: float = 0.0  # Type #CurrentFlow in CIM
    alpha: float = 0.0  # Type #AngleDegrees in CIM
    gamma: float = 0.0  # Type #AngleDegrees in CIM
    operatingMode: Optional[str] = None  # Type M:1..1 in CIM
    pPccControl: Optional[str] = None  # Type M:1..1 in CIM
    targetAlpha: float = 0.0  # Type #AngleDegrees in CIM
    targetGamma: float = 0.0  # Type #AngleDegrees in CIM
    targetIdc: float = 0.0  # Type #CurrentFlow in CIM
    # *Association not used*
    # CSCDynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=CsConverter\n"
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
                self.profiles.SV.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "maxAlpha": [
                self.profiles.EQ.value,
            ],
            "maxGamma": [
                self.profiles.EQ.value,
            ],
            "maxIdc": [
                self.profiles.EQ.value,
            ],
            "minAlpha": [
                self.profiles.EQ.value,
            ],
            "minGamma": [
                self.profiles.EQ.value,
            ],
            "minIdc": [
                self.profiles.EQ.value,
            ],
            "ratedIdc": [
                self.profiles.EQ.value,
            ],
            "alpha": [
                self.profiles.SV.value,
            ],
            "gamma": [
                self.profiles.SV.value,
            ],
            "operatingMode": [
                self.profiles.SSH.value,
            ],
            "pPccControl": [
                self.profiles.SSH.value,
            ],
            "targetAlpha": [
                self.profiles.SSH.value,
            ],
            "targetGamma": [
                self.profiles.SSH.value,
            ],
            "targetIdc": [
                self.profiles.SSH.value,
            ],
            "CSCDynamics": [
                self.profiles.DY.value,
            ],
        }
