# @ohos.app.ability.wantConstant (Want常量)

wantConstant模块提供了[Want](@ohos.app.ability.Want (Want).md)操作相关的系统预设枚举和常量，例如在启动Ability时常用的Flag、Param参数等。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wantConstant } from '@kit.AbilityKit';
```

#### Params

[Want.parameters](@ohos.app.ability.Want (Want).md#ZH-CN_TOPIC_0000002529284603__want)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的参数信息。例如在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的启动阶段，如果从onCreate回调的入参want字段中获取到ABILITY_RECOVERY_RESTART的值为true，则表示当前UIAbility发生了故障重启。

**系统能力**：SystemCapability.Ability.AbilityBase

名称值说明ABILITY_BACK_TO_OTHER_MISSION_STACKability.params.backToOtherMissionStack

表示是否支持跨任务链返回。

该参数用于控制跨应用的UIAbility返回逻辑，其核心作用是改变用户执行返回键时的应用跳转行为。例如现有UIAbility A和UIAbility B，当前前台显示的是UIAbility A，随后系统服务又拉起UIAbility B（同时在Want的Params字段配置该参数为true），那么，当UIAbility B退出时，会返回到UIAbility A（即返回到最近一次的访问任务）。如果未配置该参数，则默认直接返回桌面。需要注意的是，该字段仅支持系统设置，三方应用传入该字段不生效。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

ABILITY_RECOVERY_RESTART10+ohos.ability.params.abilityRecoveryRestart

表示当前Ability是否发生了故障恢复重启。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

CONTENT_TITLE_KEY10+ohos.extra.param.key.contentTitle

表示元服务分享的标题。

在跨端分享的[onShare](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onshare10)回调中，开发者可通过该字段设置分享的标题。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SHARE_ABSTRACT_KEY10+ohos.extra.param.key.shareAbstract

表示元服务分享的内容摘要。

在跨端分享的[onShare](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onshare10)回调中，开发者可通过该字段设置分享的摘要。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SHARE_URL_KEY10+ohos.extra.param.key.shareUrl

表示元服务分享的URL链接。

在跨端分享的[onShare](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__onshare10)回调中，开发者可通过该字段设置分享的URL链接。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SUPPORT_CONTINUE_PAGE_STACK_KEY10+ohos.extra.param.key.supportContinuePageStack

表示在跨端迁移过程中是否迁移页面栈信息。默认值为true，表示在跨端迁移过程中自动迁移页面栈信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SUPPORT_CONTINUE_SOURCE_EXIT_KEY10+ohos.extra.param.key.supportContinueSourceExit

表示跨端迁移源端应用是否退出。默认值为true，表示在跨端迁移过程中源端应用自动退出。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

SHOW_MODE_KEY12+ohos.extra.param.key.showMode

表示[EmbeddableUIAbility](@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件).md)的显示模式，值为枚举类型[ShowMode](#ZH-CN_TOPIC_0000002497604612__showmode12)

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

PARAMS_STREAM12+ability.params.stream

表示授权给目标方的文件URI列表。对应的value必须是string类型的文件URI数组。文件URI的获取参考[fileUri](@ohos.file.fileuri (文件URI).md#ZH-CN_TOPIC_0000002529285247__fileurigeturifrompath) 。该字段需要与文件URI[读写Flag](@ohos.app.ability.wantConstant (Want常量).md#ZH-CN_TOPIC_0000002497604612__flags)配合使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

APP_CLONE_INDEX_KEY12+ohos.extra.param.key.appCloneIndex

表示分身应用索引。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

CALLER_REQUEST_CODE12+ohos.extra.param.key.callerRequestCode

表示应用拉起的请求码。

当调用[startAbilityForResult](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startabilityforresult)或[openLink](../../topics/graphics/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__openlink12)拉起目标方Ability时，需要目标方返回结果。为了确保目标方能够将结果准确返回到调用方，系统会自动生成唯一的requestCode，以标识本次调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

PAGE_PATH12+ohos.param.atomicservice.pagePath

表示元服务的页面路径。

如果元服务的页面跳转是通过[router](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing)实现的，可以使用该参数指定跳转的页面，例如"library/ets/pages/menu"。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

ROUTER_NAME12+ohos.param.atomicservice.routerName

表示元服务的页面路由名称，即进行页面跳转时指定的页面名称。

如果元服务的页面跳转是通过[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)实现的，可以通过ROUTER_NAME、PAGE_SOURCE_FILE及BUILD_FUNCTION联合使用指定跳转的页面。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

PAGE_SOURCE_FILE12+ohos.param.atomicservice.pageSourceFile

表示元服务的页面源文件。

如果元服务的页面跳转是通过[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)实现的，可以通过ROUTER_NAME、PAGE_SOURCE_FILE及BUILD_FUNCTION联合使用指定跳转的页面。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

BUILD_FUNCTION12+ohos.param.atomicservice.buildFunction

表示元服务的生成函数。

如果元服务的页面跳转是通过[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)实现的，可以通过ROUTER_NAME、PAGE_SOURCE_FILE及BUILD_FUNCTION联合使用指定跳转的页面。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

SUB_PACKAGE_NAME12+ohos.param.atomicservice.subpackageName

表示元服务的分包名。应用程序包支持多模块开发，每个应用程序包可能包含多个HAP或HSP。元服务为了实现快速启动效果，对HAP和HSP文件大小做了限制，并同时优化了启动机制，元服务的这种多模块开发方式称为“分包”。

打开元服务的时候，可以通过设置该参数拉起对应的分包。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

APP_INSTANCE_KEY14+ohos.extra.param.key.appInstance

表示具体的应用实例。

在[应用创建多实例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multiinstance)时，系统会为每个实例分配唯一的标识。应用跳转时，开发者可以通过设置该参数指定希望跳转到的已创建的应用实例。

CREATE_APP_INSTANCE_KEY14+ohos.extra.param.key.createAppInstance

表示是否创建新应用实例。默认为false，表示不创建新应用实例。

开发者可以通过设置该参数为true拉起新的应用实例。需要注意的是，被拉起的应用需要支持多实例，参考[应用创建多实例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multiinstance)。

CALLER_APP_CLONE_INDEX14+ohos.param.callerAppCloneIndex表示拉起方应用的分身索引。APP_LAUNCH_TRUSTLIST17+ohos.params.appLaunchTrustList

表示隐式启动时的应用过滤列表。

隐式启动时仅匹配列表中的应用，值为string类型的[AppIdentifier](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)数组，过滤列表最多支持50个应用，传入空数组不生效。

**元服务API**：从API version 17开始，该接口支持在元服务中使用。

LAUNCH_REASON_MESSAGE18+ohos.params.launchReasonMessage

表示应用拉起的原因。

调用方必须为系统应用，且需要申请ohos.permission.SET_LAUNCH_REASON_MESSAGE权限。当前取值支持：

"ReasonMessage_SystemShare"：表示系统分享拉起。

"ReasonMessage_DesktopShortcut"：表示桌面快捷方式拉起。

"ReasonMessage_Notification"：表示通知拉起。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

DESTINATION_PLUGIN_ABILITY19+ohos.params.pluginAbility指示目标Ability是插件Ability。ATOMIC_SERVICE_SHARE_ROUTER20+ohos.params.atomicservice.shareRouter

表示被拉起的元服务的页面栈信息。仅当拉起方为UIAbilityContext，被拉起方为元服务时生效。

例如，某元服务中包含首页和第2页，如果希望直接拉起元服务的第2页，可以在拉起元服务时通过该字段传递第2页的页面栈信息。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

ABILITY_UNIFIED_DATA_KEY20+ohos.param.ability.udKey

表示基于[UDMF](@ohos.data.unifiedDataChannel (标准化数据通路).md)进行文件分享时使用的唯一标识。该字段只允许系统应用设置，三方应用可以读取。

当Want中存在URI授权Flag字段（即[FLAG_AUTH_READ_URI_PERMISSION](#ZH-CN_TOPIC_0000002497604612__flags)或[FLAG_AUTH_WRITE_URI_PERMISSION](#ZH-CN_TOPIC_0000002497604612__flags)），且同时存在PARAMS_STREAM字段时，该字段将不生效。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### Flags

[Want.flags](@ohos.app.ability.Want (Want).md#ZH-CN_TOPIC_0000002529284603__want)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的标志位信息。

**系统能力**：SystemCapability.Ability.AbilityBase

名称值说明FLAG_AUTH_READ_URI_PERMISSION0x00000001

表示临时授予接收方读取该URI指向的数据的权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

FLAG_AUTH_WRITE_URI_PERMISSION0x00000002

表示临时授予接收方写入该URI指向的数据的权限。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

FLAG_AUTH_PERSISTABLE_URI_PERMISSION12+0x00000040表示该URI可被接收方持久化。该字段仅在2in1和Tablet设备上生效。FLAG_INSTALL_ON_DEMAND0x00000800

表示拉起元服务时开启免安装功能。

- 如果开启了免安装功能，当系统检测到被拉起的元服务未安装时，会自动安装元服务，再进行拉起。

- 如果未开启免安装功能，当元服务未安装时，将拉起失败。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

FLAG_START_WITHOUT_TIPS11+0x40000000

表示是否关闭匹配失败弹窗功能。

通过[隐式方式拉起应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview)时，如果没有能够匹配的应用，默认会弹出提示弹窗“暂无可用打开方式”。开发者可以通过该字段屏蔽该弹窗。

FLAG_ABILITY_ON_COLLABORATE18+0x00002000在多设备协同场景下，调用方应用通过DMS系统发起请求并且通过Flags字段携带此标志，协同方应用才会触发生命周期回调方法[onCollaborate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002529444559__oncollaborate18)。

#### ShowMode12+

表示[EmbeddableUIAbility](@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件).md)被拉起时的显示模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

名称值说明WINDOW0表示独立窗口拉起模式。EMBEDDED_FULL1表示嵌入式全屏拉起模式。