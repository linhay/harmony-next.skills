# oh_device_manager_err_code.h

#### 概述

声明设备管理模块错误码信息。

**引用文件：** <distributedhardware/device_manager/oh_device_manager_err_code.h>

**库：** libdevicemanager_ndk.so

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 20

**相关模块：**[DeviceManager](../../topics/system-services/DeviceManager.md)

#### 汇总

#### 枚举

名称typedef关键字描述[DeviceManager_ErrorCode](#ZH-CN_TOPIC_0000002497605444__devicemanager_errorcode)DeviceManager_ErrorCode分布式设备管理错误码信息。

#### 枚举类型说明

#### DeviceManager_ErrorCode

```ets
enum DeviceManager_ErrorCode
```

**描述**

分布式设备管理错误码信息。

**起始版本：** 20

枚举项描述ERR_OK = 0执行成功。ERR_PERMISSION_ERROR = 201权限校验失败。ERR_INVALID_PARAMETER = 401非法参数。DM_ERR_FAILED = 11600101函数执行失败。DM_ERR_OBTAIN_SERVICE = 11600102获取设备管理服务失败。DM_ERR_OBTAIN_BUNDLE_NAME = 11600109获取bundleName失败。