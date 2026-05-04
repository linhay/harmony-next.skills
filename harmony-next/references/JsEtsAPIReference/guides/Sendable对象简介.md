# Sendable对象简介

本文根据华为开发者官网 `arkts-sendable` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable>
更新时间：2026-04-30 06:30:35


## 基础概念

## Sendable协议
Sendable协议定义了ArkTS的可共享对象体系及其规格约束。符合Sendable协议的数据（以下简称Sendable数据）可以在ArkTS并发实例间传递。
默认情况下，Sendable数据在ArkTS并发实例间（包括UI主线程、TaskPool线程、Worker线程）采用引用传递方式，同时还支持拷贝传递方式。

## ISendable
在ArkTS语言基础库@arkts.lang中引入了interface ISendable，没有任何方法或属性。ISendable是所有Sendable类型（除了null和undefined）的父类型。ISendable主要用于开发者自定义Sendable数据结构的场景中。类装饰器@Sendable装饰器是implement ISendable的语法糖。

## Sendable支持的数据类型
- ArkTS基本数据类型：boolean、number、string、bigint、null、undefined。
- ArkTS数据类型：const enum（常量枚举）。
- ArkTS语言标准库中定义的容器类型数据（须显式引入@arkts.collections）。
- ArkTS语言标准库中定义的异步锁对象（须显式引入@arkts.utils）。
- ArkTS语言标准库中定义的异步等待对象（须显式引入@arkts.utils）。
- ArkTS语言标准库中定义的SendableLruCache对象（须显式引入@arkts.utils）。
- 继承了ISendable的interface。
- 标注了@Sendable装饰器的class。
- 标注了@Sendable装饰器的function。
- 接入Sendable的系统对象： 共享用户首选项
- 可共享的色彩管理
- 基于Sendable对象的图片处理
- 资源管理
- SendableContext对象管理
- 元素均为Sendable类型的union type数据。
- 开发者自定义的Native Sendable对象。ArkTS支持开发者自定义Native Sendable对象，详情参见自定义Native Sendable对象的多线程操作场景。
- JS内置对象在并发实例间传递时遵循结构化克隆算法，跨线程行为是拷贝传递。因此，JS内置对象的实例不是Sendable类型。
- 对象字面量和数组字面量在并发实例间传递时遵循结构化克隆算法，跨线程行为是拷贝传递。因此，对象字面量和数组字面量不是Sendable类型。
Sendable支持const enum类型使用示例：
```
// Test.ets
export const enum ModelState {
ACTIVE,
INACTIVE
}
```
```
// Index.ets
import { taskpool } from "@kit.ArkTS";
import { ModelState } from "./Test";
@Sendable
class Model {
state: ModelState = ModelState.ACTIVE;
getState() {
console.info("model state is " + this.state);
}
setState(state: ModelState) {
this.state = state;
}
}
@Concurrent
function setModelState(model: Model) {
model.setState(ModelState.INACTIVE);
model.getState();
}
@Entry
@Component
struct Index {
@State message: string = 'Hello World';
@State num: number = 0;
build() {
RelativeContainer() {
Text(this.message)
.id('HelloWorld')
.fontSize(50)
.fontWeight(FontWeight.Bold)
.alignRules({
center: { anchor: '__container__', align: VerticalAlign.Center },
middle: { anchor: '__container__', align: HorizontalAlign.Center }
})
.onClick(async () => {
let model = new Model();
model.getState();
let task = new taskpool.Task(setModelState, model);
await taskpool.execute(task);
})
}
.height('100%')
.width('100%')
}
}
```

## @Sendable装饰器
声明并校验Sendable class和Sendable function。
| @Sendable装饰器 | 说明 |
| 装饰器参数 | 无。 |
| 使用场景限制 | 仅支持在Stage模型的.ets文件中使用。 |
| 装饰的函数类型限制 | 仅支持装饰普通function和Async function类型。 |
| 装饰的类继承关系限制 | Sendable class只能继承Sendable class，普通Class不可继承Sendable class。 |
| 装饰的对象内的属性类型限制 | 1. 支持string、number、boolean、bigint、null、undefined、const enum、Sendable class、collections容器集、ArkTSUtils.locks.AsyncLock、ArkTSUtils.SendableLruCache、ArkTSUtils.locks.ConditionVariable以及自定义的Sendable函数类型。 2. 禁止使用闭包变量，定义在顶层的Sendable class和Sendable function除外。 3. 不支持通过#定义私有属性，需用private。 4. 不支持计算属性。 5. 不支持类型别名。 |
| 装饰的对象内的属性的其他限制 | 1. 成员属性必须显式初始化，不能使用感叹号。 2. 不支持增加或删除属性，允许修改属性，修改前后属性的类型必须一致，不支持修改方法。 |
| 装饰的函数或类对象内的方法参数限制 | 允许使用local变量、入参和通过import引入的变量。禁止使用闭包变量，但定义在顶层的Sendable class和Sendable function除外。从API version 18开始，支持访问本文件导出的变量。 |
| 适用场景 | 1. 在TaskPool或Worker中使用类方法或Sendable函数。 2. 传输对象数据量较大的场景。序列化耗时会随着数据量增大而增大，使用Sendable对数据进行改造后，传输100KB数据效率提升约20倍，传输1M数据效率提升约100倍。 |
装饰器修饰Class使用示例：
```
@Sendable
class SendableTestClass {
desc: string = "sendable: this is SendableTestClass ";
num: number = 5;
printName() {
console.info("sendable: SendableTestClass desc is: " + this.desc);
}
getNum(): number {
return this.num;
}
}
```
装饰器修饰Function使用示例：
```
@Sendable
type SendableFuncType = () => void;
@Sendable
class TopLevelSendableClass {
num: number = 1;
PrintNum() {
console.info("Top level sendable class");
}
}
@Sendable
function TopLevelSendableFunction() {
console.info("Top level sendable function");
}
@Sendable
function SendableTestFunction() {
const topClass = new TopLevelSendableClass(); // 顶层sendable class
topClass.PrintNum();
TopLevelSendableFunction(); // 顶层sendable function
console.info("Sendable test function");
}
@Sendable
class SendableTestClass {
constructor(func: SendableFuncType) {
this.callback = func;
}
callback: SendableFuncType; // 顶层sendable function
CallSendableFunc() {
SendableTestFunction(); // 顶层sendable function
}
}
let sendableClass = new SendableTestClass(SendableTestFunction);
sendableClass.callback();
sendableClass.CallSendableFunc();
```
