# resmgr_common.h

**概述**

提供接口所需要的枚举类型和结构体。

引用文件： <resourcemanager/resmgr_common.h>

库： libohresmgr.so

系统能力： SystemCapability.Global.ResourceManager

起始版本： 12

相关模块： [resourcemanager](resourcemanager.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ResourceManager_Configuration | ResourceManager_Configuration | 设备状态的枚举。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ResourceManager_ErrorCode | - | 资源管理错误码。 |
| ScreenDensity | - | 屏幕密度类型的枚举。 |
| ResourceManager_Direction | ResourceManager_Direction | 屏幕方向的枚举。 |
| ResourceManager_ColorMode | ResourceManager_ColorMode | 颜色模式的枚举。 |
| ResourceManager_DeviceType | ResourceManager_DeviceType | 设备类型的枚举。 |

**枚举类型说明**

**ResourceManager_ErrorCode**

```ets
enum ResourceManager_ErrorCode
```

描述

资源管理错误码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| SUCCESS = 0 | 成功。 |
| ERROR_CODE_INVALID_INPUT_PARAMETER = 401 | 输入参数无效。 |
| ERROR_CODE_RES_ID_NOT_FOUND = 9001001 | 无效的资源ID。 |
| ERROR_CODE_RES_NOT_FOUND_BY_ID = 9001002 | 无效的资源名称。 |
| ERROR_CODE_RES_NAME_NOT_FOUND = 9001003 | 没有根据资源ID找到匹配的资源。 |
| ERROR_CODE_RES_NOT_FOUND_BY_NAME = 9001004 | 没有根据资源名称找到匹配的资源。 |
| ERROR_CODE_RES_PATH_INVALID = 9001005 | 无效的相对路径。 |
| ERROR_CODE_RES_REF_TOO_MUCH = 9001006 | 资源被循环引用。 |
| ERROR_CODE_RES_ID_FORMAT_ERROR = 9001007 | 无法格式化基于资源ID获得的资源。 |
| ERROR_CODE_RES_NAME_FORMAT_ERROR = 9001008 | 无法格式化基于资源名称获得的资源。 |
| ERROR_CODE_SYSTEM_RES_MANAGER_GET_FAILED = 9001009 | 访问系统资源失败。 |
| ERROR_CODE_OVERLAY_RES_PATH_INVALID = 9001010 | 无效的overlay路径。 |
| ERROR_CODE_OUT_OF_MEMORY = 9001100 | 内存溢出。 |

**ScreenDensity**

```ets
enum ScreenDensity
```

描述

屏幕密度类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| SCREEN_SDPI = 120 | 表示小屏幕密度。 |
| SCREEN_MDPI = 160 | 表示中屏幕密度。 |
| SCREEN_LDPI = 240 | 表示大屏幕密度。 |
| SCREEN_XLDPI = 320 | 表示特大屏幕密度。 |
| SCREEN_XXLDPI = 480 | 表示超大屏幕密度。 |
| SCREEN_XXXLDPI = 640 | 表示超特大屏幕密度。 |

**ResourceManager_Direction**

```ets
enum ResourceManager_Direction
```

描述

屏幕方向的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DIRECTION_VERTICAL = 0 | 表示垂直方向。 |
| DIRECTION_HORIZONTAL = 1 | 表示水平方向。 |

**ResourceManager_ColorMode**

```ets
enum ResourceManager_ColorMode
```

描述

颜色模式的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| COLOR_MODE_DARK = 0 | 表示深色模式。 |
| COLOR_MODE_LIGHT = 1 | 表示浅色模式。 |

**ResourceManager_DeviceType**

```ets
enum ResourceManager_DeviceType
```

描述

设备类型的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DEVICE_TYPE_PHONE = 0X00 | 手机。 |
| DEVICE_TYPE_TABLET = 0x01 | 平板。 |
| DEVICE_TYPE_CAR = 0x02 | 汽车。 |
| DEVICE_TYPE_PC = 0x03 | 电脑。 |
| DEVICE_TYPE_TV = 0x04 | 电视。 |
| DEVICE_TYPE_WEARABLE = 0x06 | 穿戴。 |
| DEVICE_TYPE_2IN1 = 0x07 | 2in1设备。 |