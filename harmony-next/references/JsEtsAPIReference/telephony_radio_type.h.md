# telephony_radio_type.h

#### 概述

定义网络搜索模块的C接口需要的数据结构。

**引用文件：** <telephony/core_service/telephony_radio_type.h>

**库：** libtelephony_radio.so

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 13

**相关模块：**[Telephony](Telephony.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Telephony_NetworkState](Telephony_NetworkState.md)Telephony_NetworkState网络状态信息。

#### 枚举

名称typedef关键字描述[Telephony_RadioResult](#ZH-CN_TOPIC_0000002529445461__telephony_radioresult)Telephony_RadioResult错误码类型枚举。[Telephony_RegState](#ZH-CN_TOPIC_0000002529445461__telephony_regstate)Telephony_RegState设备的网络注册状态类型。[Telephony_RadioTechnology](#ZH-CN_TOPIC_0000002529445461__telephony_radiotechnology)Telephony_RadioTechnology设备的无线接入技术类型。[Telephony_NsaState](#ZH-CN_TOPIC_0000002529445461__telephony_nsastate)Telephony_NsaState设备的NSA网络注册状态类型。

#### 枚举类型说明

#### Telephony_RadioResult

```ets
enum Telephony_RadioResult
```

**描述**

错误码类型枚举。

**起始版本：** 13

枚举项描述TEL_RADIO_SUCCESS = 0成功。TEL_RADIO_PERMISSION_DENIED = 201权限错误。TEL_RADIO_ERR_INVALID_PARAM = 401参数错误。TEL_RADIO_ERR_MARSHALLING_FAILED = 8300001编组错误，这是一个低概率错误，请稍后在遇到此错误时重试。TEL_RADIO_ERR_SERVICE_CONNECTION_FAILED = 8300002连接电话服务错误，当出现此错误时，请稍后重试。TEL_RADIO_ERR_OPERATION_FAILED = 8300003操作电话服务错误，当出现此错误时，请稍后重试。

#### Telephony_RegState

```ets
enum Telephony_RegState
```

**描述**

设备的网络注册状态类型。

**起始版本：** 13

枚举项描述TEL_REG_STATE_NO_SERVICE = 0设备不能使用任何服务。TEL_REG_STATE_IN_SERVICE = 1设备可以正常使用服务。TEL_REG_STATE_EMERGENCY_CALL_ONLY = 2设备只能使用紧急呼叫业务。TEL_REG_STATE_POWER_OFF = 3蜂窝无线电已关闭。

#### Telephony_RadioTechnology

```ets
enum Telephony_RadioTechnology
```

**描述**

设备的无线接入技术类型。

**起始版本：** 13

枚举项描述TEL_RADIO_TECHNOLOGY_UNKNOWN = 0未知无线接入技术（RAT）。TEL_RADIO_TECHNOLOGY_GSM = 1无线接入技术GSM（Global System for Mobile Communication）。TEL_RADIO_TECHNOLOGY_1XRTT = 2无线接入技术1XRTT（Single-Carrier Radio Transmission Technology）。TEL_RADIO_TECHNOLOGY_WCDMA = 3无线接入技术WCDMA（Wideband Code Division Multiple Access）。TEL_RADIO_TECHNOLOGY_HSPA = 4无线接入技术HSPA（High Speed Packet Access）。TEL_RADIO_TECHNOLOGY_HSPAP = 5无线接入技术HSPAP（High Speed Packet Access (HSPA+) ）。TEL_RADIO_TECHNOLOGY_TD_SCDMA = 6无线接入技术TDSCDMA（Time Division-Synchronous Code Division Multiple Access）。TEL_RADIO_TECHNOLOGY_EVDO = 7无线接入技术EVDO（Evolution Data Optimized）。TEL_RADIO_TECHNOLOGY_EHRPD = 8无线接入技术EHRPD（Evolved High Rate Package Data）。TEL_RADIO_TECHNOLOGY_LTE = 9无线接入技术LTE（Long Term Evolution）。TEL_RADIO_TECHNOLOGY_LTE_CA = 10无线接入技术LTE_CA（Long Term Evolution_Carrier Aggregation）。TEL_RADIO_TECHNOLOGY_IWLAN = 11无线接入技术IWLAN（Industrial Wireless LAN）。TEL_RADIO_TECHNOLOGY_NR = 12无线接入技术NR（New Radio）。

#### Telephony_NsaState

```ets
enum Telephony_NsaState
```

**描述**

设备的NSA网络注册状态类型。

**起始版本：** 13

枚举项描述TEL_NSA_STATE_NOT_SUPPORTED = 1设备在不支持NSA的LTE小区下处于空闲状态或连接状态。TEL_NSA_STATE_NO_DETECTED = 2在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。TEL_NSA_STATE_CONNECTED_DETECTED = 3设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。TEL_NSA_STATE_IDLE_DETECTED = 4支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。TEL_NSA_STATE_DUAL_CONNECTED = 5设备在支持NSA的LTE小区下连接到LTE + NR网络。TEL_NSA_STATE_SA_ATTACHED = 6设备在5GC附着时在NG-RAN小区下空闲或连接到NG-RAN小区。