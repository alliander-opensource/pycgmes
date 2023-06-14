"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LoadDynamics(IdentifiedObject):
    """
    Load whose behaviour is described by reference to a standard model or by definition of a user-defined model. A
      standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to
      multiple energy consumers by means of a single load definition.  The load model is always applied to
      individual bus loads (energy consumers).

    EnergyConsumer: Energy consumer to which this dynamics load model applies.
    """

    # *Association not used*
    # EnergyConsumer : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadDynamics"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "EnergyConsumer": [
                Profile.DY.value,
            ],
        }
