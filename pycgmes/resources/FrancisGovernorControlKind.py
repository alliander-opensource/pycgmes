"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class FrancisGovernorControlKind(str, Enum):
    """
    Governor control flag for Francis hydro model.
    """

    mechanicHydrolicTachoAccelerator = "mechanicHydrolicTachoAccelerator"  # Mechanic-hydraulic regulator with tacho-accelerometer (Cflag = 1).  # noqa: E501, E741, RUF003
    mechanicHydraulicTransientFeedback = "mechanicHydraulicTransientFeedback"  # Mechanic-hydraulic regulator with transient feedback (Cflag=2).  # noqa: E501, E741, RUF003
    electromechanicalElectrohydraulic = "electromechanicalElectrohydraulic"  # Electromechanical and electrohydraulic regulator (Cflag=3).  # noqa: E501, E741, RUF003
