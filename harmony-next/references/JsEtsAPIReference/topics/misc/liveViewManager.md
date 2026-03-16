# liveViewManager

本模块提供Live View Kit的基础能力，包括创建、更新和结束实况窗、获取实况窗和检查实况窗开关的功能。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { liveViewManager } from '@kit.LiveViewKit';
```

**设备行为差异：**该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

#### liveViewManager.isLiveViewEnabled

isLiveViewEnabled(): Promise<boolean>

查看应用实况窗开关，使用Promise异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Promise<boolean>

以Promise形式返回当前应用实况窗的开关状态。

- true表示实况窗开关开启。
- false表示实况窗开关关闭。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

[1003500001](../../errors/ArkTS API错误码.md#section539558125020)

Internal error.

[1003500002](../../errors/ArkTS API错误码.md#section1865682663012)

Marshalling or unmarshalling error.

[1003500003](../../errors/ArkTS API错误码.md#section7391431175215)

Failed to connect service.

**示例：**

```ets
import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  liveViewManager.isLiveViewEnabled().then((isEnabled: boolean) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in checking whether liveView is enabled, liveView is : %{public}s', isEnabled);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', e.code, e.message);
}
```

#### liveViewManager.startLiveView

startLiveView(liveView: LiveView): Promise<LiveViewResult>

创建实况窗，使用Promise异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

liveView

[LiveView](#section411410371767)

是

一个实况窗实例。

**返回值：**

类型

说明

Promise<[LiveViewResult](#section186814291982)>

Promise对象，返回创建实况窗的结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1003500001](../../errors/ArkTS API错误码.md#section539558125020)

Internal error.

[1003500002](../../errors/ArkTS API错误码.md#section1865682663012)

Marshalling or unmarshalling error.

[1003500003](../../errors/ArkTS API错误码.md#section7391431175215)

Failed to connect service.

[1003500004](../../errors/ArkTS API错误码.md#section19393182117481)

LiveView is not enabled.

[1003500005](../../errors/ArkTS API错误码.md#section105385290506)

The right of liveView is not enabled.

[1003500006](../../errors/ArkTS API错误码.md#section1722812135214)

The liveView already exists.

[1003500007](../../errors/ArkTS API错误码.md#section1495704455311)

Couldn't connect to server.

[1003500008](../../errors/ArkTS API错误码.md#section1769374975513)

Over max number liveViews per second.

**示例：**

```ets
import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function startLiveView(): Promise<void> {
  try {
    // 定义创建的liveView
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK_UP",
      sequence: 1,
      isMute: false,
      liveViewData: {
        primary: {
          title: "餐品已备好",
          content: [
            { text: "请前往" },
            { text: "一号窗口", textColor: "#FFFF0000" }
          ],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "待取餐",
            type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
            title: "取餐码",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "待取餐",
          content: "取餐码：72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.startLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in starting liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    ],
    actionType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}
```

#### liveViewManager.updateLiveView

updateLiveView(liveView: LiveView): Promise<LiveViewResult>

更新实况窗，使用Promise异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

liveView

[LiveView](#section411410371767)

是

一个实况窗实例。对于非必填字段，若无特殊说明，则不携带时默认继承上一次的状态。

**返回值：**

类型

说明

Promise<[LiveViewResult](#section186814291982)>

Promise对象，返回更新实况窗的结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1003500001](../../errors/ArkTS API错误码.md#section539558125020)

Internal error.

[1003500002](../../errors/ArkTS API错误码.md#section1865682663012)

Marshalling or unmarshalling error.

[1003500003](../../errors/ArkTS API错误码.md#section7391431175215)

Failed to connect service.

[1003500004](../../errors/ArkTS API错误码.md#section19393182117481)

LiveView is not enabled.

[1003500008](../../errors/ArkTS API错误码.md#section1769374975513)

Over max number liveViews per second.

[1003500009](../../errors/ArkTS API错误码.md#section17529152105718)

The liveView does not exist.

[1003500010](../../errors/ArkTS API错误码.md#section1456815218586)

The liveView has ended.

[1003500011](../../errors/ArkTS API错误码.md#section269192512108)

The liveView sequence is incorrect.

**示例：**

```ets
import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function updateLiveView(): Promise<void> {
  try {
    // 定义更新的liveView
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK_UP",
      sequence: 2,
      isMute: false,
      liveViewData: {
        primary: {
          title: "餐品已备好",
          content: [
            { text: "请前往" },
            { text: "一号窗口", textColor: "#FFFF0000" }
          ],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "待取餐",
            type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
            title: "取餐码",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "待取餐",
          content: "取餐码：72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.updateLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in updating liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    ],
    actionType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}
```

#### liveViewManager.stopLiveView

stopLiveView(liveView: LiveView): Promise<LiveViewResult>

结束实况窗，使用Promise异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

liveView

[LiveView](#section411410371767)

是

一个实况窗实例。对于非必填字段，若无特殊说明，则不携带时默认继承上一次的状态。

**返回值：**

类型

说明

Promise<[LiveViewResult](#section186814291982)>

Promise对象，返回结束实况窗的结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

[1003500001](../../errors/ArkTS API错误码.md#section539558125020)

Internal error.

[1003500002](../../errors/ArkTS API错误码.md#section1865682663012)

Marshalling or unmarshalling error.

[1003500003](../../errors/ArkTS API错误码.md#section7391431175215)

Failed to connect service.

[1003500004](../../errors/ArkTS API错误码.md#section19393182117481)

LiveView is not enabled.

[1003500008](../../errors/ArkTS API错误码.md#section1769374975513)

Over max number liveViews per second.

[1003500009](../../errors/ArkTS API错误码.md#section17529152105718)

The liveView does not exist.

[1003500010](../../errors/ArkTS API错误码.md#section1456815218586)

The liveView has ended.

[1003500011](../../errors/ArkTS API错误码.md#section269192512108)

The liveView sequence is incorrect.

**示例：**

```ets
import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, wantAgent } from '@kit.AbilityKit';

async function stopLiveView(): Promise<void> {
  try {
    // 定义要结束的liveView
    let liveView: liveViewManager.LiveView = {
      id: 123,
      event: "PICK_UP",
      sequence: 3,
      isMute: false,
      liveViewData: {
        primary: {
          title: "餐品已备好",
          content: [
            { text: "请前往" },
            { text: "一号窗口", textColor: "#FFFF0000" }
          ],
          keepTime: 1,
          clickAction: await buildWantAgent(),
          extensionData: {
            text: "待取餐",
            type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
            title: "取餐码",
            content: "72988",
            underlineColor: "#FFFF0000",
            descPic: "coffee.jpg"
          }
        },
        capsule: {
          type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
          status: 1,
          icon: "coffee.jpg",
          title: "待取餐",
          content: "取餐码：72988",
          backgroundColor: "#FF308977"
        }
      }
    };

    liveViewManager.stopLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in stopping liveView, result: %{public}s', JSON.stringify(liveViewResult));
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', err.code, err.message);
    });
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', e.code, e.message);
  }
}

async function buildWantAgent(): Promise<Want> {
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: 'xxx.xxx.xxx',
        abilityName: 'EntryAbility'
      } as Want
    ],
    actionType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  try {
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  } catch (e) {
    const err: BusinessError = e as BusinessError;
    hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
    throw e as Error;
  }
}
```

#### liveViewManager.getActiveLiveView

getActiveLiveView(id: number): Promise<LiveView>

获取活动的liveView，使用Promise异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

id

number

是

实况窗的id，取值范围为[-2147483648, 2147483647]。

**返回值：**

类型

说明

Promise<[LiveView](#section411410371767)>

Promise对象，返回活动的实况窗实例。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1003500001](../../errors/ArkTS API错误码.md#section539558125020)

Internal error.

[1003500002](../../errors/ArkTS API错误码.md#section1865682663012)

Marshalling or unmarshalling error.

[1003500003](../../errors/ArkTS API错误码.md#section7391431175215)

Failed to connect service.

[1003500009](../../errors/ArkTS API错误码.md#section17529152105718)

The liveView does not exist.

**示例：**

```ets
import { liveViewManager } from '@kit.LiveViewKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义需要查询的实况窗id
const id = 1;
try {
  liveViewManager.getActiveLiveView(id).then((liveView: liveViewManager.LiveView) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting active liveView, liveView is : %{public}s', JSON.stringify(liveView));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', e.code, e.message);
}
```

#### LiveView

实况窗对象参数，具体示例请见[创建实况窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-create-locally#section69141150182715)。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

id

number

是

实况窗唯一标识，取值范围为[-2147483648, 2147483647]，由开发者自行生成。对应Push Kit中LiveViewPayload的[activityId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306)字段。

event

string

是

实况窗的应用场景。

- TAXI：出行打车。
- DELIVERY：即时配送（外卖、生鲜）。
- FLIGHT：航班。
- TRAIN：高铁/火车。
- QUEUE：排队。
- PICK_UP：取餐。
- SCORE：赛事比分。
- RENT：共享租赁。
- TIMER：计时。
- WORKOUT：运动锻炼。
- NAVIGATION：导航。

使用对应场景需要申请权益，详情请参见[实况窗权益说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-rights)。

sequence

number

否

支持实况窗消息更新和结束保序能力，取值范围为[0, 2147483647]，新的实况窗版本号需大于当前展示实况窗版本号，否则更新和结束会失败。若不传入参数值，Live View Kit不会自动生成（此时，调用getActiveLiveView接口查询实况信息，返回结果中sequence：4294967295为无效值，该无效值不允许用来更新实况），也不会校验实况窗版本号。对应Push Kit中的[version](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-param#section66881469306)字段。

isMute

boolean

否

消息提醒方式。若您在创建或更改实况窗状态时不传入此字段，则始终默认静默提醒。

- true：静默提醒。
- false：铃声震动提醒。

timer

[LiveViewTimer](#section954195316811)

否

实况窗计时器，展示时每秒刷新一次。

 说明：

起始版本：5.0.0(12)。

配置了计时器后，可以在部分字段中使用占位符：**${placeholder.timer}**，系统会将占位符替换为计时器。

当前支持使用占位符的字段：

- liveViewData.primary.[title](#section452772611408)
- liveViewData.primary.[content](#section452772611408)
- liveViewData.primary.layoutData.[content](#section129929595142)
- liveViewData.primary.layoutData.[competitionTime](#section16706148183416)

liveViewData

[LiveViewData](#section980821010388)

是

实况窗详细信息。

#### LiveViewTimer

实况窗计时器参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.0(12)

名称

类型

必填

说明

time

number

否

计时器初始值，单位为毫秒，默认为0，取值范围为[0,9223372036854775807]。每秒刷新一次。

isCountdown

boolean

否

计时器是否为倒计时，默认为false。

- true：计时器为倒计时类型
- false：计时器为正计时类型

isPaused

boolean

否

计时器是否暂停，默认false。计时器暂停时，会显示暂停的那一秒。

- true：暂停。
- false：不暂停（默认值）。

countdownPreset

[CountdownPreset](#section39351532053)

否

当倒计时到0时，系统将自动更新实况窗卡片模板扩展区标题（title）和扩展区内容（content）字段为卡片预置结构体（countdownPreset）中的标题（presetTitle）和内容（presetContent）。

仅当满足以下条件时，上述功能生效：

- [layoutType](#section1765911975020)为LAYOUT_TYPE_PICKUP强调文本模板；
- liveViewData.primary.layoutData.[content](#section129929595142)中使用占位符${placeholder.timer}。

 说明：

**起始版本**：6.0.0(20)。

capsuleCountdownPreset

[CountdownPreset](#section39351532053)

否

当倒计时到0时，系统将自动更新计时器类型实况胶囊主文本（time）和实况胶囊副文本（content）为实况胶囊预设结构体（capsuleCountdownPreset）中的主文本（presetTitle）和副文本（presetContent）。

仅当满足以下条件时，上述功能生效：

- [capsuleType](#section136243383011)为CAPSULE_TYPE_TIMER计时器类型实况胶囊。

 说明：

**起始版本**：6.0.0(20)。

#### CountdownPreset

实况窗计时器预置参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**6.0.0(20)

名称

类型

必填

说明

presetTitle

string

否

自动更新扩展区标题或实况胶囊主文本为预设主文本。不支持时间占位符，若填值时不能为空，长度小于128。

presetContent

string

否

自动更新扩展区文本内容或实况胶囊副文本为预设副文本，若填值时不能为空，长度小于128。

#### LiveViewData

实况窗详细信息。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

primary

[PrimaryData](#section452772611408)

是

卡片形态内容。

capsule

[TextCapsule](#section1440294811375) | [TimerCapsule](#section613411226413) | [ProgressCapsule](#section147361526184415)

否

实况胶囊形态内容。

external

[ExternalData](#section92302515457)

否

小折叠外屏形态内容。

#### PrimaryData

卡片形态参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

title

string

创建：是

更新/结束：否

固定区标题，若填值时不能为空，长度小于1024。

content

Array<[RichText](#section28871613124714)>

创建：是

更新/结束：否

固定区内容，若填值时不能为空。

- 数组中所有对象的text字段字符串长度总和需小于1024。
- 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色。

keepTime

number

否

实况窗存档时间，在结束实况窗后，通知仍保留在通知中心的时长，**默认****0****不保留**，范围[0,3600]秒(s)。

clickAction

[WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent)

创建：是

更新/结束：否

点击实况窗默认动作，请调用wantAgent.[getWantAgent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent-1)来构造。

extensionData

[ExtensionData](#section14934174734616)

否

辅助区内容。

[layoutData](#section1258265220124)

[ProgressLayout](#section199131329165016) | [PickupLayout](#section129929595142) | [FlightLayout](#section636916193215) | [ScoreLayout](#section16706148183416) | [NavigationLayout](#section19117745094)

创建：是

更新/结束：否

扩展区数据。

 说明：

从5.0.0(12)版本开始，新增支持参数类型NavigationLayout。

liveViewLockScreenPicture

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

锁屏沉浸实况窗大图样式在指定路径下的文件名。传入实际存在的图片时，用户在锁屏下点击实况胶囊中的应用图标、长按实况胶囊内容或长按卡片内容，会进入沉浸态，展示大图。不传入或传入图片不存在时，用户点击行为不会进入沉浸态。

- string类型的取值为在“/resources/rawfile”路径下的文件名，长度小于256

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 建议使用大小约为1000*1000的图片，不支持GIF格式的图片文件。

 说明：

起始版本：5.0.0(12)。

liveViewLockScreenAbilityName

string

否

[LiveViewLockScreenExtensionAbility](../system-services/LiveViewLockScreenExtensionAbility.md)（锁屏沉浸实况窗扩展Ability）的名称，仅创建实况窗时生效，传入时值不可为空，长度最大为128。若在创建实况窗时与liveViewLockScreenPicture同时传入，则仅本字段生效。

 说明：

起始版本：5.0.0(12)。

liveViewLockScreenAbilityParameters

Record<string, string>

否

用户自定义向[LiveViewLockScreenExtensionAbility](../system-services/LiveViewLockScreenExtensionAbility.md)（锁屏沉浸实况窗扩展Ability）传入的参数，填值时不能为空，key-value键值对最多50个，传入后可在ability的onSessionCreate()中，通过want.parameters获取。

 说明：

起始版本：5.0.0(12)。

backgroundType

[BackgroundType](#section15834105743213)

否

表示实况窗卡片的背景氛围类型，仅支持左右文本模板(即[layoutType](#section1765911975020)为LAYOUT_TYPE_FLIGHT)展示背景。

当传入实况窗卡片的背景氛围类型参数backgroundType值为赏月航班或夕阳航班时，且同时传入天气类型（[WeatherInfo](#section145641518183913)）为雨、雪特殊天气，卡片上优先展示天气背景，其余非特殊天气在卡片上展示赏月航班或夕阳航班背景氛围。

 说明：

起始版本：6.0.0(20)。

#### BackgroundType

航班场景下卡片背景类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**6.0.0(20)

名称

值

说明

SYS_BACKGROUND_UNDEFINED

0

未定义，表示在卡片上不展示背景氛围。

SYS_BACKGROUND_FLIGHT_MOON

100

赏月航班，表示在卡片上展示赏月的背景氛围。

SYS_BACKGROUND_FLIGHT_SUNSET

101

夕阳航班，表示在卡片上展示夕阳的背景氛围。

#### ExtensionData

辅助区参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

type

[ExtensionType](#section171431441533)

否

辅助区显示类型，默认为[EXTENSION_TYPE_DEFAULT](#section171431441533)不显示辅助区。

text

string

创建：是（仅当type值为ExtensionType.EXTENSION_TYPE_COMMON_TEXT或ExtensionType.EXTENSION_TYPE_CAPSULE_TEXT时）

更新/结束：否

辅助区显示的文本信息，若填值时不能为空，长度小于128。

pic

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是（仅当type值为ExtensionType.EXTENSION_TYPE_PIC或ExtensionType.EXTENSION_TYPE_ICON时）

更新/结束：否

辅助区显示的图片，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

clickAction

[WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent)

否

点击辅助区的跳转动作，请调用wantAgent.[getWantAgent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent-1)来构造。

#### LayoutData

定义扩展区模板类型及公共参数。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_DEFAULT时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

layoutType

[LayoutType](#section1765911975020)

是

模板类型。

serviceButtons

Array<[ServiceButton](#section637116431585)>

否

传入连续服务按钮结构体数组。 更新连续服务按钮时，需要同时更新辅助区[ExtensionData](#section14934174734616)的clickAction字段和连续服务按钮。

 说明：

**起始版本**：5.1.1(19)。

isServiceButtonsDisplayed

boolean

否

是否显示连续服务按钮，默认false。

- true：显示按钮
- false：不显示按钮

 说明：

**起始版本**：5.1.1(19)。

weatherInfo

[WeatherInfo](#section145641518183913)

否

传入天气信息结构体。

目的地天气类型仅支持左右文本模板（即[layoutType](#section1765911975020)为LAYOUT_TYPE_FLIGHT）；

本地天气类型仅支持基础模板、进度可视化模板和强调文本模板（即[layoutType](#section1765911975020)为LAYOUT_TYPE_DEFAULT/LAYOUT_TYPE_PROGRESS/LAYOUT_TYPE_PICKUP）。

当传入天气信息，且同时传入实况窗卡片的背景氛围类型参数[backgroundType](#section15834105743213)值为赏月航班（SYS_BACKGROUND_FLIGHT_MOON）或夕阳航班（SYS_BACKGROUND_FLIGHT_SUNSET）时，若天气类型为雨、雪特殊天气，卡片上优先展示天气背景，其余非特殊天气在卡片上优先展示赏月航班或夕阳航班背景氛围。

 说明：

**起始版本**：

从6.0.0(20)开始支持展示目的地天气效果；

从6.0.2(22)开始支持展示本地天气效果。

#### WeatherInfo

应用传入天气信息的基类。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**6.0.0(20)

名称

类型

必填

说明

weatherType

[WeatherType](#section2062895313473)

否

天气类型。创建实况窗时，若weatherType不传入或传入非法值，则不展示天气效果。

locationType

[WeatherLocationType](#section1597237195618)

否

天气位置类型。创建实况窗时，若locationType不传入或传入非法值，则不展示天气效果。

highTemperature

number

否

天气最高温度，当前仅支持摄氏度，需小于等于58℃且大于传入的最低温度值（lowTemperature）。创建实况窗时，若不传入或传入非法值，则不展示温度。

lowTemperature

number

否

天气最低温度，当前仅支持摄氏度，需大于等于-95℃且小于传入的最高温度值（highTemperature）。创建实况窗时，若不传入或传入非法值，则不展示温度。

#### WeatherType

天气类型，为枚举值，雨、雪天气支持在实况卡片上展示天气动效背景，其余天气类型（WEATHER_TYPE_UNDEFINED除外）仅支持在实况卡片上展示天气图标和温度，不支持在实况卡片上展示天气动效背景。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**6.0.0(20)

名称

值

说明

WEATHER_TYPE_UNDEFINED

0

表示不展示天气效果。

WEATHER_TYPE_SUNNY

1

晴天气类型，展示天晴天气效果。

WEATHER_TYPE_HAZY

5

霾天气类型，展示霾天气效果。

WEATHER_TYPE_CLOUDY

7

多云天气类型，展示多云天气效果。

WEATHER_TYPE_OVERCAST

8

阴天气类型，展示阴天气效果。

WEATHER_TYPE_FOG

11

雾天气类型，展示雾天气效果。

WEATHER_TYPE_SHOWERS

12

阵雨天气类型，展示阵雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_T_STORMS

15

雷阵雨天气类型，展示雷阵雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_RAIN

18

雨天气类型，展示雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_SNOW

22

雪天气类型，展示雪天气效果。实况卡片支持雪动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_RAIN_AND_SNOW

29

雨夹雪天气类型，展示雨夹雪天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_HOT

30

高温天气类型，展示高温天气效果。

WEATHER_TYPE_COLD

31

低温天气类型，展示低温天气效果。

WEATHER_TYPE_WINDY

32

大风天气类型，展示大风天气效果。

WEATHER_TYPE_THUNDERSHOWER_WITH_HAIL

45

冰雹天气类型，展示冰雹天气效果。

WEATHER_TYPE_LIGHT_RAIN

46

小雨天气类型，展示小雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_MODERATE_RAIN

47

中雨天气类型，展示中雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_HEAVY_RAIN

48

大雨天气类型，展示大雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_STORM

49

暴雨天气类型，展示暴雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_SEVERE_STORM

51

特大暴雨天气类型，展示特大暴雨天气效果。实况卡片支持雨动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_LIGHT_SNOW

52

小雪天气类型，展示小雪天气效果。实况卡片支持雪动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_MODERATE_SNOW

53

中雪天气类型，展示中雪天气效果。实况卡片支持雪动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_HEAVY_SNOW

54

大雪天气类型，展示大雪天气效果。实况卡片支持雪动效背景。

 说明：

从6.0.0(20)开始支持展示天气动效背景。

WEATHER_TYPE_SNOW_STORM

55

暴雪天气类型，展示暴雪天气效果。实况卡片支持雪动效背景。

 说明：

从6.0.2(22)开始支持展示天气动效背景。

WEATHER_TYPE_DUST_STORM

56

沙尘暴天气类型，展示沙尘暴天气效果。

WEATHER_TYPE_DUST

65

浮尘天气类型，展示浮尘天气效果。

WEATHER_TYPE_SAND

66

扬沙天气类型，展示扬沙天气效果。

WEATHER_TYPE_SAND_STORM

67

强沙尘暴天气类型，展示强沙尘暴天气效果。

#### WeatherLocationType

天气位置类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**6.0.0(20)

名称

值

说明

LOCATION_TYPE_LOCAL

1

表示展示本地天气效果，仅支持基础模板、进度可视化模板和强调文本模板（即[layoutType](#section1765911975020)为LAYOUT_TYPE_DEFAULT/LAYOUT_TYPE_PROGRESS/LAYOUT_TYPE_PICKUP）。天气图标将展示在固定区标题右侧。

 说明：

从6.0.2(22)开始支持展示本地天气效果。

LOCATION_TYPE_DESTINATION

2

表示展示目的地天气效果，仅支持左右文本模板（即[layoutType](#section1765911975020)为LAYOUT_TYPE_FLIGHT）。天气图标及温度信息将展示在左右文本模板扩展区右侧，扩展区右侧标题及右侧内容的左侧。

 说明：

从6.0.0(20)开始支持展示目的地天气效果；

#### ServiceButton

应用传入连续服务按钮的基类。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.1.1(19)

名称

类型

必填

说明

name

string

否

连续服务按钮名字，长度小于128，超过该长度的字符将被截断。

clickAction

[WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent)

否

点击连续服务按钮时触发的跳转动作，请调用wantAgent.[getWantAgent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent-1)来构造。

#### ProgressLayout

进度可视化模板扩展区参数，继承[LayoutData](#section1258265220124)。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_PROGRESS时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

progress

number

是

进度百分比，决定指示器在进度条中的位置，值范围：[0,100]。

color

string

否

进度条颜色，"#ARGB"16进制格式，长度为9。默认颜色为#FF317AF7。

backgroundColor

string

否

进度条背景颜色，"#ARGB"16进制格式，长度为9。默认颜色为#19000000，深色模式默认颜色#19FFFFFF。

indicatorType

[IndicatorType](#section71841624105515)

否

扩展区指示器小图标显示类型，默认不显示指示器小图标。

indicatorIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是（仅当indicatorType值为IndicatorType.INDICATOR_TYPE_UP或IndicatorType.INDICATOR_TYPE_OVERLAY时）

更新/结束：否

进度条指示器图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

lineType

[LineType](#section1888635517564)

否

扩展区进度条显示类型，默认为虚线进度。

nodeIcons

Array<string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

创建：是

更新/结束：否

进度条每个节点图标，数组长度范围为[2, 5]，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

#### PickupLayout

强调文本模板扩展区参数，继承[LayoutData](#section1258265220124)。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_PICKUP时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

title

string

创建/模板切换：是

更新/结束：否

扩展区标题，若填值时不能为空，长度小于128。

content

string

创建/模板切换：是

更新/结束：否

扩展区内容，若填值时不能为空，长度小于128。

underlineColor

string

否

扩展区内容下划线颜色，"#ARGB"16进制格式，长度为9，默认不显示下划线。

descPic

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是

更新/结束：否

扩展区右侧产品描述图，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

#### FlightLayout

左右文本模板扩展区参数，继承[LayoutData](#section1258265220124)。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_FLIGHT时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

style

[FlightLayoutStyle](#section1181383342218)

否

左右文本子样式类型，若未填默认为强调型子样式。

- 0：强调型子样式类型。
- 1：均衡型子样式类型。

 说明：

起始版本：5.0.2(14)。

firstTitle

string

创建/模板切换：是

更新/结束：否

扩展区左侧标题，若填值时不能为空，长度小于128。

firstContent

string

创建/模板切换：是

更新/结束：否

扩展区左侧内容，若填值时不能为空，长度小于128。

lastTitle

string

创建/模板切换：是

更新/结束：否

扩展区右侧标题，若填值时不能为空，长度小于128。

lastContent

string

创建/模板切换：是

更新/结束：否

扩展区右侧内容，若填值时不能为空，长度小于128。

lastTitleSuperscript

string

否

扩展区右侧标题的右上角展示内容，若填值时不能为空，长度小于128。若用于表示到达时间跨天，传入值长度等于2，格式为"+X", 其中X为数字，例如"+1", "+2"等。

 说明：

起始版本：5.0.2(14)。

lastContentSuperscript

string

否

扩展区右侧内容的右上角展示内容，若填值时不能为空，长度小于128。若用于表示到达时间跨天，传入值长度等于2，格式为"+X", 其中X为数字，例如"+1", "+2"等。

 说明：

起始版本：5.0.2(14)。

spaceType

[SpaceType](#section173441342102410)

否

左右文本模板扩展区中间的显示类型。

- 未携带该字段或0：显示spaceIcon指定的中间间隔图标。
- 1：显示由spaceText指定的中间间隔文本。

 说明：

起始版本：5.0.2(14)。

spaceIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：未填spaceType或spaceType为SpaceType.SPACE_TYPE_ICON时必填

扩展区中间间隔图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

spaceText

string

创建：spaceType为SpaceType.SPACE_TYPE_TEXT时必填

扩展区中间间隔文本，用于展示日期，例如10/28 周六、2025/09/15等。

限制为6个中文字符长度或12个英文字符长度，若超长则截断展示。

更新/结束不携带时显示上次的文本。

 说明：

起始版本：5.0.2(14)。

isHorizontalLineDisplayed

boolean

否

是否显示扩展区分割线，默认显示分割线。

- true：显示。
- false：不显示。

additionalText

string

否

扩展区底部内容，长度小于1024。

 说明：

起始版本：5.0.0(12)。

#### ScoreLayout

赛事比分模板扩展区参数，继承[LayoutData](#section1258265220124)。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_SCORE时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

hostName

string

创建/模板切换：是

更新/结束：否

扩展区左侧名称，若填值时不能为空，长度小于128。

hostIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是

更新/结束：否

扩展区左侧图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

hostScore

string

创建/模板切换：是

更新/结束：否

扩展区左侧比分，若填值时不能为空，长度小于128。

guestName

string

创建/模板切换：是

更新/结束：否

扩展区右侧名称，若填值时不能为空，长度小于128。

guestIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是

更新/结束：否

扩展区右侧图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

guestScore

string

创建/模板切换：是

更新/结束：否

扩展区右侧比分，若填值时不能为空，长度小于128。

competitionDesc

string | Array<[RichText](#section28871613124714)>

创建/模板切换：是

更新/结束：否

扩展区中间上方描述文本，比赛介绍，若填值时不能为空。

- 填string时，字符串长度需小于128。
- 填Array<[RichText](#section28871613124714)>时：

  1. 数组中所有对象的text字段字符串长度总和需小于128。
  1. 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色

 说明：

从5.0.0(12)版本开始，新增支持入参类型Array<[RichText](#section28871613124714)>。

competitionTime

string

创建/模板切换：是

更新/结束：否

扩展区中间下方比赛时间，若填值时不能为空，长度小于128。

isHorizontalLineDisplayed

boolean

否

是否显示扩展区分割线，默认显示分割线。

- true：显示。
- false：不显示。

#### NavigationLayout

导航模板扩展区参数，继承[LayoutData](#section1258265220124)。当[layoutType](#section1765911975020)为LayoutType.LAYOUT_TYPE_NAVIGATION时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.0(12)

名称

类型

必填

说明

currentNavigationIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是

更新/结束：否

当前导航方向。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为128。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

若本地资源不存在，创建时失败，更新/结束时导航模板扩展区不更新。

 说明：

为确保图片在系统深浅模式下的显示效果，系统将对png、svg格式图片做赋色处理，其他格式图片保留原样显示不支持赋色。具体参考 [卡片模板](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274) 的 "导航定制模板"说明。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

navigationIcons

Array<string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

否

导航方向的箭头集合图片，支持1-11个。创建时不传，则不展示扩展区。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为128。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

若本地资源不存在，创建时失败，更新/结束时导航模板扩展区不更新。

 说明：

为确保在系统深浅模式下的显示效果，系统将对png、svg格式图片做赋色处理，其他格式图片保留原样显示不支持赋色。具体参考 [卡片模板](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274) 的 "导航定制模板"说明。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

isNavigationIconsDisplayed

boolean

否

控制导航方向的箭头集合图片是否展示。更新或结束未填时，继承上一次状态变更时的值。其他情况不传值时默认为展示。

- true：展示
- false：不展示

**起始版本**：5.0.3(15)

#### CapsuleData

定义实况胶囊基本属性的基类。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

type

[CapsuleType](#section136243383011)

是

实况胶囊的类型。

status

number

是

实况胶囊的显示状态。

- 1：显示实况胶囊。
- -1：结束显示实况胶囊。

icon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是

更新/结束：否

实况胶囊的图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为255。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

tailIcon

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

实况胶囊的尾部图标，更新/结束不携带时显示上次的图片。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为255。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

 说明：

**起始版本**：6.0.0(20)

backgroundColor

string

创建：是

更新/结束：否

实况胶囊的背景颜色，"#ARGB"16进制格式，长度为9。更新或结束未填时，继承上一次状态变更时的颜色。

不建议使用以下颜色：

- #FF000000
- #FFFFFFFF
- #FFF1F3F5

isContentDisplayed

boolean

否

实况胶囊的副文本是否展示。该参数未填时，继承上一次创建或更新实况窗时传入的值。其他情况不传值时默认为展示。

- true：展示
- false：不展示

isContentDisplayed与isTailIconDisplayed均为false时，实况胶囊的副文本及尾部图标区域不展示。

 说明：

**起始版本**：5.0.3(15)

isTailIconDisplayed

boolean

否

实况胶囊的尾部图标是否展示。该参数未填时，继承上一次创建或更新实况窗时传入的值。其他情况不传值时默认不展示。

- true：展示
- false：不展示

isContentDisplayed与isTailIconDisplayed均为false时，实况胶囊的副文本及尾部图标区域不展示。

 说明：

**起始版本**：6.0.0(20)

#### TextCapsule

文本实况胶囊参数，继承[CapsuleData](#section1600824135815)。当[type](#section1600824135815)为CapsuleType.CAPSULE_TYPE_TEXT时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

title

string

创建：是

更新/结束：否

实况胶囊的主文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。

 说明：

从6.0.0(20)版本开始，支持当传入值为"数值:数值"，且[layoutType](#section1765911975020)为赛事类型LAYOUT_TYPE_SCORE时，系统将自动提取实况卡片扩展区两侧图片和比分，更新实况胶囊样式，显示为赛事队伍图标及比分情况。

content

string

否

实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。

#### TimerCapsule

计时器实况胶囊参数，继承[CapsuleData](#section1600824135815)。当[type](#section1600824135815)为CapsuleType.CAPSULE_TYPE_TIMER时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

content

string

否

实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。

time

number

否

实况胶囊计时器初始值，每秒刷新一次，单位ms，默认为0。

isCountdown

boolean

否

是否显示倒计时器。

- true：倒计时。
- false：正计时（默认值）。

isPaused

boolean

否

实况胶囊计时器是否暂停，计时器暂停时，实况胶囊会显示暂停的那一秒。

- true：暂停。
- false：不暂停（默认值）。

#### ProgressCapsule

进度实况胶囊参数，继承[CapsuleData](#section1600824135815)。当[type](#section1600824135815)为CapsuleType.CAPSULE_TYPE_PROGRESS时，使用此类型。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

max

number

否

进度条最大进度值，默认为1，范围为[1, 2147483647]。

progress

number

否

进度条当前进度值，默认为0，范围为[0, 2147483647]。进度的值为progress/max的比值。

indeterminate

boolean

否

进度显示类型，默认显示为数值占比。

- true：百分比。
- false：数值占比（默认）。

content

string

否

实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。

 说明：

**起始版本**：6.0.0(20)

#### ExternalData

外屏形态模板参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

title

string

创建：是

更新/结束：否

外屏标题，若填值时不能为空，长度小于128。

content

Array<[RichText](#section28871613124714)>

创建：是

更新/结束：否

外屏内容，应用可以设置字符串中部分文本的颜色，若填值时不能为空。

- 数组中所有对象的text字段字符串长度总和需小于128。
- 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色。

type

[ExternalType](#section5925948161213)

否

外屏背景样式类型，默认为背景色。

 说明：

起始版本：5.0.0(12)。

backgroundColor

string

否

外屏背景颜色，"#RGB"16进制格式， 长度为7，默认颜色为#F1F3F5。

backgroundPicture

string | image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

创建：是（仅当type为ExternalType.BACKGROUND_PICTURE时）

更新/结束：否（当type为ExternalType.BACKGROUND_PICTURE时，此参数生效）

外屏背景图片，更新/结束不携带时显示上次的图片。

 说明：

起始版本：5.0.0(12)。

- 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。

示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。

- 当此参数类型为image.[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)时，图片大小不大于30KB。

#### RichText

富文本参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

必填

说明

text

string

是

文本内容，长度小于128。

textColor

string

否

文本颜色，"#ARGB"16进制格式，长度为9。不设置textColor时，文本颜色默认为#99000000；设置textColor时，数组中的所有对象仅能设置一种颜色。

#### LiveViewResult

实况窗结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

说明

resultCode

number

实况窗结果码。

- 0：成功。
- 1：固定区更新/结束失败。
- 2：辅助区更新/结束失败。
- 3：扩展区更新/结束失败。
- 4：实况胶囊更新/结束失败。
- 5：外屏更新/结束失败。

message

String

实况窗结果信息。

#### LayoutType

扩展区类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

值

说明

LAYOUT_TYPE_DEFAULT

-1

不显示扩展区。

LAYOUT_TYPE_PROGRESS

3

进度可视化类型。

LAYOUT_TYPE_PICKUP

4

强调文本类型。

LAYOUT_TYPE_FLIGHT

5

左右文本类型。

LAYOUT_TYPE_SCORE

7

赛事类型。

LAYOUT_TYPE_NAVIGATION

8

导航类型。

 说明：

起始版本：5.0.0(12)

#### ExtensionType

辅助区类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

值

说明

EXTENSION_TYPE_DEFAULT

0

不显示辅助区。

EXTENSION_TYPE_COMMON_TEXT

1

普通文本。

EXTENSION_TYPE_CAPSULE_TEXT

2

实况胶囊文本。

EXTENSION_TYPE_PIC

3

显示图片。

EXTENSION_TYPE_ICON

4

显示图标。

#### IndicatorType

指示器类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

值

说明

INDICATOR_TYPE_UNDISPLAYED

0

不显示指示器小图标。

INDICATOR_TYPE_UP

1

显示在进度线上方。

INDICATOR_TYPE_OVERLAY

2

显示覆盖在进度线上。

#### LineType

扩展区进度条类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

值

说明

LINE_TYPE_DOTTED_LINE

0

虚线进度。

LINE_TYPE_NORMAL_SOLID_LINE

1

实线进度。

LINE_TYPE_THICK_SOLID_LINE

2

粗实线进度。

#### CapsuleType

实况胶囊类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

值

说明

CAPSULE_TYPE_TEXT

1

文本实况胶囊。

CAPSULE_TYPE_TIMER

2

计时器实况胶囊。

CAPSULE_TYPE_PROGRESS

3

进度实况胶囊。

#### ExternalType

外屏背景样式类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.0(12)

名称

值

说明

BACKGROUND_COLOR

0

显示背景色。

BACKGROUND_PICTURE

1

显示背景图片。

#### FlightLayoutStyle

左右文本子样式类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.2(14)

名称

值

说明

STYLE_FLIGHT_EMPHASIS

0

强调型子样式类型。

STYLE_FLIGHT_BALANCE

1

均衡型子样式类型。

扩展区支持强调型和均衡型两种子样式，两种子样式区别在于左右文本标题和内容字号大小不同，均衡型左右文本标题字号缩小，内容字号增大，展示效果更均衡。详细模板设计样式请参考[实况窗设计指南>通用卡片模板>模板类型>左右文本模板](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861#section1511241615274)

#### SpaceType

左右文本模板扩展区中间的显示类型，为枚举值。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.2(14)

名称

值

说明

SPACE_TYPE_ICON

0

扩展区中间显示图标。

SPACE_TYPE_TEXT

1

扩展区中间显示文本。