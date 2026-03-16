# ArcButton

弧形按钮组件用于圆形屏幕的穿戴设备。提供强调、普通、警告等样式按钮。

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import {
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
}  from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

不支持[通用属性](../misc/通用属性.md)

#### 事件

通用事件支持[点击事件](../misc/点击事件.md)和[触摸事件](../misc/触摸事件.md)。

#### ArcButton

ArcButton({ options: ArcButtonOptions })

创建ArcButton实例，入参是弧形按钮配置选项。

**装饰器类型：** @Component

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数**：

名称类型必填装饰器类型说明options[ArcButtonOptions](#ZH-CN_TOPIC_0000002497444912__arcbuttonoptions)是@Require定义ArcButton组件的文本、背景色、阴影等参数。

#### ArcButtonOptions

定义ArcButton的默认样式或自定义样式参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

#### 属性

名称类型只读可选说明position[ArcButtonPosition](#ZH-CN_TOPIC_0000002497444912__arcbuttonposition)否否

上下弧形按钮类型属性。

默认值：ArcButtonPosition.BOTTOM_EDGE

styleMode[ArcButtonStyleMode](#ZH-CN_TOPIC_0000002497444912__arcbuttonstylemode)否否

弧形按钮样式模式。

默认值：ArcButtonStyleMode.EMPHASIZED_LIGHT

status[ArcButtonStatus](#ZH-CN_TOPIC_0000002497444912__arcbuttonstatus)否否

弧形按钮状态。

默认值：ArcButtonStatus.NORMAL

label[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否弧形按钮显示文本。backgroundBlurStyle[BlurStyle](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否否

弧形按钮背景模糊能力。

默认值：BlurStyle.NONE

backgroundColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否否

弧形按钮背景颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.Black

shadowColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否否

弧形按钮阴影颜色。

默认值：Color.Black

shadowEnabledboolean否否

弧形按钮阴影开关。

默认值：false

值为true时，显示阴影。值为false时，不显示阴影。

fontSize[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否否

弧形按钮文本大小。

默认值：19fp

fontColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否否

弧形按钮文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

pressedFontColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否否

弧形按钮按下文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

fontStyle[FontStyle](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle)否否

弧形按钮文本样式。

默认值：FontStyle.Normal

fontFamilystring | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否否弧形按钮字体名。fontMargin[LocalizedMargin](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedmargin12)否否

弧形按钮文本边距。

默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }

onTouch[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)< [TouchEvent](../misc/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)>否是弧形按钮手指触摸动作触发该回调。onClick[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)<[ClickEvent](../misc/点击事件.md#ZH-CN_TOPIC_0000002529284807__clickevent) >否是弧形按钮点击动作触发该回调。

#### constructor

constructor(options: CommonArcButtonOptions)

弧形按钮的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明options[CommonArcButtonOptions](#ZH-CN_TOPIC_0000002497444912__commonarcbuttonoptions)是定义ArcButton组件的文本、背景色、阴影等参数。

#### CommonArcButtonOptions

ArcButton的默认样式或自定义样式参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明position[ArcButtonPosition](#ZH-CN_TOPIC_0000002497444912__arcbuttonposition)否是

上下弧形按钮类型属性。

默认值：ArcButtonPosition.BOTTOM_EDGE

styleMode[ArcButtonStyleMode](#ZH-CN_TOPIC_0000002497444912__arcbuttonstylemode)否是

弧形按钮样式模式。

默认值：ArcButtonStyleMode.EMPHASIZED_LIGHT

status[ArcButtonStatus](#ZH-CN_TOPIC_0000002497444912__arcbuttonstatus)否是

弧形按钮状态。

默认值：ArcButtonStatus.NORMAL

label[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是弧形按钮显示文本。backgroundBlurStyle[BlurStyle](../misc/背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)否是

弧形按钮背景模糊能力。

默认值：BlurStyle.NONE

backgroundColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

弧形按钮背景颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.Black

shadowColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

弧形按钮阴影颜色。

默认值：Color.Black

shadowEnabledboolean否是

弧形按钮阴影开关。

默认值：false

值为true时，显示阴影。值为false时，不显示阴影。

fontSize[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否是

弧形按钮文本大小。

默认值：19fp

fontColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

弧形按钮文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

pressedFontColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

弧形按钮按下文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

fontStyle[FontStyle](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle)否是

弧形按钮文本样式。

默认值：FontStyle.Normal

fontFamilystring | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)否是弧形按钮字体名。fontMargin[LocalizedMargin](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedmargin12)否是

弧形按钮文本边距。

默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }

onTouch[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)< [TouchEvent](../misc/触摸事件.md#ZH-CN_TOPIC_0000002529444777__touchevent对象说明)>否是弧形按钮手指触摸动作触发该回调。onClick[Callback](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__voidcallback12)<[ClickEvent](../misc/点击事件.md#ZH-CN_TOPIC_0000002529284807__clickevent) >否是弧形按钮点击动作触发该回调。

#### ArcButtonPosition

定义ArcButton可设置的弧形按钮的类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称值说明TOP_EDGE0上弧形按钮，位于圆形屏幕上方。BOTTOM_EDGE1底部弧形按钮，位于圆形屏幕底部。

#### ArcButtonStyleMode

定义ArcButton可设置弧形按钮样式模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称值说明EMPHASIZED_LIGHT0强调样式，亮色，表现为蓝色背景、白色文字。EMPHASIZED_DARK1警告样式，暗色，表现为红色背景、白色文字。NORMAL_LIGHT2常规样式，亮色，表现为深蓝色背景、蓝色文字。NORMAL_DARK3常规样式，暗色，表现为深灰色背景、蓝色文字。CUSTOM4自定义按钮颜色和字体颜色。

#### ArcButtonStatus

定义ArcButton可设置的弧形按钮状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称值说明NORMAL0正常状态。PRESSED1按压状态。DISABLED2禁用状态。

#### 示例

从API version18开始，该示例展示了ArcButton的基本用法。

topOptions定义了上弧形按钮，按钮文本为ButtonTop，字体大小为15fp，按钮状态为正常状态，按钮样式为亮色强调，启用阴影。

bottomOptions定义了底部弧形按钮，按钮文本为ButtonBottom，字体大小为15fp，按钮样式为亮色强调，启用阴影，设置了按钮的点击事件。

运行该示例需要Wearable设备的支持。在src/main目录下的工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中[deviceTypes标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)内配置wearable。

```ets
// module.json5
{
  "module": {
    // ...
    "deviceTypes": [
      "wearable",
      "phone"
    ]
    // ...
  }
}
```

```ets
// xxx.ets
import {
  LengthMetrics,
  LengthUnit,
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
}  from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

  aboutToAppear() {
    this.topOptions = new ArcButtonOptions({
      label: 'ButtonTop',
      status: ArcButtonStatus.NORMAL,
      position: ArcButtonPosition.TOP_EDGE,
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true
    })

    this.bottomOptions = new ArcButtonOptions({
      label: 'ButtonBottom',
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        console.info('click from ArcButton.');
      }
    })
  }

  build() {
    Stack() {
      Stack() {
        Circle({ width: 233, height: 233 })
          .strokeWidth(0.1)
          .fill(Color.White)

        Column() {
          ArcButton({ options: this.topOptions })
          Blank()
          ArcButton({ options: this.bottomOptions })

        }.width('100%')
        .height('100%')
      }.width(233)
      .height(233)
    }.width('100%')
    .height('100%')
    .alignContent(Alignment.Center)
    .backgroundColor(Color.Gray)
  }
}
```