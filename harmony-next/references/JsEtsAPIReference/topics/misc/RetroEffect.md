# RetroEffect

RetroEffect接口封装了复古风格的效果参数。可实现自定义的复古风格。

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

colorNum

number

否

否

使用多少种颜色来作为[颜色抖动](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-glossary#section1745314193505)。通常值越大图像质量越高、值越小复古风格越重。取值范围大于0。默认值8。

pixelSize

number

否

否

下采样的程度。越大越重。若为1，则不会进行下采样。取值范围大于等于1。默认值4。

blendEnabled

boolean

否

否

是否把处理后的图片与原始图片融合，设置为true会把处理后的图片与原始图片融合，设置为false不会做融合。复古风格会造成图像的亮度下降、色彩偏移。设为true用以维持图像的亮度与色彩。默认值true。

curve

number

否

否

显像管电视屏幕带有的曲率。复古风格会模拟显像管电视的显示特征，

curve代表显像管电视屏幕带有的曲率，值越大曲率越大。取值范围[0, 1]。默认值0.25。

**示例：**

```ets
import { Scene, RenderContext, RenderingPipelineType } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.RetroEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID }) as spatialRender.RetroEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```