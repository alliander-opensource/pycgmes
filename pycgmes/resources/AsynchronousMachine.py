"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .RotatingMachine import RotatingMachine


@dataclass(config=DataclassConfig)
class AsynchronousMachine(RotatingMachine, ModuleType):
    """
    A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine
      with no external connection to the rotor windings, e.g. squirrel-cage induction machine.

    nominalFrequency: Nameplate data indicates if the machine is 50 Hz or 60 Hz.
    nominalSpeed: Nameplate data.  Depends on the slip and number of pole pairs.
    converterFedDrive: Indicates whether the machine is a converter fed drive. Used for short circuit data exchange
      according to IEC 60909.
    efficiency: Efficiency of the asynchronous machine at nominal operation as a percentage. Indicator for converter
      drive motors. Used for short circuit data exchange according to IEC 60909.
    iaIrRatio: Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data
      exchange according to IEC 60909.
    polePairNumber: Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909.
    ratedMechanicalPower: Rated mechanical power (Pr in IEC 60909-0). Used for short circuit data exchange according to
      IEC 60909.
    reversible: Indicates for converter drive motors if the power can be reversible. Used for short circuit data
      exchange according to IEC 60909.
    rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909.
    asynchronousMachineType: Indicates the type of Asynchronous Machine (motor or generator).
    AsynchronousMachineDynamics: Asynchronous machine dynamics model used to describe dynamic behaviour of this
      asynchronous machine.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AsynchronousMachine(*args, **kwargs)

    nominalFrequency: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    nominalSpeed: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    converterFedDrive: bool = Field(
        default=False,
        in_profiles=[
            Profile.SC,
        ],
    )

    efficiency: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    iaIrRatio: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    polePairNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.SC,
        ],
    )

    ratedMechanicalPower: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    reversible: bool = Field(
        default=False,
        in_profiles=[
            Profile.SC,
        ],
    )

    rxLockedRotorRatio: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    asynchronousMachineType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SSH,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # AsynchronousMachineDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import AsynchronousMachine"
# work as well as
# "from AsynchronousMachine import AsynchronousMachine".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AsynchronousMachine
