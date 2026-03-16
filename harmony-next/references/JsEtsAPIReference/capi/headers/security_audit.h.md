# security_audit.h

#### 概述

文件中定义了与安全审计相关的函数。

**库：** libsecurityaudit_ndk.z.so

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**相关模块：**[SecurityAudit](../../topics/security/SecurityAudit.md)

#### 汇总

#### 结构体

名称

描述

struct [SecurityAudit_Event](../../topics/security/SecurityAudit_Event.md)

定义审计事件信息。

struct [SecurityAudit_Filter](../../topics/security/SecurityAudit_Filter.md)

提供过滤条件。

#### 类型定义

名称

描述

typedef void(* [SecurityAudit_Handler](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370)) (const [SecurityAudit_Event](../../topics/security/SecurityAudit_Event.md) *events, uint64_t count)

定义事件处理函数。

typedef struct SecurityAudit_AuthClient_Impl [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868)

定义阻断事件客户端。

typedef struct SecurityAudit_Client_Impl [SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974)

定义通知事件客户端。

#### 枚举

名称

描述

[SecurityAudit_Notify_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) {

SECURITY_AUDIT_NOTIFY_EVENT_PASTEBOARD = 0x27000000, SECURITY_AUDIT_NOTIFY_EVENT_FILE = 0x1C000007, SECURITY_AUDIT_NOTIFY_EVENT_FILE_INTERCEPTED = 0x1C001100, SECURITY_AUDIT_NOTIFY_EVENT_ACCOUNT = 0x10000100,

SECURITY_AUDIT_NOTIFY_EVENT_WINDOW = 0x07000000, SECURITY_AUDIT_NOTIFY_EVENT_VOLUME = 0x0F000000, SECURITY_AUDIT_NOTIFY_EVENT_PRINTER = 0x2E000000, SECURITY_AUDIT_NOTIFY_EVENT_PROCESS = 0x1C000008,

SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_TRAFFIC = 0x1C00000E, SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_CONN = 0x1C00000F, SECURITY_AUDIT_NOTIFY_EVENT_CAMERA = 0x2D000000, SECURITY_AUDIT_NOTIFY_EVENT_APP = 0x10000000,

SECURITY_AUDIT_NOTIFY_EVENT_EDM = 0x11000000, SECURITY_AUDIT_NOTIFY_EVENT_CERT = 0x12003000, SECURITY_AUDIT_NOTIFY_EVENT_KIA_CREATE = 0x1C00000B, SECURITY_AUDIT_NOTIFY_EVENT_KIA_READ = 0x1C000012,

SECURITY_AUDIT_NOTIFY_EVENT_KIA_VARIANT = 0x1C00000C, SECURITY_AUDIT_NOTIFY_EVENT_KIA_INTERCEPT = 0x1C00000A, SECURITY_AUDIT_NOTIFY_EVENT_PERMISSION = 0x0B000000, SECURITY_AUDIT_NOTIFY_EVENT_DNS = 0x03000001,

SECURITY_AUDIT_NOTIFY_EVENT_APP_INSTALL_INTERCEPTED = 0x18000100, SECURITY_AUDIT_NOTIFY_EVENT_APP_UNINSTALL_INTERCEPTED = 0x18000101, SECURITY_AUDIT_NOTIFY_EVENT_APP_UPDATE_INTERCEPTED = 0x18000102, SECURITY_AUDIT_NOTIFY_EVENT_APP_RECOVER_INTERCEPTED = 0x18000103,

SECURITY_AUDIT_NOTIFY_EVENT_APP_START_INTERCEPTED = 0x18000104, SECURITY_AUDIT_NOTIFY_EVENT_USB_ACCESS_INTERCEPTED = 0x30000000

}

定义通知事件的事件ID。

[SecurityAudit_Auth_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) {

SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE = 0x1C801100, SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN = 0x1C801101, SECURITY_AUDIT_AUTH_EVENT_FILE_RENAME = 0x1C801102, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETE = 0x1C801103,

SECURITY_AUDIT_AUTH_EVENT_FILE_SETEXTATTR = 0x1C801104, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETEEXTATTR = 0x1C801105

}

定义阻断事件的事件ID。

[SecurityAudit_FilterType](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) {

EVENT_TYPE_EQUAL = 0x00000100, EVENT_SUBTYPE_EQUAL = 0x00000200, FILE_PATH_EQUAL = 0x00010000, FILE_PATH_PREFIX = 0x00010001,

FILE_PATH_SUFFIX = 0x00010002, PROCESS_UID_EQUAL = 0x00020000, PROCESS_PID_EQUAL = 0x00020100, PROCESS_NAME_EQUAL = 0x00020200,

PROCESS_NAME_PREFIX = 0x00020201, PROCESS_NAME_SUFFIX = 0x00020202

}

定义过滤器类型。

[SecurityAudit_AuthResult](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) { SECURITY_AUDIT_AUTH_RESULT_ALLOW = 0, SECURITY_AUDIT_AUTH_RESULT_DENY = 1 }

定义阻断结果的类型。

#### 函数

名称

描述

int32_t [HMS_SecurityAudit_NewClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga18d7c9fe5c578d6113c86dd0c09353b4) ([SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) **client, [SecurityAudit_Handler](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

创建一个新的通知事件客户端。

int32_t [HMS_SecurityAudit_DeleteClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga26838e6288eea1421f03e6130aafd837) ([SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client)

删除通知客户端。

int32_t [HMS_SecurityAudit_Subscribe](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3530687f761edfb0141f6c17ff3ba4cd) (const [SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, const [SecurityAudit_Notify_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) *events, uint64_t count)

订阅通知事件。

int32_t [HMS_SecurityAudit_Unsubscribe](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga208aff2c03535311e85428fbd375d09f) (const [SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, const [SecurityAudit_Notify_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) *events, uint64_t count)

取消订阅通知事件。

int32_t [HMS_SecurityAudit_AddFilter](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga292bdf10008513a439d6bb08450328b0) (const [SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, [SecurityAudit_Notify_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](../../topics/security/SecurityAudit_Filter.md) *filter)

为通知事件添加过滤条件。

int32_t [HMS_SecurityAudit_RemoveFilter](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3c7aa36f4cff9a0107bf144f7fbbdcd5) (const [SecurityAudit_Client](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gac8326d6e61c24a60ae07e7b9b78c7974) *client, [SecurityAudit_Notify_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaf23b070cfdcb7b9c9e6320fe599939ea) event, const [SecurityAudit_Filter](../../topics/security/SecurityAudit_Filter.md) *filter)

删除通知事件的过滤条件。

int32_t [HMS_SecurityAudit_NewAuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gab59201b529a964c3cc7f9ed12ab0330e) ([SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) **client, [SecurityAudit_Handler](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gacba1c566db7aa3b55e478c57c1def370) handler)

创建一个新的阻断类事件客户端。

int32_t [HMS_SecurityAudit_DeleteAuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga0a518a6380e80f47869a58f9cf14af87) ([SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client)

删除阻断类事件客户端。

int32_t [HMS_SecurityAudit_SubscribeAuthEvent](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gab33847480e92d3107a91d76a10b8c82f) (const [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Auth_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) *events, uint64_t count)

订阅阻断类事件。

int32_t [HMS_SecurityAudit_UnsubscribeAuthEvent](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaebf52f27e5409c29dc3ad0c3eba47783) (const [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Auth_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) *events, uint64_t count)

取消订阅阻断类事件。

int32_t [HMS_SecurityAudit_AddAuthEventFilter](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga3d9df28411da9cc483c2e82d304cb38e) (const [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, [SecurityAudit_Auth_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](../../topics/security/SecurityAudit_Filter.md) *filter)

为阻断类事件添加过滤条件。

int32_t [HMS_SecurityAudit_RemoveAuthEventFilter](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaef069b340e428715c10531885326c079) (const [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, [SecurityAudit_Auth_Event](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga9ef4ede60da98e07612cb0cf0b03188f) event, const [SecurityAudit_Filter](../../topics/security/SecurityAudit_Filter.md) *filter)

删除阻断类事件的过滤条件。

int32_t [HMS_SecurityAudit_Auth](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gafbb9c2e5389b79d8def76c530e01e26c) (const [SecurityAudit_AuthClient](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_ga43a0f7f5dec522e7dadfa81a9c157868) *client, const [SecurityAudit_Event](../../topics/security/SecurityAudit_Event.md) *event, [SecurityAudit_AuthResult](../../topics/security/SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gae1e5585e31b60ada1569093893aab3de) authResult)

设置审计事件的阻断结果。

int32_t [HMS_SecurityAudit_QueryAllProcesses](../../topics/security/SecurityAudit.md#section0945443114617) (char** result)

获取所有的应用进程信息。

int32_t [HMS_SecurityAudit_QueryProcesses](../../topics/security/SecurityAudit.md#section11373745488) (uint64_t* pids, uint64_t count, char** result)

获取输入的pid的应用进程信息。