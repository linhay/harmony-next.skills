# Class (MaskFilter)

蒙版滤镜对象。

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

#### createBlurMaskFilter12+

static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter

创建具有模糊效果的蒙版滤镜。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

参数名类型必填说明blurType[BlurType](Enums.md#ZH-CN_TOPIC_0000002529285977__blurtype12)是模糊类型。sigmanumber是高斯模糊的标准偏差，必须为大于0的浮点数。

**返回值：**

类型说明[MaskFilter](Class (MaskFilter).md)返回创建的蒙版滤镜对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed.

**示例：**

```ets
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
  }
}
```