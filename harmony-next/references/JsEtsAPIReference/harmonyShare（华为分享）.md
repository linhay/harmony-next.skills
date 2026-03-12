# harmonyShare（华为分享）

本模块提供华为分享的事件注册。

**模型约束：**此模块的接口仅可在Stage模型下使用。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { harmonyShare } from '@kit.ShareKit';
```

#### SharableErrorCode

拒绝分享回调时，提供拒绝原因，用户可收到系统通知消息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**5.0.3(15)

名称

值

说明

NO_CONTENT_ERROR

1

用于无内容分享场景。

NO_INTERNET_ERROR

2

用于无网络场景。

DOWNLOAD_ERROR

3

用于下载失败场景。

#### ReceivableErrorCode

拒绝沙箱接收回调时，提供拒绝原因，用户可收到系统通知消息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

值

说明

NO_RECEIVABLE_ERROR

1

用于当前无法接收数据的场景。

#### ShareResultCode

沙箱接收结果通知成功或失败原因。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

值

说明

SHARE_SUCCESS

0

沙箱接收成功。

SEND_FAILED

1

数据传输失败。

CANCEL_BY_SENDER

2

发送端取消发送。

CANCEL_BY_RECEIVER

3

接收端取消接收。

#### SharableTarget

华为分享事件触发后回调参数，可通过此参数跨端分享。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**5.0.0(12)

#### share

share(data: systemShare.SharedData): Promise<void>

跨端分享，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

data

[systemShare.SharedData](systemShare（分享）.md#section816451553012)

是

分享数据。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

#### reject

reject(error: SharableErrorCode): Promise<void>

当开发者收到回调时，由于某些原因无法继续分享时，可选择拒绝本次分享，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**5.0.3(15)

**参数：**

参数名

类型

必填

说明

error

[SharableErrorCode](#section98742174617)

是

拒绝本次分享的原因。通过系统弹窗提示用户。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

#### updateShareData

updateShareData(data: UpdatedData): Promise<void>

在分享数据未发送前，开发者可通过此接口更新预览图，使用Promise异步回调。

仅支持碰一碰分享功能。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

data

[UpdatedData](#section108971112124018)

是

需要更新的数据信息。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

#### clarifyNonShare

clarifyNonShare(info: SharableErrorInfo): Promise<void>

当开发者收到回调时，可通过此接口告知用户当前界面无可分享内容，并给出恰当的提示引导用户。

仅支持碰一碰分享功能。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.2(22)

**参数：**

参数名

类型

必填

说明

info

[SharableErrorInfo](#section10176454018)

是

提示信息，用于告知用户无法分享的原因。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

#### ReceivableTarget

沙箱接收事件触发后回调参数，可通过此参数进行沙箱接收。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

#### receive

receive(receiveUri: string, callback: ReceiveCallback): Promise<void>

提供沙箱接收目录uri，接收的文件将保存至此目录下，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

receiveUri

string

是

沙箱接收时，存放数据的目录（必须真实存在）。

 说明：

Share Kit会在传输开始前获取此目录的授权，在数据传输完成后自动撤销授权，建议使用已存在的空文件夹，保护信息安全。

callback

[ReceiveCallback](#section496835162818)

是

沙箱接收的回调。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

#### reject

reject(error: ReceivableErrorCode): Promise<void>

当开发者收到回调时，由于某些原因无法继续接收分享内容时，可选择拒绝本次接收，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

error

[ReceivableErrorCode](#section1884011169111)

是

拒绝本次沙箱接收的原因。通过系统弹窗提示用户。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

#### UpdatedData

华为分享事件发送的数据信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

thumbnailUri

string

否

是

预览图的uri。

#### BaseCapabilityRegistry

华为分享事件注册基础配置。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

windowId

number

否

否

窗口id。

#### SendCapabilityRegistry

华为分享事件窗口注册配置项。继承[BaseCapabilityRegistry](#section7252115555417)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

sendOnly

boolean

否

是

设置是否仅支持发送数据。默认值：false，表示可同时接收分享数据。当双端设备均设置为true时，双向分享会被拦截。

 说明：

仅支持碰一碰分享功能。

#### RecvCapability

设置沙箱接收支持的能力范围（可接收的文件类型及最大数量限制）。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

utd

string

否

否

统一数据类型，参考[@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor)。

maxSupportedCount

number

否

否

可接收文件的最大数量限制，仅允许设置大于0的整数。

#### RecvCapabilityRegistry

沙箱接收事件窗口注册配置项。继承[BaseCapabilityRegistry](#section7252115555417)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

capabilities

[RecvCapability](#section5644182344013)[]

否

否

沙箱接收能力设置，用于设置可接收的数据类型和数量。

#### TransferBaseResults

沙箱接收时，文件数据传输完成的回调函数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

onResult

Callback<[ShareResultCode](#section943818433405)>

否

是

传输完成的回调函数。用于通知传输结果。

#### ReceiveCallback

沙箱接收传输完成后回调函数。可用此方法监听完成事件，并处理接收后的数据。继承[TransferBaseResults](#section54808149718)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

onDataReceived

Callback<[systemShare.SharedData](systemShare（分享）.md#section816451553012)>

否

否

沙箱接收传输完成后回调函数。用于接收已保存至沙箱路径下的文件列表。

#### SharableErrorInfo

提示信息，用于告知用户无法分享的原因。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.2(22)

名称

类型

只读

可选

说明

message

string

否

是

提示文案。

#### on('knockShare')

on(event: 'knockShare', callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在Tablet中无效果，在其他设备类型中可正常调用。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。

callback

Callback<[SharableTarget](#section9147845115614)>

是

事件回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

**示例：**

```ets
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 构造分享数据
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: '这是一段文本内容'
  });
  // 发起分享
  sharableTarget.share(shareData);
});
```

#### off('knockShare')

off(event: 'knockShare', callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在Tablet中无效果，在其他设备类型中可正常调用。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'knockShare'，取消设备轻贴的事件监听。

callback

Callback<[SharableTarget](#section9147845115614)>

否

回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

**示例：**

```ets
// 取消设备轻贴'knockShare'监听事件
harmonyShare.off('knockShare');
```

#### on('knockShare')

on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册设备轻贴的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在Tablet中无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'knockShare'，当设备轻贴时，触发该事件。

capability

[SendCapabilityRegistry](#section7361949172719)

是

事件属性。

callback

Callback<[SharableTarget](#section9147845115614)>

是

事件回调。

**示例：**

```ets
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
}
// 注册设备轻贴'knockShare'监听事件
harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
  // 构造分享数据
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: '这是一段文本内容'
  });
  // 发起分享
  sharableTarget.share(shareData);
});
```

#### off('knockShare')

off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消设备轻贴的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在Tablet中无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'knockShare'，取消设备轻贴的事件监听。

capability

[SendCapabilityRegistry](#section7361949172719)

是

事件属性。

callback

Callback<[SharableTarget](#section9147845115614)>

否

回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。

**示例：**

```ets
let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
}
// 取消设备轻贴'knockShare'监听事件
harmonyShare.off('knockShare', capabilityRegistry);
```

#### on('gesturesShare')

on(event: 'gesturesShare', callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。

callback

Callback<[SharableTarget](#section9147845115614)>

是

事件回调。

**示例：**

```ets
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

// 注册隔空传送'gesturesShare'监听事件
harmonyShare.on('gesturesShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // 构造分享数据
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: '这是一段文本内容'
  });
  // 发起分享
  sharableTarget.share(shareData);
});
```

#### off('gesturesShare')

off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'gesturesShare'，取消隔空传送的事件监听。

callback

Callback<[SharableTarget](#section9147845115614)>

否

回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。

**示例：**

```ets
// 取消隔空传送'gesturesShare'监听事件
harmonyShare.off('gesturesShare');
```

#### on('gesturesShare')

on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

注册隔空传送的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'gesturesShare'，当抓取握拳时，触发该事件。

capability

[SendCapabilityRegistry](#section7361949172719)

是

事件属性。

callback

Callback<[SharableTarget](#section9147845115614)>

是

事件回调。

**示例：**

```ets
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
}
// 注册隔空传送'gesturesShare'监听事件
harmonyShare.on('gesturesShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
  // 构造分享数据
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: '这是一段文本内容'
  });
  // 发起分享
  sharableTarget.share(shareData);
});
```

#### off('gesturesShare')

off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

取消隔空传送的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'gesturesShare'，取消隔空传送的事件监听。

capability

[SendCapabilityRegistry](#section7361949172719)

是

事件属性。

callback

Callback<[SharableTarget](#section9147845115614)>

否

回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。

**示例：**

```ets
let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
}
// 取消隔空传送'gesturesShare'监听事件
harmonyShare.off('gesturesShare', capabilityRegistry);
```

#### on('dataReceive')

on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void

注册沙箱接收事件监听。仅支持文件类型数据。文本（包含链接）类型的数据保持原有接收逻辑。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'dataReceive'，当手机设备轻贴PC/2in1设备屏幕时，触发该事件。

capability

[RecvCapabilityRegistry](#section145341487280)

是

事件属性。

callback

Callback<[ReceivableTarget](#section13539165583)>

是

事件回调。

**示例：**

```ets
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { common } from '@kit.AbilityKit';

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
  capabilities: [{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }]
}
// 注册沙箱接收'dataReceive'监听事件
harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
  let uiContext: UIContext = this.getUIContext();
  let context = uiContext.getHostContext() as common.UIAbilityContext;
  receivableTarget.receive(context.filesDir, { // 此路径仅为示例 使用时请替换实际路径
    onDataReceived: (sharedData: systemShare.SharedData) => {
      let sharedRecords = sharedData.getRecords();
      sharedRecords.forEach((record: systemShare.SharedRecord) => {
        // 处理分享数据
      });
    },
    onResult(resultCode: harmonyShare.ShareResultCode) {
      if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
        // To do things.
      }
    }
  });
});
```

#### off('dataReceive')

off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void

取消沙箱接收的事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.HarmonyShare

**设备行为差异：**该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.0(20)

参数名

类型

必填

说明

event

string

是

事件回调类型，取值为'dataReceive'，取消沙箱接收的事件监听。

capability

[RecvCapabilityRegistry](#section145341487280)

是

事件属性。

callback

Callback<[ReceivableTarget](#section13539165583)>

否

回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。

**示例：**

```ets
let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
  capabilities: [{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }]
}
// 取消沙箱接收'dataReceive'监听事件
harmonyShare.off('dataReceive', capabilityRegistry);
```