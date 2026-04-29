# oh_location.h

**概述**

定义查询位置开关状态、启动定位、停止定位的接口。

引用文件： <LocationKit/oh_location.h>

库： liblocation_ndk.so

系统能力： SystemCapability.Location.Location.Core

起始版本： 13

相关模块： [Location](Location.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| Location_ResultCode OH_Location_IsLocatingEnabled(bool* enabled) | 查询位置开关是否开启。 |
| Location_ResultCode OH_Location_StartLocating(const Location_RequestConfig* requestConfig) | 启动定位并订阅位置变化。 |
| Location_ResultCode OH_Location_StopLocating(const Location_RequestConfig* requestConfig) | 停止定位并取消订阅位置变化。 |

**函数说明**

**OH_Location_IsLocatingEnabled()**

```ets
Location_ResultCode OH_Location_IsLocatingEnabled(bool* enabled)
```

描述

查询位置开关是否开启。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| bool* enabled | bool类型的指针，用于接收位置开关状态值。  等于true表示位置开关开启，false表示位置开关关闭。  需要传入非空指针，否则会返回错误。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Location_ResultCode | 返回操作结果，详细定义参见Location_ResultCode。  LOCATION_SUCCESS 查询位置开关状态成功。  LOCATION_INVALID_PARAM 入参是空指针。  LOCATION_SERVICE_UNAVAILABLE 位置服务运行异常导致查询位置开关状态失败。 |

**OH_Location_StartLocating()**

```ets
Location_ResultCode OH_Location_StartLocating(const Location_RequestConfig* requestConfig)
```

描述

启动定位并订阅位置变化。

需要权限： ohos.permission.APPROXIMATELY_LOCATION

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const Location_RequestConfig* requestConfig | 指向定位请求参数的指针，该参数用于指定发起定位的场景信息和位置上报间隔。  详细定义请参考Location_RequestConfig，可以使用OH_Location_CreateRequestConfig创建。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Location_ResultCode | 返回操作结果，详细定义参见Location_ResultCode。  LOCATION_SUCCESS 启动定位成功。  LOCATION_INVALID_PARAM 入参requestConfig为空指针。  LOCATION_PERMISSION_DENIED 权限校验失败。  LOCATION_NOT_SUPPORTED 当前设备不支持该功能。  LOCATION_SERVICE_UNAVAILABLE 位置服务运行异常。  LOCATION_SWITCH_OFF 位置开关未打开导致无法启动定位。 |

**OH_Location_StopLocating()**

```ets
Location_ResultCode OH_Location_StopLocating(const Location_RequestConfig* requestConfig)
```

描述

停止定位并取消订阅位置变化。

需要权限： ohos.permission.APPROXIMATELY_LOCATION

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const Location_RequestConfig* requestConfig | 指向定位请求参数的指针。  该参数需要与OH_Location_StartLocating中的requestConfig是同一个指针。  详细定义请参考Location_RequestConfig。  需要传入非空指针，否则会返回错误。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Location_ResultCode | 返回操作结果，详细定义参见Location_ResultCode。  LOCATION_SUCCESS 停止定位成功。  LOCATION_INVALID_PARAM 1. 入参为空指针。  2. 入参与OH_Location_StartLocating的requestConfig指针不同。  LOCATION_PERMISSION_DENIED 权限校验失败。  LOCATION_NOT_SUPPORTED 当前设备不支持该功能。  LOCATION_SERVICE_UNAVAILABLE 位置服务运行异常。  LOCATION_SWITCH_OFF 位置开关未打开。 |