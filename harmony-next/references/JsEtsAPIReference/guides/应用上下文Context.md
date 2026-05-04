# 应用上下文Context

本文根据华为开发者官网 `application-context-stage` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage>
更新时间：2026-04-30 02:41:24

## 概述
Context是应用中对象的上下文，其提供了应用的一些基础信息，例如resourceManager（资源管理）、applicationInfo（当前应用信息）、area（文件分区）等。

## 不同类型Context的对比
UIAbility组件和各种ExtensionAbility派生类组件都有各自不同的Context类。分别有基类Context、ApplicationContext、AbilityStageContext、UIAbilityContext、ExtensionContext等Context。各类Context的继承和持有关系详见不同类型Context的继承和持有关系。
不同类型Context的获取方式与使用场景说明，如下表所示。
不同类型的Context具有不同的能力，不可相互替代或强行转换。例如，ApplicationContext绑定了setFontSizeScale方法，但UIAbilityContext中没有此方法。因此，即使将UIAbilityContext强行转换为ApplicationContext，也无法调用setFontSizeScale方法。
表1 不同类型Context的说明
Context类型
说明
获取方式
使用场景
ApplicationContext
应用的全局上下文，提供应用级别的信息和能力。
- 从API version 14开始，可以直接使用getApplicationContext获取。
- API version 14以前版本，只能使用其他Context实例的getApplicationContext方法获取。

## Context的获取方式
开发者如果需要通过Context获取应用资源、应用路径等信息，或者使用Context提供的方法来实现应用跳转、设置环境变量、清理数据、获取权限等操作，需要先获取对应的Context。本节分别介绍不同类型Context的获取方式与使用场景。

## 获取ApplicationContext（应用的全局上下文）
ApplicationContext在基类Context的基础上提供了监听应用内应用组件的生命周期的变化、监听系统内存变化、监听应用内系统环境变化、设置应用语言、设置应用颜色模式、清除应用自身数据的同时撤销应用向用户申请的权限等能力，在UIAbility、ExtensionAbility、AbilityStage中均可以获取。
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit'; export default class EntryAbility extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { let applicationContext = this.context.getApplicationContext(); } }

## 获取AbilityStageContext（模块级别的上下文）
AbilityStageContext和基类Context相比，额外提供HapModuleInfo、Configuration等信息。
import { AbilityStage } from '@kit.AbilityKit'; export default class MyAbilityStage extends AbilityStage { onCreate(): void { let abilityStageContext = this.context; // ... } }

## 获取本应用中其他Module的Context（模块级别的上下文）
调用createModuleContext方法，获取本应用中其他Module的Context。获取到其他Module的Context之后，即可获取到相应Module的资源信息。
import { common, application } from '@kit.AbilityKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG = '[CreateModuleContext]'; const DOMAIN = 0xF811; let storageEventCall = new LocalStorage(); @Entry(storageEventCall) @Component struct CreateModuleContext { private context = this.getUIContext().getHostContext() as common.UIAbilityContext; build() { Column() { // ... List({ initialIndex: 0 }) { ListItem() { Row() { // ... } .onClick(() => { let moduleName2: string = 'entry'; application.createModuleContext(this.context, moduleName2) .then((data: common.Context) => { hilog.info(DOMAIN, TAG, `CreateModuleContext success, data: ${JSON.stringify(data)}`); if (data !== null) { this.getUIContext().getPromptAction().showToast({ // 请将$r('app.string.success_message')替换为实际资源文件，在本示例中该资源文件的value值为"成功获取Context" message: $r('app.string.success_message') }); } }) .catch((err: BusinessError) => { hilog.error(DOMAIN, TAG, `CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}`); }); }) } // ... } // ... } // ... } }

## 获取UIAbilityContext（UIAbility组件的上下文）
UIAbilityContext和基类Context相比，额外提供abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，也可以获取操作UIAbility实例的方法（如startAbility()、connectServiceExtensionAbility()、terminateSelf()等）。
在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit'; export default class EntryAbility extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { // 获取UIAbility实例的上下文 let context = this.context; } }
在页面中获取UIAbility实例的上下文信息。
import { common, Want } from '@kit.AbilityKit'; // 导入依赖资源context模块 @Entry @Component struct EventHub { // 定义context变量 private context = this.getUIContext().getHostContext() as common.UIAbilityContext; startAbilityTest(): void { let want: Want = { // Want参数信息 }; this.context.startAbility(want); } // 页面展示 build() { // ··· } }
也可以在导入依赖资源context模块后，在具体使用UIAbilityContext前进行变量定义。
import { common, Want } from '@kit.AbilityKit'; @Entry @Component struct UIAbilityComponentsBasicUsage { startAbilityTest(): void { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; let want: Want = { // Want参数信息 }; context.startAbility(want); } // 页面展示 build() { // ··· } }
当业务完成后，开发者如果想要终止当前UIAbility实例，可以通过调用terminateSelf()方法实现。
import { common } from '@kit.AbilityKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; const TAG = '[UIAbilityComponentsUsage]'; const DOMAIN = 0xF811; @Entry @Component struct UIAbilityComponentsUsage { // 页面展示 build() { Column() { // ··· Button('FuncAbilityB') .onClick(() => { let context = this.getUIContext().getHostContext() as common.UIAbilityContext; try { context.terminateSelf((err: BusinessError) => { if (err.code) { // 处理业务逻辑错误 hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${err.code}, message is ${err.message}.`); return; } // 执行正常业务 hilog.info(DOMAIN, TAG, `terminateSelf succeed.`); }); } catch (err) { // 捕获同步的参数错误 let code = (err as BusinessError).code; let message = (err as BusinessError).message; hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${code}, message is ${message}.`); } }) } } }

## 获取ExtensionAbilityContext (ExtensionAbility组件的上下文)
获取特定场景ExtensionContext。以FormExtensionContext为例，表示卡片服务的上下文环境，继承自ExtensionContext，提供卡片服务相关的接口能力。
import { FormExtensionAbility, formBindingData } from '@kit.FormKit'; import { Want } from '@kit.AbilityKit'; export default class MyFormExtensionAbility extends FormExtensionAbility { onAddForm(want: Want) { let formExtensionContext = this.context; let dataObj1: Record<string, string> = { 'temperature': '11c', 'time': '11:00' }; let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1); return obj1; } }

## Context的典型使用场景
本章节通过以下具体场景来介绍Context的用法：
获取基本信息
获取应用文件路径
获取和修改加密分区
监听应用前后台变化
监听UIAbility生命周期变化

## 获取基本信息
继承自Context的不同类型Context，默认会继承父类的方法和属性，还会拥有自己独立的方法与属性。
通过Context属性可以获取当前应用、模块、UIAbility或ExtensionAbility的基本信息（例如资源管理对象、应用程序信息等），下面以UIAbility的信息获取为例：
如果需要跨包获取资源对象，可以参考资源访问。
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit'; export default class EntryAbility extends UIAbility { onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { // 获取ResourceManager（资源管理） let resourceManager = this.context.getApplicationContext().resourceManager; // 获取applicationInfo（当前应用信息） let applicationInfo = this.context.getApplicationContext().applicationInfo; } }

## 获取应用文件路径
基类Context提供了获取应用文件路径的能力，ApplicationContext、AbilityStageContext、UIAbilityContext和ExtensionContext均继承该能力。不同类型的Context获取的路径可能存在差异。
通过ApplicationContext可以获取应用级的文件路径。该路径用于存放应用全局信息，路径下的文件会跟随应用的卸载而删除。
通过AbilityStageContext、UIAbilityContext、ExtensionContext，可以获取Module级的文件路径。该路径用于存放Module相关信息，路径下的文件会跟随HAP/HSP的卸载而删除。HAP/HSP的卸载不会影响应用级路径下的文件，除非该应用的HAP/HSP已全部卸载。
UIAbilityContext：可以获取UIAbility所在Module的文件路径。
ExtensionContext：可以获取ExtensionAbility所在Module的文件路径。
AbilityStageContext：由于AbilityStageContext创建时机早于UIAbilityContext和ExtensionContext，通常用于在AbilityStage中获取文件路径。
应用文件路径属于应用沙箱路径，具体请参见应用沙箱目录。
表1 不同级别Context获取的应用文件路径说明
属性
说明
ApplicationContext获取的路径
AbilityStageContext、UIAbilityContext、ExtensionContext获取的路径
