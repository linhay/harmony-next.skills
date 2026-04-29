# oh_device_manager.h

**概述**

提供访问可信设备和本地设备信息的接口。

引用文件： <distributedhardware/device_manager/oh_device_manager.h>

库： libdevicemanager_ndk.so

系统能力： SystemCapability.DistributedHardware.DeviceManager

起始版本： 20

相关模块： [DeviceManager](DeviceManager.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len) | 获取本地设备显示名。 设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |

**函数说明**

**OH_DeviceManager_GetLocalDeviceName()**

```ets
int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len)
```

描述

获取本地设备显示名。

设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。

需要权限： ohos.permission.READ_LOCAL_DEVICE_NAME

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| char **localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备 ohos.permission.READ_LOCAL_DEVICE_NAME 权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int &len | 表示本地设备显示名字符串的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的错误码。错误码定义详见DeviceManager_ErrorCode。  返回ERR_OK，表示执行成功。  返回DM_ERR_FAILED，表示函数执行失败。  返回DM_ERR_OBTAIN_SERVICE，表示获取设备管理服务失败。  返回DM_ERR_OBTAIN_BUNDLE_NAME，表示获取bundleName失败。  返回ERR_INVALID_PARAMETER，表示参数localDeviceName是空指针或者*localDeviceName是非空指针。 |

示例：

```ets
#include "napi/native_api.h"
#include "hilog/log.h"
#include <distributedhardware/device_manager/oh_device_manager.h>
#include <distributedhardware/device_manager/oh_device_manager_err_code.h>
static napi_value GetDeviceName(napi_env env, napi_callback_info info) {
    napi_value result = nullptr;
    napi_create_object(env, &result);
    char *localDeviceName = nullptr; // 声明空字符串，不需要提前分配地址，接口内部会分配
    unsigned int len = 0;
    // 将空字符串的地址传给接口
    int32_t ret = OH_DeviceManager_GetLocalDeviceName(&localDeviceName, len);
    if (ret != ERR_OK) {
        OH_LOG_ERROR(LOG_APP, "ret:%{public}d", ret);
    }

    napi_value code = nullptr;
    napi_create_int32(env, ret, &code);
    napi_set_named_property(env, result, "code", code);

    if (ret == ERR_OK && localDeviceName != nullptr) {
        napi_value deviceName = nullptr;
        napi_create_string_utf8(env, localDeviceName, NAPI_AUTO_LENGTH, &deviceName);
        napi_set_named_property(env, result, "deviceName", deviceName);
        delete[] localDeviceName; // 释放内存

        napi_value deviceNameLen = nullptr;
        napi_create_int32(env, len, &deviceNameLen);
        napi_set_named_property(env, result, "deviceNameLen", deviceNameLen);
    }
    return result;
}
```