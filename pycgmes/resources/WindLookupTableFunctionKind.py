"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class WindLookupTableFunctionKind(str, Enum):
    """
    Function of the lookup table.  # noqa: E501
    """

    prr = "prr"  # Power versus speed change (negative slip) lookup table (p&lt;sub&gt;rr&lt;/sub&gt;(deltaomega)). It is used for the rotor resistance control model, IEC 61400-27-1:2015, 5.6.5.3.  # noqa: E501
    omegap = "omegap"  # Power vs. speed lookup table (omega(p)). It is used for the P control model type 3, IEC 61400-27-1:2015, 5.6.5.4.  # noqa: E501
    ipmax = "ipmax"  # Lookup table for voltage dependency of active current limits (i&lt;sub&gt;pmax&lt;/sub&gt;(u&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8.  # noqa: E501
    iqmax = "iqmax"  # Lookup table for voltage dependency of reactive current limits (i&lt;sub&gt;qmax&lt;/sub&gt;(u&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8.  # noqa: E501
    pwp = "pwp"  # Power vs. frequency lookup table (p&lt;sub&gt;WPbias&lt;/sub&gt;(f)). It is used for the wind power plant frequency and active power control model, IEC 61400-27-1:2015, Annex D.  # noqa: E501
    tcwdu = "tcwdu"  # Crowbar duration versus voltage variation look-up table (T&lt;sub&gt;CW&lt;/sub&gt;(du)). It is a case-dependent parameter. It is used for the type 3B generator set model, IEC 61400-27-1:2015, 5.6.3.3.  # noqa: E501
    tduwt = "tduwt"  # Lookup table to determine the duration of the power reduction after a voltage dip, depending on the size of the voltage dip (T&lt;sub&gt;d&lt;/sub&gt;(u&lt;sub&gt;WT&lt;/sub&gt;)). It is a type-dependent parameter. It is used for the pitch control power model, IEC 61400-27-1:2015, 5.6.5.1.  # noqa: E501
    qmaxp = "qmaxp"  # Lookup table for active power dependency of reactive power maximum limit (q&lt;sub&gt;maxp&lt;/sub&gt;(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qminp = "qminp"  # Lookup table for active power dependency of reactive power minimum limit (q&lt;sub&gt;minp&lt;/sub&gt;(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qmaxu = "qmaxu"  # Lookup table for voltage dependency of reactive power maximum limit (q&lt;sub&gt;maxu&lt;/sub&gt;(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    qminu = "qminu"  # Lookup table for voltage dependency of reactive power minimum limit (q&lt;sub&gt;minu&lt;/sub&gt;(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10.  # noqa: E501
    tuover = "tuover"  # Disconnection time versus over-voltage lookup table (T&lt;sub&gt;uover&lt;/sub&gt;(u&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tuunder = "tuunder"  # Disconnection time versus under-voltage lookup table (T&lt;sub&gt;uunder&lt;/sub&gt;(u&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tfover = "tfover"  # Disconnection time versus over-frequency lookup table (T&lt;sub&gt;fover&lt;/sub&gt;(f&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    tfunder = "tfunder"  # Disconnection time versus under-frequency lookup table (T&lt;sub&gt;funder&lt;/sub&gt;(f&lt;sub&gt;WT&lt;/sub&gt;)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6.  # noqa: E501
    qwp = "qwp"  # Look up table for the UQ static mode (q&lt;sub&gt;WP&lt;/sub&gt;(u&lt;sub&gt;err&lt;/sub&gt;)). It is used for the voltage and reactive power control model, IEC 61400-27-1:2015, Annex D.  # noqa: E501
