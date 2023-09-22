"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LoadDynamics(IdentifiedObject, ModuleType):
    """
    Load whose behaviour is described by reference to a standard model or by definition of a user-defined model. A
      standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to
      multiple energy consumers by means of a single load definition.  The load model is always applied to
      individual bus loads (energy consumers).

    EnergyConsumer: Energy consumer to which this dynamics load model applies.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return LoadDynamics(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # EnergyConsumer : list = Field(default_factory=list, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import LoadDynamics"
# work as well as
# "from LoadDynamics import LoadDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = LoadDynamics
