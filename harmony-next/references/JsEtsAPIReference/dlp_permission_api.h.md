# dlp_permission_api.h

#### 概述

声明用于跨设备的文件的权限管理、加密存储、授权访问等能力的接口。

**库：** libohdlp_permission.so

**引用文件：** <DataProtectionKit/dlp_permission_api.h>

**系统能力：** SystemCapability.Security.DataLossPrevention

**起始版本：** 14

**相关模块：**[DlpPermissionApi](DlpPermissionApi.md)

#### 汇总

#### 枚举

名称typedef关键字描述[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)DLP_ErrCodeDLP错误码的枚举。[DLP_FileAccess](#ZH-CN_TOPIC_0000002529285371__dlp_fileaccess)DLP_FileAccessDLP文件授权类型的枚举。

#### 函数

名称描述[DLP_ErrCode OH_DLP_GetDlpPermissionInfo(DLP_FileAccess *dlpFileAccess, uint32_t *flags)](#ZH-CN_TOPIC_0000002529285371__oh_dlp_getdlppermissioninfo)查询当前DLP沙箱的权限信息。[DLP_ErrCode OH_DLP_GetOriginalFileName(const char *fileName, char **originalFileName)](#ZH-CN_TOPIC_0000002529285371__oh_dlp_getoriginalfilename)获取指定DLP文件名的原始文件名。[DLP_ErrCode OH_DLP_IsInSandbox(bool *isInSandbox)](#ZH-CN_TOPIC_0000002529285371__oh_dlp_isinsandbox)查询当前应用是否运行在DLP沙箱环境。[DLP_ErrCode OH_DLP_SetSandboxAppConfig(const char *configInfo)](#ZH-CN_TOPIC_0000002529285371__oh_dlp_setsandboxappconfig)设置沙箱应用配置信息。[DLP_ErrCode OH_DLP_GetSandboxAppConfig(char **configInfo)](#ZH-CN_TOPIC_0000002529285371__oh_dlp_getsandboxappconfig)获取沙箱应用配置信息。[DLP_ErrCode OH_DLP_CleanSandboxAppConfig()](#ZH-CN_TOPIC_0000002529285371__oh_dlp_cleansandboxappconfig)清理沙箱应用配置信息。

#### 枚举类型说明

#### DLP_ErrCode

```ets
enum DLP_ErrCode
```

**描述**

DLP错误码的枚举。

**起始版本：** 14

枚举项描述ERR_OH_SUCCESS = 0表示操作成功。ERR_OH_INVALID_PARAMETER = 19100001表示入参错误。ERR_OH_API_ONLY_FOR_SANDBOX = 19100006表示非DLP沙箱应用。ERR_OH_API_NOT_FOR_SANDBOX = 19100007表示DLP沙箱应用不允许调用此接口。ERR_OH_SYSTEM_SERVICE_EXCEPTION = 19100011表示系统服务工作异常。ERR_OH_OUT_OF_MEMORY = 19100012表示内存申请失败。ERR_OH_APPLICATION_NOT_AUTHORIZED = 19100018表示应用未授权。

#### DLP_FileAccess

```ets
enum DLP_FileAccess
```

**描述**

DLP文件授权类型的枚举。

**起始版本：** 14

枚举项描述NO_PERMISSION = 0表示无文件权限。READ_ONLY = 1表示文件的只读权限。CONTENT_EDIT = 2表示文件的编辑权限。FULL_CONTROL = 3表示文件的完全控制权限。

#### 函数说明

#### OH_DLP_GetDlpPermissionInfo()

```ets
DLP_ErrCode OH_DLP_GetDlpPermissionInfo(DLP_FileAccess *dlpFileAccess, uint32_t *flags)
```

**描述**

查询当前DLP沙箱的权限信息。

**起始版本：** 14

**参数：**

参数项描述[DLP_FileAccess](#ZH-CN_TOPIC_0000002529285371__dlp_fileaccess) *dlpFileAccess表示DLP文件针对用户的授权类型，例如：只读。uint32_t *flags

表示DLP文件的详细操作权限，操作权限的具体含义为：

0x00000000-表示无文件权限。

0x00000001-表示文件的查看权限。

0x00000002-表示文件的保存权限。

0x00000004-表示文件的另存为权限。

0x00000008-表示文件的编辑权限。

0x00000010-表示文件的截屏权限。

0x00000020-表示文件的共享屏幕权限。

0x00000040-表示文件的录屏权限。

0x00000080-表示文件的复制权限。

0x00000100-表示文件的打印权限。

0x00000200-表示文件的导出权限。

0x00000400-表示文件的修改文件权限。

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100001 - 入参错误。

 19100006 - 非DLP沙箱应用。

 19100011 - 系统服务工作异常。

 19100012 - 内存申请失败。

#### OH_DLP_GetOriginalFileName()

```ets
DLP_ErrCode OH_DLP_GetOriginalFileName(const char *fileName, char **originalFileName)
```

**描述**

获取指定DLP文件名的原始文件名。

**起始版本：** 14

**参数：**

参数项描述const char *fileName指定要查询的文件名。char **originalFileNameDLP文件的原始文件名。

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100001 - 入参错误。

 19100012 - 内存申请失败。

#### OH_DLP_IsInSandbox()

```ets
DLP_ErrCode OH_DLP_IsInSandbox(bool *isInSandbox)
```

**描述**

查询当前应用是否运行在DLP沙箱环境。

**起始版本：** 14

**参数：**

参数项描述bool *isInSandboxtrue表示当前应用运行在DLP沙箱环境，false表示当前应用不是运行在DLP沙箱环境。

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100011 - 系统服务工作异常。

 19100012 - 内存申请失败。

#### OH_DLP_SetSandboxAppConfig()

```ets
DLP_ErrCode OH_DLP_SetSandboxAppConfig(const char *configInfo)
```

**描述**

设置沙箱应用配置信息。

**起始版本：** 14

**参数：**

参数项描述const char *configInfo沙箱应用配置信息。

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100001 - 入参错误。

 19100007 - DLP沙箱应用不允许调用此接口。

 19100011 - 系统服务工作异常。

 19100018 - 应用未授权。

#### OH_DLP_GetSandboxAppConfig()

```ets
DLP_ErrCode OH_DLP_GetSandboxAppConfig(char **configInfo)
```

**描述**

获取沙箱应用配置信息。

**起始版本：** 14

**参数：**

参数项描述char **configInfo沙箱应用配置信息。

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100011 - 系统服务工作异常。

 19100012 - 内存申请失败。

 19100018 - 应用未授权。

#### OH_DLP_CleanSandboxAppConfig()

```ets
DLP_ErrCode OH_DLP_CleanSandboxAppConfig()
```

**描述**

清理沙箱应用配置信息。

**起始版本：** 14

**返回：**

类型说明[DLP_ErrCode](#ZH-CN_TOPIC_0000002529285371__dlp_errcode)

0 - 操作成功。

 19100007 - DLP沙箱应用不允许调用此接口。

 19100011 - 系统服务工作异常。

 19100018 - 应用未授权。