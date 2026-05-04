# 获取Push Token

本文根据华为开发者官网 `push-get-token` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-get-token>
更新时间：2026-04-28 03:31:56

## 场景介绍
Push Kit对Push Token进行了权益校验，请在进行开发前先阅读开通推送服务章节，完成相关配置。
Push Token标识了每台设备上每个应用，开发者调用getToken()接口向Push Kit服务端请求Push Token，获取到之后使用Push Token来推送消息。
Push Token一般情况不会变化，仅下列场景会导致之前的Push Token发生变化而失效：
卸载应用后重新安装。
设备恢复出厂设置。
应用显式调用deleteToken()接口后重新调用getToken()接口。
应用显式调用deleteAAID()接口后重新调用getToken()接口。
将设备（仅涉及Wearable设备）拿到海外其他国家或者地区后，系统会更新设备的token。更新后的token通过pushService.on('tokenUpdate')接口的回调返回。
因此，建议您在应用启动时调用getToken()接口，若设备的Push Token发生变化，及时上报到您的应用服务器更新Push Token，以防由于Push Token失效导致收不到消息。

## 约束与限制
获取Push Token能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 注意事项
请勿使用Push Token跟踪标记用户。
应用不要固定判断Push Token长度，因为Push Token长度可能会变化。
禁止应用频繁申请Push Token。建议应用每次启动时获取Push Token。
只有在AppGallery Connect平台开通推送服务后，getToken方法才会返回Push Token。

## 接口说明
接口返回值有两种返回形式：Callback和Promise回调。下表中仅展示Promise回调形式的接口，Promise和Callback只是返回值方式不一样，功能相同。
接口名
描述
getToken(): Promise<string>
以Promise形式获取Push Token。
deleteToken(): Promise<void>
以Promise形式删除Push Token。

## 获取Push Token
Push Kit对Push Token进行了权益校验，请在进行开发前先阅读开通推送服务章节，完成相关配置。
导入pushService模块及相关公共模块。
import { pushService } from '@kit.PushKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
建议在您的UIAbility（例如EntryAbility）的onCreate()方法中调用getToken()接口获取Push Token并上报到您的服务端，方便您的服务端向终端推送消息。代码示例：
// 文件路径: src/main/ets/entryability/EntryAbility.ets export default class EntryAbility extends UIAbility { // 入参want与launchParam并未使用，为初始化项目时自带参数 onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { // 获取Push Token pushService.getToken().then(token => { hilog.info(0x0000, 'testTag', 'Succeeded in getting push token'); }).catch((err: BusinessError) => { hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message); }) // 上报Push Token并上报到您的服务端 } }
若您获取Push Token时发生APP身份验证失败错误（1000900010），请参考ArkTS API错误码排查。

## 删除Push Token
删除Push Token后，本应用下的所有Push Kit历史数据会一并删除。非必要情况，请您不要主动调用deleteToken()接口。
导入pushService模块。
import { pushService } from '@kit.PushKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { UIAbility } from '@kit.AbilityKit';
调用PushService.deleteToken()接口删除Push Token。代码示例：
// 文件路径: src/main/ets/entryability/EntryAbility.ets export default class EntryAbility extends UIAbility { async myDeletePushToken() { try { await pushService.deleteToken(); hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token'); } catch (err) { let e: BusinessError = err as BusinessError; hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message); } } }

## Push Token更新回调
Push Token更新回调能力支持Wearable设备。并且从6.1.0(23)版本开始，新增支持Phone、Tablet、PC/2in1设备。
当设备离开当前国家或地区时，可能会触发Push Token自动更新，如果应用期望感知到Push Token更新事件，需要调用on接口进行回调注册；对应的，可以调用off接口解除回调注册，解除后当Push Token更新时，应用将不会收到回调。
导入pushService模块。
import { pushService } from '@kit.PushKit';
在您项目的ability（下以PushMessageAbility为例）内导入push模块，调用on()方法接收token更新的消息。注意，您仅能使用UIAbility接收token更新消息。代码示例：
// 文件路径: src/main/ets/abilities/PushMessageAbility.ets import { UIAbility } from '@kit.AbilityKit'; import { pushService } from '@kit.PushKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; // 无需新增UIAbility，在原有UIAbility的onCreate方法中调用即可。以PushMessageAbility为例 export default class PushMessageAbility extends UIAbility { onCreate(): void { const callBack = (data: string) => { try { hilog.info(0x0000, 'testTag', 'update token: %{public}s', data); } catch (e) { let err: BusinessError = e as BusinessError; hilog.error(0x0000, 'testTag', 'Failed to update data: %{public}d %{public}s', err.code, err.message); } } try { // 注册token更新回调场景 pushService.on('tokenUpdate', this, callBack); hilog.info(0x0000, 'testTag', 'Register on success'); } catch (e) { let err: BusinessError = e as BusinessError; hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', err.code, err.message); } } onDestroy(): void { try { // 解除注册token更新回调场景 pushService.off('tokenUpdate'); hilog.info(0x0000, 'testTag', 'Register off success'); } catch (e) { let err: BusinessError = e as BusinessError; hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', err.code, err.message); } } }
在项目工程的 src/main/module.json5文件的abilities模块的skills标签中配置actions内容为action.ohos.push.listener（有且只能有一个ability定义该action，若同时添加uris参数，则uris内容需为空）。
"abilities": [ { "name": "PushMessageAbility", "srcEntry": "./ets/abilities/PushMessageAbility.ets", "launchType": "singleton", "startWindowIcon": "$media:startIcon", "startWindowBackground": "$color:start_window_background", "exported": false, "skills": [ { "actions": [ "action.ohos.push.listener" ] } ] } ]
