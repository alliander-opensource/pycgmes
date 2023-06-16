"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TransformerEnd import TransformerEnd


@dataclass(config=DataclassConfig)
class PowerTransformerEnd(TransformerEnd):
    """
    A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0
      of a PowerTransformerEnd represents a star equivalent as follows. 1) for a two Terminal PowerTransformer the
      high voltage (TransformerEnd.endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while
      the low voltage (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0.
      Parameters are always provided, even if the PowerTransformerEnds have the same rated voltage.  In this case,
      the parameters are provided at the PowerTransformerEnd which has TransformerEnd.endNumber equal to 1. 2) for a
      three Terminal PowerTransformer the three PowerTransformerEnds represent a star equivalent with each leg in
      the star represented by r, r0, x, and x0 values. 3) For a three Terminal transformer each PowerTransformerEnd
      shall have g, g0, b and b0 values corresponding to the no load losses distributed on the three
      PowerTransformerEnds. The total no load loss shunt impedances may also be placed at one of the
      PowerTransformerEnds, preferably the end numbered 1, having the shunt values on end 1.  This is the preferred
      way. 4) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot
      be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
      Each PowerTransformerEnd must be contained by a PowerTransformer. Because a PowerTransformerEnd (or any other
      object) can not be contained by more than one parent, a PowerTransformerEnd can not have an association to an
      EquipmentContainer (Substation, VoltageLevel, etc).

    PowerTransformer: The power transformer of this power transformer end.
    b: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    connectionKind: Kind of connection.
    ratedS: Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the
      values for the high and low voltage sides shall be identical.
    g: Magnetizing branch conductance.
    ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-
      phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is
      greater than or equal to ratedU for the lower voltage sides. The attribute shall be a positive value.
    r: Resistance (star-model) of the transformer end. The attribute shall be equal to or greater than zero for non-
      equivalent transformers.
    x: Positive sequence series reactance (star-model) of the transformer end.
    b0: Zero sequence magnetizing branch susceptance.
    phaseAngleClock: Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The
      valid values are 0 to 11. For example, for the secondary side end of a transformer with
      vector group code of `Dyn11`, specify the connection kind as wye with neutral and specify the
      phase angle of the clock as 11.  The clock value of the transformer end number specified as
      1, is assumed to be zero.  Note the transformer end number is not assumed to be the same as
      the terminal sequence number.
    g0: Zero sequence magnetizing branch conductance (star-model).
    r0: Zero sequence series resistance (star-model) of the transformer end.
    x0: Zero sequence series reactance of the transformer end.
    """

    PowerTransformer: Optional[str] = None  # Type M:1..1 in CIM
    b: float = 0.0  # Type #Susceptance in CIM
    connectionKind: Optional[str] = None  # Type M:0..1 in CIM
    ratedS: float = 0.0  # Type #ApparentPower in CIM
    g: float = 0.0  # Type #Conductance in CIM
    ratedU: float = 0.0  # Type #Voltage in CIM
    r: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    b0: float = 0.0  # Type #Susceptance in CIM
    phaseAngleClock: int = 0  # Type #Integer in CIM
    g0: float = 0.0  # Type #Conductance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    x0: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PowerTransformerEnd"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SC.value,
            ],
            # Attributes
            "PowerTransformer": [
                Profile.EQ.value,
            ],
            "b": [
                Profile.EQ.value,
            ],
            "connectionKind": [
                Profile.EQ.value,
            ],
            "ratedS": [
                Profile.EQ.value,
            ],
            "g": [
                Profile.EQ.value,
            ],
            "ratedU": [
                Profile.EQ.value,
            ],
            "r": [
                Profile.EQ.value,
            ],
            "x": [
                Profile.EQ.value,
            ],
            "b0": [
                Profile.SC.value,
            ],
            "phaseAngleClock": [
                Profile.SC.value,
            ],
            "g0": [
                Profile.SC.value,
            ],
            "r0": [
                Profile.SC.value,
            ],
            "x0": [
                Profile.SC.value,
            ],
        }
