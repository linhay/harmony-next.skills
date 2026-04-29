# os_account.h

**概述**

声明访问和管理系统帐号信息的API。

库： libos_account_ndk.so

引用文件： <BasicServicesKit/os_account.h>

系统能力： SystemCapability.Account.OsAccount

起始版本： 12

相关模块： [OsAccount](OsAccount.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OsAccount_ErrCode OH_OsAccount_GetName(char *buffer, size_t buffer_size) | 获取调用方进程所属的系统帐号的名称。 |

**函数说明**

**OH_OsAccount_GetName()**

```ets
OsAccount_ErrCode OH_OsAccount_GetName(char *buffer, size_t buffer_size)
```

描述

获取调用方进程所属的系统帐号的名称。

系统能力： SystemCapability.Account.OsAccount

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char *buffer | 名称字符数组，其应具有能够存放名称（最大长度为LOGIN_NAME_MAX）和结束字符（'\0'）的空间。 |
| size_t buffer_size | 名称字符数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OsAccount_ErrCode | OS_ACCOUNT_ERR_OK：表示成功。 OS_ACCOUNT_ERR_INTERNAL_ERROR：表示内部错误。 OS_ACCOUNT_ERR_INVALID_PARAMETER：表示buffer为NULL指针，或名称（不包括结束字符'\0'）的长度大于等于buffer_size。 |