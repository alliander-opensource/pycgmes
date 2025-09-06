"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class GenericNonLinearLoadModelKind(str, Enum):
    """
    Type of generic non-linear load model.
    """

    exponentialRecovery = "exponentialRecovery"  # Exponential recovery model.  # noqa: E501
    loadAdaptive = "loadAdaptive"  # Load adaptive model.  # noqa: E501
