"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class VisibilityLayer(IdentifiedObject):
    """
    Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or
      hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information
      depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen
      size). This is also called de-cluttering. CIM based graphics exchange supports an m:n relationship between
      diagram objects and layers. The importing system shall convert an m:n case into an appropriate 1:n
      representation if the importing system does not support m:n.

    VisibleObjects: A visibility layer can contain one or more diagram objects.
    drawingOrder: The drawing order for this layer.  The higher the number, the later the layer and the objects within
      it are rendered.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    VisibleObjects: list = field(default_factory=list)  # Type M:1..n in CIM
    drawingOrder: int = 0  # Type #Integer in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VisibilityLayer\n"
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
                self.profiles.DL.value,
            ],
            # Attributes
            "VisibleObjects": [
                self.profiles.DL.value,
            ],
            "drawingOrder": [
                self.profiles.DL.value,
            ],
        }
