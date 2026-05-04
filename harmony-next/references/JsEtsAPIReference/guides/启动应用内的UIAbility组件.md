# 启动应用内的UIAbility组件

本文根据华为开发者官网 `uiability-intra-device-interaction` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction>
更新时间：2026-04-30 02:41:24

## 启动应用内的UIAbility
当一个应用内包含多个UIAbility时，存在应用内启动UIAbility的场景。例如在支付应用中从入口UIAbility启动收付款UIAbility。
假设应用中有两个UIAbility：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。
在EntryAbility中，通过调用startAbility()方法启动UIAbility，want为UIAbility实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的Ability名称，moduleName在待启动的UIAbility属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式请参见获取UIAbility的上下文信息。
import { common, Want } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; const TAG: string = '[MainPage]'; const DOMAIN_NUMBER: number = 0xFF00; @Entry @Component struct MainPage { private context = this.getUIContext().getHostContext() as common.UIAbilityContext; build() { Column() { List({ initialIndex: 0, space: 8 }) { ListItem() { Row() { // ... } .onClick(() => { // context为Ability对象的成员，在非Ability对象内部调用需要 // 将Context对象传递过去 let wantInfo: Want = { deviceId: '', // deviceId为空表示本设备 bundleName: 'com.samples.uiabilityinteraction', moduleName: 'entry', // moduleName非必选 abilityName: 'FuncAbilityA', parameters: { // 自定义信息 // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面" info: $r('app.string.main_page_return_info') }, }; // context为调用方UIAbility的UIAbilityContext this.context.startAbility(wantInfo).then(() => { hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.'); }).catch((error: BusinessError) => { hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.'); }); }) } // ... } // ... } // ... } }
在FuncAbility的onCreate()或者onNewWant()生命周期回调文件中接收EntryAbility传递过来的参数。
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit'; // ··· export default class FuncAbilityA extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { // 接收调用方UIAbility传过来的参数 let funcAbilityWant = want; let info = funcAbilityWant?.parameters?.info; // ··· } // ··· }
在被拉起的FuncAbility中，可以通过获取传递过来的want参数的parameters来获取拉起方UIAbility的PID、Bundle Name等信息。
在FuncAbility业务完成之后，如需要停止当前UIAbility实例，在FuncAbility中通过调用terminateSelf()方法实现。
import { common } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG: string = '[FuncAbilityAPage]'; const DOMAIN_NUMBER: number = 0xFF00; @Entry @Component struct FuncAbilityAPage { build() { Column() { // 请将$r('app.string.Stop_AbilityA')替换为实际资源文件，在本示例中该资源文件的value值为"StopFuncAbilityA" Button($r('app.string.Stop_AbilityA')) .onClick(() => { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext // context为需要停止的UIAbility实例的AbilityContext context.terminateSelf((err) => { if (err.code) { hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self. Code is ${err.code}, message is ${err.message}`); return; } }); }) // ... } // ... } }
调用terminateSelf()方法停止当前UIAbility实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应UIAbility的module.json5配置文件中，将abilities标签的removeMissionAfterTerminate字段配置为true。
如需要关闭应用所有的UIAbility实例，可以调用ApplicationContext的killAllProcesses()方法实现关闭应用所有的进程。

## 启动应用内的UIAbility并获取返回结果
在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和账号登录功能分别设计为两个独立的UIAbility，在账号登录UIAbility中完成登录操作后，需要将登录的结果返回给入口UIAbility。
在EntryAbility中，调用startAbilityForResult()接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式请参见获取UIAbility的上下文信息。
import { common, Want } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; const TAG: string = '[MainPage]'; const DOMAIN_NUMBER: number = 0xFF00; @Entry @Component struct MainPage { private context = this.getUIContext().getHostContext() as common.UIAbilityContext; build() { Column() { List({ initialIndex: 0, space: 8 }) { // ... ListItem() { Row() { // ... } .onClick(() => { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext const RESULT_CODE: number = 1001; let want: Want = { deviceId: '', // deviceId为空表示本设备 bundleName: 'com.samples.uiabilityinteraction', moduleName: 'entry', // moduleName非必选 abilityName: 'FuncAbilityA', parameters: { // 自定义信息 // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面" info: $r('app.string.main_page_return_info') } }; context.startAbilityForResult(want).then((data) => { if (data?.resultCode === RESULT_CODE) { // 解析被调用方UIAbility返回的信息 let info = data.want?.parameters?.info; hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? ''); if (info !== null) { this.getUIContext().getPromptAction().showToast({ message: JSON.stringify(info) }); } } hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? ''); }).catch((err: BusinessError) => { hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`); }); }) } // ... } // ... } // ... } }
在FuncAbility停止自身时，需要调用terminateSelfWithResult()方法，入参abilityResult为FuncAbility需要返回给EntryAbility的信息。
import { common } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG: string = '[FuncAbilityAPage]'; const DOMAIN_NUMBER: number = 0xFF00; @Entry @Component struct FuncAbilityAPage { build() { Column() { // ... List({ initialIndex: 0 }) { ListItem() { Row() { // ... } .onClick(() => { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext const RESULT_CODE: number = 1001; // FuncAbilityA返回的结果 let abilityResult: common.AbilityResult = { resultCode: RESULT_CODE, want: { bundleName: 'com.samples.uiabilityinteraction', moduleName: 'entry', // moduleName非必选 abilityName: 'FuncAbilityA', parameters: { // 请将$r('app.string.ability_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自FuncAbility Index页面" info: context.resourceManager.getStringSync($r('app.string.ability_return_info').id) }, }, }; context.terminateSelfWithResult(abilityResult, (err) => { if (err.code) { hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self with result. Code is ${err.code}, message is ${err.message}`); return; } }); }) } } // ... } // ... } }
FuncAbility停止自身后，EntryAbility通过startAbilityForResult()方法回调接收被FuncAbility返回的信息，RESULT_CODE需要与前面的数值保持一致。

## 启动UIAbility的指定页面

## 概述
一个UIAbility可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。
UIAbility的启动分为两种情况：UIAbility冷启动和UIAbility热启动。
UIAbility冷启动：指的是UIAbility实例处于完全关闭状态下被启动，这需要完整地加载和初始化UIAbility实例的代码、资源等。
UIAbility热启动：指的是UIAbility实例已经启动并在前台运行过，由于某些原因切换到后台，再次启动该UIAbility实例，这种情况下可以快速恢复UIAbility实例的状态。
本文主要讲解目标UIAbility冷启动和目标UIAbility热启动两种启动指定页面的场景，以及在讲解启动指定页面之前会讲解到在调用方如何指定启动页面。

## 调用方UIAbility指定启动页面
调用方UIAbility启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，Second对应功能A页面），此时需要在传入的want参数中配置指定的页面路径信息，可以通过Want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式请参见获取UIAbility的上下文信息。
import { common, Want } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { BusinessError } from '@kit.BasicServicesKit'; const TAG: string = '[MainPage]'; const DOMAIN_NUMBER: number = 0xFF00; @Entry @Component struct MainPage { private context = this.getUIContext().getHostContext() as common.UIAbilityContext; build() { Column() { List({ initialIndex: 0, space: 8 }) { // ... ListItem() { Row() { // ... } .onClick(() => { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext let want: Want = { deviceId: '', // deviceId为空表示本设备 bundleName: 'com.samples.uiabilityinteraction', moduleName: 'entry', // moduleName非必选 abilityName: 'ColdStartAbility', parameters: { // 自定义参数传递页面信息 router: 'funcA' } }; // context为调用方UIAbility的UIAbilityContext context.startAbility(want).then(() => { hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting ability.'); }).catch((err: BusinessError) => { hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${err.code}, message is ${err.message}`); }); }) } // ... } // ... } // ... } }

## 目标UIAbility冷启动
目标UIAbility冷启动时，在目标UIAbility的onCreate()生命周期回调中，接收调用方传过来的参数。然后在目标UIAbility的onWindowStageCreate()生命周期回调中，解析调用方传递过来的want参数，获取到需要加载的页面信息url，传入windowStage.loadContent()方法。
import { AbilityConstant, Want, UIAbility } from '@kit.AbilityKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; import { window, UIContext } from '@kit.ArkUI'; const DOMAIN_NUMBER: number = 0xFF00; const TAG: string = '[ColdStartAbility]'; export default class ColdStartAbility extends UIAbility { private funcAbilityWant: Want | undefined = undefined; private uiContext: UIContext | undefined = undefined; onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { // 接收调用方UIAbility传过来的参数 this.funcAbilityWant = want; } onWindowStageCreate(windowStage: window.WindowStage): void { // Main window is created, set main page for this ability hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate'); // Main window is created, set main page for this ability let url = 'pages/Index'; if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') { url = 'pages/ColdPage'; } windowStage.loadContent(url, (err, data) => { // ··· }); } }

## 目标UIAbility热启动
在应用开发中，会遇到目标UIAbility实例之前已经启动过的场景，这时再次启动目标UIAbility时，不会重新走初始化逻辑，只会直接触发onNewWant()生命周期方法。为了实现跳转到指定页面，需要在onNewWant()中解析参数进行处理。
例如短信应用和联系人应用配合使用的场景。
用户先打开短信应用，短信应用的UIAbility实例启动，显示短信应用的主页。
用户将设备回到桌面界面，短信应用进入后台运行状态。
用户打开联系人应用，找到联系人张三。
用户点击联系人张三的短信按钮，会再次启动短信应用的UIAbility实例。
由于短信应用的UIAbility实例已经启动过了，此时会触发该UIAbility的onNewWant()回调，而不会再走onCreate()和onWindowStageCreate()等初始化逻辑。
图1 目标UIAbility热启动
开发步骤如下所示。
冷启动短信应用的UIAbility实例时，在onWindowStageCreate()生命周期回调中，通过调用getUIContext()接口获取UI上下文实例UIContext对象。
import { hilog } from '@kit.PerformanceAnalysisKit'; import { Want, UIAbility } from '@kit.AbilityKit'; import { window, UIContext } from '@kit.ArkUI'; const DOMAIN_NUMBER: number = 0xFF00; const TAG: string = '[HotStartAbility]'; export default class HotStartAbility extends UIAbility { private funcAbilityWant: Want | undefined = undefined; private uiContext: UIContext | undefined = undefined; // ··· onWindowStageCreate(windowStage: window.WindowStage): void { // Main window is created, set main page for this ability hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate'); let url = 'pages/Index'; windowStage.loadContent(url, (err, data) => { if (err.code) { return; } let windowClass: window.Window; windowStage.getMainWindow((err, data) => { if (err.code) { hilog.error(DOMAIN_NUMBER, TAG, `Failed to obtain the main window. Code is ${err.code}, message is ${err.message}`); return; } windowClass = data; this.uiContext = windowClass.getUIContext(); }); hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? ''); }); } // ··· }
在短信应用UIAbility的onNewWant()回调中通过AppStorage设置全局变量nameForNavi的值，并进行指定页面的跳转。此时再次启动该短信应用的UIAbility实例时，即可跳转到该短信应用的UIAbility实例的指定页面。
