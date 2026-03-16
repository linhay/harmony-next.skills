# ColorEditingEffect

ColorEditingEffect接口封装了颜色编辑风格的参数。可帮助开发者实现自定义的图像风格。

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

exposure

number

否

否

图像的曝光度，推荐取值范围[-5，5]，默认值0.0。

contrast

number

否

否

图像的对比度，推荐取值范围[0, 2]，默认值1.0。

temperature

number

否

否

图像的色温，推荐取值范围[-2, 2]，默认值0.0。

tint

number

否

否

图像的色调，推荐取值范围[-1，1]，默认值0.0。

saturation

number

否

否

图像的饱和度，推荐取值范围[0, 2]，默认值1.0。

vibrance

number

否

否

图像的自然饱和度，推荐取值范围[-1, 1]，默认值0.0。

**示例：**

```ets
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.ColorEditingEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COLOR_EDITING_EFFECT_ID }) as spatialRender.ColorEditingEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```