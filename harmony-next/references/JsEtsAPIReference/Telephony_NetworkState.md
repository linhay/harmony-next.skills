# Telephony_NetworkState

```ets
typedef struct {...} Telephony_NetworkState
```

#### 概述

网络状态信息。

**起始版本：** 13

**相关模块：**[Telephony](Telephony.md)

**所在头文件：**[telephony_radio_type.h](telephony_radio_type.h.md)

#### 汇总

#### 成员变量

名称描述char longOperatorName_[TELEPHONY_MAX_OPERATOR_LEN]注册网络的长运营商名称。char shortOperatorName_[TELEPHONY_MAX_OPERATOR_LEN]注册网络的短运营商名称。char plmnNumeric_[TELEPHONY_MAX_PLMN_NUMERIC_LEN]注册网络的PLMN码。bool isRoaming_是否处于漫游状态。Telephony_RegState regState_设备的网络注册状态。Telephony_RadioTechnology cfgTech_设备的无线接入技术。Telephony_NsaState nsaState_设备的NSA网络注册状态。bool isCaActive_CA的状态。bool isEmergency_此设备是否只允许拨打紧急呼叫。