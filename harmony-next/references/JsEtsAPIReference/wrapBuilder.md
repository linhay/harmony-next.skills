# wrapBuilder

使用wrapBuilder封装全局@Builder，可以帮助维护代码。开发指南见[wrapBuilder：封装全局@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder)。

本模块首批接口从API version 11开始支持。

后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### wrapBuilder

wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。模板参数Args extends Object[]是需要包装的builder函数的参数列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明builder(...args: Args) => void是@Builder装饰的全局函数。

**返回值：**

类型说明[WrappedBuilder<Args>](#ZH-CN_TOPIC_0000002529284943__wrappedbuilder)WrappedBuilder对象。

**示例：**

```ets
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(MyBuilder);
```

#### WrappedBuilder

@Builder函数的包装类。模板参数Args extends Object[]应传入@Builder函数的参数类型列表。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明builder(...args: Args) => void否否@Builder修饰的全局函数。

#### constructor

constructor(builder: (...args: Args) => void)

WrappedBuilder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明builder(...args: Args) => void是@Builder装饰的全局函数。

**示例：**

```ets
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(MyBuilder);
```