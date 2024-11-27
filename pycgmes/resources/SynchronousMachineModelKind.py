"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SynchronousMachineModelKind(str, Enum):
    """
    Type of synchronous machine model used in dynamic simulation applications.
    """

    subtransient = "subtransient"  # Subtransient synchronous machine model.  # noqa: E501, E741, RUF003
    subtransientTypeF = "subtransientTypeF"  # WECC type F variant of subtransient synchronous machine model.  # noqa: E501, E741, RUF003
    subtransientTypeJ = "subtransientTypeJ"  # WECC type J variant of subtransient synchronous machine model.  # noqa: E501, E741, RUF003
    subtransientSimplified = "subtransientSimplified"  # Simplified version of subtransient synchronous machine model where magnetic coupling between the direct- and quadrature- axes is ignored.  # noqa: E501, E741, RUF003
    subtransientSimplifiedDirectAxis = "subtransientSimplifiedDirectAxis"  # Simplified version of a subtransient synchronous machine model with no damper circuit on the direct-axis.  # noqa: E501, E741, RUF003
