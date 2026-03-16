[]()[]()

# SecurityAudit（安全审计）

提供统一的安全审计数据订阅与取消订阅接口，应用可以获取设备上的安全审计数据，以支撑审计业务。

**起始版本：**5.0.0(12)

[]()[]()

#### 导入模块

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
```

[]()[]()

#### AuditEventInfo

用于订阅或取消订阅接口的请求参数。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

eventId

number

否

否

审计事件ID，用于指定需要获取的安全审计数据。例如：0x810800800

审计事件ID的取值范围是[0, 0xFFFFFFFFF]。

[]()[]()

#### AuditEvent

安全审计数据。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

eventId

number

否

否

审计事件ID，与请求参数中的审计事件ID相同。

version

string

否

是

审计事件版本号。

timestamp

string

否

是

审计事件发生时间。格式为： YYYYMMDDHHMMSS

content

string

否

是

审计事件内容。不同审计事件具备不同的内容，内容为json格式字符串。例如：{"type": 1}

userId

number

否

是

发生审计事件时，登录的用户ID。

deviceId

string

否

是

审计事件发生的设备ID。

metadata

string

否

是

审计事件元数据。包含事件版本号、事件接收时间、设备ID和用户ID。**起始版本：**6.0.0(20)

[]()[]()

#### NotifyEvent

通知类事件枚举。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

名称

值

说明

PASTEBOARD

0x27000000

剪切板复制粘贴事件。

FILE

0x1C000007

文件事件。

FILE_INTERCEPTED

0x1C001100

文件访问规则违规事件。

ACCOUNT

0x10000100

帐户登录或注销事件。

WINDOW

0x07000000

屏幕截图、屏幕录制或屏幕投影事件。

VOLUME

0x0F000000

可移动存储设备的插入或移除事件。

PRINTER

0x2E000000

打印机事件。

PROCESS

0x1C000008

进程创建或退出事件。

NETWORK_TRAFFIC

0x1C00000E

网络流量事件。

NETWORK_CONN

0x1C00000F

网络连接事件。

CAMERA

0x2D000000

相机事件。

APP

0x10000000

应用程序事件。

EDM

0x11000000

企业设备管理事件。

CERT

0x12003000

证书操作事件。

KIA_CREATE

0x1C00000B

KIA文件创建事件。

KIA_READ

0x1C000012

KIA文件读取事件。

KIA_VARIANT

0x1C00000C

关键信息资产（KIA）文件变化事件。

KIA_INTERCEPT

0x1C00000A

KIA文件拦截事件。

PERMISSION

0x0B000000

应用程序权限更改事件。

DNS

0x03000001

DNS审计事件。

APP_INSTALL_INTERCEPTED

0x18000100

应用程序安装拦截事件。

APP_UNINSTALL_INTERCEPTED

0x18000101

应用程序卸载拦截事件。

APP_UPDATE_INTERCEPTED

0x18000102

应用程序更新拦截事件。

APP_RECOVER_INTERCEPTED

0x18000103

应用程序恢复拦截事件。

APP_START_INTERCEPTED

0x18000104

应用程序启动拦截事件。

USB_ACCESS_INTERCEPTED

0x30000000

USB访问拦截事件。

[]()[]()

#### FilterType

事件过滤类型枚举。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

名称

值

说明

EVENT_TYPE_EQUAL

0x00000100

事件类型的过滤器类型。

EVENT_SUBTYPE_EQUAL

0x00000200

事件子类型的过滤器类型。

FILE_PATH_EQUAL

0x00010000

文件路径类型的过滤器类型。

FILE_PATH_PREFIX

0x00010001

文件路径前缀类型的过滤器类型。

FILE_PATH_SUFFIX

0x00010002

文件路径后缀类型的过滤器类型。

PROCESS_UID_EQUAL

0x00020000

过滤进程的UID类型。

PROCESS_PID_EQUAL

0x00020100

过滤进程ID类型。

PROCESS_NAME_EQUAL

0x00020200

筛选进程名称类型。

PROCESS_NAME_PREFIX

0x00020201

进程名称前缀的过滤类型。

PROCESS_NAME_SUFFIX

0x00020202

进程名称后缀的过滤类型。

[]()[]()

#### AuthEvent

阻断类事件枚举。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

名称

值

说明

FILE_CREATE

0x1C801100

文件创建阻断事件。

FILE_OPEN

0x1C801101

文件打开阻断事件。

FILE_RENAME

0x1C801102

文件重命名阻断事件。

FILE_DELETE

0x1C801103

文件删除阻断事件。

FILE_SETEXTATTR

0x1C801104

文件设置扩展属性的阻断事件。

FILE_DELETEEXTATTR

0x1C801105

文件删除扩展属性的阻断事件。

[]()[]()

#### AuthResult

阻断结果的枚举。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

名称

值

说明

ALLOW

0

对阻断事件放行操作。

DENY

1

对阻断事件拒绝操作。

[]()[]()

#### on('auditEventOccur')

on(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](#section1962713117486), callback: Callback<[AuditEvent](#section5557545175113)>): void

订阅安全审计数据。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

订阅的事件类型名称，固定值 'auditEventOccur'，表示审计事件。

auditEventInfo

[AuditEventInfo](#section1962713117486)

是

订阅的审计数据信息。

callback

Callback<[AuditEvent](#section5557545175113)>

是

用于接收审计事件的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

401

invalid parameters.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};

try {
  hilog.info(0x0000, TAG, 'on begin.');
  securityAudit.on('auditEventOccur', auditEventInfo, callback);
  hilog.info(0x0000, TAG, 'Succeeded in on.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### off('auditEventOccur')

off(type: 'auditEventOccur', auditEventInfo: [AuditEventInfo](#section1962713117486), callback?: Callback<[AuditEvent](#section5557545175113)>): void

取消订阅安全审计数据。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

取消订阅的事件类型名称，固定值 ‘auditEventOccur’，表示审计事件。

auditEventInfo

[AuditEventInfo](#section1962713117486)

是

取消订阅的审计数据信息。

callback

Callback<[AuditEvent](#section5557545175113)>

否

用于接收审计数据的回调函数。如果传入了callback，则取消该callback的订阅，否则取消所有callback的订阅。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

401

invalid parameters.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuditJsTest";
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};

try {
  hilog.info(0x0000, TAG, 'off begin.');
  securityAudit.off('auditEventOccur', auditEventInfo);
  hilog.info(0x0000, TAG, 'Succeeded in off.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### Filter

用户提供的过滤条件信息。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

isInclude

boolean

否

否

过滤标签，决定符合条件的事件是否返回给订阅者。

**true**：设置反过滤，符合过滤条件的事件将返回给订阅者。

**false**：设置过滤，符合过滤条件的事件将不会返回给订阅者。

type

[FilterType](#section141981957164611)

否

否

过滤类型。

values

string[]

否

否

过滤条件的值的数组。

[]()[]()

#### Client

为通知客户端提供条件。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

需要通过[newClient](#section1137616421363)构造实例。

[]()[]()

#### subscribe

subscribe(events: NotifyEvent[]): void

订阅通知事件。

**需要权限**：ohos.permission.QUERY_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

events

[NotifyEvent](#section116663494309)[]

是

需要订阅的通知事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  client?.subscribe([0x02D000000]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### unsubscribe

unsubscribe(events: NotifyEvent[]): void

取消订阅通知事件。

**需要权限**：ohos.permission.QUERY_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

events

[NotifyEvent](#section116663494309)[]

是

已订阅的通知事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  client?.unsubscribe([0x02D000000]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### addFilter

addFilter(event: NotifyEvent, filter: Filter): void

为通知事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**需要权限**：ohos.permission.QUERY_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

[NotifyEvent](#section116663494309)

是

通知事件ID。

filter

[Filter](#section17889177696)

是

通知事件的过滤器。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000004

The number of filters exceeds the upper limit.

1012000005

The event does not support the filter condition.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : ["2"]
};
try {
  client = securityAudit.newClient(callback);
  client?.addFilter(0x02D000000, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### removeFilter

removeFilter(event: NotifyEvent, filter: Filter): void

删除通知事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**需要权限**：ohos.permission.QUERY_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

[NotifyEvent](#section116663494309)

是

通知事件ID 。

filter

[Filter](#section17889177696)

是

通知事件的过滤器。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000005

The event does not support the filter condition.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let filter : securityAudit.Filter = {
  type: 0x00000200,
  isInclude: true,
  values : ["2"]
};
try {
  client = securityAudit.newClient(callback);
  client?.removeFilter(0x02D000000, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### newClient

newClient(callback: Callback<[AuditEvent](#section5557545175113)>): Client

创建一个新的通知客户端，该客户端提供的方法可以实现通知类事件的订阅、过滤功能。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

callback

Callback<[AuditEvent](#section5557545175113)>

是

用于接收审计数据的回调函数。

**返回值：**

类型

说明

[Client](#section119445151153)

通知类客户端实例对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000002

The number of clients exceeds the global upper limit.

1012000003

The number of clients exceeds the current process upper limit.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### deleteClient

deleteClient(client: Client): void

删除通知客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

client

[Client](#section119445151153)

是

通知客户端信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let client: securityAudit.Client | undefined = undefined;
const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
try {
  client = securityAudit.newClient(callback);
  securityAudit.deleteClient(client);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### AuthClient

为阻断类事件客户端提供条件。

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

需要通过[newAuthClient](#section1768135711112)构造实例。

[]()[]()

#### subscribe

subscribe(events: AuthEvent[]): void

订阅阻断事件。

**需要权限**：ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

events

[AuthEvent](#section131951026124112)[]

是

要订阅的阻断事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### unsubscribe

unsubscribe(events: AuthEvent[]): void

取消订阅阻断事件。

**需要权限**：ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

events

[AuthEvent](#section131951026124112)[]

是

已订阅的阻断事件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.subscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.unsubscribe([securityAudit.AuthEvent.FILE_CREATE]);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### addFilter

addFilter(event: AuthEvent, filter: Filter): void

为阻断事件添加过滤条件，符合过滤条件的事件将根据过滤器中的过滤标签决定是否返回给用户。

**需要权限**：ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

[AuthEvent](#section131951026124112)

是

阻断事件ID。

filter

[Filter](#section17889177696)

是

阻断事件的过滤器。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000004

The number of filters exceeds the upper limit.

1012000005

The event does not support the filter condition.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS_PID_EQUAL,
  isInclude: true,
  values : ["2"]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### removeFilter

removeFilter(event: AuthEvent, filter: Filter): void

删除阻断事件的过滤条件，满足该过滤条件的事件将不会再根据过滤器中的过滤标签进行处理。

**需要权限**：ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

[AuthEvent](#section131951026124112)

是

阻断事件ID 。

filter

[Filter](#section17889177696)

是

阻断事件的过滤器。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000005

The event does not support the filter condition.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
let filter : securityAudit.Filter = {
  type: securityAudit.FilterType.PROCESS_PID_EQUAL,
  isInclude: true,
  values : ["2"]
};
try {
  authClient?.addFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
}
try {
  authClient?.removeFilter(securityAudit.AuthEvent.FILE_CREATE, filter);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### auth

auth(auditEvent: AuditEvent, authResult: AuthResult): void

设置阻断事件的阻断结果，审计模块会根据阻断结果对事件进行放行或拒绝的处理。

**需要权限**：ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力**：SystemCapability.Security.SecurityAudit

**起始版本**：6.0.0(20)

**参数：**

参数名

类型

必填

说明

auditEvent

[AuditEvent](#section5557545175113)

是

阻断事件信息 。

authResult

[AuthResult](#section10801114725511)

是

阻断结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000007

The auth event cannot be found.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const allowEventCallback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
  try {
    authClient?.auth(event, securityAudit.AuthResult.ALLOW);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, TAG, 'allowEventCallback', 'auth error:' + e.code);
  }
};
try {
  authClient = securityAudit.newAuthClient(allowEventCallback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### newAuthClient

newAuthClient(callback: Callback<[AuditEvent](#section5557545175113)>): AuthClient

创建一个新的阻断客户端，该客户端提供的方法可以实现阻断类事件的订阅、过滤和阻断功能。

**需要权限：**ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

callback

Callback<[AuditEvent](#section5557545175113)>

是

用于接收审计数据的回调函数。

**返回值：**

类型

说明

[AuthClient](#section85535761112)

阻断类客户端实例对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000002

The number of clients exceeds the global upper limit.

1012000003

The number of clients exceeds the current process upper limit.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### deleteAuthClient

deleteAuthClient(client: AuthClient): void

删除阻断客户端，用户将无法使用该客户端提供的方法，并会清空客户端记录的订阅与过滤信息。

**需要权限：**ohos.permission.kernel.AUTH_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

client

[AuthClient](#section85535761112)

是

阻断客户端信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditAuthJsTest";
let authClient: securityAudit.AuthClient | undefined = undefined;
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_Auth_JsApi_Func metadata= ' + event.metadata);
};
try {
  authClient = securityAudit.newAuthClient(callback);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
try {
  securityAudit.deleteAuthClient(authClient);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### queryAllProcesses

queryAllProcesses(): string;

查询获取所有的应用进程信息。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

string

应用进程信息内容，内容为json格式字符串。例如：{"1": {}}。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditJsTest";
try {
  hilog.info(0x0000, TAG, 'queryAllProcesses begin.');
  const result = securityAudit.queryAllProcesses();
  hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
}
```

[]()[]()

#### queryProcesses

queryProcesses(pids: number[]): string;

查询获取输入的PID的应用进程信息。

**需要权限：**ohos.permission.QUERY_AUDIT_EVENT

**系统能力：**SystemCapability.Security.SecurityAudit

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

pids

number[]

是

要查询的进程ID组。

**返回值：**

类型

说明

string

应用进程信息内容，内容为json格式字符串。例如：{"1": {}}。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SecurityAudit（安全审计） (devicesecurity-arktsapi-errcode-securityaudit).md)**。**

错误码ID

错误信息

201

check permission fail.

1012000001

Internal error.

1012000006

The number of queried processes exceeds the threshold.

**示例：**

```ets
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SecurityAuditJsTest";
let pids: number[] = [1, 2];
try {
  hilog.info(0x0000, TAG, 'queryProcesses begin.');
  const result = securityAudit.queryProcesses(pids);
  hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message);
}
```