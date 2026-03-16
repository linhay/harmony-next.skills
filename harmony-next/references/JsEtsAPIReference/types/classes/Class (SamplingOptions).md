# Class (SamplingOptions)

采样选项对象。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 12开始支持。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### constructor12+

constructor()

构造一个新的采样选项对象，[FilterMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__filtermode12)的默认值为FILTER_MODE_NEAREST。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

#### constructor12+

constructor(filterMode: FilterMode)

构造一个新的采样选项对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明filterMode[FilterMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285977__filtermode12)是过滤模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```