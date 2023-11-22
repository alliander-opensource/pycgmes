# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydroPelton(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and
      surge chamber. The DetailedHydroModelHydraulicSystem diagram, located under the GovHydroFrancis class,
      provides a schematic of the hydraulic system of detailed hydro unit models, such as Francis and Pelton.

    av0: Area of the surge tank (AV0). Unit = m2. Typical value = 30.
    av1: Area of the compensation tank (AV1). Unit = m2. Typical value = 700.
    bp: Droop (bp).  Typical value = 0,05.
    db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical value = 0.
    db2: Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical value = 0,01.
    h1: Head of compensation chamber water level with respect to the level of penstock (H1).  Unit = km.  Typical value
      = 0,004.
    h2: Head of surge tank water level with respect to the level of penstock (H2).  Unit = km.  Typical value = 0,040.
    hn: Rated hydraulic head (Hn).  Unit = km.  Typical value = 0,250.
    kc: Penstock loss coefficient (due to friction) (Kc).  Typical value = 0,025.
    kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical value = 0,025.
    qc0: No-load turbine flow at nominal head (Qc0).  Typical value = 0,05.
    qn: Rated flow (Qn). Unit = m3/s. Typical value = 250.
    simplifiedPelton: Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation
      false = enable of complete Pelton model simulation (non-linear gain). Typical value = true.
    staticCompensating: Static compensating characteristic (Cflag). It should be true if simplifiedPelton = false. true
      = enable of static compensating characteristic  false = inhibit of static compensating
      characteristic. Typical value = false.
    ta: Derivative gain (accelerometer time constant) (Ta) (>= 0).  Typical value = 3.
    ts: Gate servo time constant (Ts) (>= 0).  Typical value = 0,15.
    tv: Servomotor integrator time constant (Tv) (>= 0).  Typical value = 0,3.
    twnc: Water inertia time constant (Twnc) (>= 0).  Typical value = 1.
    twng: Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3.
    tx: Electronic integrator time constant (Tx) (>= 0).  Typical value = 0,5.
    va: Maximum gate opening velocity (Va).  Unit = PU / s.  Typical value = 0,06.
    valvmax: Maximum gate opening (ValvMax) (> GovHydroPelton.valvmin).  Typical value = 1,1.
    valvmin: Minimum gate opening (ValvMin) (< GovHydroPelton.valvmax).  Typical value = 0.
    vav: Maximum servomotor valve opening velocity (Vav).  Typical value = 0,1.
    vc: Maximum gate closing velocity (Vc).  Unit = PU / s.  Typical value = -0,06.
    vcv: Maximum servomotor valve closing velocity (Vcv).  Typical value = -0,1.
    waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel
      and surge chamber simulation false = inhibit of water tunnel and surge
      chamber simulation. Typical value = false.
    zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = km.  Typical value = 0,025.
    """

    av0: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    av1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    bp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    db1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    db2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    h1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    h2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    hn: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kg: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    qc0: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    qn: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    simplifiedPelton: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    staticCompensating: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ta: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ts: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tv: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twnc: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twng: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tx: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    va: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    valvmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    valvmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vav: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vcv: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    waterTunnelSurgeChamberSimulation: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    zsfc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
