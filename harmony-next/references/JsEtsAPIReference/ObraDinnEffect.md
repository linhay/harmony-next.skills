# ObraDinnEffect

ObraDinnEffect接口封装了bit风格的效果参数。可实现自定义的bit风格。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：**6.0.1(21)

#### 导入模块

```ets
import { spatialRender } from '@kit.SpatialReconKit';
```

#### 属性

名称

类型

只读

可选

说明

noiseStrength

number

否

否

选择哪些像素用来[颜色抖动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-glossary#section1745314193505)。可以起到平滑边缘的效果。加大噪声强度会导致边缘更模糊。取值范围[0, 1]，默认值0.3。

threshold

number

否

否

把像素分为前景颜色或后景颜色的阈值。高于该阈值的像素会被处理为前景颜色。threshold越低，图像整体的颜色会越接近前景颜色。threshold越高，图像整体的颜色会越接近后景颜色。取值范围[0, 1]，默认值0.4。

foregroundColor

[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#color)

否

否

前景颜色。

backgroundColor

[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#color)

否

否

背景颜色。

**示例：**

```ets
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ObraDinnEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.OBRA_DINN_EFFECT_ID }) as spatialRender.ObraDinnEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```