# ProgressButtonV2

文本下载按钮，可显示具体的下载进度。

该组件基于[状态管理V2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v2)实现，相较于[状态管理V1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，状态管理V2增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理V2，开发者可以通过该组件更灵活地控制文本下载按钮的数据和状态，实现更高效的用户界面刷新。

- 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { ColorMetrics, LengthMetrics, ProgressButtonV2,  ProgressButtonV2Color } from '@kit.ArkUI';
```

#### ProgressButtonV2

ProgressButtonV2({progress: number, content: ResourceStr, progressButtonWidth?: LengthMetrics, onClicked: ClickCallback,

isEnabled: boolean, colorOptions?: ProgressButtonColorOptions, progressButtonRadius?: LengthMetrics})

文本下载按钮，可显示具体下载进度。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型必填装饰器类型说明progressnumber是

@Require

@Param

下载按钮的当前进度值。

取值范围：[0,100]。设置小于0的数值时置为0，设置大于100的数值置为100。

默认值：0

content[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)是

@Require

@Param

下载按钮的文本。progressButtonWidth[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否

@Param

@Once

下载按钮的宽度。

默认值：44vp

onClicked[ClickCallback](#ZH-CN_TOPIC_0000002529444927__clickcallback)是@Param下载按钮的点击回调。isEnabledboolean是@Param

下载按钮是否可以点击。

isEnabled为true时，表示可以点击。

isEnabled为false时，表示不可点击。

colorOptions[ProgressButtonV2Color](#ZH-CN_TOPIC_0000002529444927__progressbuttonv2color)否@Param下载按钮颜色选项。progressButtonRadius18+[LengthMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)否@Param

下载按钮的圆角（不支持百分比设置）。

取值范围：[0, height/2]

默认值：height/2

设置非法数值时，按照默认值处理。

#### 属性

不支持[通用属性](../misc/通用属性.md)。

#### ClickCallback

type ClickCallback = () => void

下载按钮的点击回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

#### ProgressButtonV2Color

下载按钮颜色选项。

**装饰器类型：**@ObservedV2

#### 属性

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明progressColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

进度条颜色。

默认值：#330A59F7

装饰器类型：@Trace

borderColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮描边颜色。

默认值：#330A59F7

装饰器类型：@Trace

textColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮文本颜色。

默认值：系统默认值，#CE000000

装饰器类型：@Trace

backgroundColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮背景颜色。

默认值：$r('sys.color.ohos_id_color_foreground_contrary')

装饰器类型：@Trace

#### constructor

constructor(options: ProgressButtonV2ColorOptions);

下载按钮颜色选项构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明options[ProgressButtonV2ColorOptions](#ZH-CN_TOPIC_0000002529444927__progressbuttonv2coloroptions)是色彩信息。

#### ProgressButtonV2ColorOptions

下载按钮色彩信息选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明progressColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

进度条颜色。

默认值：#330A59F7

borderColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮描边颜色。

默认值：#330A59F7

textColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮文本颜色。

默认值：系统默认值(#CE000000)

backgroundColor[ColorMetrics](../graphics/Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)否是

按钮背景颜色。

默认值：$r('sys.color.ohos_id_color_foreground_contrary')

#### 事件

不支持[通用事件](../misc/通用事件.md)。

#### 示例

该示例实现了一个简单的带加载进度的文本下载按钮。

```ets
import { LengthMetrics, ProgressButtonV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local progressIndex: number = 0;
  @Local textState: string = '下载';
  @Local buttonWidth: LengthMetrics = LengthMetrics.vp(200);
  @Local isRunning: boolean = false;
  @Local enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButtonV2({
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            isEnabled: this.enableState,
            onClicked: () => {
              if (this.textState && !this.isRunning && this.progressIndex < 100) {
                this.textState = '继续';
              }
              this.isRunning = !this.isRunning;
              let timer = setInterval(() => {
                if (this.isRunning) {
                  if (this.progressIndex === 100) {
                    clearInterval(timer);
                  } else {
                    this.progressIndex++;
                    if (this.progressIndex === 100) {
                      this.textState = '已完成';
                      this.enableState = false;
                    }
                  }
                } else {
                  clearInterval(timer);
                }
              }, 20);
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 });
      }
    }
  }
}
```