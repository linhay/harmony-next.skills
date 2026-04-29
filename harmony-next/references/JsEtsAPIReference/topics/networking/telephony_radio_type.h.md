# telephony_radio_type.h

**概述**

定义网络搜索模块的C接口需要的数据结构。

引用文件： <telephony/core_service/telephony_radio_type.h>

库： libtelephony_radio.so

系统能力： SystemCapability.Telephony.CoreService

起始版本： 13

相关模块： [Telephony](Telephony.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Telephony_NetworkState | Telephony_NetworkState | 网络状态信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Telephony_RadioResult | Telephony_RadioResult | 错误码类型枚举。 |
| Telephony_RegState | Telephony_RegState | 设备的网络注册状态类型。 |
| Telephony_RadioTechnology | Telephony_RadioTechnology | 设备的无线接入技术类型。 |
| Telephony_NsaState | Telephony_NsaState | 设备的NSA网络注册状态类型。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| TELEPHONY_MAX_OPERATOR_LEN 64 | 定义运营商名称的最大长度。 起始版本： 13 |
| TELEPHONY_MAX_PLMN_NUMERIC_LEN 6 | 定义PLMN的最大长度。 起始版本： 13 |

**枚举类型说明**

**Telephony_RadioResult**

```ets
enum Telephony_RadioResult
```

描述

错误码类型枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| TEL_RADIO_SUCCESS = 0 | 成功。 |
| TEL_RADIO_PERMISSION_DENIED = 201 | 权限错误。 |
| TEL_RADIO_ERR_INVALID_PARAM = 401 | 参数错误。 |
| TEL_RADIO_ERR_MARSHALLING_FAILED = 8300001 | 编组错误，这是一个低概率错误，请稍后在遇到此错误时重试。 |
| TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED = 8300002 | 连接电话服务错误，当出现此错误时，请稍后重试。 |
| TEL_RADIO_ERR_OPERATION_FAILED = 8300003 | 操作电话服务错误，当出现此错误时，请稍后重试。 |

**Telephony_RegState**

```ets
enum Telephony_RegState
```

描述

设备的网络注册状态类型。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| TEL_REG_STATE_NO_SERVICE = 0 | 设备不能使用任何服务。 |
| TEL_REG_STATE_IN_SERVICE = 1 | 设备可以正常使用服务。 |
| TEL_REG_STATE_EMERGENCY_CALL_ONLY = 2 | 设备只能使用紧急呼叫业务。 |
| TEL_REG_STATE_POWER_OFF = 3 | 蜂窝无线电已关闭。 |

**Telephony_RadioTechnology**

```ets
enum Telephony_RadioTechnology
```

描述

设备的无线接入技术类型。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| TEL_RADIO_TECHNOLOGY_UNKNOWN = 0 | 未知无线接入技术（RAT）。 |
| TEL_RADIO_TECHNOLOGY_GSM = 1 | 无线接入技术GSM（Global System for Mobile Communication）。 |
| TEL_RADIO_TECHNOLOGY_1XRTT = 2 | 无线接入技术1XRTT（Single-Carrier Radio Transmission Technology）。 |
| TEL_RADIO_TECHNOLOGY_WCDMA = 3 | 无线接入技术WCDMA（Wideband Code Division Multiple Access）。 |
| TEL_RADIO_TECHNOLOGY_HSPA = 4 | 无线接入技术HSPA（High Speed Packet Access）。 |
| TEL_RADIO_TECHNOLOGY_HSPAP = 5 | 无线接入技术HSPAP（High Speed Packet Access (HSPA+) ）。 |
| TEL_RADIO_TECHNOLOGY_TD_SCDMA = 6 | 无线接入技术TDSCDMA（Time Division-Synchronous Code Division Multiple Access）。 |
| TEL_RADIO_TECHNOLOGY_EVDO = 7 | 无线接入技术EVDO（Evolution Data Optimized）。 |
| TEL_RADIO_TECHNOLOGY_EHRPD = 8 | 无线接入技术EHRPD（Evolved High Rate Package Data）。 |
| TEL_RADIO_TECHNOLOGY_LTE = 9 | 无线接入技术LTE（Long Term Evolution）。 |
| TEL_RADIO_TECHNOLOGY_LTE_CA = 10 | 无线接入技术LTE_CA（Long Term Evolution_Carrier Aggregation）。 |
| TEL_RADIO_TECHNOLOGY_IWLAN = 11 | 无线接入技术IWLAN（Industrial Wireless LAN）。 |
| TEL_RADIO_TECHNOLOGY_NR = 12 | 无线接入技术NR（New Radio）。 |

**Telephony_NsaState**

```ets
enum Telephony_NsaState
```

描述

设备的NSA网络注册状态类型。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| TEL_NSA_STATE_NOT_SUPPORTED = 1 | 设备在不支持NSA的LTE小区下处于空闲状态或连接状态。 |
| TEL_NSA_STATE_NO_DETECTED = 2 | 在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。 |
| TEL_NSA_STATE_CONNECTED_DETECTED = 3 | 设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。 |
| TEL_NSA_STATE_IDLE_DETECTED = 4 | 支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。 |
| TEL_NSA_STATE_DUAL_CONNECTED = 5 | 设备在支持NSA的LTE小区下连接到LTE + NR网络。 |
| TEL_NSA_STATE_SA_ATTACHED = 6 | 设备在5GC附着时在NG-RAN小区下空闲或连接到NG-RAN小区。 |