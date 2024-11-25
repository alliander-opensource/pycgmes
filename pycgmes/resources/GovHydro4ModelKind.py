"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class GovHydro4ModelKind(str, Enum):
    """
    Possible types of GovHydro4 models.  # noqa: E501
    """

    simple = "simple"  # Simple model.  # noqa: E501
    francisPelton = "francisPelton"  # Francis or Pelton model.  # noqa: E501
    kaplan = "kaplan"  # Kaplan model.  # noqa: E501
