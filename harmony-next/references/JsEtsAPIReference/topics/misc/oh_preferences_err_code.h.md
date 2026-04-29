# oh_preferences_err_code.h

**概述**

声明首选项模块统一使用的错误码信息。

引用文件： <database/preferences/oh_preferences_err_code.h>

库： libohpreferences.so

系统能力： SystemCapability.DistributedDataManager.Preferences.Core

起始版本： 13

相关模块： [Preferences](Preferences.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Preferences_ErrCode | OH_Preferences_ErrCode | 错误码信息。 |

**枚举类型说明**

**OH_Preferences_ErrCode**

```ets
enum OH_Preferences_ErrCode
```

描述

错误码信息。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| PREFERENCES_OK = 0 | 操作执行成功。 |
| PREFERENCES_ERROR_INVALID_PARAM = 401 | 参数不合法。 |
| PREFERENCES_ERROR_NOT_SUPPORTED = 801 | 系统能力不支持。 |
| PREFERENCES_ERROR_BASE = 15500000 | 基准错误码。 |
| PREFERENCES_ERROR_DELETE_FILE = 15500010 | 删除文件失败。 |
| PREFERENCES_ERROR_STORAGE = 15500011 | 存储异常。 |
| PREFERENCES_ERROR_MALLOC = 15500012 | 申请内存失败。 |
| PREFERENCES_ERROR_KEY_NOT_FOUND = 15500013 | Key不存在。 |
| PREFERENCES_ERROR_GET_DATAOBSMGRCLIENT = 15500019 | 获取数据变更订阅服务失败。 |