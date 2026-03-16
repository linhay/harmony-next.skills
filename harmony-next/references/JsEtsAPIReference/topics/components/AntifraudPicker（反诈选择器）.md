# AntifraudPicker（反诈选择器）

本模块提供获取诈骗消息、诈骗通话记录的接口，应用可以获取选择的消息或通话记录数据，以支撑反诈业务。

**起始版本：**5.0.3(15)

#### 导入模块

```ets
import {antifraudPicker} from '@kit.DeviceSecurityKit';
```

#### AntifraudMessageOptions

获取诈骗消息的请求参数。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

maxSelectNumber

number

否

是

最大可选项数。如果不传，则默认为50。取值范围为1~50。

#### SingleAntifraudMessageInfo

单条诈骗消息信息。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

senderNumber

string

否

否

消息发送方号码。

receivingTime

number

否

否

消息接收时间戳，单位：毫秒。

messageContent

string

否

否

消息内容，最长17152个字符。

senderName

string

否

否

发送方名称。

senderPlace

string

否

否

消息发送方号码归属地。

messageType

string

否

否

消息类型。'0' ：短信，'1'：彩信。

mmsSubject

string

否

是

彩信主题。该字段仅当消息类型为彩信时生效。

mmsAttachments

[MmsAttachmentInfo](#section14579643718)[]

否

是

彩信附件信息列表。该字段仅当消息类型为彩信时生效。

#### MmsAttachmentInfo

彩信附件信息。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

attachmentType

number

否

否

彩信附件类型。

- -1：彩信未下载；
- 0：smil文件；
- 1：图片；
- 2：视频；
- 3：音频；
- 4：联系人卡片；
- 5：主题；
- 6：幻灯片；
- 7：文本；
- 8：位置。

uri

string

否

否

附件URI。

#### AntifraudMessageResult

诈骗消息结果。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

messageInfo

[SingleAntifraudMessageInfo](#section143653475548)[]

否

否

诈骗消息结果列表。

#### SingleAntifraudCallLogInfo

单条诈骗通话记录信息。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

callerNumber

string

否

否

来电方号码。

receivingTime

number

否

否

接听通话的时间戳，单位：毫秒。

callLogType

number

否

否

通话记录类型。0：来电，1：拨出。

callerName

string

否

否

来电方名称。

callDuration

number

否

否

通话时长，单位：毫秒。

#### AntifraudCallLogResult

诈骗通话记录结果。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

callLogInfo

[SingleAntifraudCallLogInfo](#section123791738142115)[]

否

否

诈骗通话记录列表。

#### AntifraudCallLogOptions

获取诈骗通话记录的请求参数。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**名称**

**类型**

****只读

可选

**说明**

maxSelectNumber

number

否

是

最大可选项数。如果不传，则默认为50。取值范围为1~50。

#### selectFraudMessage

selectFraudMessage(context: common.Context, options?: [AntifraudMessageOptions](#section11617213173419)): Promise<[AntifraudMessageResult](#section1874123611170)>

拉起诈骗消息选择器，并获取用户选择的诈骗消息信息。使用Promise异步回调。

**需要权限：**ohos.permission.USE_FRAUD_MESSAGES_PICKER

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**参数**：

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

应用上下文。

options

[AntifraudMessageOptions](#section11617213173419)

否

请求参数。如果不传，则最大可选项数默认为50。

**返回值：**

类型

说明

Promise<[AntifraudMessageResult](#section1874123611170)>

Promise对象，返回诈骗消息结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)**。**

错误码ID

错误信息

201

Permission denied. Interface caller does not have permission "ohos.permission.USE_FRAUD_MESSAGES_PICKER".

401

Input parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1017100001

Unknown error.

1017100002

The device type is not supported.

**示例：**

```ets
import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// 请求获取诈骗消息信息，并进行业务处理
let options: antifraudPicker.AntifraudMessageOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
}

```

#### selectFraudCallLog

selectFraudCallLog(context: common.Context, options?: [AntifraudCallLogOptions](#section27151161387)): Promise<[AntifraudCallLogResult](#section1746504983517)>

拉起诈骗通话记录选择器，并获取用户选择的诈骗通话记录信息。使用Promise异步回调。

**需要权限：**ohos.permission.USE_FRAUD_CALL_LOG_PICKER

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.0.3(15)

**参数**：

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

应用上下文。

options

[AntifraudCallLogOptions](#section27151161387)

否

请求参数。如果不传，则最大可选项数默认为50。

**返回值：**

类型

说明

Promise<[AntifraudCallLogResult](#section1746504983517)>

Promise对象，返回诈骗通话记录结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)**。**

错误码ID

错误信息

201

Permission denied. Interface caller does not have permission "ohos.permission.USE_FRAUD_CALL_LOG_PICKER".

401

Input parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1017100001

Unknown error.

1017100002

The device type is not supported.

**示例：**

```ets
import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// 请求获取诈骗通话记录信息，并进行业务处理
let options: antifraudPicker.AntifraudCallLogOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
}

```

#### AntifraudAppOptions

获取诈骗应用的请求参数。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.1.1(19)

**名称**

**类型**

****只读

可选

**说明**

maxSelectNumber

number

否

是

最大可选项数。如果不传，则默认为50。取值范围为1~50。

#### AntifraudAppResult

诈骗应用结果。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.1.1(19)

**名称**

**类型**

****只读

可选

**说明**

appInfo

[SingleAntifraudAppInfo](#section244421110162)[]

否

否

诈骗应用列表。

#### SingleAntifraudAppInfo

单条诈骗应用信息。

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.1.1(19)

**名称**

**类型**

****只读

可选

**说明**

applicationName

string

否

否

应用程序的名称。

bundleName

string

否

否

APP包名。

versionCode

number

否

否

应用版本编码。

versionName

string

否

否

应用版本名称。

installTime

number

否

否

应用安装时间戳，单位：毫秒。

appId

string

否

否

应用ID。

label

string

否

否

应用名称，为用户视角的应用名称，如”时钟”。

installSource

string

否

否

应用程序的安装来源，支持的取值如下：

- pre-installed表示应用为第一次开机时安装的预置应用。

- ota表示应用为系统升级时新增的预置应用。

- recovery表示卸载后再恢复的预置应用。

- 安装来源的格式为包名表示应用由此包名对应的应用安装。

- unknown表示应用安装来源未知

#### selectFraudApp

selectFraudApp(context: common.Context, options?: [AntifraudAppOptions](#section1550072910133)): Promise<[AntifraudAppResult](#section13366182610149)>

拉起诈骗应用选择器，并获取用户选择的诈骗应用信息。使用Promise异步回调。

**需要权限：**ohos.permission.USE_FRAUD_APP_PICKER

**系统能力：**SystemCapability.Security.Antifraud

**起始版本：**5.1.1(19)

**参数**：

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

应用上下文。

options

[AntifraudAppOptions](#section1550072910133)

否

请求参数。如果不传，则最大可选项数默认为50。

**返回值：**

类型

说明

Promise<[AntifraudAppResult](#section13366182610149)>

Promise对象，返回诈骗应用结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)**。**

错误码ID

错误信息

201

Permission denied. Interface caller does not have permission "ohos.permission.USE_FRAUD_APP_PICKER".

1017600001

Unknown error.

1017600002

The device type is not supported.

1017600003

Parameter verification failed.

**示例：**

```ets
import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

const TAG = "AntifraudPickerJsTest";

// 请求获取诈骗应用信息，并进行业务处理
let options: antifraudPicker.AntifraudAppOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudApp begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudAppResult = await antifraudPicker.selectFraudApp(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudApp failed: %{public}d %{public}s', e.code, e.message);
}

```