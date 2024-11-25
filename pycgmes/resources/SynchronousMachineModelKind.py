"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class SynchronousMachineModelKind(str, Enum):
    """
    Type of synchronous machine model used in dynamic simulation applications.  # noqa: E501
    """

    subtransient = "subtransient"  # Subtransient synchronous machine model.  # noqa: E501
    subtransientTypeF = "subtransientTypeF"  # WECC type F variant of subtransient synchronous machine model.  # noqa: E501
    subtransientTypeJ = "subtransientTypeJ"  # WECC type J variant of subtransient synchronous machine model.  # noqa: E501
    subtransientSimplified = "subtransientSimplified"  # Simplified version of subtransient synchronous machine model where magnetic coupling between the direct- and quadrature- axes is ignored.  # noqa: E501
    subtransientSimplifiedDirectAxis = "subtransientSimplifiedDirectAxis"  # Simplified version of a subtransient synchronous machine model with no damper circuit on the direct-axis.  # noqa: E501
