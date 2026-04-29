# spatialRender

spatialRender模块主要用于渲染3DGS数据，展示3DGS渲染场景。

系统能力： SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**导入模块**

```ets
import { spatialRender } from '@kit.SpatialReconKit';
```

**GSNode（3DGS渲染对象）**

GSNode类继承自[Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)，代表一个3DGS（3D Gaussian Splatting）渲染对象，帮助开发者操作3DGS模型。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**使用说明**

GSNode类的使用方法请参考[Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)。

**GSPlugin**

GSPlugin类封装了与3DGS相关的内容，包括3DGS插件ID和3DGS模型加载接口，帮助开发者实现对3DGS的自定义功能。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

   ![image](public_sys-resources/caution_3.0-zh-cn.webp)

调用GSPlugin接口前，必须先加载对应的插件ID，否则会出现未定义的行为。

```ets
import { spatialRender } from '@kit.SpatialReconKit';
import { Scene } from '@kit.ArkGraphics3D';

let renderContext = Scene.getDefaultRenderContext();
if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
}
```

**常量**

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| PLUGIN_ID | string | 表示该类对应的插件ID。 |
| RETRO_EFFECT_ID | string | 表示复古效果对应的ID。 |
| COMIC_EFFECT_ID | string | 表示漫画效果对应的ID。 |
| OBRA_DINN_EFFECT_ID | string | 表示黑白bit效果对应的ID。 |
| COLOR_EDITING_EFFECT_ID | string | 表示颜色编辑效果对应的ID。 |

开发者不需要感知各ID的具体值，推荐直接使用字符串变量。

**loadGSNode**

加载3DGS模型。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | Scene | 是 | 指定在应用界面想要显示的场景，是ArkGraphics 3D基础模块。建议通过调用Scene.load来获取。 |
| params | GSImportSettings | 是 | 加载3DGS模型的设置。 |
| parent | Node | 否 | 预期挂载3DGS模型的节点。如果不传，加载的3DGS模型会被挂载到Scene的根节点上。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<GSNode> | 通过Promise获取3DGS模型对应的GSNode。 |

示例：

```ets
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb"; //3DGS模型的uri，根据实际情况修改
    let offset = 0;
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}
```

**GSImportSettings**

GSImportSettings类封装了加载3DGS模型的设置，包括模型路径和数据在文件中的偏移量，帮助开发者加载3DGS模型。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 3DGS模型的文件路径。 |
| offset | number | 否 | 是 | 待加载数据在3DGS模型文件中的偏移量。默认值0。 |

示例：

```ets
import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/doll.glb";
    let offset = 0;
    let setting: spatialRender.GSImportSettings = { uri: uri, offset : offset};
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, setting, scene.root);
  });
}
```

**RetroEffectParams**

RetroEffect参数，该类型为字符串枚举，该枚举值可在[Effect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources#effect21)的[getPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

系统能力： SystemCapability.Graphics.SpatialRender

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR_NUM | 'colorNum' | RetroEffect中colorNum属性的名称。 属性对应取值类型为number。该属性表示使用多少种颜色来作为颜色抖动。通常属性值越大图像质量越高、值越小复古风格越重。属性取值范围大于0，默认值8。 |
| PIXEL_SIZE | 'pixelSize' | RetroEffect中pixelSize属性的名称。 属性对应取值类型为number。该属性表示下采样的程度。越大越重。若该属性取值为1，则不会进行下采样。属性取值范围大于等于1，默认值4。 |
| BLEND_ENABLED | 'blendEnabled' | RetroEffect中blendEnabled属性的名称。 属性对应取值类型为boolean。该属性表示是否把处理后的图片与原始图片融合，属性值设置为true会把处理后的图片与原始图片融合，设置为false不会做融合。由于复古风格会造成图像的亮度下降、色彩偏移，将该属性值设为true用以维持图像的亮度与色彩。属性取值默认为true。 |
| CURVE | 'curve' | RetroEffect中curve属性的名称。 属性对应取值类型为number。该属性表示显像管电视屏幕带有的曲率。复古风格会模拟显像管电视的显示特征。该属性代表显像管电视屏幕带有的曲率，属性取值越大曲率越大。属性取值范围[0, 1]，默认值0.25。 |

示例：

```ets
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID });
    let colNum = effect.getPropertyValue(spatialRender.RetroEffectParams.COLOR_NUM);
    let res = effect.setPropertyValue(spatialRender.RetroEffectParams.COLOR_NUM, 4);
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```

**RetroEffect**

RetroEffect接口封装了复古风格的效果参数。可实现自定义的复古风格。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorNum | number | 否 | 否 | 使用多少种颜色来作为颜色抖动。通常值越大图像质量越高、值越小复古风格越重。取值范围大于0。默认值8。 |
| pixelSize | number | 否 | 否 | 下采样的程度。越大越重。若为1，则不会进行下采样。取值范围大于等于1。默认值4。 |
| blendEnabled | boolean | 否 | 否 | 是否把处理后的图片与原始图片融合，设置为true会把处理后的图片与原始图片融合，设置为false不会做融合。复古风格会造成图像的亮度下降、色彩偏移。设为true用以维持图像的亮度与色彩。默认值true。 |
| curve | number | 否 | 否 | 显像管电视屏幕带有的曲率。复古风格会模拟显像管电视的显示特征， curve代表显像管电视屏幕带有的曲率，值越大曲率越大。取值范围[0, 1]。默认值0.25。 |

示例：

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

**ComicEffectParams**

ComicEffect参数，该类型为字符串枚举，该枚举值可在[Effect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources#effect21)的[getPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

系统能力： SystemCapability.Graphics.SpatialRender

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINE_THRESHOLD | 'lineThreshold' | ComicEffect中lineThreshold属性的名称。 属性对应取值类型为number。该属性表示用来判定像素为轮廓线的阈值，图像梯度大于该阈值的像素会被判定为轮廓线。该属性取值范围[0, 1]，默认值为0.2。 |
| LINE_COLOR | 'lineColor' | ComicEffect中lineThreshold属性的名称。 属性对应取值类型为Color。该属性表示轮廓线的颜色。 |

示例：

```ets
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COMIC_EFFECT_ID });
    let threshold = effect.getPropertyValue(spatialRender.ComicEffectParams.LINE_THRESHOLD);
    let res = effect.setPropertyValue(spatialRender.ComicEffectParams.LINE_THRESHOLD, 0.5);
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```

**ComicEffect**

ComicEffect接口封装了漫画风格的效果的参数。可实现自定义的漫画风格。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lineThreshold | number | 否 | 否 | 判定像素为轮廓线的阈值。图像梯度大于该阈值的像素会被判定为轮廓线。取值范围[0, 1] ，默认值0.2。 |
| lineColor | Color | 否 | 否 | 轮廓线的颜色。 |

示例：

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

**ObraDinnEffectParams**

ObraDinnEffect参数，该类型为字符串枚举，该枚举值可在[Effect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources#effect21)的[getPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

系统能力： SystemCapability.Graphics.SpatialRender

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOISE_STRENGTH | 'noiseStrength' | ObraDinnEffect中的noiseStrength属性的名称。 属性对应取值类型为number。该属性表示选择哪些像素用来颜色抖动。该属性可以起到平滑边缘的效果，加大噪声强度会导致边缘更模糊。属性取值范围[0, 1]，默认值0.3。 |
| THRESHOLD | 'threshold' | ObraDinnEffect中的threshold属性的名称。 属性对应取值类型为number。该属性表示将像素分为前景颜色或后景颜色的阈值。该属性取值越高，图像整体的颜色会越接近后景颜色。属性值取值范围[0, 1]，默认值0.4。 |
| FOREGROUND_COLOR | 'foregroundColor' | ObraDinnEffect中的foregroundColor属性的名称。 属性对应取值类型为Color。该属性表示前景颜色。 |
| BACKGROUND_COLOR | 'backgroundColor' | ObraDinnEffect中的backgroundColor属性的名称。 属性对应取值类型为Color。该属性表示背景颜色。 |

示例：

```ets
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.OBRA_DINN_EFFECT_ID });
    let noiseStrength = effect.getPropertyValue(spatialRender.ObraDinnEffectParams.NOISE_STRENGTH);
    let res = effect.setPropertyValue(spatialRender.ObraDinnEffectParams.NOISE_STRENGTH, 0.5);
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```

**ObraDinnEffect**

ObraDinnEffect接口封装了bit风格的效果参数。可实现自定义的bit风格。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| noiseStrength | number | 否 | 否 | 选择哪些像素用来颜色抖动。可以起到平滑边缘的效果。加大噪声强度会导致边缘更模糊。取值范围[0, 1]，默认值0.3。 |
| threshold | number | 否 | 否 | 把像素分为前景颜色或后景颜色的阈值。高于该阈值的像素会被处理为前景颜色。threshold越低，图像整体的颜色会越接近前景颜色。threshold越高，图像整体的颜色会越接近后景颜色。取值范围[0, 1]，默认值0.4。 |
| foregroundColor | Color | 否 | 否 | 前景颜色。 |
| backgroundColor | Color | 否 | 否 | 背景颜色。 |

示例：

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

**ColorEditingEffectParams**

ColorEditingEffect参数，该类型为字符串枚举，该枚举值可在[Effect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources#effect21)的[getPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#getpropertyvalue23)和[setPropertyValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources.md#setpropertyvalue23)方法中使用，用于声明属性的名称，以获取属性的当前值或更新属性的值。

系统能力： SystemCapability.Graphics.SpatialRender

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXPOSURE | 'exposure' | ColorEditingEffect中的exposure属性的名称。 属性对应取值类型为number。该属性表示图像的曝光度。属性推荐取值范围[-5, 5]，默认值0.0。 |
| CONTRAST | 'contrast' | ColorEditingEffect中的contrast属性的名称。 属性对应取值类型为number。该属性表示图像的对比度。属性推荐取值范围[0, 2]，默认值1.0。 |
| TEMPERATURE | 'temperature' | ColorEditingEffect中的temperature属性的名称。 属性对应取值类型为number。该属性表示图像的色温。属性推荐取值范围[-2, 2]，默认值0.0。 |
| TINT | 'tint' | ColorEditingEffect中的tint属性的名称。 属性对应取值类型为number。该属性表示图像的色调。属性推荐取值范围[-1, 1]，默认值0.0。 |
| SATURATION | 'saturation' | ColorEditingEffect中的saturation属性的名称。 属性对应取值类型为number。该属性表示图像的饱和度。属性推荐取值范围[0, 2]，默认值1.0。 |
| VIBRANCE | 'vibrance' | ColorEditingEffect中的vibrance属性的名称。 属性对应取值类型为number。该属性表示图像的自然饱和度。属性推荐取值范围[-1, 1]，默认值0.0。 |

示例：

```ets
import { Scene, RenderContext, RenderingPipelineType, Effect } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : Effect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.COLOR_EDITING_EFFECT_ID });
    let exposure = effect.getPropertyValue(spatialRender.ColorEditingEffectParams.EXPOSURE);
    let res = effect.setPropertyValue(spatialRender.ColorEditingEffectParams.EXPOSURE, 0.5);
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
```

**ColorEditingEffect**

ColorEditingEffect接口封装了颜色编辑风格的参数。可帮助开发者实现自定义的图像风格。

系统能力：SystemCapability.Graphics.SpatialRender

起始版本： 6.0.1(21)

**属性**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exposure | number | 否 | 否 | 图像的曝光度，推荐取值范围[-5，5]，默认值0.0。 |
| contrast | number | 否 | 否 | 图像的对比度，推荐取值范围[0, 2]，默认值1.0。 |
| temperature | number | 否 | 否 | 图像的色温，推荐取值范围[-2, 2]，默认值0.0。 |
| tint | number | 否 | 否 | 图像的色调，推荐取值范围[-1，1]，默认值0.0。 |
| saturation | number | 否 | 否 | 图像的饱和度，推荐取值范围[0, 2]，默认值1.0。 |
| vibrance | number | 否 | 否 | 图像的自然饱和度，推荐取值范围[-1, 1]，默认值0.0。 |

示例：

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