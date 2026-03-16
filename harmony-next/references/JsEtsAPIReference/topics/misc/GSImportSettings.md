# GSImportSettings

GSImportSettings类封装了加载3DGS模型的设置，包括模型路径和数据在文件中的偏移量，帮助开发者加载3DGS模型。

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

uri

string

否

否

3DGS模型的沙箱路径。

offset

number

否

是

需要加载的数据在3DGS模型文件中的偏移量。默认值0。

**示例：**

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