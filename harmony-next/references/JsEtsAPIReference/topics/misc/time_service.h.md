# time_service.h

**概述**

声明获取时间时区信息的API。

库： libtime_service_ndk.so

引用文件： <BasicServicesKit/time_service.h>

系统能力： SystemCapability.MiscServices.Time

起始版本： 12

相关模块： [TimeService](TimeService.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| TimeService_ErrCode | TimeService_ErrCode | 枚举错误码。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| TimeService_ErrCode OH_TimeService_GetTimeZone(char *timeZone, uint32_t len) | 获取当前系统时区。 |

**枚举类型说明**

**TimeService_ErrCode**

```ets
enum TimeService_ErrCode
```

描述

枚举错误码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| TIMESERVICE_ERR_OK = 0 | 成功。 |
| TIMESERVICE_ERR_INTERNAL_ERROR = 13000001 | 获取系统参数失败。 |
| TIMESERVICE_ERR_INVALID_PARAMETER = 13000002 | 无效的参数。 |

**函数说明**

**OH_TimeService_GetTimeZone()**

```ets
TimeService_ErrCode OH_TimeService_GetTimeZone(char *timeZone, uint32_t len)
```

描述

获取当前系统时区。

系统能力： SystemCapability.MiscServices.Time

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char *timeZone | 时区ID字符数组，成功时写入当前系统时区ID字符串，失败时写入空字符串，字符串以'\0'结尾。 |
| uint32_t len | 时区ID字符数组分配的内存大小，当前时区字符串没有最大长度规格，建议申请足够多的内存，至少不能低于31字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| TimeService_ErrCode | 返回TIMESERVICE_ERR_OK表示成功。 返回TIMESERVICE_ERR_INTERNAL_ERROR表示获取系统参数失败。 返回TIMESERVICE_ERR_INVALID_PARAMETER表示timeZone为NULL指针或时区名称（不包括结束字符（'\0'））的大小大于或等于len。 |