# Scene

本模块作为ArkGraphics 3D基础模块，提供SceneResourceParameters、SceneNodeParameters等通用数据类型。同时提供glTF模型加载，场景元素、资源创建等基础方法。

- 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。
- 关于.shader资源文件，具体请见[.shader资源文件格式要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-shader-resource)。

#### 导入模块

```ets
import { SceneResourceParameters, SceneNodeParameters, RaycastResult, RaycastParameters,RenderResourceFactory,
  SceneResourceFactory, SceneComponent, RenderContext, RenderParameters, Scene } from '@kit.ArkGraphics3D';
```

#### SceneResourceParameters

场景资源参数对象，包含name和uri，用于提供场景资源的名称以及3D场景所需的资源文件路径。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明namestring否否要创建资源的名称，可由开发者自定填写，用于标识该场景资源。uri[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否是3D场景所需的资源文件路径。默认值为undefined。

**示例：**

```ets
import { Shader, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createShaderPromise(): Promise<Shader> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();

      // 创建shader资源（通过SceneResourceParameters配置），路径和文件名可根据项目实际资源自定义
      let sceneResourceParameter: SceneResourceParameters = { name: "shaderResource",
        uri: $rawfile("shaders/custom_shader/custom_material_sample.shader") };
      let shader: Shader = await sceneFactory.createShader(sceneResourceParameter);
      resolve(shader);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### SceneNodeParameters

场景结点参数对象，它用于提供场景结点层次中的名称和路径。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明namestring否否要创建的结点名称，可由开发者自定义填写，用于标识场景结点。pathstring否是场景结点层次中的路径。用于指定创建的摄影机、灯光或结点在场景结点层次中的放置位置。每层之间使用'/'符号进行分割。如果未提供，则将其设置为根结点的子结点。默认值为undefined。

**示例：**

```ets
import { SceneNodeParameters, SceneResourceFactory, Scene, Node } from '@kit.ArkGraphics3D';

function createNodePromise() : Promise<Node> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();

      // 创建SceneNodeParameters类型变量并以此创建node
      let sceneNodeParameter: SceneNodeParameters = { name: "empty_node",
        path:"/rootNode_/empty_node" };
      let node: Node = await sceneFactory.createNode(sceneNodeParameter);
      resolve(node);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### RaycastResult20+

射线检测命中结果对象，包含被射线击中的3D物体详细信息。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明node[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)否否被射线击中的3D场景节点，可通过该节点操作目标物体（如移动、旋转、隐藏）。centerDistancenumber否否命中物体包围盒中心到摄像机中心的距离，取值范围大于0。hitPosition[Position3](SceneType.md#ZH-CN_TOPIC_0000002497446096__position3)否否射线与物体碰撞点的精确世界坐标（{x: number, y: number, z: number}）。

#### RaycastParameters20+

射线检测参数配置，用于定义射线检测的行为。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明rootNode[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)否是限定检测范围：仅检测该节点及其子节点。未设置时检测全场景。

#### RenderResourceFactory20+

用于创建可在共享RenderContext的多个场景（Scene）中共享的渲染资源。

#### createShader20+

createShader(params: SceneResourceParameters): Promise<Shader>

根据指定场景资源参数创建一个着色器，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是创建着色器的参数。详细.shader文件格式请参考[.shader资源文件格式要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics3d-shader-resource)。

**返回值：**

类型说明Promise<[Shader](SceneResource.md#ZH-CN_TOPIC_0000002529286067__shader)>Promise对象，返回创建的着色器对象。

**示例：**

```ets
import { Shader, SceneResourceParameters, Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

function createShaderResource(): Promise<Shader> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    return Promise.reject(new Error("RenderContext is null"));
  }
  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  // 创建shader资源，路径和文件名可根据项目实际资源自定义
  let shaderParams: SceneResourceParameters = {
    name: "custom_shader",
    uri: $rawfile("shaders/custom_shader/custom_material_sample.shader")
  };
  return renderResourceFactory.createShader(shaderParams);
}
```

#### createImage20+

createImage(params: SceneResourceParameters): Promise<Image>

根据指定场景资源参数创建一个图像资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是创建图像的参数。

**返回值：**

类型说明Promise<[Image](SceneResource.md#ZH-CN_TOPIC_0000002529286067__image)>Promise对象，返回创建的图像对象。

**示例：**

```ets
import { Image, SceneResourceParameters, Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

function createImageResource(): Promise<Image> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    return Promise.reject(new Error("RenderContext is null"));
  }
  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  // 加载图片资源，路径和文件名可根据项目实际资源自定义
  let imageParams: SceneResourceParameters = {
    name: "sampleImage",
    uri: $rawfile("image/Cube_BaseColor.png")
  };
  return renderResourceFactory.createImage(imageParams);
}
```

#### createMesh20+

createMesh(params: SceneResourceParameters, geometry: GeometryDefinition): Promise<MeshResource>

根据指定场景资源参数和几何体定义（GeometryDefinition）创建一个网格资源（MeshResource），使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是创建网格资源的参数。geometry[GeometryDefinition](zh-cn_topic_0000002497446096.html#ZH-CN_TOPIC_0000002497446096__geometrydefinition18)是几何形状定义，描述要创建的网格形状。

**返回值：**

类型说明Promise<[MeshResource](SceneResource.md#ZH-CN_TOPIC_0000002529286067__meshresource18)>Promise对象，返回创建的网格资源对象。

**示例：**

```ets
import { SceneResourceParameters, Scene, CustomGeometry, PrimitiveTopology, RenderContext, RenderResourceFactory,
  MeshResource }  from '@kit.ArkGraphics3D';

function createMeshResource(): Promise<MeshResource> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    return Promise.reject(new Error("RenderContext is null"));
  }
  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  const geometry = new CustomGeometry();
  geometry.vertices = [
    { x: 0, y: 0, z: 0 },
    { x: 1, y: 0, z: 0 },
    { x: 1, y: 1, z: 0 },
    { x: 0, y: 1, z: 0 },
    { x: 0, y: 0, z: 1 },
    { x: 1, y: 0, z: 1 },
    { x: 1, y: 1, z: 1 },
    { x: 0, y: 1, z: 1 }
  ];
  geometry.indices = [
    0, 1, 2, 2, 3, 0,     // front
    4, 5, 6, 6, 7, 4,     // back
    0, 4, 5, 5, 1, 0,     // bottom
    1, 5, 6, 6, 2, 1,     // right
    3, 2, 6, 6, 7, 3,     // top
    3, 7, 4, 4, 0, 3      // left
  ];
  geometry.topology = PrimitiveTopology.TRIANGLE_LIST;
  geometry.normals = [
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 },
    { x: 0, y: 0, z: 1 }
  ];
  geometry.uvs = [
    { x: 0, y: 0 },
    { x: 1, y: 0 },
    { x: 1, y: 1 },
    { x: 0, y: 1 },
    { x: 0, y: 0 },
    { x: 1, y: 0 },
    { x: 1, y: 1 },
    { x: 0, y: 1 }
  ];
  geometry.colors = [
    { r: 1, g: 0, b: 0, a: 1 },
    { r: 0, g: 1, b: 0, a: 1 },
    { r: 0, g: 0, b: 1, a: 1 },
    { r: 1, g: 1, b: 0, a: 1 },
    { r: 1, g: 0, b: 1, a: 1 },
    { r: 0, g: 1, b: 1, a: 1 },
    { r: 1, g: 1, b: 1, a: 1 },
    { r: 0, g: 0, b: 0, a: 1 }
  ];
  // 加载图片资源，路径和文件名可根据项目实际资源自定义
  let sceneResourceParameter: SceneResourceParameters = {
    name: "cubeMesh",
    uri: $rawfile("image/Cube_BaseColor.png")
  };
  return renderResourceFactory.createMesh(sceneResourceParameter, geometry);
}
```

#### createSampler20+

createSampler(params:SceneResourceParameters): Promise<Sampler>

根据指定场景资源参数创建一个采样器资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是创建采样器的参数。

**返回值：**

类型说明Promise<[Sampler](SceneResource.md#ZH-CN_TOPIC_0000002529286067__sampler20)>Promise对象，返回创建的采样器对象。

**示例：**

```ets
import { SceneResourceParameters, Scene, RenderContext, RenderResourceFactory, Sampler } from '@kit.ArkGraphics3D';

function createSamplerResource(): Promise<Sampler> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    return Promise.reject(new Error("RenderContext is null"));
  }
  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  // 加载图片资源，路径和文件名可根据项目实际资源自定义
  let samplerParams: SceneResourceParameters = {
    name: "sampler1",
    uri: $rawfile("image/Cube_BaseColor.png")
  };
  return renderResourceFactory.createSampler(samplerParams);
}
```

#### createScene20+

createScene(uri?: ResourceStr): Promise<Scene>

从指定的资源URI创建一个新的场景。如果不指定URI，则创建一个空场景，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明uri[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否创建场景使用的资源路径，如果未传入资源路径，则默认创建一个空场景。

**返回值：**

类型说明Promise<[Scene](#ZH-CN_TOPIC_0000002529446039__scene-1)>Promise对象，返回创建的场景对象。

**示例：**

```ets
import { Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

// fromFile=true：从指定glb文件加载场景，fromFile=false：创建一个空场景，此参数是为了示例展示两种常见场景创建方式
function createScenePromise(fromFile: boolean = false): Promise<Scene> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    return Promise.reject(new Error("RenderContext is null"));
  }

  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  if (fromFile) {
    // 创建场景并加载.gltf或.glb文件作为初始内容，路径和名称可根据项目实际资源自定义
    return renderResourceFactory.createScene($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  } else {
    // 创建空场景
    return renderResourceFactory.createScene();
  }
}
```

#### CameraParameters21+

相机创建参数配置，用于定义相机创建的额外选项。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明msaa22+boolean否是相机是否使能MSAA，true表示使能MSAA，false表示不使能MSAA。默认值为false。renderingPipeline21+[RenderingPipelineType](SceneType.md#ZH-CN_TOPIC_0000002497446096__renderingpipelinetype21)否是选择初始渲染管线类型，默认为轻量级前向渲染管线类型。

#### EffectParameters21+

特效参数。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明effectIdstring否否用于创建特效的ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'。

#### SceneResourceFactory

用于创建3D场景中资源的接口，例如相机、光源等，继承自[RenderResourceFactory](#ZH-CN_TOPIC_0000002529446039__renderresourcefactory20)。

#### createCamera

createCamera(params: SceneNodeParameters): Promise<Camera>

根据结点参数创建相机，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneNodeParameters](#ZH-CN_TOPIC_0000002529446039__scenenodeparameters)是场景结点参数。

**返回值：**

类型说明Promise<[Camera](SceneNode.md#ZH-CN_TOPIC_0000002497606076__camera)>Promise对象，返回相机对象。

**示例：**

```ets
import { SceneNodeParameters, Camera, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createCameraPromise(): Promise<Camera> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneCameraParameter: SceneNodeParameters = { name: "camera1" };
      // 创建相机
      let camera: Camera = await sceneFactory.createCamera(sceneCameraParameter);
      resolve(camera);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createCamera21+

createCamera(params: SceneNodeParameters, cameraParams: CameraParameters): Promise<Camera>

根据结点参数与相机参数创建相机，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneNodeParameters](#ZH-CN_TOPIC_0000002529446039__scenenodeparameters)是场景结点参数。cameraParams[CameraParameters](#ZH-CN_TOPIC_0000002529446039__cameraparameters21)是相机参数。

**返回值：**

类型说明Promise<[Camera](SceneNode.md#ZH-CN_TOPIC_0000002497606076__camera)>Promise对象，返回相机对象。

**示例：**

```ets
import { SceneNodeParameters, Camera, SceneResourceFactory, Scene, CameraParameters,
  RenderingPipelineType } from '@kit.ArkGraphics3D';

function createCameraPromise(): Promise<Camera> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let nodeParameter: SceneNodeParameters = { name: "camera1" };
      let camParameter: CameraParameters = {renderingPipeline: RenderingPipelineType.FORWARD};
      // 创建相机
      let camera: Camera = await sceneFactory.createCamera(nodeParameter, camParameter);
      resolve(camera);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createLight

createLight(params: SceneNodeParameters, lightType: LightType): Promise<Light>

根据结点参数和灯光类型创建灯光，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneNodeParameters](#ZH-CN_TOPIC_0000002529446039__scenenodeparameters)是场景结点参数。lightType[LightType](zh-cn_topic_0000002497606076.html#ZH-CN_TOPIC_0000002497606076__lighttype)是灯光类型。

**返回值：**

类型说明Promise<[Light](SceneNode.md#ZH-CN_TOPIC_0000002497606076__light)>Promise对象，返回灯光对象。

**示例：**

```ets
import { SceneNodeParameters, LightType, Light, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createLightPromise() : Promise<Light> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneLightParameter: SceneNodeParameters = { name: "light" };
      // 创建平行光
      let light: Light = await sceneFactory.createLight(sceneLightParameter, LightType.DIRECTIONAL);
      resolve(light);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createNode

createNode(params: SceneNodeParameters): Promise<Node>

创建结点，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneNodeParameters](#ZH-CN_TOPIC_0000002529446039__scenenodeparameters)是场景结点参数。

**返回值：**

类型说明Promise<[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)>Promise对象，返回结点对象。

**示例：**

```ets
import { SceneNodeParameters, SceneResourceFactory, Scene, Node } from '@kit.ArkGraphics3D';

function createNodePromise(): Promise<Node> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneNodeParameter: SceneNodeParameters = { name: "empty_node",
        path:"/rootNode_/empty_node" };
      // 创建节点
      let node: Node = await sceneFactory.createNode(sceneNodeParameter);
      resolve(node);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createMaterial

createMaterial(params: SceneResourceParameters, materialType: MaterialType): Promise<Material>

根据场景资源参数和材质类型创建材质，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是场景资源参数。materialType[MaterialType](zh-cn_topic_0000002529286067.html#ZH-CN_TOPIC_0000002529286067__materialtype)是材质类型。

**返回值：**

类型说明Promise<[Material](SceneResource.md#ZH-CN_TOPIC_0000002529286067__material)>Promise对象，返回材质对象。

**示例：**

```ets
import { MaterialType, Material, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createMaterialPromise() : Promise<Material> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let sceneMaterialParameter: SceneResourceParameters = { name: "material" };
      // 创建材质
      let material: Material = await sceneFactory.createMaterial(sceneMaterialParameter, MaterialType.SHADER);
      resolve(material);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createEnvironment

createEnvironment(params: SceneResourceParameters): Promise<Environment>

根据场景资源参数创建环境，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneResourceParameters](#ZH-CN_TOPIC_0000002529446039__sceneresourceparameters)是场景资源参数。

**返回值：**

类型说明Promise<[Environment](SceneResource.md#ZH-CN_TOPIC_0000002529286067__environment)>Promise对象，返回环境对象。

**示例：**

```ets
import { Environment, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function createEnvironmentPromise(): Promise<Environment> {
  return new Promise((resolve, reject) => {
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
    scene.then(async (result: Scene) => {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // 加载环境贴图资源，路径和文件名可根据项目实际资源自定义
      let sceneEnvironmentParameter: SceneResourceParameters = { name: "env", uri: $rawfile("KTX/quarry_02_2k_radiance.ktx") };
      // 创建Environment
      let env: Environment = await sceneFactory.createEnvironment(sceneEnvironmentParameter);
      resolve(env);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createGeometry18+

createGeometry(params: SceneNodeParameters, mesh:MeshResource): Promise<Geometry>

根据场景结点参数和网格数据创建几何对象，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[SceneNodeParameters](#ZH-CN_TOPIC_0000002529446039__scenenodeparameters)是场景结点参数。mesh[MeshResource](zh-cn_topic_0000002529286067.html#ZH-CN_TOPIC_0000002529286067__meshresource18)是网格数据参数。

**返回值：**

类型说明Promise<[Geometry](SceneNode.md#ZH-CN_TOPIC_0000002497606076__geometry)>Promise对象，返回几何对象。

**示例：**

```ets
import { SceneResourceFactory, Scene, Geometry, CubeGeometry } from '@kit.ArkGraphics3D';

function createGeometryPromise() : Promise<Geometry> {
  return new Promise((resolve, reject) => {
    let scene: Promise<Scene> = Scene.load();
    scene.then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      let cubeGeom = new CubeGeometry();
      cubeGeom.size = { x: 1, y: 1, z: 1 };
      let meshRes = await sceneFactory.createMesh({ name: "MeshName" }, cubeGeom);
      console.info("TEST createGeometryPromise");
      let geometry: Geometry = await sceneFactory.createGeometry({ name: "GeometryName" }, meshRes);
      resolve(geometry);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### createEffect21+

createEffect(params: EffectParameters): Promise<Effect>

根据特效参数创建特效对象，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[EffectParameters](#ZH-CN_TOPIC_0000002529446039__effectparameters21)是特效参数。

**返回值：**

类型说明Promise<[Effect](SceneResource.md#ZH-CN_TOPIC_0000002529286067__effect21)>Promise对象，返回特效对象。

**示例：**

```ets
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function createEffect() : Promise<Effect> {
  return new Promise((resolve, reject) => {
    let scene: Promise<Scene> = Scene.load();
    scene.then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
      let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"}
      let effect: Effect = await sceneFactory.createEffect(params);
      resolve(effect);
    }).catch((error: Error) => {
      console.error('Scene load failed:', error);
      reject(error);
    });
  });
}
```

#### SceneComponent20+

表示基础场景组件，用于描述场景节点的组件信息，包括组件名称及其对应的属性集合。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明namestring否否要创建场景组件的名称，可由开发者自定填写，用于标识场景组件。propertyRecord<string, string | number | [Vec2](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec2) | [Vec3](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec3) | [Vec4](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec4) | [SceneResource](SceneResource.md#ZH-CN_TOPIC_0000002529286067__sceneresource-1) | boolean | number[] | string[] | [SceneResource](SceneResource.md#ZH-CN_TOPIC_0000002529286067__sceneresource-1)[] | [Vec2](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec2)[] | [Vec3](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec3)[] | [Vec4](SceneType.md#ZH-CN_TOPIC_0000002497446096__vec4)[] | null | undefined>是否组件的属性集合，以键值对形式存储。支持多种基础类型和复杂类型，用于描述场景组件的各种属性。

#### RenderContext20+

定义了所有渲染资源的上下文。在同一渲染上下文中创建的多个场景之间，可以共享渲染资源。

#### getRenderResourceFactory20+

getRenderResourceFactory() : RenderResourceFactory

获取渲染资源工厂，提供创建不同渲染资源的功能。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

类型说明[RenderResourceFactory](#ZH-CN_TOPIC_0000002529446039__renderresourcefactory20)返回一个RenderResourceFactory实例，用于创建渲染资源。

**示例：**

```ets
import { Scene, RenderContext, RenderResourceFactory } from '@kit.ArkGraphics3D';

function getRenderResourceFactory(): void {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    console.error("RenderContext is null");
    return;
  }
  const renderResourceFactory: RenderResourceFactory = renderContext.getRenderResourceFactory();
  console.info("TEST getRenderResourceFactory");
}
```

#### loadPlugin20+

loadPlugin(name: string): Promise<boolean>

用于加载指定名称的插件，通过插件名称查找并加载对应的插件资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明namestring是要加载的插件名称，必须是系统预定义或已注册且可用的插件名称，且符合命名规范。

**返回值：**

类型说明Promise<boolean>返回一个Promise对象，解析结果为boolean类型，表示插件加载是否成功。true表示加载成功，false表示加载失败。

**示例：**

```ets
import { Scene, RenderContext } from '@kit.ArkGraphics3D';

function loadPlugin(): Promise<boolean> {
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (!renderContext) {
    console.error("RenderContext is null");
    return Promise.reject(new Error("RenderContext is null"));
  }
  return renderContext.loadPlugin("pluginName");
}
```

#### registerResourcePath20+

registerResourcePath(protocol: string, uri: string): boolean

注册shader等资产文件所在的路径目录及其检索名，通过检索名查找并替换shader内部关联文件的路径描述，找到对应的资产路径目录，实现资产及其关联文件的正确加载。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明protocolstring是要注册的路径检索名，必须是系统未预定义或未注册且非空的检索名称。uristring是要注册的资产路径目录，与检索名对应，必须是资产文件所在文件夹路径。

**返回值：**

类型说明boolean返回资产文件路径是否注册成功。true表示注册成功；false表示注册失败，可能原因为检索名已被注册或输入参数不可用。

**示例：**

```ets
import { Scene, RenderContext } from '@kit.ArkGraphics3D';

function registerResourcePath(): void {
  // 创建shader资源，路径和文件名可根据项目实际资源自定义
  Scene.load($rawfile("shaders/custom_shader/custom_material_sample.shader"))
    .then(scene => {
      const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
      if (!renderContext) {
        console.error("RenderContext is null");
        return false;
      }
      return renderContext.registerResourcePath("protocol", "OhosRawFile://uri");
    })
    .then(result => {
      if (result) {
        console.info("resource path registration success");
      } else {
        console.error("resource path registration failed");
      }
    });
}
```

#### RenderParameters15+

渲染参数接口。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明alwaysRender15+boolean否是表示是否每一帧都渲染。true表示每一帧都渲染，false表示按需渲染。默认值为true。

#### Scene

用于设置场景。

#### 属性

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明environment[Environment](SceneResource.md#ZH-CN_TOPIC_0000002529286067__environment)否否环境对象。animations[Animation](SceneResource.md#ZH-CN_TOPIC_0000002529286067__animation)[]是否动画数组，用于保存3D场景中的动画对象。root[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node) | null是否3D场景树根结点。

#### load

static load(uri?: ResourceStr): Promise<Scene>

通过传入的资源路径加载资源，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明uri[ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否待加载的模型文件资源路径，默认值为undefined。

**返回值：**

类型说明Promise<[Scene](#ZH-CN_TOPIC_0000002529446039__scene-1)>Promise对象，返回场景对象。

**示例：**

示例1：通过rawfile加载（相对路径）

```ets
import { Scene } from '@kit.ArkGraphics3D';

function loadModel(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {});
}
```

示例2：通过绝对路径加载（从应用沙盒目录/data/storage/el2/base/files加载模型）

```ets
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { Scene } from '@kit.ArkGraphics3D';

async loadModelFromAbsolutePath(): Promise<void> {
  // 获取应用沙盒目录（Scene.load仅能读取应用自身写入的文件，不能读取hdc/adb push写入的文件）
  const uiCtx = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const appCtx = uiCtx.getApplicationContext();
  const filesDir = appCtx.filesDir; // /data/storage/el2/base/files

  // 从rawfile读取模型内容（实际使用中也可以替换为其他来源的数据）
  // 使用.glb文件更易于复制加载；若为.gltf，请将其.bin和贴图文件一并复制到同一目录
  const src = 'gltf/CubeWithFloor/glTF/AnimatedCube.glb';
  const load_uri = `${filesDir}/AnimatedCube.glb`;

  // 写入模型文件到应用沙盒目录，生成可被Scene.load(绝对路径)访问的实际文件
  const rawData = await uiCtx.resourceManager.getRawFileContent(src);
  const file = fileIo.openSync(load_uri, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
  fileIo.writeSync(file.fd, rawData.buffer.slice(rawData.byteOffset, rawData.byteOffset + rawData.byteLength));
  fileIo.closeSync(file);

  // 使用绝对路径加载模型
  Scene.load(load_uri).then((scene: Scene) => {
    // 加载成功后的逻辑处理
  }).catch((error: string) => {
    console.error('Scene load failed: ' + error);
  });
}
```

#### getNodeByPath

getNodeByPath(path: string, type?: NodeType): Node | null

通过路径获取结点。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明pathstring是场景结点层次中的路径。每层之间使用'/'符号进行分割。type[NodeType](SceneNode.md#ZH-CN_TOPIC_0000002497606076__nodetype)否预期返回的结点类型。默认值为空。

**返回值：**

类型说明[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node) | null返回请求结点的实例，如果没有找到或者找到的节点类型与传入的参数不相符则返回空。

**示例：**

```ets
import { Scene, Node } from '@kit.ArkGraphics3D';

function getNode(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // 寻找指定路径的节点
        let node : Node | null = result.getNodeByPath("rootNode_");
    }
  });
}
```

#### getResourceFactory

getResourceFactory(): SceneResourceFactory

获取场景资源工厂对象。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

类型说明[SceneResourceFactory](Scene.md#ZH-CN_TOPIC_0000002529446039__sceneresourcefactory)返回场景资源工厂对象。

**示例：**

```ets
import { SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function getFactory(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // 获得SceneResourceFactory对象
        let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    }
  });
}
```

#### destroy

destroy(): void

销毁场景，释放所有的场景资源。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**示例：**

```ets
import { Scene } from '@kit.ArkGraphics3D';

function destroy(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
         // 销毁scene
        result.destroy();
    }
  });
}
```

#### importNode18+

importNode(name: string, node: Node, parent: Node | null): Node

一般用于从其他场景导入结点。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明namestring是导入结点后的名称，由开发者自定义，无特殊要求。node[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)是被导入的结点。parent[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node) | null是被导入结点在新场景中的父结点。

**返回值：**

类型说明[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)被导入的结点。

**示例：**

```ets
import { Scene } from '@kit.ArkGraphics3D';

function ImportNodeTest() {
  Scene.load().then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    Scene.load($rawfile("gltf/AnimatedCube/glTF/AnimatedCube.glb"))
      .then(async (extScene: Scene) => {
        let extNode = extScene.getNodeByPath("rootNode_/Unnamed Node 1/AnimatedCube");
        console.info("TEST ImportNodeTest");
        let node = result.importNode("scene", extNode, result.root);
        if (node) {
          node.position.x = 5;
        }
      });
  });
}
```

#### importScene18+

importScene(name: string, scene: Scene, parent: Node | null): Node

在当前场景中导入其他场景。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明namestring是导入场景的根结点名称，由开发者自定义，无特殊要求。scene[Scene](#ZH-CN_TOPIC_0000002529446039__scene-1)是被导入的场景。parent[Node](zh-cn_topic_0000002497606076.html#ZH-CN_TOPIC_0000002497606076__node) | null是被导入场景在新场景中的父结点。

**返回值：**

类型说明[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)被导入场景的根结点。

**示例：**

```ets
import { Scene } from '@kit.ArkGraphics3D';

function ImportSceneTest() {
  Scene.load().then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
    let content = await result.getResourceFactory().createScene($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    console.info("TEST ImportSceneTest");
    result.importScene("helmet", content, null);
  });
}
```

#### renderFrame15+

renderFrame(params?: RenderParameters): boolean

通过该接口可以实现按需渲染，例如控制渲染帧率。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明params[RenderParameters](#ZH-CN_TOPIC_0000002529446039__renderparameters15)否渲染参数，默认值为undefined。

**返回值：**

类型说明boolean渲染被成功调度返回true，否则返回false。

**示例：**

```ets
import { Scene } from '@kit.ArkGraphics3D';

function RenderFrameTest() {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(async (result: Scene | undefined) => {
      if (!result) {
        return;
      }
      console.info("TEST RenderFrameTest");
      result.renderFrame({ alwaysRender: true });
  });
}
```

#### createComponent20+

createComponent(node: Node, name: string): Promise<SceneComponent>

在指定节点上创建新的组件，根据组件名称异步创建并附加到节点上，使用Promise异步回调。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明node[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)是组件需要附加到的节点。namestring是要创建的组件名称，由各插件定义有效名称。

**返回值：**

类型说明Promise<[SceneComponent](#ZH-CN_TOPIC_0000002529446039__scenecomponent20)>Promise对象，返回新创建的场景组件。

**示例：**

```ets
import { Scene, SceneComponent } from '@kit.ArkGraphics3D';

function createComponentTest(): Promise<SceneComponent> {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  return Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(scene => {
      if (!scene) {
        return Promise.reject(new Error("Scene load failed"));
      }
      // RenderConfigurationComponent为引擎内置组件，创建时无需依赖插件
      return scene.createComponent(scene.root, "RenderConfigurationComponent");
    })
    .then(component => {
      if (!component) {
        return Promise.reject(new Error("createComponent failed"));
      }
      return component;
    });
}
```

#### getComponent20+

getComponent(node: Node, name: string): SceneComponent | null

根据指定的组件名称，从给定节点上获取对应的组件实例。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

参数名类型必填说明node[Node](SceneNode.md#ZH-CN_TOPIC_0000002497606076__node)是组件附加的节点。namestring是需要获取的组件名称，必须为系统预定义或已注册的自定义组件名称，且需符合命名规范。

**返回值：**

类型说明[SceneComponent](#ZH-CN_TOPIC_0000002529446039__scenecomponent20) | null返回对应名称的组件对象，若未找到则返回null。

**示例：**

```ets
import { Scene } from '@kit.ArkGraphics3D';

function getComponentTest() {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  Scene.load($rawfile("gltf/DamagedHelmet/glTF/DamagedHelmet.glb"))
    .then(async (result: Scene | undefined) => {
      if (!result) {
        console.error("Scene load failed");
        return;
      }
      console.info("TEST getComponentTest");
      let component = result.getComponent(result.root, "myComponent");
      if (component) {
        console.info("getComponent success");
      } else {
        console.warn("Component not found");
      }
    });
}
```

#### getDefaultRenderContext20+

static getDefaultRenderContext(): RenderContext | null

获取当前图形对象所关联的渲染环境信息。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

类型说明[RenderContext](#ZH-CN_TOPIC_0000002529446039__rendercontext20) | null返回当前对象关联的渲染上下文，若对象尚未关联任何渲染上下文，则返回null。

**示例：**

```ets
import { Scene, RenderContext } from '@kit.ArkGraphics3D';

function getDefaultRenderContextTest() {
  console.info("TEST getDefaultRenderContextTest");
  const renderContext: RenderContext | null = Scene.getDefaultRenderContext();
  if (renderContext) {
    console.info("getDefaultRenderContext success");
  } else {
    console.error("RenderContext is null");
  }
}
```