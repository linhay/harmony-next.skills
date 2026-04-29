# @ohos.app.ability.common (Ability公共模块)

本模块提供Ability Kit中常用公共能力的纯类型定义，包含各类上下文对象、回调接口和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { common } from '@kit.AbilityKit';
```

#### UIAbilityContext

type UIAbilityContext = [_UIAbilityContext.default](../../topics/misc/UIAbilityContext.md)

[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_UIAbilityContext.default](../../topics/misc/UIAbilityContext.md) | UIAbilityContext组件上下文。 |

#### AbilityStageContext

type AbilityStageContext = [_AbilityStageContext.default](../../topics/misc/AbilityStageContext.md)

[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_AbilityStageContext.default](../../topics/misc/AbilityStageContext.md) | AbilityStage组件上下文。 |

#### ApplicationContext

type ApplicationContext = _ApplicationContext.default

应用上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _ApplicationContext.default | 应用上下文。 |

#### BaseContext

type BaseContext = [_BaseContext.default](../../topics/misc/BaseContext.md)

所有Context类型的父类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_BaseContext.default](../../topics/misc/BaseContext.md) | 所有Context的父类。 |

#### Context

type Context = _Context.default

[Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#stage模型)的上下文基类。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _Context.default | Stage模型的上下文基类。 |

#### [ExtensionContext](../../topics/misc/ExtensionContext.md)

type ExtensionContext = [_ExtensionContext.default](../../topics/misc/ExtensionContext.md)

[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)组件上下文，继承自Context。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_ExtensionContext.default](../../topics/misc/ExtensionContext.md) | ExtensionAbility组件上下文。 |

#### Form[ExtensionContext](../../topics/misc/ExtensionContext.md)

type Form[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_FormExtensionContext.default](../../topics/misc/FormExtensionContext.md)

[FormExtensionAbility](@ohos.app.form.FormExtensionAbility (FormExtensionAbility).md)组件上下文，继承自[ExtensionContext](ExtensionContext.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _Form[ExtensionContext](../../topics/misc/ExtensionContext.md).default | FormExtensionAbility组件上下文。 |

#### Vpn[ExtensionContext](../../topics/misc/ExtensionContext.md)11+

type Vpn[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_VpnExtensionContext.default](../../topics/networking/VpnExtensionContext.md)

[VpnExtensionAbility](@ohos.app.ability.VpnExtensionAbility (三方VPN能力).md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _Vpn[ExtensionContext](../../topics/misc/ExtensionContext.md).default | VpnExtensionAbility组件上下文。 |

#### EventHub

type EventHub = [_EventHub.default](../../topics/misc/EventHub.md)

EventHub是系统提供的基于发布-订阅模式实现的事件通信机制。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_EventHub.default](../../topics/misc/EventHub.md) | 系统提供的基于发布-订阅模式实现的事件通信机制。 |

#### PacMap

type PacMap = [_PacMap](../../topics/misc/DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__pacmap)

存储基础数据类型的容器。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [_PacMap](../../topics/misc/DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__pacmap) | 存储基础数据类型的容器。 |

#### AbilityResult

type AbilityResult = [_AbilityResult](../../topics/misc/AbilityResult.md)

定义Ability被拉起并退出后返回的结果码和数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_AbilityResult](../../topics/misc/AbilityResult.md) | 定义Ability被拉起并退出后返回的结果码和数据。 |

#### AbilityStartCallback11+

type AbilityStartCallback = [_AbilityStartCallback](../../topics/misc/AbilityStartCallback.md)

定义了拉起UIExtensionAbility的回调结果，通常作为[UIAbilityContext.startAbilityByType](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__startabilitybytype11)/[UIExtensionContext.startAbilityByType](@ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类).md#ZH-CN_TOPIC_0000002522080542__startabilitybytype11)的入参传入。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_AbilityStartCallback](../../topics/misc/AbilityStartCallback.md) | 定义拉起UIExtensionAbility的回调结果。 |

#### ConnectOptions

type ConnectOptions = [_ConnectOptions](../../topics/misc/ConnectOptions.md)

在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_ConnectOptions](../../topics/misc/ConnectOptions.md) | 在连接指定的后台服务时作为入参，用于接收与后台服务的连接状态。 |

#### UI[ExtensionContext](../../topics/misc/ExtensionContext.md)10+

type UI[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_[UIExtensionContext](../../topics/misc/UIExtensionContext.md).default](../../topics/misc/UIExtensionContext.md)

[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _UI[ExtensionContext](../../topics/misc/ExtensionContext.md).default | UIExtensionAbility组件上下文。 |

#### EmbeddableUIAbilityContext12+

type EmbeddableUIAbilityContext = [_EmbeddableUIAbilityContext.default](../../topics/misc/EmbeddableUIAbilityContext.md)

[EmbeddableUIAbility](@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件).md)组件上下文，继承自Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_EmbeddableUIAbilityContext.default](../../topics/misc/EmbeddableUIAbilityContext.md) | EmbeddableUIAbility组件上下文。 |

#### PhotoEditor[ExtensionContext](../../topics/misc/ExtensionContext.md)12+

type PhotoEditor[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_PhotoEditorExtensionContext.default](../../topics/misc/PhotoEditorExtensionContext.md)

[PhotoEditorExtensionAbility](@ohos.app.ability.PhotoEditorExtensionAbility (支持图片编辑能力的ExtensionAbility组件).md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AppExtension.PhotoEditorExtension

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _PhotoEditor[ExtensionContext](../../topics/misc/ExtensionContext.md).default | PhotoEditorExtensionAbility组件上下文。 |

#### UIServiceProxy14+

type UIServiceProxy = [_UIServiceProxy.default](../../topics/misc/UIServiceProxy.md)

UIServiceProxy提供了与UIServiceExtensionAbility服务端数据通信的能力。UIServiceExtensionAbility是一类特殊的ExtensionAbility组件，这类组件由系统提供，通常用于提供浮窗组件相关扩展能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_UIServiceProxy.default](../../topics/misc/UIServiceProxy.md) | 提供与UIServiceExtensionAbility服务端数据通信的能力。 |

#### UIServiceExtensionConnectCallback14+

type UIServiceExtensionConnectCallback = [_UIServiceExtensionConnectCallback.default](../../topics/misc/UIServiceExtensionConnectCallback.md)

在连接指定的UIServiceExtensionAbility服务时作为入参，用于提供UIServiceExtensionAbility连接回调数据能力。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_UIServiceExtensionConnectCallback.default](../../topics/misc/UIServiceExtensionConnectCallback.md) | 提供UIServiceExtensionAbility连接回调数据能力。 |

#### AppService[ExtensionContext](../../topics/misc/ExtensionContext.md)20+

type AppService[ExtensionContext](../../topics/misc/ExtensionContext.md) = _AppServiceExtensionContext.default

[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)组件上下文，继承自Context。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _AppService[ExtensionContext](../../topics/misc/ExtensionContext.md).default | AppServiceExtensionAbility组件上下文。 |

#### FormEdit[ExtensionContext](../../topics/misc/ExtensionContext.md)22+

type FormEdit[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_FormEditExtensionContext.default](../../topics/misc/FormEditExtensionContext.md)

[FormEditExtensionAbility](@ohos.app.form.FormEditExtensionAbility  (FormEditExtensionAbility).md)组件上下文，继承自[UIExtensionContext](UIExtensionContext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _FormEdit[ExtensionContext](../../topics/misc/ExtensionContext.md).default | FormEditExtensionAbility组件上下文。 |

#### LiveForm[ExtensionContext](../../topics/misc/ExtensionContext.md)22+

type LiveForm[ExtensionContext](../../topics/misc/ExtensionContext.md) = [_LiveFormExtensionContext.default](../../topics/misc/LiveFormExtensionContext.md)

[LiveFormExtensionAbility](@ohos.app.form.LiveFormExtensionAbility  (LiveFormExtensionAbility).md)组件上下文，继承自[ExtensionContext](ExtensionContext.md)。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _LiveForm[ExtensionContext](../../topics/misc/ExtensionContext.md).default | LiveFormExtensionAbility组件上下文。 |

**示例：**

```ets
import { common } from '@kit.AbilityKit';

let uiAbilityContext: common.UIAbilityContext;
let abilityStageContext: common.AbilityStageContext;
let applicationContext: common.ApplicationContext;
let baseContext: common.BaseContext;
let context: common.Context;
let uiExtensionContext: common.UIExtensionContext;
let extensionContext: common.ExtensionContext;
let formExtensionContext: common.FormExtensionContext;
let vpnExtensionContext: common.VpnExtensionContext;
let eventHub: common.EventHub;
let pacMap: common.PacMap;
let abilityResult: common.AbilityResult;
let abilityStartCallback: common.AbilityStartCallback;
let connectOptions: common.ConnectOptions;
let embeddableUIAbilityContext: common.EmbeddableUIAbilityContext;
let photoEditorExtensionContext: common.PhotoEditorExtensionContext;
let uiServiceProxy : common.UIServiceProxy;
let uiServiceExtensionConnectCallback : common.UIServiceExtensionConnectCallback;
let appServiceExtensionContext : common.AppServiceExtensionContext;
let formEditExtensionContext : common.FormEditExtensionContext;
let liveFormExtensionContext : common.LiveFormExtensionContext;
```