# telephony_radio.h

**概述**

为网络搜索模块定义C接口。

引用文件： <telephony/core_service/telephony_radio.h>

库： libtelephony_radio.so

系统能力： SystemCapability.Telephony.CoreService

起始版本： 13

相关模块： [Telephony](Telephony.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| Telephony_RadioResult OH_Telephony_GetNetworkState(Telephony_NetworkState *state) | 获取网络状态。 |
| Telephony_RadioResult OH_Telephony_GetNetworkStateForSlot(int32_t slotId, Telephony_NetworkState *state) | 获取给定卡槽ID的网络状态。 |

**函数说明**

**OH_Telephony_GetNetworkState()**

```ets
Telephony_RadioResult OH_Telephony_GetNetworkState(Telephony_NetworkState *state)
```

描述

获取网络状态。

系统能力： SystemCapability.Telephony.CoreService

需要权限： ohos.permission.GET_NETWORK_INFO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| Telephony_NetworkState *state | 用户接收网络状态信息的结构体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Telephony_RadioResult | 结果定义在 Telephony_RadioResult。  TEL_RADIO_SUCCESS 成功。  TEL_RADIO_PERMISSION_DENIED 权限错误。  TEL_RADIO_ERR_MARSHALLING_FAILED 编组错误。  TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED 连接电话服务错误。  TEL_RADIO_ERR_OPERATION_FAILED 操作电话服务错误。  TEL_RADIO_ERR_INVALID_PARAM 参数错误。 |

**OH_Telephony_GetNetworkStateForSlot()**

```ets
Telephony_RadioResult OH_Telephony_GetNetworkStateForSlot(int32_t slotId, Telephony_NetworkState *state)
```

描述

获取给定卡槽ID的网络状态。

系统能力： SystemCapability.Telephony.CoreService

需要权限： ohos.permission.GET_NETWORK_INFO

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t slotId | 卡槽ID。 |
| Telephony_NetworkState *state | 用户接收网络状态信息的结构体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Telephony_RadioResult | 结果定义在 Telephony_RadioResult。  TEL_RADIO_SUCCESS 成功。  TEL_RADIO_PERMISSION_DENIED 权限错误。  TEL_RADIO_ERR_MARSHALLING_FAILED 编组错误。  TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED 连接电话服务错误。  TEL_RADIO_ERR_OPERATION_FAILED 操作电话服务错误。  TEL_RADIO_ERR_INVALID_PARAM 参数错误。 |