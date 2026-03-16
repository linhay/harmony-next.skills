# SecurityAudit

#### 概述

提供安全审计的API。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

#### 汇总

#### 文件

名称

描述

[security_audit.h](../../capi/headers/security_audit.h.md)

文件中定义了与安全审计相关的函数。

#### 结构体

名称

描述

struct [SecurityAudit_Event](SecurityAudit_Event.md)

定义审计事件信息。

struct [SecurityAudit_Filter](SecurityAudit_Filter.md)

提供过滤条件。

#### 类型定义

名称

描述

typedef void(* [SecurityAudit_Handler](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370)) (const [SecurityAudit_Event](SecurityAudit_Event.md) *events, uint64_t count)

定义事件处理函数。

typedef struct SecurityAudit_AuthClient_Impl [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)

定义阻断事件客户端。

typedef struct SecurityAudit_Client_Impl [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)

定义通知事件客户端。

#### 枚举

名称

描述

[SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) {

SECURITY_AUDIT_NOTIFY_EVENT_PASTEBOARD = 0x27000000, SECURITY_AUDIT_NOTIFY_EVENT_FILE = 0x1C000007, SECURITY_AUDIT_NOTIFY_EVENT_FILE_INTERCEPTED = 0x2700003C, SECURITY_AUDIT_NOTIFY_EVENT_ACCOUNT = 0x10000100,

SECURITY_AUDIT_NOTIFY_EVENT_WINDOW = 0x07000000, SECURITY_AUDIT_NOTIFY_EVENT_VOLUME = 0x0F000000, SECURITY_AUDIT_NOTIFY_EVENT_PRINTER = 0x2E000000, SECURITY_AUDIT_NOTIFY_EVENT_PROCESS = 0x1C000008,

SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_TRAFFIC = 0x1C00000E, SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_CONN = 0x1C00000F, SECURITY_AUDIT_NOTIFY_EVENT_CAMERA = 0x2D000000, SECURITY_AUDIT_NOTIFY_EVENT_APP = 0x10000000,

SECURITY_AUDIT_NOTIFY_EVENT_EDM = 0x11000000, SECURITY_AUDIT_NOTIFY_EVENT_CERT = 0x12003000, SECURITY_AUDIT_NOTIFY_EVENT_KIA_CREATE = 0x1C00000B, SECURITY_AUDIT_NOTIFY_EVENT_KIA_READ = 0x1C000012,

SECURITY_AUDIT_NOTIFY_EVENT_KIA_VARIANT = 0x1C00000C, SECURITY_AUDIT_NOTIFY_EVENT_KIA_INTERCEPT = 0x1C00000A, SECURITY_AUDIT_NOTIFY_EVENT_PERMISSION = 0x0B000000, SECURITY_AUDIT_NOTIFY_EVENT_DNS = 0x03000001,

SECURITY_AUDIT_NOTIFY_EVENT_APP_INSTALL_INTERCEPTED = 0x18000100, SECURITY_AUDIT_NOTIFY_EVENT_APP_UNINSTALL_INTERCEPTED = 0x18000101, SECURITY_AUDIT_NOTIFY_EVENT_APP_UPDATE_INTERCEPTED = 0x18000102, SECURITY_AUDIT_NOTIFY_EVENT_APP_RECOVER_INTERCEPTED = 0x18000103,

SECURITY_AUDIT_NOTIFY_EVENT_APP_START_INTERCEPTED = 0x18000104, SECURITY_AUDIT_NOTIFY_EVENT_USB_ACCESS_INTERCEPTED = 0x30000000

}

定义通知事件的事件ID。

[SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) {

SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE = 0x1C801100, SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN = 0x1C801101, SECURITY_AUDIT_AUTH_EVENT_FILE_RENAME = 0x1C801102, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETE = 0x1C801103,

SECURITY_AUDIT_AUTH_EVENT_FILE_SETEXTATTR = 0x1C801104, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETEEXTATTR = 0x1C801105

}

定义阻断类事件的事件ID。

[SecurityAudit_FilterType](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) {

EVENT_TYPE_EQUAL = 0x00000100, EVENT_SUBTYPE_EQUAL = 0x00000200, FILE_PATH_EQUAL = 0x00010000, FILE_PATH_PREFIX = 0x00010001,

FILE_PATH_SUFFIX = 0x00010002, PROCESS_UID_EQUAL = 0x00020000, PROCESS_PID_EQUAL = 0x00020100, PROCESS_NAME_EQUAL = 0x00020200,

PROCESS_NAME_PREFIX = 0x00020201, PROCESS_NAME_SUFFIX = 0x00020202

}

定义过滤器类型。

[SecurityAudit_AuthResult](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) { SECURITY_AUDIT_AUTH_RESULT_ALLOW = 0, SECURITY_AUDIT_AUTH_RESULT_DENY = 1 }

定义阻断结果的类型。

#### 函数

名称

描述

int32_t [HMS_SecurityAudit_NewClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga18d7c9fe5c578d6113c86dd0c09353b4) ([SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) **client, [SecurityAudit_Handler](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

创建一个新的通知事件客户端。

int32_t [HMS_SecurityAudit_DeleteClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga26838e6288eea1421f03e6130aafd837) ([SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client)

删除通知客户端。

int32_t [HMS_SecurityAudit_Subscribe](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3530687f761edfb0141f6c17ff3ba4cd) (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, const [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) *events, uint64_t count)

订阅通知事件。

int32_t [HMS_SecurityAudit_Unsubscribe](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga208aff2c03535311e85428fbd375d09f) (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, const [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) *events, uint64_t count)

取消订阅通知事件。

int32_t [HMS_SecurityAudit_AddFilter](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga292bdf10008513a439d6bb08450328b0) (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) *filter)

为通知事件添加过滤条件。

int32_t [HMS_SecurityAudit_RemoveFilter](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3c7aa36f4cff9a0107bf144f7fbbdcd5) (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) *filter)

删除通知事件的过滤条件。

int32_t [HMS_SecurityAudit_NewAuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gab59201b529a964c3cc7f9ed12ab0330e) ([SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) **client, [SecurityAudit_Handler](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

创建一个新的阻断类事件客户端。

int32_t [HMS_SecurityAudit_DeleteAuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga0a518a6380e80f47869a58f9cf14af87) ([SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client)

删除阻断类事件客户端。

int32_t [HMS_SecurityAudit_SubscribeAuthEvent](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gab33847480e92d3107a91d76a10b8c82f) (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) *events, uint64_t count)

订阅阻断类事件。

int32_t [HMS_SecurityAudit_UnsubscribeAuthEvent](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaebf52f27e5409c29dc3ad0c3eba47783) (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) *events, uint64_t count)

取消订阅阻断类事件。

int32_t [HMS_SecurityAudit_AddAuthEventFilter](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3d9df28411da9cc483c2e82d304cb38e) (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) *filter)

为阻断类事件添加过滤条件。

int32_t [HMS_SecurityAudit_RemoveAuthEventFilter](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaef069b340e428715c10531885326c079) (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) *filter)

删除阻断类事件的过滤条件。

int32_t [HMS_SecurityAudit_Auth](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gafbb9c2e5389b79d8def76c530e01e26c) (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Event](SecurityAudit_Event.md) *event, [SecurityAudit_AuthResult](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult)

设置审计事件的阻断结果。

int32_t [HMS_SecurityAudit_QueryAllProcesses](#section0945443114617)(char** result)

获取所有的应用进程信息。

int32_t [HMS_SecurityAudit_QueryProcesses](#section11373745488)(uint64_t* pids, uint64_t count, char** result)

获取输入的pid的应用进程信息。

#### 类型定义说明

#### SecurityAudit_AuthClient

```ets
typedef struct SecurityAudit_AuthClient_Impl [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)
```

**描述**

定义阻断事件客户端。

**起始版本：** 6.0.0(20)

#### SecurityAudit_Client

```ets
typedef struct SecurityAudit_Client_Impl [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)
```

**描述**

定义通知事件客户端。

**起始版本：** 6.0.0(20)

#### SecurityAudit_Handler

```ets
typedef void(* SecurityAudit_Handler) (const [SecurityAudit_Event](SecurityAudit_Event.md) *events, uint64_t count)
```

**描述**

定义事件处理函数。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

events

指向审计事件信息的指针。

count

数组中的事件数。

#### 枚举类型说明

#### SecurityAudit_Auth_Event

```ets
enum [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f)
```

**描述**

定义阻断事件的事件ID。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

枚举值

描述

****SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE

文件创建阻断事件。

****SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN

文件打开阻断事件。

****SECURITY_AUDIT_AUTH_EVENT_FILE_RENAME

文件重命名阻断事件。

****SECURITY_AUDIT_AUTH_EVENT_FILE_DELETE

文件删除阻断事件。

****SECURITY_AUDIT_AUTH_EVENT_FILE_SETEXTATTR

文件设置扩展属性的阻断事件。

****SECURITY_AUDIT_AUTH_EVENT_FILE_DELETEEXTATTR

文件删除扩展属性的阻断事件。

#### SecurityAudit_AuthResult

```ets
enum [SecurityAudit_AuthResult](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de)
```

**描述**

定义阻断结果的类型。

**起始版本：** 6.0.0(20)

枚举值

描述

****SECURITY_AUDIT_AUTH_RESULT_ALLOW

允许的阻断事件。

****SECURITY_AUDIT_AUTH_RESULT_DENY

拒绝的阻断事件。

#### SecurityAudit_FilterType

```ets
enum [SecurityAudit_FilterType](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f)
```

**描述**

定义过滤器类型。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

枚举值

描述

****EVENT_TYPE_EQUAL

事件类型的过滤器类型。

****EVENT_SUBTYPE_EQUAL

事件子类型的过滤器类型。

****FILE_PATH_EQUAL

文件路径类型的过滤器类型。

****FILE_PATH_PREFIX

文件路径前缀类型的过滤器类型。

****FILE_PATH_SUFFIX

文件路径后缀类型的过滤器类型。

****PROCESS_UID_EQUAL

过滤进程的 UID 类型。

****PROCESS_PID_EQUAL

过滤进程 ID 类型。

****PROCESS_NAME_EQUAL

筛选进程名称类型。

****PROCESS_NAME_PREFIX

进程名称前缀的过滤类型。

****PROCESS_NAME_SUFFIX

进程名称后缀的过滤类型。

#### SecurityAudit_Notify_Event

```ets
enum [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea)
```

**描述**

定义通知事件的事件ID。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

枚举值

描述

****SECURITY_AUDIT_NOTIFY_EVENT_PASTEBOARD

剪贴板复制和粘贴事件。

****SECURITY_AUDIT_NOTIFY_EVENT_FILE

文件事件。

****SECURITY_AUDIT_NOTIFY_EVENT_FILE_INTERCEPTED

文件访问规则违规事件。

****SECURITY_AUDIT_NOTIFY_EVENT_ACCOUNT

账户登录和注销事件。

****SECURITY_AUDIT_NOTIFY_EVENT_WINDOW

窗口截图、屏幕录制、屏幕投影事件。

****SECURITY_AUDIT_NOTIFY_EVENT_VOLUME

可移动存储设备的插入和移除事件。

****SECURITY_AUDIT_NOTIFY_EVENT_PRINTER

打印机事件。

****SECURITY_AUDIT_NOTIFY_EVENT_PROCESS

进程创建退出事件。

****SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_TRAFFIC

网络流量事件。

****SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_CONN

网络连接事件。

****SECURITY_AUDIT_NOTIFY_EVENT_CAMERA

相机事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP

应用程序事件。

****SECURITY_AUDIT_NOTIFY_EVENT_EDM

企业设备管理事件。

****SECURITY_AUDIT_NOTIFY_EVENT_CERT

证书操作事件。

****SECURITY_AUDIT_NOTIFY_EVENT_KIA_CREATE

KIA文件创建事件。

****SECURITY_AUDIT_NOTIFY_EVENT_KIA_READ

KIA文件读取事件。

****SECURITY_AUDIT_NOTIFY_EVENT_KIA_VARIANT

KIA文件变体事件。

****SECURITY_AUDIT_NOTIFY_EVENT_KIA_INTERCEPT

KIA文件拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_PERMISSION

应用程序权限更改事件。

****SECURITY_AUDIT_NOTIFY_EVENT_DNS

DNS审计事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP_INSTALL_INTERCEPTED

应用程序安装拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP_UNINSTALL_INTERCEPTED

应用程序卸载拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP_UPDATE_INTERCEPTED

应用程序更新拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP_RECOVER_INTERCEPTED

应用程序恢复拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_APP_START_INTERCEPTED

应用程序开始拦截事件。

****SECURITY_AUDIT_NOTIFY_EVENT_USB_ACCESS_INTERCEPTED

USB访问拦截事件。

#### 函数说明

#### HMS_SecurityAudit_AddAuthEventFilter()

```ets
int32_t HMS_SecurityAudit_AddAuthEventFilter (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client, [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) * filter )
```

**描述**

为阻断类事件添加过滤条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的阻断类事件客户端。

event

需要添加过滤条件的阻断类事件。

filter

阻断类事件的过滤器描述。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果过滤器数量超过上限，则返回1012000004。 如果事件不支持过滤条件，则返回1012000005。

#### HMS_SecurityAudit_AddFilter()

```ets
int32_t HMS_SecurityAudit_AddFilter (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) * client, [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) * filter )
```

**描述**

为通知事件添加过滤条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的通知类事件客户端。

event

通知要添加过滤条件的事件。

filter

通知事件的过滤器描述。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果过滤器数量超过上限，则返回1012000004。 如果事件不支持过滤条件，则返回1012000005。

#### HMS_SecurityAudit_Auth()

```ets
int32_t HMS_SecurityAudit_Auth (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client, const [SecurityAudit_Event](SecurityAudit_Event.md) * event, [SecurityAudit_AuthResult](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult )
```

**描述**

设置审计事件的阻断结果

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的阻断类事件客户端。

event

审计阻断类事件信息。

authResult

阻断结果。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_DeleteAuthClient()

```ets
int32_t HMS_SecurityAudit_DeleteAuthClient ([SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client)
```

**描述**

删除阻断类事件客户端。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

要删除的阻断类事件客户端实例。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_DeleteClient()

```ets
int32_t HMS_SecurityAudit_DeleteClient ([SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) * client)
```

**描述**

删除通知客户端。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

要删除的客户端实例。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_NewAuthClient()

```ets
int32_t HMS_SecurityAudit_NewAuthClient ([SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) ** client, [SecurityAudit_Handler](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler )
```

**描述**

创建一个新的阻断类客户端。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

指向新阻断类事件客户端实例的指针。

handler

处理发送到此客户端的所有消息的处理器。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果客户端数量超过总上限，返回1012000002。 如果客户端数量超过当前进程的上限，则返回1012000003。

#### HMS_SecurityAudit_NewClient()

```ets
int32_t HMS_SecurityAudit_NewClient ([SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) ** client, [SecurityAudit_Handler](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler )
```

**描述**

创建一个新的通知事件客户端。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

指向新客户端实例的指针。

handler

处理发送到此客户端的所有消息的处理器。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果客户端数量超过总上限，返回1012000002。 如果客户端数量超过当前进程的上限，则返回1012000003。

#### HMS_SecurityAudit_RemoveAuthEventFilter()

```ets
int32_t HMS_SecurityAudit_RemoveAuthEventFilter (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client, [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) * filter )
```

**描述**

删除阻断类事件的过滤条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的阻断类事件客户端。

event

要删除过滤条件的阻断类事件。

filter

阻断类事件的过滤器描述。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果事件不支持过滤条件，则返回1012000005。

#### HMS_SecurityAudit_RemoveFilter()

```ets
int32_t HMS_SecurityAudit_RemoveFilter (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) * client, [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](SecurityAudit_Filter.md) * filter )
```

**描述**

删除通知事件的过滤条件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的通知类事件客户端。

event

通知要删除过滤条件的事件。

filter

通知事件的过滤器描述。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果事件不支持过滤条件，则返回1012000005。

#### HMS_SecurityAudit_Subscribe()

```ets
int32_t HMS_SecurityAudit_Subscribe (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) * client, const [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) * events, uint64_t count )
```

**描述**

订阅通知事件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

订阅通知事件的客户端。

events

要订阅的通知事件数组。

count

数组中的通知事件数。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_SubscribeAuthEvent()

```ets
int32_t HMS_SecurityAudit_SubscribeAuthEvent (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client, const [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) * events, uint64_t count )
```

**描述**

订阅阻断类事件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的阻断类事件客户端。

events

要订阅的阻断类事件数组。

count

数组中的阻断类事件数。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_Unsubscribe()

```ets
int32_t HMS_SecurityAudit_Unsubscribe (const [SecurityAudit_Client](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) * client, const [SecurityAudit_Notify_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) * events, uint64_t count )
```

**描述**

取消订阅通知事件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

取消订阅通知事件的客户端。

events

要取消订阅的通知事件数组。

count

数组中的通知事件数。

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_UnsubscribeAuthEvent()

```ets
int32_t HMS_SecurityAudit_UnsubscribeAuthEvent (const [SecurityAudit_AuthClient](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) * client, const [SecurityAudit_Auth_Event](#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) * events, uint64_t count )
```

**描述**

取消订阅阻断类事件。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

client

客户已创建的阻断类事件客户端。

events

要取消订阅的阻断类事件数组。

count

数组中的阻断类事件数。

**Permission：**

ohos.permission.kernel.AUTH_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001

#### HMS_SecurityAudit_QueryAllProcesses()

```ets
int32_t HMS_SecurityAudit_QueryAllProcesses(char** result)
```

**描述**

查询获取所有的应用进程信息。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

result

查询获取到的应用进程信息

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

#### HMS_SecurityAudit_QueryProcesses()

```ets
int32_t HMS_SecurityAudit_QueryProcesses(uint64_t* pids, uint64_t count, char** result)
```

**描述**

查询获取输入的pid的应用进程信息。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

pids

应用要查询的pid数组名。

count

应用要查询的pid数组元素个数。

result

查询获取到的应用进程信息.

**Permission：**

ohos.permission.QUERY_AUDIT_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。如果要查询的pid数组元素个数超过限制，则返回1012000006。