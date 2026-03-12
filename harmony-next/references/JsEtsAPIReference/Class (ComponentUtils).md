# Class (ComponentUtils)

提供获取组件绘制区域坐标和大小的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 10开始支持。

-

以下API需先使用UIContext中的[getComponentUtils()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getcomponentutils)方法获取到ComponentUtils对象，再通过该对象调用对应方法。

#### getRectangleById

getRectangleById(id: string): componentUtils.ComponentInfo

获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。

该接口需要在目标组件布局、完成以后获取目标组件区域大小信息，建议在[onAppear](挂载卸载事件.md#ZH-CN_TOPIC_0000002529284813__onappear)中使用该接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明idstring是组件唯一标识id。

**返回值：**

类型说明[componentUtils.ComponentInfo](@ohos.arkui.componentUtils (componentUtils).md#ZH-CN_TOPIC_0000002529284761__componentinfo)组件大小、位置、平移缩放旋转及仿射矩阵属性信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息100001UI execution context not found.

**示例：**

```ets
import { ComponentUtils } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
          let modePosition = componentUtils.getRectangleById("HelloWorld");
          let width = modePosition.size.width; //获取组件的宽度
          let height = modePosition.size.height; //获取组件的高度
          let localOffsetX = modePosition.localOffset.x; // 获取组件相对于父组件的x轴偏移
          let localOffsetY = modePosition.localOffset.y; // 获取组件相对于父组件的y轴偏移
          console.info(`width: ${width}, height: ${height}, localOffsetX: ${localOffsetX}, localOffsetY: ${localOffsetY}`);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```