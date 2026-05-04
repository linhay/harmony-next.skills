# UIAbility组件启动模式

本文根据华为开发者官网 `uiability-launch-type` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type>
更新时间：2026-04-30 09:02:20

## singleton启动模式
singleton启动模式为单实例模式，也是默认情况下的启动模式。
每次调用startAbility()方法时，如果应用进程中该类型的UIAbility实例已经存在，则复用系统中的UIAbility实例。系统中只存在唯一一个该UIAbility实例，即在最近任务列表中只存在一个该类型的UIAbility实例。
图1 单实例模式演示效果
应用的UIAbility实例已创建，该UIAbility配置为单实例模式，再次调用startAbility()方法启动该UIAbility实例。由于启动的还是原来的UIAbility实例，并未重新创建一个新的UIAbility实例，此时只会进入该UIAbility的onNewWant()回调，不会进入其onCreate()和onWindowStageCreate()生命周期回调。如果已经创建的实例仍在启动过程中，调用startAbility()方法启动该实例，将收到错误码16000082。
如果需要使用singleton启动模式，在module.json5配置文件中的launchType字段配置为singleton即可。
{ "module": { // ··· "abilities": [ // ··· { "launchType": "singleton", // ··· } // ··· ] } }

## multiton启动模式
multiton启动模式为多实例模式，每次调用startAbility()方法时，都会在应用进程中创建一个新的该类型UIAbility实例。即在最近任务列表中可以看到有多个该类型的UIAbility实例。这种情况下可以将UIAbility配置为multiton（多实例模式）。
图2 多实例模式演示效果
multiton启动模式的开发使用，在module.json5配置文件中的launchType字段配置为multiton即可。
{ "module": { // ··· "abilities": [ // ··· { "launchType": "multiton", // ··· } // ··· ] } }

## specified启动模式
specified启动模式为指定实例模式，针对一些特殊场景使用（例如文档应用中每次新建文档希望都能新建一个文档实例，重复打开一个已保存的文档希望打开的都是同一个文档实例）。
图3 指定实例启动模式原理
假设应用有两个UIAbility实例，即EntryAbility和SpecifiedAbility。EntryAbility以specified模式启动SpecifiedAbility。基本原理如下：
EntryAbility调用startAbility()方法，并在Want的parameters字段中设置唯一的Key值，用于标识SpecifiedAbility。
系统在拉起SpecifiedAbility之前，会先进入对应的AbilityStage的onAcceptWant()生命周期回调，获取用于标识目标UIAbility的Key值。
如果匹配到对应的UIAbility，则会启动该UIAbility实例，并进入onNewWant()生命周期回调。
如果无法匹配对应的UIAbility，则会创建一个新的UIAbility实例，并进入该UIAbility实例的onCreate()生命周期回调和onWindowStageCreate()生命周期回调。
图4 指定实例模式演示效果
在SpecifiedAbility中，需要将module.json5配置文件的launchType字段配置为specified。
{ "module": { // ··· "abilities": [ { "launchType": "specified", // ··· } // ··· ] } }
在EntryAbility中，调用startAbility()方法时，可以在want参数中传入了自定义参数instanceKey作为唯一标识符，以此来区分不同的UIAbility实例。示例中instanceKey的value值设置为字符串'KEY'。
// 在启动指定实例模式的UIAbility时，给每一个UIAbility实例配置一个独立的Key标识 // 例如在文档使用场景中，可以用文档路径作为Key标识 import { common, Want } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; const TAG: string = '[SpecifiedPage]'; const DOMAIN_NUMBER: number = 0xFF00; function getInstance(): string { return 'KEY'; } @Entry @Component struct SpecifiedPage { private KEY_NEW = 'KEY'; build() { Row() { Column() { // ... // 请将$r('app.string.new_doc')替换为实际资源文件，在本示例中该资源文件的value值为"新建一个文档" Button($r('app.string.new_doc')) // ... .onClick(() => { let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // context为调用方UIAbility的UIAbilityContext; let want: Want = { deviceId: '', // deviceId为空表示本设备 bundleName: 'com.samples.uiabilitylaunchtype', abilityName: 'SpecifiedFirstAbility', moduleName: 'entry', // moduleName非必选 parameters: { // 自定义信息 instanceKey: this.KEY_NEW } }; context.startAbility(want).then(() => { hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.'); }).catch((err: BusinessError) => { hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`); }); this.KEY_NEW = this.KEY_NEW + 'a'; }) // 请将$r('app.string.open_old_doc')替换为实际资源文件，在本示例中该资源文件的value值为"打开已保存文档" Button($r('app.string.open_old_doc')) // ... .onClick(() => { let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // context为调用方UIAbility的UIAbilityContext; let want: Want = { deviceId: '', // deviceId为空表示本设备 bundleName: 'com.samples.uiabilitylaunchtype', abilityName: 'SpecifiedSecondAbility', moduleName: 'entry', // moduleName非必选 parameters: { // 自定义信息 instanceKey: getInstance() } }; context.startAbility(want).then(() => { hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.'); }).catch((err: BusinessError) => { hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`); }); this.KEY_NEW = this.KEY_NEW + 'a'; }) } .width('100%') } .height('100%') } }

## 示例代码
UIAbility的启动方式
