# @Builder装饰器：自定义构建函数

本文根据华为开发者官网 `arkts-builder` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder>
更新时间：2026-04-30 06:29:55


## 装饰器使用说明
@Builder装饰器有两种使用方式，分别是定义在自定义组件内部的私有自定义构建函数和定义在全局的全局自定义构建函数。

## 私有自定义构建函数
示例：
```
@Entry
@Component
struct BuilderDemo {
@Builder
showTextBuilder() {
// @Builder装饰此函数，使其能以链式调用的方式配置并构建Text组件
Text('Hello World')
.fontSize(30)
.fontWeight(FontWeight.Bold)
}
@Builder
showTextValueBuilder(param: string) {
Text(param)
.fontSize(30)
.fontWeight(FontWeight.Bold)
}
build() {
Column() {
// 无参数
this.showTextBuilder()
// 有参数
this.showTextValueBuilder('Hello @Builder')
}
}
}
```
使用方法：
- 允许在自定义组件内定义一个或多个@Builder函数，该函数被认为是该组件的私有、特殊类型的成员函数。
- 私有自定义构建函数允许在自定义组件内、build函数和其他自定义构建函数中调用。
- 在自定义组件中，this指代当前所属组件，组件的状态变量可在自定义构建函数内访问。建议通过this访问组件的状态变量，而不是通过参数传递。

## 全局自定义构建函数
示例：
```
// 全局自定义构建函数showTextBuilder
@Builder
function showTextBuilder() {
Text('Hello World')
.fontSize(30)
.fontWeight(FontWeight.Bold)
}
@Entry
@Component
struct BuilderSample {
build() {
Column() {
showTextBuilder()
}
}
}
```
- 如果不涉及组件状态变量变化，建议使用全局的自定义构建函数。
- 全局自定义构建函数允许在build函数和其他自定义构建函数中调用。

## 参数传递规则
自定义构建函数的参数传递有按回调传递，按引用传递和按值传递，均需遵守以下规则：
- @Builder装饰的函数参数类型不允许为undefined、null和返回undefined、null的表达式。
- 在@Builder装饰的函数内部，不允许改变参数值。
- @Builder内UI语法遵循UI语法规则。
- 按回调传递和按引用传递时，支持@Builder函数内UI组件刷新。按引用传递只在传入一个参数且该参数直接传入对象字面量时生效，有多个参数时不支持@Builder函数内UI组件刷新。
- 使用引用传递时，在@Builder函数中不能修改参数的属性，但使用UIUtils.makeBinding并传入写回调时，我们可以在@Builder函数内修改属性，并同步到调用@Builder的组件中。

## 限制条件
- @Builder装饰的函数内部在没有使用MutableBinding时不允许修改参数值，修改不会触发UI刷新。若按引用传递参数且仅传入一个参数时，修改参数内部的属性会抛出运行时错误。使用MutableBinding可以帮助开发者在@Builder装饰的函数内部修改参数值，请参考在@Builder装饰的函数内部修改入参内容。
- @Builder按引用传递传入一个参数时，可以触发动态渲染UI，请参考按引用传递参数。
- 如果@Builder传入的参数是两个或两个以上，且未使用按回调传递参数，不会触发动态渲染UI，请参考@Builder存在两个或两个以上参数。
- @Builder传入的参数中同时包含按值传递和按引用传递，不会触发动态渲染UI，请参考@Builder存在两个或两个以上参数。
- 不允许在@Builder函数里修改参数的属性，否则会抛出运行时错误，从API version 23开始，将返回错误码140109，示例请参考在@Builder装饰的函数内部修改入参内容。

## 全局自定义构建函数
创建全局的@Builder函数，并在Column中通过overBuilder()方式调用。传递参数时，可以使用对象字面量形式，无论是简单类型还是复杂类型，值的任何变化都会触发UI界面的刷新。
```
class ChildTmp {
public val: number = 1;
}
class ParamTmp {
public strValue: string = 'Hello';
public numValue: number = 0;
public tmpValue: ChildTmp = new ChildTmp();
public arrayTmpValue: Array = [];
}
@Builder
function overBuilder(param: ParamTmp) {
Column() {
Text(`strValue: ${param.strValue}`)
.width(230)
.height(40)
.margin(12)
.backgroundColor('#0d000000')
.fontColor('#e6000000')
.borderRadius(20)
.textAlign(TextAlign.Center)
Text(`numValue: ${param.numValue}`)
.width(230)
.height(40)
.margin(12)
.backgroundColor('#0d000000')
.fontColor('#e6000000')
.borderRadius(20)
.textAlign(TextAlign.Center)
Text(`tmpValue: ${param.tmpValue.val}`)
.width(230)
.height(40)
.margin(12)
.backgroundColor('#0d000000')
.fontColor('#e6000000')
.borderRadius(20)
.textAlign(TextAlign.Center)
ForEach(param.arrayTmpValue, (item: ChildTmp) => {
ListItem() {
Text(`arrayTmpValue: ${item.val}`)
.width(230)
.height(40)
.margin(12)
.backgroundColor('#0d000000')
.fontColor('#e6000000')
.borderRadius(20)
.textAlign(TextAlign.Center)
}
}, (item: ChildTmp) => JSON.stringify(item))
}
}
@Entry
@Component
struct ParentDemo {
@State objParam: ParamTmp = new ParamTmp();
build() {
Column() {
Text('UI Rendered via @Builder')
.fontSize(20)
.margin(12)
// 调用全局@Builder函数overBuilder
overBuilder({
strValue: this.objParam.strValue,
numValue: this.objParam.numValue,
tmpValue: this.objParam.tmpValue,
arrayTmpValue: this.objParam.arrayTmpValue
})
// 点击Button更新objParam，触发overBuilder内组件的刷新
Button('Update Values').onClick(() => {
this.objParam.strValue = 'Hello World';
this.objParam.numValue = 1;
this.objParam.tmpValue.val = 8;
const childValue: ChildTmp = {
val: 2
}
this.objParam.arrayTmpValue.push(childValue);
})
}
.height('100%')
.width('100%')
}
}
```
示例效果图
