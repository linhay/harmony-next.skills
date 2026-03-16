# module_install.h

#### 概述

声明按需分发能力的API。

**库：** libhmsmoduleinstall.so

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 5.0.2(14)

**相关模块：**[ModuleInstall](../../topics/system-services/ModuleInstall.md)

#### 汇总

#### 类型

名称

描述

typedef struct [ModuleInstall_InstalledModule](../../topics/system-services/ModuleInstall.md#ZH-CN_TOPIC_0000002459017220__osaccount_errcode)[ModuleInstall_InstalledModule](../../topics/system-services/ModuleInstall.md#ZH-CN_TOPIC_0000002459017220__osaccount_errcode)

安装模块信息。

typedef struct [ModuleInstall_FetchModulesResult](../../topics/system-services/ModuleInstall.md#section115389533615)[ModuleInstall_FetchModulesResult](../../topics/system-services/ModuleInstall.md#section115389533615)

安装模块结果。

typedef struct [ModuleInstall_StatusCallback](../../topics/system-services/ModuleInstall.md#section48269177812)[ModuleInstall_StatusCallback](../../topics/system-services/ModuleInstall.md#section48269177812)

模块安装状态回调。

[ModuleInstall_OnStatusCallback](../../topics/system-services/ModuleInstall.md#section9881414171010)

监听回调函数

#### 枚举

名称

描述

typedef enum [ModuleInstall_ErrCode](../../topics/system-services/ModuleInstall.md#ZH-CN_TOPIC_0000002459017220__osaccount_errcode-1) {

E_NO_ERROR = 0,

E_PARAMS = 401,

E_QUERY_MODULE = 1006500001,

E_REPEATED_CALL = 1006500002,

E_CONNECT_SA = 1006500004,

E_OFF_WITHOUT_ON = 1006500006,

E_CONNECT_SERVICE_EXTENSION = 1006500007,

E_WRITE_PARAM = 1006500008,

E_REQUEST_SERVER = 1006500009,

E_RESPONSE_INVALID = 1006500010,

E_INNER_ERROR = 1006500011

}

枚举错误码。

typedef enum [ModuleInstall_InstallStatus](../../topics/system-services/ModuleInstall.md#section19925459265) {

INSTALLED = 0,

NOT_INSTALLED = 1

}

枚举安装状态。

typedef enum [ModuleInstall_RequestCode](../../topics/system-services/ModuleInstall.md#section10742174163618) {

MODULE_ALREADY_EXISTS = -8,

MODULE_UNAVAILABLE = -7,

INVALID_REQUEST = -6,

NETWORK_ERROR = -5,

INVOKER_VERIFICATION_FAILED = -4,

FOREGROUND_REQUIRED = -3,

ACTIVE_SESSION_LIMIT_EXCEEDED = -2,

FAILURE = -1,

SUCCESS = 0,

DOWNLOAD_WAIT_WIFI = 1

}

枚举请求码。

typedef enum [ModuleInstall_TaskStatus](../../topics/system-services/ModuleInstall.md#section14463723193715) {

CREATE_TASK_FAILED = -4,

HIGHER_VERSION_INSTALLED = -3,

TASK_ALREADY_EXISTS = -2,

TASK_UNFOUND = -1,

TASK_CREATED = 0,

DOWNLOADING = 1,

DOWNLOAD_PAUSED = 2,

DOWNLOAD_WAITING = 3,

DOWNLOAD_SUCCESSFUL = 4,

DOWNLOAD_FAILED = 5,

DOWNLOAD_WAIT_FOR_WIFI = 6,

INSTALL_WAITING = 20,

INSTALLING = 21,

INSTALL_SUCCESSFUL = 22,

INSTALL_FAILED = 23

}

枚举任务状态。

#### 函数

名称

描述

[HMS_ModuleInstall_GetInstalledModule](../../topics/system-services/ModuleInstall.md#ZH-CN_TOPIC_0000002459017220__oh_osaccount_getname)

查询模块是否安装。

[HMS_ModuleInstall_GetInstalledModuleName](../../topics/system-services/ModuleInstall.md#section19475184213526)

获取模块名。

[HMS_ModuleInstall_GetInstalledModuleType](../../topics/system-services/ModuleInstall.md#section39341746155513)

获取模块类型。

[HMS_ModuleInstall_GetModuleInstallStatus](../../topics/system-services/ModuleInstall.md#section84699521566)

获取模块安装状态。

[HMS_ModuleInstall_FetchModules](../../topics/system-services/ModuleInstall.md#section1533121613581)

请求下载模块。

[HMS_ModuleInstall_GetFetchModulesRequestCode](../../topics/system-services/ModuleInstall.md#section191414113614)

获取模块下载请求码。

[HMS_ModuleInstall_GetFetchModulesTaskStatus](../../topics/system-services/ModuleInstall.md#section142448141910)

获取模块下载任务状态。

[HMS_ModuleInstall_GetFetchModulesTaskId](../../topics/system-services/ModuleInstall.md#section979412409101)

获取模块下载任务id。

[HMS_ModuleInstall_GetFetchModulesDesc](../../topics/system-services/ModuleInstall.md#section762681812121)

获取模块下载描述。

[HMS_ModuleInstall_GetFetchModules](../../topics/system-services/ModuleInstall.md#section55521545111313)

获取模块下载模块名。

[HMS_ModuleInstall_GetFetchModulesTotalSize](../../topics/system-services/ModuleInstall.md#section1071043411515)

获取模块下载总大小。

[HMS_ModuleInstall_GetFetchModulesDownloadedSize](../../topics/system-services/ModuleInstall.md#section04641118168)

获取模块下载已下载大小。

[HMS_ModuleInstall_CancelTask](../../topics/system-services/ModuleInstall.md#section1177619221712)

取消下载任务。

[HMS_ModuleInstall_ShowCellularDataConfirmation](../../topics/system-services/ModuleInstall.md#section1897653081720)

展示流量弹窗。

[HMS_ModuleInstall_CreateStatusCallback](../../topics/system-services/ModuleInstall.md#section1710031151816)

创建下载进度监听回调。

[HMS_ModuleInstall_On](../../topics/system-services/ModuleInstall.md#section18492123951816)

下载进度监听。

[HMS_ModuleInstall_ReleaseStatusCallback](../../topics/system-services/ModuleInstall.md#section1541418516194)

释放下载进度监听回调。

[HMS_ModuleInstall_Off](../../topics/system-services/ModuleInstall.md#section1260162551917)

取消下载进度监听。