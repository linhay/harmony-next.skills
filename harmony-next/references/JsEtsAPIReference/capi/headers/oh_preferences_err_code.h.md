# oh_preferences_err_code.h

#### 概述

声明首选项模块统一使用的错误码信息。

**引用文件：** <database/preferences/oh_preferences_err_code.h>

**库：** libohpreferences.so

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 13

**相关模块：**[Preferences](../../topics/misc/Preferences.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Preferences_ErrCode](#ZH-CN_TOPIC_0000002497444720__oh_preferences_errcode)OH_Preferences_ErrCode错误码信息。

#### 枚举类型说明

#### OH_Preferences_ErrCode

```ets
enum OH_Preferences_ErrCode
```

**描述**

错误码信息。

**起始版本：** 13

枚举项描述PREFERENCES_OK = 0操作执行成功。PREFERENCES_ERROR_INVALID_PARAM = 401参数不合法。PREFERENCES_ERROR_NOT_SUPPORTED = 801系统能力不支持。PREFERENCES_ERROR_BASE = 15500000基准错误码。PREFERENCES_ERROR_DELETE_FILE = 15500010删除文件失败。PREFERENCES_ERROR_STORAGE = 15500011存储异常。PREFERENCES_ERROR_MALLOC = 15500012申请内存失败。PREFERENCES_ERROR_KEY_NOT_FOUND = 15500013Key不存在。PREFERENCES_ERROR_GET_DATAOBSMGRCLIENT = 15500019获取数据变更订阅服务失败。