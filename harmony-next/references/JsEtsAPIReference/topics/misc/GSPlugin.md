# GSPlugin

GSPlugin类封装了与3DGS相关的内容，包括3DGS插件ID和3DGS模型加载接口，帮助开发者实现对3DGS的自定义功能。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：**6.0.1(21)

#### 导入模块

```ets
import { spatialRender } from '@kit.SpatialReconKit';
```

#### 注意事项

调用GSPlugin接口前，必须先加载对应的插件ID，否则会出现未定义的行为。

```ets
import { spatialRender } from '@kit.SpatialReconKit';
import { Scene } from '@kit.ArkGraphics3D';

let renderContext = Scene.getDefaultRenderContext();
if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
}
```

#### 常量

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：**6.0.1(21)

名称

类型

说明

PLUGIN_ID

string

表示该类对应的插件ID，。

RETRO_EFFECT_ID

string

表示复古效果对应的ID。

COMIC_EFFECT_ID

string

表示漫画效果对应的ID。

OBRA_DINN_EFFECT_ID

string

表示黑白bit效果对应的ID。

COLOR_EDITING_EFFECT_ID

string

表示颜色编辑效果对应的ID。

开发者不需要感知各ID的具体值，推荐直接使用字符串变量。

#### loadGSNode

加载3DGS模型。

**系统能力**：SystemCapability.Graphics.SpatialRender

**起始版本：**6.0.1(21)

**参数：**

参数名

类型

必填

说明

scene

[Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene)

是

指定在应用界面想要显示的场景，是ArkGraphics 3D基础模块。建议通过调用[Scene.load](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene#load)来获取。

params

[GSImportSettings](GSImportSettings.md)

是

加载3DGS模型的设置。

parent

[Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)

否

预期挂载3DGS模型的节点。如果不传，加载的3DGS模型会被挂载到Scene的根节点上

**返回值：**

类型

说明

Promise<[GSNode](../components/GSNode（3DGS渲染对象）.md)>

通过Promise获取3DGS模型对应的[GSNode](../components/GSNode（3DGS渲染对象）.md)。

**示例：**

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