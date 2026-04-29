# Stack

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

可以包含子组件。

**接口**

Stack(options?: StackOptions)

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠容器的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization#section78181114123811)。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | StackOptions | 否 | 设置子组件在容器内的对齐方式。 |

**StackOptions18+对象说明**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

卡片能力： 从API version 18开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alignContent7+ | Alignment | 否 | 是 | 设置子组件在容器内的对齐方式。 默认值：Alignment.Center  非法值：按默认值处理。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**alignContent**

alignContent(value: Alignment)

设置子组件在容器内的对齐方式。该属性与[align](位置设置.md#ZH-CN_TOPIC_0000002522240778__align)同时设置时，后设置的属性生效。该属性与接口的构造入参同时设置时，生效属性上的设置效果。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Alignment | 是 | 所有子组件在容器内的对齐方式。 默认值：Alignment.Center  非法值：按默认值处理。 |

**事件**

支持[通用事件](通用事件.md)。

**示例**

Stack的alignContent设置为Alignment.Bottom条件下子组件显示效果。

```ets
// xxx.ets
@Entry
@Component
struct StackExample {
  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)
      Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)
    }.width('100%').height(150).margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204819.webp)