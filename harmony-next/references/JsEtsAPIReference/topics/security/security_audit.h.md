# security_audit.h

**概述**

文件中定义了与安全审计相关的函数。

引用文件： <DeviceSecurityKit/security_audit.h>

库： libsecurityaudit_ndk.z.so

系统能力： SystemCapability.Security.SecurityAudit

起始版本： 6.0.0(20)

相关模块： [SecurityAudit](SecurityAudit.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct SecurityAudit_Event | 定义审计事件信息。 |
| struct SecurityAudit_Filter | 提供过滤条件。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef void(* SecurityAudit_Handler) (const SecurityAudit_Event *events, uint64_t count) | 定义事件处理函数。 |
| typedef struct SecurityAudit_AuthClient_Impl SecurityAudit_AuthClient | 定义阻断事件客户端。 |
| typedef struct SecurityAudit_Client_Impl SecurityAudit_Client | 定义通知事件客户端。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| SecurityAudit_Notify_Event { SECURITY_AUDIT_NOTIFY_EVENT_PASTEBOARD = 0x27000000, SECURITY_AUDIT_NOTIFY_EVENT_FILE = 0x1C000007, SECURITY_AUDIT_NOTIFY_EVENT_FILE_INTERCEPTED = 0x1C001100, SECURITY_AUDIT_NOTIFY_EVENT_ACCOUNT = 0x10000100, SECURITY_AUDIT_NOTIFY_EVENT_WINDOW = 0x07000000, SECURITY_AUDIT_NOTIFY_EVENT_VOLUME = 0x0F000000, SECURITY_AUDIT_NOTIFY_EVENT_PRINTER = 0x2E000000, SECURITY_AUDIT_NOTIFY_EVENT_PROCESS = 0x1C000008, SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_TRAFFIC = 0x1C00000E, SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_CONN = 0x1C00000F, SECURITY_AUDIT_NOTIFY_EVENT_CAMERA = 0x2D000000, SECURITY_AUDIT_NOTIFY_EVENT_APP = 0x10000000, SECURITY_AUDIT_NOTIFY_EVENT_EDM = 0x11000000, SECURITY_AUDIT_NOTIFY_EVENT_CERT = 0x12003000, SECURITY_AUDIT_NOTIFY_EVENT_KIA_CREATE = 0x1C00000B, SECURITY_AUDIT_NOTIFY_EVENT_KIA_READ = 0x1C000012, SECURITY_AUDIT_NOTIFY_EVENT_KIA_VARIANT = 0x1C00000C, SECURITY_AUDIT_NOTIFY_EVENT_KIA_INTERCEPT = 0x1C00000A, SECURITY_AUDIT_NOTIFY_EVENT_PERMISSION = 0x0B000000, SECURITY_AUDIT_NOTIFY_EVENT_DNS = 0x03000001, SECURITY_AUDIT_NOTIFY_EVENT_APP_INSTALL_INTERCEPTED = 0x18000100, SECURITY_AUDIT_NOTIFY_EVENT_APP_UNINSTALL_INTERCEPTED = 0x18000101, SECURITY_AUDIT_NOTIFY_EVENT_APP_UPDATE_INTERCEPTED = 0x18000102, SECURITY_AUDIT_NOTIFY_EVENT_APP_RECOVER_INTERCEPTED = 0x18000103, SECURITY_AUDIT_NOTIFY_EVENT_APP_START_INTERCEPTED = 0x18000104, SECURITY_AUDIT_NOTIFY_EVENT_USB_ACCESS_INTERCEPTED = 0x30000000, SECURITY_AUDIT_NOTIFY_EVENT_SMB_FILE_SEND = 0x0F000001, SECURITY_AUDIT_NOTIFY_EVENT_KIA_PRE_OPEN = 0x1C000014, SECURITY_AUDIT_NOTIFY_EVENT_HDC_DEBUG = 0x27000100, SECURITY_AUDIT_NOTIFY_EVENT_HDC_DEBUG_INTERCEPTED = 0x27000101, SECURITY_AUDIT_NOTIFY_EVENT_USER_SPACE_DATA_TRANSFER = 0x2F000000, SECURITY_AUDIT_NOTIFY_EVENT_USER_SPACE_DATA_TRANSFER_POLICY = 0x2F000001, SECURITY_AUDIT_NOTIFY_EVENT_SERIAL_PORT_ACCESS = 0x30000100, SECURITY_AUDIT_NOTIFY_EVENT_NETWORK_INTERCEPTED = 0x03000002, SECURITY_AUDIT_NOTIFY_EVENT_WIFI_INTERCEPTED = 0x03000100, SECURITY_AUDIT_NOTIFY_EVENT_PRINT_INTERCEPTED = 0x2E000001 } | 定义通知事件的事件ID。 |
| SecurityAudit_Auth_Event { SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE = 0x1C801100, SECURITY_AUDIT_AUTH_EVENT_FILE_OPEN = 0x1C801101, SECURITY_AUDIT_AUTH_EVENT_FILE_RENAME = 0x1C801102, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETE = 0x1C801103, SECURITY_AUDIT_AUTH_EVENT_FILE_SETEXTATTR = 0x1C801104, SECURITY_AUDIT_AUTH_EVENT_FILE_DELETEEXTATTR = 0x1C801105 } | 定义阻断事件的事件ID。 |
| SecurityAudit_FilterType { EVENT_TYPE_EQUAL = 0x00000100, EVENT_SUBTYPE_EQUAL = 0x00000200, FILE_PATH_EQUAL = 0x00010000, FILE_PATH_PREFIX = 0x00010001, FILE_PATH_SUFFIX = 0x00010002, PROCESS_UID_EQUAL = 0x00020000, PROCESS_PID_EQUAL = 0x00020100, PROCESS_NAME_EQUAL = 0x00020200, PROCESS_NAME_PREFIX = 0x00020201, PROCESS_NAME_SUFFIX = 0x00020202 } | 定义过滤器类型。 |
| SecurityAudit_AuthResult { SECURITY_AUDIT_AUTH_RESULT_ALLOW = 0, SECURITY_AUDIT_AUTH_RESULT_DENY = 1 } | 定义阻断结果的类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t HMS_SecurityAudit_NewClient (SecurityAudit_Client **client, SecurityAudit_Handler handler) | 创建一个新的通知事件客户端。 |
| int32_t HMS_SecurityAudit_DeleteClient (SecurityAudit_Client *client) | 删除通知客户端。 |
| int32_t HMS_SecurityAudit_Subscribe (const SecurityAudit_Client *client, const SecurityAudit_Notify_Event *events, uint64_t count) | 订阅通知事件。 |
| int32_t HMS_SecurityAudit_Unsubscribe (const SecurityAudit_Client *client, const SecurityAudit_Notify_Event *events, uint64_t count) | 取消订阅通知事件。 |
| int32_t HMS_SecurityAudit_AddFilter (const SecurityAudit_Client *client, SecurityAudit_Notify_Event event, const SecurityAudit_Filter *filter) | 为通知事件添加过滤条件。 |
| int32_t HMS_SecurityAudit_RemoveFilter (const SecurityAudit_Client *client, SecurityAudit_Notify_Event event, const SecurityAudit_Filter *filter) | 删除通知事件的过滤条件。 |
| int32_t HMS_SecurityAudit_NewAuthClient (SecurityAudit_AuthClient **client, SecurityAudit_Handler handler) | 创建一个新的阻断类事件客户端。 |
| int32_t HMS_SecurityAudit_DeleteAuthClient (SecurityAudit_AuthClient *client) | 删除阻断类事件客户端。 |
| int32_t HMS_SecurityAudit_SubscribeAuthEvent (const SecurityAudit_AuthClient *client, const SecurityAudit_Auth_Event *events, uint64_t count) | 订阅阻断类事件。 |
| int32_t HMS_SecurityAudit_UnsubscribeAuthEvent (const SecurityAudit_AuthClient *client, const SecurityAudit_Auth_Event *events, uint64_t count) | 取消订阅阻断类事件。 |
| int32_t HMS_SecurityAudit_AddAuthEventFilter (const SecurityAudit_AuthClient *client, SecurityAudit_Auth_Event event, const SecurityAudit_Filter *filter) | 为阻断类事件添加过滤条件。 |
| int32_t HMS_SecurityAudit_RemoveAuthEventFilter (const SecurityAudit_AuthClient *client, SecurityAudit_Auth_Event event, const SecurityAudit_Filter *filter) | 删除阻断类事件的过滤条件。 |
| int32_t HMS_SecurityAudit_Auth (const SecurityAudit_AuthClient *client, const SecurityAudit_Event *event, SecurityAudit_AuthResult authResult) | 设置审计事件的阻断结果。 |
| int32_t HMS_SecurityAudit_QueryAllProcesses (char** result) | 获取所有的应用进程信息。 |
| int32_t HMS_SecurityAudit_QueryProcesses (uint64_t* pids, uint64_t count, char** result) | 获取输入的pid的应用进程信息。 |