# pushCommon（推送服务公共信息）

本模块提供了推送服务公共信息，包括：绑定账号的类型和场景化消息数据PushPayload、扩展通知消息数据、扩展通知替换内容、点击事件时可以替换的数据以及应用内通话消息数据。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { pushCommon } from '@kit.PushKit';
```

#### AppProfileType

绑定账号类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该枚举值在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该枚举值在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

名称

值

说明

PROFILE_TYPE_OS_DISTRIBUTED_ACCOUNT

1

华为账号。

PROFILE_TYPE_APPLICATION_ACCOUNT

2

应用账号。

#### PushPayload

应用可以通过[receiveMessage](../system-services/pushService（推送服务基础能力）.md#section125883044911)()获取场景化消息数据的参数定义。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

名称

类型

只读

可选

说明

type

string

否

否

传递给Ability的消息类型，取值范围：

'IM'：通知扩展消息

'VoIP'：应用内通话消息

'BACKGROUND'：后台消息

'EMERGENCY'：紧急事件消息

'ALERT'：通知消息

data

string

否

否

传递给Ability的数据。

- type为'IM'时，data取值样例（格式化后）：

```ets
{
    "data": "extraData", **// data为Rest API接口payload中携带的extraData**
    "header": {
        "token": "MA**"
    },
    "messageAction": 0,
    "notification": {
        "bigBody": "bigBodyXX",
        "bigTitle": "bigTitleXX",
        "body": "bodyXX",
        "data": "",
        "image": "https://**/image**.png",
        "notifyId": -1,
        "title": "titleXX"
    }
}
```

- type为 'VoIP' | 'BACKGROUND' | 'EMERGENCY'时，data取值样例（格式化后）：

```ets
{
    "data": "extraData", **// data为Rest API接口payload中携带的extraData**
    "header": {
        "token": "MA**"
    }
}
```

- type为 'ALERT'时，无需额外配置data字段：  notification完整字段参考AlertPayload 通知消息中 [Notification](../../guides/请求体参数说明.md#section17371529101117)结构体。

```ets
{
    "data": "", // 传入空字符串
    "header": {
        "token": "MA**"
    },
    "messageAction": 0,
    "notification": {
        // 完整字段参考AlertPayload 通知消息中Notification结构体
    }
}
```

#### RemoteNotificationInfo

扩展通知消息数据，继承[PushPayload](#section16335431712)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

id

number

否

否

通知id。

type

string

否

否

继承自[PushPayload](#section16335431712)，表示传递给[RemoteNotificationExtensionAbility](../system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md)的消息类型。

data

string

否

否

继承自[PushPayload](#section16335431712)，表示传递给[RemoteNotificationExtensionAbility](../system-services/RemoteNotificationExtensionAbility（通知扩展Ability）.md)的数据。

#### RemoteNotificationContent

扩展通知替换内容。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

title

string

否

是

扩展通知标题。

 说明：

title从5.0.0(12)起变更为非必填字段。

text

string

否

是

扩展通知内容。

 说明：

text从5.0.0(12)起变更为非必填字段。

overlayIcon

image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

是

扩展通知的叠加图标。

 说明：

图片长*宽建议小于128*128像素，若超过49152像素，则图片不展示。

badgeNumber

number

否

是

扩展通知展示时增加的角标数量，取值范围(0, 100)。

setBadgeNumber

number

否

是

扩展通知展示时显示的角标数量 ，取值范围[0, 100)。与badgeNumber同时返回时，优先于badgeNumber。

 说明：

起始版本：5.0.0(12)。

wantAgent

[RemoteWantAgent](#section122049160211)

否

是

点击事件时可以替换的数据。

#### RemoteWantAgent

点击事件时可以替换的数据。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

abilityName

string

否

否

自定义页面名称。

parameters

Record<string, Object>

否

是

传递给应用的数据。

#### VoIPInfo

应用内通话消息数据，继承[PushPayload](#section16335431712)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

callId

string

否

否

当次呼叫的唯一标识。

type

string

否

否

继承自[PushPayload](#section16335431712)，表示传递给[VoIPExtensionAbility](../system-services/VoIPExtensionAbility（应用内通话消息扩展Ability）.md)的消息类型。

data

string

否

否

继承自[PushPayload](#section16335431712)，表示传递给[VoIPExtensionAbility](../system-services/VoIPExtensionAbility（应用内通话消息扩展Ability）.md)的数据。