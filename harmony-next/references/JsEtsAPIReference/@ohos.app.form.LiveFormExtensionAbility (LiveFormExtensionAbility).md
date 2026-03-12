# @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)

LiveFormExtensionAbility模块提供互动卡片功能，包括创建、销毁互动卡片等，继承自[ExtensionAbility](@ohos.app.ability.ExtensionAbility (扩展能力基类).md)。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](@ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility).md#ZH-CN_TOPIC_0000002497605280__附录)。

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

名称类型只读可选说明context[LiveFormExtensionContext](LiveFormExtensionContext.md)否否LiveFormExtensionAbility的上下文环境，继承自[ExtensionContext](ExtensionContext.md)。

#### onLiveFormCreate

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

LiveFormExtensionAbility界面内容对象创建后调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明liveFormInfo[LiveFormInfo](#ZH-CN_TOPIC_0000002497605280__liveforminfo)是互动卡片信息，包括卡片id等信息。session[UIExtensionContentSession](zh-cn_topic_0000002497444616.html)是LiveFormExtensionAbility界面内容相关信息。

**示例：**

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    console.info(TAG, `onLiveFormCreate, liveFormInfo: ${JSON.stringify(liveFormInfo)}`);
  }
}
```

#### onLiveFormDestroy

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

LiveFormExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明liveFormInfo[LiveFormInfo](#ZH-CN_TOPIC_0000002497605280__liveforminfo)是互动卡片信息，包括卡片id等信息。

**示例：**

```ets
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
    console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${JSON.stringify(liveFormInfo)}`);
  }
}
```

#### LiveFormInfo

互动卡片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

名称类型只读可选说明formIdstring否否卡片id。rect[formInfo.Rect](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__rect20)否否卡片位置和大小信息。borderRadiusnumber否否卡片圆角半径信息。取值大于0，单位vp。

#### 附录

本模块不允许调用的API名单如下。

Kit名称模块名称AbilityKit

[@ohos.ability.featureAbility (FeatureAbility模块)](@ohos.ability.featureAbility (FeatureAbility模块).md)

[@ohos.ability.particleAbility (ParticleAbility模块)](@ohos.ability.particleAbility (ParticleAbility模块).md)

[@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](@ohos.bundle.launcherBundleManager (launcherBundleManager模块).md)

[@ohos.continuation.continuationManager (流转/协同管理)](@ohos.continuation.continuationManager (流转_协同管理).md)

BasicServicesKit

[@ohos.account.appAccount (应用账号管理)](@ohos.account.appAccount (应用账号管理).md)

[@ohos.account.distributedAccount (分布式账号管理)](@ohos.account.distributedAccount (分布式账号管理).md)

[@ohos.account.osAccount (系统账号管理)](@ohos.account.osAccount (系统账号管理).md)

[@ohos.pasteboard (剪贴板)](@ohos.pasteboard (剪贴板).md)

[@ohos.request (上传下载)](@ohos.request (上传下载).md)

[@ohos.wallpaper (壁纸)](@ohos.wallpaper (壁纸).md)

BackgroundTasksKit

[@ohos.backgroundTaskManager (后台任务管理)](@ohos.backgroundTaskManager (后台任务管理).md)

[@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](@ohos.resourceschedule.backgroundTaskManager (后台任务管理).md)

[@ohos.reminderAgent (后台代理提醒)](@ohos.reminderAgent (后台代理提醒).md)

[@ohos.reminderAgentManager (后台代理提醒)](@ohos.reminderAgentManager (后台代理提醒).md)

CalendarKit[@ohos.calendarManager (日程管理能力)](@ohos.calendarManager (日程管理能力).md)ConnectivityKit

[@ohos.connectedTag (有源标签)](@ohos.connectedTag (有源标签).md)

[@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](@ohos.nfc.cardEmulation (标准NFC-cardEmulation).md)

[@ohos.nfc.controller (标准NFC)](@ohos.nfc.controller (标准NFC).md)

[@ohos.nfc.tag (标准NFC-Tag)](@ohos.nfc.tag (标准NFC-Tag).md)

[nfctech (标准NFC-Tag Nfc 技术)](nfctech (标准NFC-Tag Nfc 技术).md)

[tagSession (标准NFC-Tag TagSession)](tagSession (标准NFC-Tag TagSession).md)

ContactsKit[@ohos.contact (联系人)](@ohos.contact (联系人).md)ArkData

[@ohos.data.distributedData (分布式数据管理)](@ohos.data.distributedData (分布式数据管理).md)

[@ohos.data.distributedDataObject (分布式数据对象)](@ohos.data.distributedDataObject (分布式数据对象).md)

[@ohos.data.distributedKVStore (分布式键值数据库)](@ohos.data.distributedKVStore (分布式键值数据库).md)

MDMKit

[@ohos.enterprise.adminManager (admin权限管理)](@ohos.enterprise.adminManager（admin权限管理）.md)

[@ohos.enterprise.deviceInfo（设备信息管理）](@ohos.enterprise.deviceInfo（设备信息管理）.md)

CoreFileKit[@ohos.file.picker (选择器)](@ohos.file.picker (选择器).md)MediaLibraryKit

[@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块).md)

[@ohos.file.AlbumPickerComponent (Album Picker组件)](@ohos.file.AlbumPickerComponent (Album Picker组件).md)

[@ohos.file.PhotoPickerComponent (PhotoPicker组件)](@ohos.file.PhotoPickerComponent (PhotoPicker组件).md)

[@ohos.file.RecentPhotoComponent (最近图片组件)](@ohos.file.RecentPhotoComponent (最近图片组件).md)

[@ohos.multimedia.movingphotoview (动态照片)](@ohos.multimedia.movingphotoview (动态照片).md)

PerformanceAnalysisKit[@ohos.hidebug (Debug调试)](@ohos.hidebug (Debug调试).md)AudioKit[@ohos.multimedia.audio (音频管理)](模块描述.md)CameraKit

[@ohos.multimedia.cameraPicker (相机选择器)](@ohos.multimedia.cameraPicker (相机选择器).md)

[@ohos.multimedia.camera (相机管理)](模块描述.md)

AVSessionKit

[@ohos.multimedia.avCastPicker (投播组件)](@ohos.multimedia.avCastPicker (投播组件).md)

[@ohos.multimedia.avsession (媒体会话管理)](模块描述.md)

MediaKit[@ohos.multimedia.media (媒体服务)](模块描述.md)NotificationKit

[@ohos.notification (Notification模块)](@ohos.notification (Notification模块).md)

[@ohos.notificationManager (NotificationManager模块)](@ohos.notificationManager (NotificationManager模块).md)

TelephonyKit

[@ohos.telephony.call (拨打电话)](@ohos.telephony.call (拨打电话).md)

[@ohos.telephony.data (蜂窝数据)](@ohos.telephony.data (蜂窝数据).md)

[@ohos.telephony.observer (observer)](@ohos.telephony.observer (observer).md)

[@ohos.telephony.radio (网络搜索)](@ohos.telephony.radio (网络搜索).md)

[@ohos.telephony.sim (SIM卡管理)](@ohos.telephony.sim (SIM卡管理).md)

[@ohos.telephony.sms (短信服务)](@ohos.telephony.sms (短信服务).md)

UserAuthenticationKit[@ohos.userIAM.userAuth (用户认证)](@ohos.userIAM.userAuth (用户认证).md)ArkUI[@ohos.window (窗口)](模块描述.md)MapKit[sceneMap（场景化控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-scenemap)PaymentKit[paymentService (鸿蒙支付服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice)ServiceCollaborationKit

[devicePicker (设备选择控制器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-devicepicker)

[CollaborationDevicePicker (流转控件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdevicepicker)

ShareKit

[systemShare（分享）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-system-share)

[harmonyShare（华为分享）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-harmony-share)

VisionKit

[CardRecognition（卡证识别控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition#section143611912403)

[DocumentScanner（文档扫描控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-document-scanner#section143611912403)

ScanKit[Scan Kit（统一扫码服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-api)