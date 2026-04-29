# @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)

本模块实现故障的延迟通知功能。

[HiAppEvent](@ohos.hiviewdfx.hiAppEvent (应用事件打点).md)订阅崩溃、应用冻屏事件时，只有当应用下次启动后才能接收上一次的事件。如果应用无法启动或长时间未打开，则存在故障无法及时上报的局限性。

本模块作为该场景的补充。在应用实现FaultLogExtensionAbility后，当应用发生崩溃或冻屏时，系统服务预计会在30分钟后拉起FaultLogExtensionAbility。

开发者可在[onFaultReportReady](#ZH-CN_TOPIC_0000002553361699__onfaultreportready)中订阅并处理故障事件。


- 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。

- 本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](#ZH-CN_TOPIC_0000002553361699__附录)。

#### 导入模块

```ets
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';
```

#### FaultLogExtensionAbility

应用接入故障延迟通知需要通过FaultLogExtensionAbility实现，开发者可以在[onFaultReportReady](#ZH-CN_TOPIC_0000002553361699__onfaultreportready)中订阅并处理故障事件。


- FaultLogExtensionAbility被拉起后只有很短的时间完成故障处理，建议处理时间不要超过10秒。超时没有处理完成可以在[onDisconnect](#ZH-CN_TOPIC_0000002553361699__ondisconnect)中保存状态。

- 从开机或上次拉起FaultLogExtensionAbility后，应用首次触发崩溃或冻屏开始计时。在拉起FaultLogExtensionAbility前反复触发崩溃或冻屏事件均不会重新计时。
- FaultLogExtensionAbility自身崩溃时，不会再次被系统服务拉起。

#### 属性

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | FaultLog[ExtensionContext](../../topics/misc/ExtensionContext.md) | 否 | 否 | FaultLogExtensionAbility的上下文环境，继承自ExtensionContext。 |

#### onConnect

onConnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成连接时调用此接口，用于执行初始化操作，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ets
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onConnect() {
      console.info('onConnect');
    }
```

#### onDisconnect

onDisconnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成断开连接时调用此接口，用于释放资源清理运行状态，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ets
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onDisconnect() {
      console.info('onDisconnect');
}
```

#### onFaultReportReady

onFaultReportReady(): void

FaultLogExtensionAbility回调。系统服务通知FaultLogExtensionAbility可以进行故障处理时，回调此接口，可以在该方法中订阅故障事件进行处理。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ets
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        hiAppEvent.addWatcher({
            name: "watcher",
            appEventFilters: [
                {
                    domain: hiAppEvent.domain.OS,
                    names: [hiAppEvent.event.APP_CRASH, hiAppEvent.event.APP_FREEZE]
                }
            ],
            onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
                // 进行故障事件处理
            }
        });
    }
```

#### 附录

本模块不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| AVSessionKit | @ohos.multimedia.avsession (媒体会话管理) |
| AbilityKit | [@ohos.UIAbilityContext](../../topics/misc/UIAbilityContext.md) |
| ArkUI | @ohos.window (窗口) |
| AudioKit | @ohos.multimedia.audio (音频管理) |
| BackgroundTasksKit | @ohos.backgroundTaskManager (后台任务管理) |
| BackgroundTasksKit | @ohos.reminderAgent (后台代理提醒) |
| BackgroundTasksKit | @ohos.reminderAgentManager (后台代理提醒) |
| BackgroundTasksKit | @ohos.resourceschedule.backgroundTaskManager (后台任务管理) |
| BasicServicesKit | @ohos.power (系统电源管理) |
| BasicServicesKit | @ohos.wallpaper (壁纸) |
| CameraKit | @ohos.multimedia.camera (相机管理) |
| CameraKit | @ohos.multimedia.cameraPicker (相机选择器) |
| ConnectivityKit | @ohos.wifiManager (WLAN) |
| ConnectivityKit | @ohos.wifiManagerExt (WLAN扩展接口) |
| ConnectivityKit | @ohos.wifiext (WLAN扩展接口) |
| IMEKit | @ohos.inputMethod (输入法框架) |
| MediaLibraryKit | @ohos.multimedia.movingphotoview (动态照片) |
| NotificationKit | @ohos.notification (Notification模块) |
| NotificationKit | @ohos.notificationManager (NotificationManager模块) |
| SensorServiceKit | @ohos.vibrator (振动) |
| TelephonyKit | @ohos.telephony.call (拨打电话) |
| TelephonyKit | @ohos.telephony.sim (SIM卡管理) |
| TelephonyKit | @ohos.telephony.sms (短信服务) |
| UserAuthenticationKit | @ohos.userIAM.userAuth (用户认证) |