# oh_wifi.h

#### 概述

定义查询WIFI开关状态的接口。

**引用文件：** <ConnectivityKit/wifi/oh_wifi.h>

**库：** libwifi_ndk.so

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 13

**相关模块：**[Wifi](Wifi.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Wifi_ResultCode](#ZH-CN_TOPIC_0000002497605430__wifi_resultcode)Wifi_ResultCode定义WIFI接口返回值的错误码。

#### 函数

名称描述[Wifi_ResultCode OH_Wifi_IsWifiEnabled(bool *enabled)](#ZH-CN_TOPIC_0000002497605430__oh_wifi_iswifienabled)查询WIFI开关是否开启。[Wifi_ResultCode OH_Wifi_GetDeviceMacAddress(char *macAddr, unsigned int *macAddrLen)](#ZH-CN_TOPIC_0000002497605430__oh_wifi_getdevicemacaddress)该接口用于获取设备真实Mac地址。

#### 枚举类型说明

#### Wifi_ResultCode

```ets
enum Wifi_ResultCode
```

**描述**

定义WIFI接口返回值的错误码。

**起始版本：** 13

枚举项描述WIFI_SUCCESS = 0操作成功。WIFI_PERMISSION_DENIED = 201权限校验失败。WIFI_INVALID_PARAM = 401

参数错误。

 可能原因：1.输入参数为空指针；2.参数数值超出定义范围。

WIFI_NOT_SUPPORTED = 801该功能不支持。由于设备能力有限，无法调用该函数。WIFI_OPERATION_FAILED = 2501000

操作失败。

 可能原因：服务内部执行失败。

WIFI_STA_DISABLED = 2501001

STA服务未拉起。

 可能原因：WiFi未打开。

#### 函数说明

#### OH_Wifi_IsWifiEnabled()

```ets
Wifi_ResultCode OH_Wifi_IsWifiEnabled(bool *enabled)
```

**描述**

查询WIFI开关是否开启。

**起始版本：** 13

**参数：**

参数项描述bool *enabled

- bool类型的指针，用于接收WIFI开关状态值。

 等于true表示WIFI开关开启，false表示WIFI开关关闭。

 需要传入非空指针，否则会返回错误。

**返回：**

类型说明[Wifi_ResultCode](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode)

返回操作结果，详细定义参见[Wifi_ResultCode](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode).

[WIFI_SUCCESS](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 查询WIFI开关状态成功。

[WIFI_INVALID_PARAM](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 入参为空指针。

[WIFI_OPERATION_FAILED](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 服务内部执行错误。

#### OH_Wifi_GetDeviceMacAddress()

```ets
Wifi_ResultCode OH_Wifi_GetDeviceMacAddress(char *macAddr, unsigned int *macAddrLen)
```

**描述**

该接口用于获取设备真实Mac地址。

**需要权限：** ohos.permission.GET_WIFI_LOCAL_MAC 和 ohos.permission.GET_WIFI_INFO

**起始版本：** 21

**参数：**

参数项描述char *macAddr设备Mac地址的字符数组，以'\0'结尾。unsigned int *macAddrLen为macAddr字符数组分配的内存大小。

**返回：**

类型说明[Wifi_ResultCode](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode)

返回操作结果，详细定义参见[Wifi_ResultCode](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode)。

[WIFI_SUCCESS](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 成功获取设备Mac地址。

[WIFI_PERMISSION_DENIED](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 权限拒绝。

[WIFI_NOT_SUPPORTED](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 不支持该能力。

[WIFI_INVALID_PARAM](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 输入参数macAddr是空指针。

[WIFI_OPERATION_FAILED](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) 内部执行失败。

[WIFI_STA_DISABLED](oh_wifi.h.md#ZH-CN_TOPIC_0000002497605430__wifi_resultcode) Wi-Fi STA模式未启用。