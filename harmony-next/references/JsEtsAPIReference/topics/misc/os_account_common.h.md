# os_account_common.h

**概述**

提供OsAccount接口的公共类型定义。

库： libos_account_ndk.so

引用文件： <BasicServicesKit/os_account_common.h>

系统能力： SystemCapability.Account.OsAccount

起始版本： 12

相关模块： [OsAccount](OsAccount.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OsAccount_ErrCode | OsAccount_ErrCode | 枚举错误码。 |

**枚举类型说明**

**OsAccount_ErrCode**

```ets
enum OsAccount_ErrCode
```

描述

枚举错误码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OS_ACCOUNT_ERR_OK = 0 | 成功。 |
| OS_ACCOUNT_ERR_INTERNAL_ERROR = 12300001 | 内部错误。 |
| OS_ACCOUNT_ERR_INVALID_PARAMETER = 12300002 | 无效的参数。 |