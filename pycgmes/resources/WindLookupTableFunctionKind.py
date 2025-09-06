"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindLookupTableFunctionKind(str, Enum):
    """
    Function of the lookup table.
    """

    prr = "prr"  # Power versus speed change (negative slip) lookup table (p<sub>rr</sub>(deltaomega)). It is used for the rotor resistance control model, IEC 61400-27-1:2015, 5.6.5.3.  # noqa: E501
    omegap = "omegap"  # Power vs. speed lookup table (omega(p)). It is used for the P control model type 3, IEC 61400-27-1:2015, 5.6.5.4.  # noqa: E501
    ipmax = "ipmax"  # Lookup table for voltage dependency of active current limits (i<sub>pmax</sub>(u<sub>WT</sub>)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8.  # noqa: E501
    iqmax = "iqmax"  # Lookup table for voltage dependency of reactive current limits (i<sub>qmax</sub>(u<sub>WT</sub>)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8.  # noqa: E501
    pwp = "pwp"  # Power vs. frequency lookup table (p<sub>WPbias</sub>(f)). It is used for the wind power plant frequency and active power control model, IEC 61400-27-1:2015, Annex D.  # noqa: E501
    tcwdu = "tcwdu"  # Crowbar duration versus voltage variation look-up table (T<sub>CW</sub>(du)). It is a case-dependent parameter. It is used for the type 3B generator set model, IEC 61400-27-1:2015, 5.6.3.3.  # noqa: E501
    tduwt = "tduwt"  # Lookup table to determine the duration of the power reduction after a voltage dip, depending on the size of the voltage dip (T<sub>d</sub>(u<sub>WT</sub>)). It is a type-dependent parameter. It is used for the pitch control power model, IEC 61400-27-1:2015, 5.6.5.1.  # noqa: E501
    qmaxp = "qmaxp"  # Lookup table for active power dependency of reactive power maximum limit (q<sub>maxp</sub>(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qminp = "qminp"  # Lookup table for active power dependency of reactive power minimum limit (q<sub>minp</sub>(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qmaxu = "qmaxu"  # Lookup table for voltage dependency of reactive power maximum limit (q<sub>maxu</sub>(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qminu = "qminu"  # Lookup table for voltage dependency of reactive power minimum limit (q<sub>minu</sub>(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    tuover = "tuover"  # Disconnection time versus over-voltage lookup table (T<sub>uover</sub>(u<sub>WT</sub>)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tuunder = "tuunder"  # Disconnection time versus under-voltage lookup table (T<sub>uunder</sub>(u<sub>WT</sub>)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tfover = "tfover"  # Disconnection time versus over-frequency lookup table (T<sub>fover</sub>(f<sub>WT</sub>)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tfunder = "tfunder"  # Disconnection time versus under-frequency lookup table (T<sub>funder</sub>(f<sub>WT</sub>)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    qwp = "qwp"  # Look up table for the UQ static mode (q<sub>WP</sub>(u<sub>err</sub>)). It is used for the voltage and reactive power control model, IEC 61400-27-1:2015, Annex D.  # noqa: E501
