# RowSplit

将子组件横向布局，并在每个子组件之间插入纵向分割线。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

可以包含子组件。

RowSplit通过分割线限制子组件的宽度。初始化时，分割线位置根据子组件的宽度来计算。初始化后，动态修改子组件的宽度不生效，分割线位置保持不变，可以通过拖动相邻分割线改变子组件宽度。

初始化后，动态修改[margin](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__margin)、[border](边框设置.md#ZH-CN_TOPIC_0000002522080782__border)、[padding](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__padding)通用属性导致子组件宽度大于相邻分割线间距的异常情况下，不支持拖动分割线改变子组件的宽度。

**接口**

RowSplit()

带分割线的子组件横向分隔布局。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

RowSplit组件[形状裁剪](形状裁剪.md)的默认值为true。

**resizeable**

resizeable(value: boolean)

设置分割线是否可拖拽。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 分割线是否可拖拽。设置为true时表示分割线可拖拽，设置为false时表示分割线不可拖拽。 默认值：false  非法值：按默认值处理。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

RowSplit的分割线可以改变左右两边子组件的宽度，子组件可改变宽度的范围取决于子组件的最大最小宽度。

**事件**

支持[通用事件](通用事件.md)。

**示例**

RowSplit的基本用法。设置可拖动的、横向布局的子组件。

```ets
// xxx.ets
@Entry
@Component
struct RowSplitExample {
  build() {
    Column() {
      Text('The second line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      RowSplit() {
        Text('1').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .resizeable(true) // 可拖拽
      .width('90%').height(100)
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553204827.webp)