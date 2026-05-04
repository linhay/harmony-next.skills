# if/else：条件渲染

本文根据华为开发者官网 `arkts-rendering-control-ifelse` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse>
更新时间：2026-04-30 06:28:58

ArkTS提供了渲染控制能力。条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。
从API version 9开始，该接口支持在ArkTS卡片中使用。
## 使用规则
- 支持if、else和else if语句。
- if和else if后的条件语句可以使用状态变量或常规变量（状态变量的值改变时会实时渲染UI，而常规变量的值改变则不会）。
- 允许在容器组件内使用，通过条件渲染语句构建不同的子组件。
- 条件渲染语句在涉及到组件的父子关系时是“透明”的，父组件和子组件之间的条件渲染语句不影响父组件关于子组件使用的限制。例如，某些容器组件限制子组件的类型或数量。将条件渲染语句用于这些组件内时，这些限制同样适用于条件渲染语句内创建的组件。具体而言，Grid容器组件的子组件仅支持GridItem组件。在Grid内使用条件渲染语句时，条件渲染语句内仅允许使用GridItem组件。
- 每个分支内部的构建函数必须遵循构建函数的规则，并创建一个或多个组件。无法创建组件的空构建函数会产生语法错误。关于构建函数的规则，请参考：基本语法概述、声明式UI描述。
## 更新机制
当if、else if后跟随的状态判断中使用的状态变量值变化时，条件渲染语句会进行更新，更新步骤如下：
- 评估if和else if的状态判断条件，如果分支没有变化，无需执行以下步骤。如果分支有变化，则执行2、3步骤。
- 移除此前构建的所有子组件。
- 执行新分支的构造函数，将生成的子组件添加到if父容器中。如果缺少适用的else分支，则不创建任何内容。
条件可以包含Typescript表达式。构造函数中的表达式不得更改应用程序状态。
## 使用场景
## 使用if进行条件渲染
```
@Entry
@Component
struct IfExample {
@State count: number = 0;
build() {
Column() {
Text(`count=${this.count}`)
if (this.count > 0) {
Text(`count is positive`)
.fontColor(Color.Green)
}
Button('increase count')
.onClick(() => {
this.count++;
})
Button('decrease count')
.onClick(() => {
this.count--;
})
}
}
}
```
if语句的每个分支都包含一个构建函数。此类构建函数必须创建一个或多个子组件。在初始渲染时，if语句会执行构建函数，并将生成的子组件添加到其父组件中。
每当if或else if条件语句中使用的状态变量发生变化时，条件语句都会更新并重新评估新的条件值。如果条件值评估发生了变化，这意味着需要构建另一个条件分支。此时ArkUI框架将：
- 移除所有以前渲染的（早期分支的）组件。
- 执行新分支的构造函数，将生成的子组件添加到其父组件中。
在以上示例中，当count从0增至1时，if (this.count > 0)更新为true，执行该分支的构造函数，创建一个Text组件并添加到父组件Column中。如果后续count更改为0，则Text组件将从Column组件中删除。由于没有else分支，因此不会执行新的构造函数。
## if ... else ...语句和子组件状态
以下示例包含if ... else ...语句与拥有@State装饰变量的子组件。
```
@Component
struct CounterView {
@State counter: number = 0;
label: string = 'unknown';
build() {
Column({ space: 20 }) {
Text(`${this.label}`)
Button(`counter ${this.counter} +1`)
.onClick(() => {
this.counter += 1;
})
}
.margin(10)
.padding(10)
.border({ width: 1 })
}
}
@Entry
@Component
struct MainView {
@State toggle: boolean = true;
build() {
Column() {
if (this.toggle) {
CounterView({ label: 'CounterView #positive' });
} else {
CounterView({ label: 'CounterView #negative' });
}
Button(`toggle ${this.toggle}`)
.onClick(() => {
this.toggle = !this.toggle;
})
}
.width('100%')
.justifyContent(FlexAlign.Center)
}
}
```
初次渲染：创建CounterView子组件（label为 'CounterView #positive'），其状态变量counter初始值为0。
修改CounterView的counter状态变量：CounterView子组件（label为 'CounterView #positive'）重新渲染并保留状态变量值。
修改MainView.toggle状态变量为false：MainView父组件内的if语句将更新，并进行以下处理：
- 删除旧的CounterView子组件（label为 'CounterView #positive'）。
- 创建新的CounterView子组件（label为 'CounterView #negative'），其状态变量counter初始值为0。
CounterView（label为 'CounterView #positive'）和CounterView（label为 'CounterView #negative'）是同一自定义组件的两个不同实例。if分支的更改，不会更新现有子组件，也不会保留状态。
以下示例展示了条件更改时，若需要保留counter值所做的修改。
```
@Component
struct KeepCounterView {
@Link counter: number;
label: string = 'unknown';
build() {
Column({ space: 20 }) {
Text(`${this.label}`)
.fontSize(20)
Button(`counter ${this.counter} +1`)
.onClick(() => {
this.counter += 1;
})
}
.margin(10)
.padding(10)
.border({ width: 1 })
}
}
@Entry
@Component
struct KeepMainView {
@State toggle: boolean = true;
@State counter: number = 0;
build() {
Column() {
if (this.toggle) {
KeepCounterView({ counter: $counter, label: 'CounterView #positive' });
} else {
KeepCounterView({ counter: $counter, label: 'CounterView #negative' });
}
Button(`toggle ${this.toggle}`)
.onClick(() => {
this.toggle = !this.toggle;
})
}
.width('100%')
.justifyContent(FlexAlign.Center)
}
}
```
此处，@State counter变量归父组件所有。因此，当KeepCounterView组件实例被删除时，该变量不会被销毁。KeepCounterView组件通过@Link装饰器引用状态。状态必须从子级移动到其父级（或父级的父级），以避免在条件内容或重复内容被销毁时丢失状态。
## 嵌套if语句
嵌套条件语句不会影响父组件的相关规则。
```
@Entry
@Component
struct NestedIf {
@State toggle: boolean = false;
@State toggleColor: boolean = false;
build() {
Column({ space: 20 }) {
Text('Before')
.fontSize(15)
if (this.toggle) {
Text('Top True, positive 1 top')
.backgroundColor('#aaffaa').fontSize(20)
// 内部if语句
if (this.toggleColor) {
Text('Top True, Nested True, positive COLOR Nested ')
.backgroundColor('#00aaaa').fontSize(15)
} else {
Text('Top True, Nested False, Negative COLOR Nested ')
.backgroundColor('#aaaaff').fontSize(15)
}
} else {
Text('Top false, negative top level').fontSize(20)
.backgroundColor('#ffaaaa')
if (this.toggleColor) {
Text('positive COLOR Nested ')
.backgroundColor('#00aaaa').fontSize(15)
} else {
Text('Negative COLOR Nested ')
.backgroundColor('#aaaaff').fontSize(15)
}
}
Text('After')
.fontSize(15)
Button('Toggle Outer')
.onClick(() => {
this.toggle = !this.toggle;
})
Button('Toggle Inner')
.onClick(() => {
this.toggleColor = !this.toggleColor;
})
}
.width('100%')
.justifyContent(FlexAlign.Center)
}
}
```
