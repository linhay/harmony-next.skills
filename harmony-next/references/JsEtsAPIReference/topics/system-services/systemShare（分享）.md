# systemShare（分享）

本模块提供分享数据创建及分享面板拉起的功能，提供多种系统标准分享服务，例如分享数据给其他应用、复制、打印等。

- 分享接入应用需要配置、呈现和关闭分享面板。
- 分享面板的配置包括数据对象、呈现视图的方式、预览模式等。

**模型约束：**此模块的接口仅可在Stage模型下使用。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { systemShare } from '@kit.ShareKit';
```

#### SharedRecord

用于构造一条分享数据记录。包含数据类型、数据内容及描述等信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

utd

string

否

否

统一数据类型，参考[@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor)

建议开发者传入精准的数据类型，有助于匹配到精确的目标应用，参见：[Share Kit体验规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-precautions)

title

string

否

是

如果是文本、链接等内容，建议填入title标识其标题。缺省时，若分享内容为文本类型，则文本内容作为title字段；若分享内容为文件类型，则文件名作为title字段。

label

string

否

是

标识当前数据记录类型的标签，在单选模式时生效。缺省为[UniformDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor#ZH-CN_TOPIC_0000001930756561__uniformdatatype)类型相应的标签。具体如下：HYPERLINK显示为链接；HTML显示为网页；TEXT显示为文本；VIDEO显示为视频；AUDIO显示为音乐；IMAGE显示为图片；FILE显示为文件；

description

string

否

是

数据记录的描述。缺省为空字符串。

thumbnail

Uint8Array

否

是

数据记录缩略图。缺省时使用与分享内容类型匹配的图标作为缩略图。

建议开发者传入符合数据记录的缩略图，如无，可传入应用图标。

 说明：

限制图片大小：32KB以下。过大的图片可能导致want数据超限无法拉起分享，可使用[ImagePacker.packToData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodata13)压缩图片质量。

thumbnailUri

string

否

是

数据记录缩略图的uri。缺省时使用与分享内容类型匹配的图标作为缩略图。支持的uri类型：

- 应用文件uri，参见：[应用文件分享](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file)
- 用户文件uri，参见：[用户文件uri介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro)

**起始版本**：5.0.0(12)。

 说明：

与thumbnail字段同时存在时，优先使用thumbnail字段。

uri

string

否

是

数据记录的uri。支持的uri类型：

- 应用文件uri，参见：[应用文件分享](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file)
- 用户文件uri，参见：[用户文件uri介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro)

 说明：

沙箱路径可通过[fileUri.getUriFromPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath)方法获取文件URI。

content和uri二者至少有一个不为空。

content

string

否

是

数据记录内容。链接（包含App Linking）、文本类型的内容通过该字段传递。

 说明：

content和uri二者至少有一个不为空。

extraData

Record<string, string | number | boolean | Array<string | number | boolean>>

否

是

扩展数据，用于向目标应用/设备分享自定义的扩展内容。

#### ShareControllerOptions

分享控制器配置项。用于配置分享预览模式，选择模式等，决定了分享面板的显示样式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**需要权限：**如需使用appLaunchTrustInfo字段时，需申请权限ohos.permission.SET_SYSTEMSHARE_APPLAUNCHTRUSTLIST，该能力受限开放，仅支持企业应用限制内部数据分享到企业集团信任的应用。权限申请方式请参考[申请使用受限权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

anchor

[ShareControllerAnchor](#section19505934714) | string

否

是

类型为string时，表示分享面板关联的控件ID（[ArkUI组件常规属性的id值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes#常规属性)）。

类型为ShareControllerAnchor时，表示锚点位置。

不传此参数时，面板会显示在默认位置(居中)。

previewMode

[SharePreviewMode](#section71597311103)

否

是

预览的模式，缺省为卡片模式。

selectionMode

[SelectionMode](#section188631791714)

否

是

选择的模式，缺省为单选模式。

excludedAbilities

Array<[ShareAbilityType](#section205631342153016)>

否

是

操作区不需要显示的能力列表。

**起始版本**：5.0.0(12)。

appLaunchTrustInfo

Array<string>

否

是

通过配置[应用唯一标识符](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo#signatureinfo)（appIdentifier字段）列表，指定可分享的目标应用名单。仅取前50个配置项，超出部分不生效。需申请权限ohos.permission.SET_SYSTEMSHARE_APPLAUNCHTRUSTLIST，

该能力受限开放，仅支持企业应用限制内部数据分享到企业集团信任的应用。

**起****始版本**：6.0.1(21)。

#### ShareControllerAnchor

分享悬浮窗视图依附锚点，分享面板会根据屏幕大小选择是否在指定的位置显示悬浮窗。

设备屏幕宽度较小时，不会以悬浮形态展示，而是以模态形式/弹窗形式显示。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

windowOffset

[Offset](#section747515217482)

否

否

相对锚点的窗体偏移值。

size

[Size](#section16811150124912)

否

是

锚点矩形的尺寸，缺省时，锚点是一个点，即宽高都为0。

#### Offset

可以设置的相对锚点的窗口偏移值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

x

number

否

否

x点的坐标。单位：像素。

y

number

否

否

y点的坐标。单位：像素。

#### Size

锚点矩形的尺寸，缺省时，锚点是一个点，即宽高都为0。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

width

number

否

否

组件宽度，单位：像素。负数按0处理。

height

number

否

否

组件高度，单位：像素。负数按0处理。

#### ShareOperationResult

shareCompleted事件的返回值，用于获知用户分享渠道信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

targetAbilityInfo

[ShareAbilityInfo](#section8809223154210)

是

否

用户分享渠道的信息。

#### ShareAbilityInfo

用户分享渠道的信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

name

string

否

否

分享渠道的名称。

- 系统操作有固定名称。请参见：[ShareAbilityName](#section16531512163920)。
- 非系统操作采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。

#### ContactInfo

意图框架推荐联系人的信息。当分享到推荐联系人时，携带此参数用于区分。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

contactType

string

否

否

联系人类型：取值来源应用向意图捐赠数据中的entityName字段，例如"Contact"、"ChatGroup"。

contactId

string

否

否

联系人ID：取值来源应用向意图捐赠数据中的entityId字段。

#### SharePreviewMode

分享预览模式。图片、视频等格式推荐使用详细预览图模式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

值

说明

DEFAULT

0

默认模式（缩略图卡片）。推荐文本、链接等数据使用此模式。

DETAIL

1

详细预览图模式。推荐图片、视频等数据使用此模式。

#### SelectionMode

分享面板选择模式。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

名称

值

说明

SINGLE

0

单选模式，当传入多条分享数据记录（SharedRecord）时，需要用户多选一进行分享。

BATCH

1

批量模式，分享全部数据记录。

#### ShareAbilityType

系统能力类型定义。用于排除操作区的系统能力。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.0.0(12)

名称

值

说明

COPY_TO_PASTEBOARD

0

复制

SAVE_TO_MEDIA_ASSET

1

保存至图库

SAVE_AS_FILE

2

另存为

PRINT

3

打印

SAVE_TO_SUPERHUB

4

添加至中转站

#### ShareAbilityResultCode

从UIExtensionAbility返回的Code值。可控制分享面板的行为。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.0.0(12)

名称

值

说明

ERROR

-1

发生错误。如果同时传递message参数，将弹出toast提示。

BACK

0

用户点击返回按钮。返回分享面板。

CLOSE

1

用户点击关闭按钮。关闭分享面板。

#### ShareAbilityName

系统操作的名称，用于返回分享结果数据。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.1.0(18)

名称

值

说明

COPY_TO_PASTEBOARD

SystemShare_CopyToPasteboard

复制

SAVE_TO_MEDIA_ASSET

SystemShare_SaveToMediaAsset

保存至图库

SAVE_AS_FILE

SystemShare_SaveAsFile

另存为

PRINT

SystemShare_Print

打印

SAVE_TO_SUPERHUB

SystemShare_Superhub

添加至中转站

COLLECTION

SystemShare_Collection

小艺知识空间

HARMONYSHARE

SystemShare_HarmonyShare

华为分享

ENCRYPT

SystemShare_Encrypt

加密分享

#### SharedData

表示分享数据对象，提供封装一组数据记录的方法。

一个分享数据对象至少存在一条记录，开发者需要在SharedData实例化过程中，通过构造器第一个参数传入；当分享数据包含多条数据记录时，则需要使用addRecord(record: SharedRecord)方法追加记录。

数据记录当前最大可支持500条，且需同时满足数据总大小不超过IPC传输上限200KB。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

#### constructor

constructor(record: SharedRecord)

用于构造分享数据对象。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

record

[SharedRecord](#section20696483813)

是

分享数据记录对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});
```

#### addRecord

addRecord(record: SharedRecord): void

在当前分享数据中添加一条分享数据记录。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

record

[SharedRecord](#section20696483813)

是

要添加到分享数据对象中的数据记录，该记录为SharedRecord对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[分享服务错误码](../../errors/ArkTS API错误码 (share-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1003700001](../../errors/ArkTS API错误码.md#section16205152494111)

The number of records exceeds the maximum.

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});
```

#### getRecords

getRecords(): Array<SharedRecord>

获取当前分享数据中的所有数据记录。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Array<[SharedRecord](#section20696483813)>

当前分享数据对象内所包含的记录。

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

let records: systemShare.SharedRecord[] = data.getRecords();
records.forEach((record: systemShare.SharedRecord) => {
  // To do things.
});
```

#### ShareController

分享面板在不同设备下有不同的展示形式，根据屏幕规格&参数为应用提供不同的预览形式以及分享方式。

- 例如手机设备中，分享以模态显示；横屏/折叠屏展开状态时，分享面板以对话框形式显示；
- 而2in1设备及tablet，需要传入锚点信息并且以悬浮窗（Popup）形式显示。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

#### constructor

constructor(data: SharedData)

用于创建分享面板的控制器。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

data

[SharedData](#section816451553012)

是

分享数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
```

#### show

show(context: common.UIAbilityContext, options: ShareControllerOptions): Promise<void>

显示分享面板，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

context

[common.UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

拉起分享面板的上下文对象。

options

[ShareControllerOptions](#section107934816010)

是

分享控制器配置项。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[分享服务错误码](../../errors/ArkTS API错误码 (share-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1003702001](../../errors/ArkTS API错误码.md#section1559215645516)

Record types are not support.(The batch and multiple selection modes support { @link UDMF.File } type records only.)

[1003702002](../../errors/ArkTS API错误码.md#section1761113519576)

IPC data is oversized.

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
export struct ShareUtdText {
  build() {
  }

  private share() {
    // 构造ShareData，需配置一条有效数据信息
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.TEXT,
      content: '这是一段文本内容'
    });
    // 进行分享面板显示
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DETAIL,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
    });
  }
}
```

#### on('dismiss')

on(event: 'dismiss', callback: () => void): void

注册分享面板关闭事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，支持的事件为'dismiss'，当分享面板关闭时，触发该事件。

callback

() => void

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
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});
data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
controller.on('dismiss', () => {
  console.info('Share panel closed');
});
```

#### off('dismiss')

off(event: 'dismiss', callback: () => void): void

取消分享面板关闭事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

event

string

是

事件回调类型，支持的事件为'dismiss'，取消触发该事件。

callback

() => void

是

回调函数。传入on中的callback取消对应的监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

**示例：**

```ets
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});
data.addRecord({
  utd: utd.UniformDataType.PNG,
  uri: 'file://.../test.png'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
let callback = () => {
  console.info('Share panel closed');
};
controller.on('dismiss', callback);
controller.off('dismiss', callback);
```

#### on('shareCompleted')

on(type: 'shareCompleted', callback: Callback<ShareOperationResult>): void

注册用户完成分享事件监听。返回用户分享渠道，可用于数据统计等。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**设备行为差异：**该接口在TV中无效果，在其他设备类型中可正常调用。

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

type

string

是

事件回调类型，支持的事件为'shareCompleted'，当用户完成分享时，触发该事件。

callback

Callback<[ShareOperationResult](#section17135118312)>

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
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
  console.info('shareCompleted name:', result.targetAbilityInfo.name);
});
```

#### off('shareCompleted')

off(type: 'shareCompleted', callback?: Callback<ShareOperationResult>): void

取消用户完成分享事件监听。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**设备行为差异：**该接口在TV中无效果，在其他设备类型中可正常调用。

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

type

string

是

事件回调类型，支持的事件为'shareCompleted'，取消触发该事件。

callback

Callback<[ShareOperationResult](#section17135118312)>

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
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';

let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

let controller: systemShare.ShareController = new systemShare.ShareController(data);
let callback = (result: systemShare.ShareOperationResult) => {
  console.info('shareCompleted name:', result.targetAbilityInfo.name);
};
controller.on('shareCompleted', callback);
controller.off('shareCompleted', callback);
```

#### getSharedData

getSharedData(want: Want): Promise<SharedData>

通过目标应用获取的want信息，从中解析出分享数据，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

want

[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want)

是

目标应用获取的want信息。

**返回值：**

类型

说明

Promise<[SharedData](#section816451553012)>

Promise对象，返回分享数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[分享服务错误码](../../errors/ArkTS API错误码 (share-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1003703001](../../errors/ArkTS API错误码.md#section13612105175717)

Parse data failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    systemShare.getSharedData(want)
      .then((data: systemShare.SharedData) => {
        data.getRecords().forEach((record: systemShare.SharedRecord) => {
          // 处理分享数据
        });
        session.loadContent('pages/Index');
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
        session.terminateSelf();
      });
  }
}
```

#### getContactInfo

getContactInfo(want: Want): Promise<ContactInfo>

通过目标应用获取的want信息，从中解析联系人信息，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

want

[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want)

是

目标应用获取的want信息。

**返回值：**

类型

说明

Promise<[ContactInfo](#section102532316184)>

Promise对象，返回联系人信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[分享服务错误码](../../errors/ArkTS API错误码 (share-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1003703001](../../errors/ArkTS API错误码.md#section13612105175717)

Parse data failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    systemShare.getContactInfo(want)
      .then(async (contact: systemShare.ContactInfo) => {
        // 处理联系人信息，可通过联系人类型（如：个人，群组等），联系人ID，进行指定用户分享。
        // 获取分享数据
        let data = await systemShare.getSharedData(want);
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getContactInfo. Code: ${error.code}, message: ${error.message}`);
        // 联系人不存在或数据获取异常
        session.terminateSelf();
      });
  }
}
```

#### getWant

getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>

基于SharedData和预览模式构造want数据，使用Promise异步回调。

请勿随意修改返回值want数据中的参数，可能会导致未知的错误。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Collaboration.SystemShare

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

data

[SharedData](#section816451553012)

是

分享目标应用的分享数据信息。

options

[ShareControllerOptions](#section107934816010)

否

分享控制器配置项。

**返回值：**

类型

说明

Promise<[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want)>

Promise对象，返回分享目标应用的want信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[分享服务错误码](../../errors/ArkTS API错误码 (share-error-code).md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1003703001](../../errors/ArkTS API错误码.md#section13612105175717)

Parse data failed.

**示例：**

 不配置预览模式

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // 处理分享数据
    // To do things.
    // 准备返回数据
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN_TEXT,
      content: 'Hello HarmonyOS'
    });
    data.addRecord({
      utd: utd.UniformDataType.PNG,
      uri: 'file://.../test.png'
    });
    systemShare.getWant(data)
      .then((want) => {
        console.info('want = ', JSON.stringify(want));
        session!.terminateSelfWithResult({
          resultCode: 2,
          want: want
        })
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getWant. Code: ${error.code}, message: ${error.message}`);
      });
  }
}
```

配置预览模式

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';

export default class TestShareAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // 处理分享数据
    // To do things.
    // 准备返回数据
    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.PLAIN_TEXT,
      content: 'Hello HarmonyOS'
    });
    data.addRecord({
      utd: utd.UniformDataType.PNG,
      uri: 'file://.../test.png'
    });
    let options : systemShare.ShareControllerOptions = {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.SINGLE
    };
    systemShare.getWant(data,options)
      .then((want) => {
        console.info('want = ', JSON.stringify(want));
        session!.terminateSelfWithResult({
          resultCode: 2,
          want: want
        })
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getWant. Code: ${error.code}, message: ${error.message}`);
      });
  }
}
```
