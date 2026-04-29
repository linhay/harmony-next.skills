# ModuleInstall

**概述**

描述AppGallery kit提供按需分发能力。

起始版本： 5.0.2(14)

**汇总**

**文件**

| 名称 | 描述 |
| --- | --- |
| module_install.h | 声明按需分发能力提供的API。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct ModuleInstall_InstalledModule ModuleInstall_InstalledModule | 安装模块信息。 |
| typedef struct ModuleInstall_FetchModulesResult ModuleInstall_FetchModulesResult | 安装模块结果。 |
| typedef struct ModuleInstall_StatusCallback ModuleInstall_StatusCallback | 模块安装状态回调。 |
| typedef void (*ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo) | 监听回调函数。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_ErrCode | 枚举错误码。 |
| ModuleInstall_InstallStatus | 枚举安装状态。 |
| ModuleInstall_RequestCode | 枚举请求码。 |
| ModuleInstall_TaskStatus | 枚举任务状态。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| HMS_ModuleInstall_GetInstalledModule | 查询模块是否安装。 |
| HMS_ModuleInstall_GetInstalledModuleName | 获取模块名。 |
| HMS_ModuleInstall_GetInstalledModuleType | 获取模块类型。 |
| HMS_ModuleInstall_GetModuleInstallStatus | 获取模块安装状态。 |
| HMS_ModuleInstall_FetchModules | 请求下载模块。 |
| HMS_ModuleInstall_GetFetchModulesRequestCode | 获取模块下载请求码。 |
| HMS_ModuleInstall_GetFetchModulesTaskStatus | 获取模块下载任务状态。 |
| HMS_ModuleInstall_GetFetchModulesTaskId | 获取模块下载任务id。 |
| HMS_ModuleInstall_GetFetchModulesDesc | 获取模块下载描述。 |
| HMS_ModuleInstall_GetFetchModules | 获取模块下载模块名。 |
| HMS_ModuleInstall_GetFetchModulesTotalSize | 获取模块下载总大小。 |
| HMS_ModuleInstall_GetFetchModulesDownloadedSize | 获取模块下载已下载大小。 |
| HMS_ModuleInstall_CancelTask | 取消下载任务。 |
| HMS_ModuleInstall_ShowCellularDataConfirmation | 展示流量弹窗。 |
| HMS_ModuleInstall_CreateStatusCallback | 创建下载进度监听回调。 |
| HMS_ModuleInstall_On | 下载进度监听。 |
| HMS_ModuleInstall_ReleaseStatusCallback | 释放下载进度监听回调。 |
| HMS_ModuleInstall_Off | 取消下载进度监听。 |

**类型定义说明**

**ModuleInstall_InstalledModule**

```ets
typedef struct ModuleInstall_InstalledModule ModuleInstall_InstalledModule
```

描述

安装模块信息。

起始版本： 5.0.2(14)

**ModuleInstall_FetchModulesResult**

```ets
typedef struct ModuleInstall_FetchModulesResult ModuleInstall_FetchModulesResult
```

描述

安装模块结果。

起始版本： 5.0.2(14)

**ModuleInstall_StatusCallback**

```ets
typedef struct ModuleInstall_StatusCallback ModuleInstall_StatusCallback
```

描述

模块安装状态回调。

起始版本： 5.0.2(14)

**ModuleInstall_OnStatusCallback**

```ets
typedef void (*ModuleInstall_OnStatusCallback)(char *bundleName, char *eventInfo)
```

描述

监听回调函数。

起始版本： 5.0.2(14)

**枚举类型说明**

**ModuleInstall_ErrCode**

```ets
enum ModuleInstall_ErrCode
```

描述

枚举错误码。

起始版本： 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| E_NO_ERROR = 0 | 成功。 |
| E_PARAMS = 401 | 无效的参数。 |
| E_QUERY_MODULE = 1006500001 | 调用包管理模块接口异常。 |
| E_REPEATED_CALL = 1006500002 | 重复调用接口，输入相同。 |
| E_CONNECT_SA = 1006500004 | 服务异常。 |
| E_OFF_WITHOUT_ON = 1006500006 | 未与HMS_ModuleInstall_On接口共同使用。 |
| E_CONNECT_SERVICE_EXTENSION = 1006500007 | 服务连接失败。 |
| E_WRITE_PARAM = 1006500008 | 参数写入异常。 |
| E_REQUEST_SERVER = 1006500009 | 请求服务异常。 |
| E_RESPONSE_INVALID = 1006500010 | 响应参数无法解析。 |
| E_INNER_ERROR = 1006500011 | 内部错误。 |

**ModuleInstall_InstallStatus**

```ets
enum ModuleInstall_InstallStatus
```

描述

枚举安装状态。

起始版本： 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| INSTALLED = 0 | 已安装。 |
| NOT_INSTALLED = 1 | 未安装。 |

**ModuleInstall_RequestCode**

```ets
enum ModuleInstall_RequestCode
```

描述

枚举按需下载模块请求码。

起始版本： 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| MODULE_ALREADY_EXISTS = -8 | 模块已存在。 |
| MODULE_UNAVAILABLE = -7 | 要下载的模块不存在或者模块不适配该设备。 |
| INVALID_REQUEST = -6 | 该请求无效，请求中包含的信息不准确。 |
| NETWORK_ERROR = -5 | 网络异常，请求失败。 |
| INVOKER_VERIFICATION_FAILED = -4 | 调用者信息异常。 |
| FOREGROUND_REQUIRED = -3 | 仅允许应用在前台时请求按需加载。 |
| ACTIVE_SESSION_LIMIT_EXCEEDED = -2 | 请求被拒绝，因为当前至少有一个请求正在下载。 |
| FAILURE = -1 | 失败。 |
| SUCCESS = 0 | 成功。 |
| DOWNLOAD_WAIT_WIFI = 1 | 当前使用的是流量，开发者需要调用 HMS_ModuleInstall_ShowCellularDataConfirmation接口，提醒用户确认是否使用流量下载。 |

**ModuleInstall_TaskStatus**

```ets
enum ModuleInstall_TaskStatus
```

描述

枚举任务状态。

起始版本： 5.0.2(14)

| 枚举值 | 描述 |
| --- | --- |
| CREATE_TASK_FAILED = -4 | 创建下载任务失败。 |
| HIGHER_VERSION_INSTALLED = -3 | 本地存在相同或者更高版本。 |
| TASK_ALREADY_EXISTS = -2 | 下载任务已存在。 |
| TASK_UNFOUND = -1 | 下载任务不存在。 |
| TASK_CREATED = 0 | 创建下载任务成功。 |
| DOWNLOADING = 1 | 下载中。 |
| DOWNLOAD_PAUSED = 2 | 暂停中。 |
| DOWNLOAD_WAITING = 3 | 等待下载中。 |
| DOWNLOAD_SUCCESSFUL = 4 | 下载成功。 |
| DOWNLOAD_FAILED = 5 | 下载失败。 |
| DOWNLOAD_WAIT_FOR_WIFI = 6 | Wi-Fi预约。 |
| INSTALL_WAITING = 20 | 等待安装。 |
| INSTALLING = 21 | 安装中。 |
| INSTALL_SUCCESSFUL = 22 | 安装完成。 |
| INSTALL_FAILED = 23 | 安装失败。 |

**函数说明**

**HMS_ModuleInstall_GetInstalledModule**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_GetInstalledModule(const char *moduleName, unsigned int length,
    ModuleInstall_InstalledModule **installedModule)
```

描述

查询模块是否安装。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *moduleName | 模块名。 |
| int length | 模块名长度，最大长度512。 |
| ModuleInstall_InstalledModule **installedModule | 模块信息。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_QUERY_MODULE表示调用包管理模块接口异常。

**HMS_ModuleInstall_GetInstalledModuleName**

```ets
char *HMS_ModuleInstall_GetInstalledModuleName(const ModuleInstall_InstalledModule *installedModule)
```

描述

获取模块名。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_InstalledModule *installedModule | 模块信息。 |

返回：

返回模块名。

**HMS_ModuleInstall_GetInstalledModuleType**

```ets
int HMS_ModuleInstall_GetInstalledModuleType(const ModuleInstall_InstalledModule *installedModule)
```

描述

获取模块类型。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_InstalledModule *installedModule | 模块信息。 |

返回：

返回模块类型, 取值参考：[bundleManager.ModuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#moduletype)。当[ModuleInstall_InstallStatus](#ZH-CN_TOPIC_0000002522082316__moduleinstall_installstatus)=1时，默认返回0。

**HMS_ModuleInstall_GetModuleInstallStatus**

```ets
ModuleInstall_InstallStatus HMS_ModuleInstall_GetModuleInstallStatus(const ModuleInstall_InstalledModule *installedModule)
```

描述

获取模块安装状态。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_InstalledModule *installedModule | 模块信息。 |

返回：

模块安装状态，取值参考：[ModuleInstall_InstallStatus](#ZH-CN_TOPIC_0000002522082316__moduleinstall_installstatus)。

**HMS_ModuleInstall_FetchModules**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_FetchModules(const char *bundleName, unsigned int length, char **moduleNames, unsigned int moduleNamesLength, ModuleInstall_FetchModulesResult **fetchModulesResult)
```

描述

请求下载模块。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| char **moduleNames | 模块名数组。 |
| int moduleNamesLength | 模块名数组长度，最大长度512。 |
| ModuleInstall_FetchModulesResult **fetchModulesResult | 模块安装结果。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_CONNECT_SA表示服务异常；返回E_CONNECT_SERVICE_EXTENSION表示服务连接失败；返回E_WRITE_PARAM表示参数写入异常；返回E_REQUEST_SERVER表示请求服务异常；返回E_RESPONSE_INVALID表示响应参数无法解析；返回E_INNER_ERROR表示内部错误。

**HMS_ModuleInstall_GetFetchModulesRequestCode**

```ets
ModuleInstall_RequestCode HMS_ModuleInstall_GetFetchModulesRequestCode(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载请求码。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

按需下载模块请求码，取值参考: [ModuleInstall_RequestCode](#ZH-CN_TOPIC_0000002522082316__moduleinstall_requestcode)。

**HMS_ModuleInstall_GetFetchModulesTaskStatus**

```ets
ModuleInstall_TaskStatus HMS_ModuleInstall_GetFetchModulesTaskStatus(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载任务状态。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

模块下载任务状态，取值参考：[ModuleInstall_TaskStatus](#ZH-CN_TOPIC_0000002522082316__moduleinstall_taskstatus)。

**HMS_ModuleInstall_GetFetchModulesTaskId**

```ets
char *HMS_ModuleInstall_GetFetchModulesTaskId(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载任务id。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

任务id。

**HMS_ModuleInstall_GetFetchModulesDesc**

```ets
char *HMS_ModuleInstall_GetFetchModulesDesc(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载描述。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

下载描述。

**HMS_ModuleInstall_GetFetchModules**

```ets
char* HMS_ModuleInstall_GetFetchModules(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载模块名。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

下载模块名。

**HMS_ModuleInstall_GetFetchModulesTotalSize**

```ets
int HMS_ModuleInstall_GetFetchModulesTotalSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载总大小。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

下载模块总大小。

**HMS_ModuleInstall_GetFetchModulesDownloadedSize**

```ets
int HMS_ModuleInstall_GetFetchModulesDownloadedSize(const ModuleInstall_FetchModulesResult *fetchModulesResult)
```

描述

获取模块下载已下载大小。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_FetchModulesResult *fetchModulesResult | 模块安装结果。 |

返回：

已下载模块大小。

**HMS_ModuleInstall_CancelTask**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_CancelTask(const char *taskId, unsigned int length, unsigned int cancelResult)
```

描述

取消下载任务。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int cancelResult | 取消下载结果。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_CONNECT_SERVICE_EXTENSION表示服务连接失败；返回E_WRITE_PARAM表示参数写入异常；返回E_REQUEST_SERVER表示请求服务异常；返回E_RESPONSE_INVALID表示响应参数无法解析；

**HMS_ModuleInstall_ShowCellularDataConfirmation**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_ShowCellularDataConfirmation(const char *taskId, unsigned int length, unsigned int showResult)
```

描述

展示流量弹窗。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *taskId | 任务id。 |
| int length | 任务id长度，最大长度512。 |
| int showResult | 展示流量弹窗结果。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_CONNECT_SERVICE_EXTENSION表示服务连接失败；返回E_WRITE_PARAM表示参数写入异常；返回E_REQUEST_SERVER表示请求服务异常；返回E_RESPONSE_INVALID表示响应参数无法解析。

**HMS_ModuleInstall_CreateStatusCallback**

```ets
ModuleInstall_StatusCallback *HMS_ModuleInstall_CreateStatusCallback(ModuleInstall_OnStatusCallback *onStatusCallback)
```

描述

创建下载进度监听回调。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_OnStatusCallback *onStatusCallback | 回调函数。 |

返回：

下载进度监听回调。

**HMS_ModuleInstall_On**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_On(const char *bundleName, unsigned int length, unsigned int appIndex, unsigned int period, ModuleInstall_StatusCallback **callback)
```

描述

下载进度监听。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |
| int period | 监听周期。 |
| ModuleInstall_StatusCallback **callback | 下载进度监听回调。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_REPEATED_CALL表示重复调用接口；返回E_CONNECT_SA表示服务异常。

**HMS_ModuleInstall_ReleaseStatusCallback**

```ets
void HMS_ModuleInstall_ReleaseStatusCallback(ModuleInstall_StatusCallback *statusCallback)
```

描述

释放下载进度监听回调。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| ModuleInstall_StatusCallback *statusCallback | 下载进度监听回调。 |

**HMS_ModuleInstall_Off**

```ets
ModuleInstall_ErrCode HMS_ModuleInstall_Off(const char *bundleName, unsigned int length, unsigned int appIndex)
```

描述

取消下载进度监听。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 5.0.2(14)

参数:

| 名称 | 描述 |
| --- | --- |
| char *bundleName | 包名。 |
| int length | 包名长度，最大长度512。 |
| int appIndex | 应用分身索引。 |

返回：

返回E_NO_ERROR表示成功；返回E_PARAMS表示输入参数错误；返回E_OFF_WITHOUT_ON表示未与监听接口共同使用；返回E_CONNECT_SA表示服务异常。