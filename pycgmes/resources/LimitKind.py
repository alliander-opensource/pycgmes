"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class LimitKind(str, Enum):
    """
    Limit kinds.  # noqa: E501
    """

    patl = "patl"  # The Permanent Admissible Transmission Loading (PATL) is the loading in amperes, MVA or MW that can be accepted by a network branch for an unlimited duration without any risk for the material. The OperationnalLimitType.isInfiniteDuration is set to true. There shall be only one OperationalLimitType of kind PATL per OperationalLimitSet if the PATL is ApparentPowerLimit, ActivePowerLimit, or CurrentLimit for a given Terminal or Equipment.  # noqa: E501
    patlt = "patlt"  # Permanent Admissible Transmission Loading Threshold  (PATLT) is a value in engineering units defined for PATL and calculated using a percentage less than 100 % of the PATL type intended to alert operators of an arising condition. The percentage should be given in the name of the OperationalLimitSet. The aceptableDuration is another way to express the severity of the limit.  # noqa: E501
    tatl = "tatl"  # Temporarily Admissible Transmission Loading (TATL) which is the loading in amperes, MVA or MW that can be accepted by a branch for a certain limited duration. The TATL can be defined in different ways: &lt;ul&gt; 	&lt;li&gt;as a fixed percentage of the PATL for a given time (for example, 115% of the PATL that can be accepted during 15 minutes),&lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; 	&lt;li&gt;pairs of TATL type and Duration calculated for each line taking into account its particular configuration and conditions of functioning (for example, it can define a TATL acceptable during 20 minutes and another one acceptable during 10 minutes).&lt;/li&gt; &lt;/ul&gt; Such a definition of TATL can depend on the initial operating conditions of the network element (sag situation of a line). The duration attribute can be used to define several TATL limit types. Hence multiple TATL limit values may exist having different durations.  # noqa: E501
    tc = "tc"  # Tripping Current (TC) is the ultimate intensity without any delay. It is defined as the threshold the line will trip without any possible remedial actions. The tripping of the network element is ordered by protections against short circuits or by overload protections, but in any case, the activation delay of these protections is not compatible with the reaction delay of an operator (less than one minute). The duration is always zero if the OperationalLimitType.acceptableDuration is exchanged. Only one limit value exists for the TC type.  # noqa: E501
    tct = "tct"  # Tripping Current Threshold  (TCT) is a value in engineering units defined for TC and calculated using a percentage less than 100 % of the TC type intended to alert operators of an arising condition. The percentage should be given in the name of the OperationalLimitSet. The aceptableDuration is another way to express the severity of the limit.  # noqa: E501
    highVoltage = "highVoltage"  # Referring to the rating of the equipments, a voltage too high can lead to accelerated ageing or the destruction of the equipment.  This limit type may or may not have duration.  # noqa: E501
    lowVoltage = "lowVoltage"  # A too low voltage can disturb the normal operation of some protections and transformer equipped with on-load tap changers, electronic power devices or can affect the behaviour of the auxiliaries of generation units. This limit type may or may not have duration.  # noqa: E501
    operationalVoltageLimit = "operationalVoltageLimit"  # Operational voltage limit.  # noqa: E501
    alarmVoltage = "alarmVoltage"  # Voltage alarm.  # noqa: E501
    warningVoltage = "warningVoltage"  # Voltage warning.  # noqa: E501
    stability = "stability"  # Stability.  # noqa: E501
