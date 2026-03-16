# ComicEffect

ComicEffect接口封装了漫画风格的效果的参数。可实现自定义的漫画风格。

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

lineThreshold

number

否

否

判定像素为轮廓线的阈值。图像梯度大于该阈值的像素会被判定为轮廓线。取值范围[0, 1] ，默认值0.2。

lineColor

[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#color)

否

否

轮廓线的颜色。

**示例：**

```ets
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ComicEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COMIC_EFFECT_ID }) as spatialRender.ComicEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```