# @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)

LiveFormExtensionAbility模块提供互动卡片功能，包括创建、销毁互动卡片等，继承自[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](@ohos.app.form.LiveFormExtensionAbility  (LiveFormExtensionAbility).md#ZH-CN_TOPIC_0000002522081252__附录)。

#### 导入模块

```ets
import { LiveFormExtensionAbility } from '@kit.FormKit';
```

#### LiveFormExtensionAbility

互动卡片扩展类。包含互动卡片提供方接收创建和销毁互动卡片的通知接口。

#### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveFormExtensionContext](../../topics/misc/LiveForm[ExtensionContext](../../topics/misc/ExtensionContext.md).md) | 否 | 否 | LiveFormExtensionAbility的上下文环境，继承自ExtensionContext。 |

#### onLiveFormCreate

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

LiveFormExtensionAbility界面内容对象创建后调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | LiveFormInfo | 是 | 互动卡片信息，包括卡片id等信息。 |
| session | UIExtensionContentSession | 是 | LiveFormExtensionAbility界面内容相关信息。 |

**示例：**

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    console.info(TAG, `onLiveFormCreate, formId: ${liveFormInfo.formId}`);
  }
```

#### onLiveFormDestroy

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

LiveFormExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | LiveFormInfo | 是 | 互动卡片信息，包括卡片id等信息。 |

**示例：**

```ets
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
    console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}`);
  }
```

#### LiveFormInfo

互动卡片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 否 | 否 | 卡片id。 |
| rect | formInfo.Rect | 否 | 否 | 卡片位置和大小信息。 |
| borderRadius | number | 否 | 否 | 卡片圆角半径信息。取值大于0，单位vp。 |

#### 附录

本模块不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| AbilityKit | @ohos.ability.featureAbility (FeatureAbility模块) @ohos.ability.particleAbility (ParticleAbility模块) @ohos.bundle.launcherBundleManager (launcherBundleManager模块) @ohos.continuation.continuationManager (流转/协同管理) |
| BasicServicesKit | @ohos.account.appAccount (应用账号管理) @ohos.account.distributedAccount (分布式账号管理) @ohos.account.osAccount (系统账号管理) @ohos.pasteboard (剪贴板) @ohos.request (上传下载) @ohos.wallpaper (壁纸) |
| BackgroundTasksKit | @ohos.backgroundTaskManager (后台任务管理) @ohos.resourceschedule.backgroundTaskManager (后台任务管理) @ohos.reminderAgent (后台代理提醒) @ohos.reminderAgentManager (后台代理提醒) |
| CalendarKit | @ohos.calendarManager (日程管理能力) |
| ConnectivityKit | @ohos.connectedTag (有源标签) @ohos.nfc.cardEmulation (标准NFC-cardEmulation) @ohos.nfc.controller (标准NFC) @ohos.nfc.tag (标准NFC-Tag) nfctech (标准NFC-Tag Nfc 技术) tagSession (标准NFC-Tag TagSession) |
| ContactsKit | @ohos.contact (联系人) |
| ArkData | @ohos.data.distributedData (分布式数据管理) @ohos.data.distributedDataObject (分布式数据对象) @ohos.data.distributedKVStore (分布式键值数据库) |
| MDMKit | [@ohos.enterprise.adminManager (admin权限管理)](@ohos.enterprise.adminManager（admin权限管理）.md) [@ohos.enterprise.deviceInfo（设备信息管理）](@ohos.enterprise.deviceInfo（设备信息管理）.md) |
| CoreFileKit | @ohos.file.picker (选择器) |
| MediaLibraryKit | @ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块) @ohos.file.AlbumPickerComponent (Album Picker组件) @ohos.file.PhotoPickerComponent (PhotoPicker组件) @ohos.file.RecentPhotoComponent (最近图片组件) @ohos.multimedia.movingphotoview (动态照片) |
| PerformanceAnalysisKit | @ohos.hidebug (Debug调试) |
| AudioKit | @ohos.multimedia.audio (音频管理) |
| CameraKit | @ohos.multimedia.cameraPicker (相机选择器) @ohos.multimedia.camera (相机管理) |
| AVSessionKit | @ohos.multimedia.avCastPicker (投播组件) @ohos.multimedia.avsession (媒体会话管理) |
| MediaKit | @ohos.multimedia.media (媒体服务) |
| NotificationKit | @ohos.notification (Notification模块) @ohos.notificationManager (NotificationManager模块) |
| TelephonyKit | @ohos.telephony.call (拨打电话) @ohos.telephony.data (蜂窝数据) @ohos.telephony.observer (observer) @ohos.telephony.radio (网络搜索) @ohos.telephony.sim (SIM卡管理) @ohos.telephony.sms (短信服务) |
| UserAuthenticationKit | @ohos.userIAM.userAuth (用户认证) |
| ArkUI | @ohos.window (窗口) |
| MapKit | sceneMap（场景化控件） |
| PaymentKit | paymentService (鸿蒙支付服务) |
| ServiceCollaborationKit | devicePicker (设备选择控制器) CollaborationDevicePicker (流转控件) |
| ShareKit | systemShare（分享） harmonyShare（华为分享） |
| VisionKit | CardRecognition（卡证识别控件） DocumentScanner（文档扫描控件） |
| ScanKit | Scan Kit（统一扫码服务） |