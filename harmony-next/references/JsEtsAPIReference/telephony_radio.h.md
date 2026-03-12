# telephony_radio.h

#### 概述

为网络搜索模块定义C接口。

**库：** libtelephony_radio.so

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 13

**相关模块：**[Telephony](Telephony.md)

#### 汇总

#### 函数

名称描述[Telephony_RadioResult OH_Telephony_GetNetworkState(Telephony_NetworkState *state)](#ZH-CN_TOPIC_0000002529285487__oh_telephony_getnetworkstate)获取网络状态。[Telephony_RadioResult OH_Telephony_GetNetworkStateForSlot(int32_t slotId, Telephony_NetworkState *state)](#ZH-CN_TOPIC_0000002529285487__oh_telephony_getnetworkstateforslot)获取给定卡槽ID的网络状态。

#### 函数说明

#### OH_Telephony_GetNetworkState()

```ets
Telephony_RadioResult OH_Telephony_GetNetworkState(Telephony_NetworkState *state)
```

**描述**

获取网络状态。

**系统能力：** SystemCapability.Telephony.CoreService

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 13

**参数：**

参数项描述[Telephony_NetworkState](Telephony_NetworkState.md) *state用户接收网络状态信息的结构体。

**返回：**

类型说明[Telephony_RadioResult](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult)

结果定义在 [Telephony_RadioResult](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult)。

[TEL_RADIO_SUCCESS](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 成功。

[TEL_RADIO_PERMISSION_DENIED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 权限错误。

[TEL_RADIO_ERR_MARSHALLING_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 编组错误。

[TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 连接电话服务错误。

[TEL_RADIO_ERR_OPERATION_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 操作电话服务错误。

[TEL_RADIO_ERR_INVALID_PARAM](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 参数错误。

#### OH_Telephony_GetNetworkStateForSlot()

```ets
Telephony_RadioResult OH_Telephony_GetNetworkStateForSlot(int32_t slotId, Telephony_NetworkState *state)
```

**描述**

获取给定卡槽ID的网络状态。

**系统能力：** SystemCapability.Telephony.CoreService

**需要权限：** ohos.permission.GET_NETWORK_INFO

**起始版本：** 13

**参数：**

参数项描述int32_t slotId卡槽ID。[Telephony_NetworkState](Telephony_NetworkState.md) *state用户接收网络状态信息的结构体。

**返回：**

类型说明[Telephony_RadioResult](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult)

结果定义在 [Telephony_RadioResult](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult)。

[TEL_RADIO_SUCCESS](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 成功。

[TEL_RADIO_PERMISSION_DENIED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 权限错误。

[TEL_RADIO_ERR_MARSHALLING_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 编组错误。

[TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 连接电话服务错误。

[TEL_RADIO_ERR_OPERATION_FAILED](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 操作电话服务错误。

[TEL_RADIO_ERR_INVALID_PARAM](telephony_radio_type.h.md#ZH-CN_TOPIC_0000002529445461__telephony_radioresult) 参数错误。