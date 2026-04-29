# SceneResource

本模块提供3D图形中常用的基本资源类型。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

**导入模块**

```ets
import { SceneResourceType, SceneResource, Shader, MaterialType, CullMode, Blend, RenderSort, Material,
  MaterialProperty, MetallicRoughnessMaterial, ShaderMaterial, SamplerFilter, SamplerAddressMode, Sampler,
  SubMesh, Morpher, Mesh, MeshResource, Animation, EnvironmentBackgroundType, Environment, Image } from '@kit.ArkGraphics3D';
```

**SceneResourceType**

场景资源类型枚举，对场景中的资源进行分类。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未定义类型。 |
| NODE | 1 | 结点类型。 |
| ENVIRONMENT | 2 | 环境类型。 |
| MATERIAL | 3 | 材质类型。 |
| MESH | 4 | 网格类型。 |
| ANIMATION | 5 | 动画类型。 |
| SHADER | 6 | 着色器类型。 |
| IMAGE | 7 | 图片类型。 |
| MESH_RESOURCE18+ | 8 | 网格资源类型。 |
| EFFECT21+ | 9 | 后处理特效类型。 |

**SceneResource**

用于表示场景中的资源。

**属性**

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 名称，没有特殊格式要求。 |
| resourceType | SceneResourceType | 是 | 否 | 场景资源类型，默认值为undefined。 |
| uri | ResourceStr | 是 | 是 | 需要加载的资源，默认值为undefined。 |

**destroy**

destroy(): void

销毁场景资源，释放所有关联的资源或引用，一旦被释放，资源就不能被再次使用或访问。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Shader, SceneResourceParameters, SceneResourceFactory, Scene } from '@kit.ArkGraphics3D';

function destroy(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let sceneFactory: SceneResourceFactory = result.getResourceFactory();
      // 创建shader资源，路径和文件名可根据项目实际资源自定义
      let sceneResourceParameter: SceneResourceParameters = { name: "shaderResource",
        uri: $rawfile("shaders/custom_shader/custom_material_sample.shader") };
      let shader: Promise<Shader> = sceneFactory.createShader(sceneResourceParameter);
      shader.then(async (shaderResult:Shader) => {
         // 释放资源
         shaderResult.destroy();
      });
    }
  });
}
```

**Shader**

着色器，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

**属性**

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputs | Record<string, number | Vec2 | Vec3 | Vec4 | Image> | 是 | 否 | 着色器输入。 |

**setShaderInputs23+**

setShaderInputs(inputs: Record<string, number | Vec2 | Vec3 | Vec4 | Image>): void

设置[Shader](#ZH-CN_TOPIC_0000002553202193__shader)的输入，该接口性能优于直接设置inputs属性。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ArkUi.Graphics3D

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | Record<string, number | Vec2 | Vec3 | Vec4 | Image> | 是 | 一个字符串到值的映射，用于设置shader输入。 |

示例：

```ets
import { Image, MaterialType, Scene, SceneResourceFactory, Shader, ShaderMaterial } from '@kit.ArkGraphics3D';

function setinputs(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result) {
      let rf : SceneResourceFactory | null = await result.getResourceFactory();
      if (!rf) {
        return;
      }
      // 创建材质和shader
      let material: ShaderMaterial | null = await rf.createMaterial({name: "CustomMaterial"}, MaterialType.SHADER);
      let shader : Shader | null = await rf.createShader(
        {name: "CustomShader", uri: $rawfile("shaders/custom_shader/custom_material_sample.shader")});
      if (!material || !shader) {
        return;
      }
      // 加载纹理资源
      let image : Image | null = await rf.createImage({name: "envImg", uri: $rawfile("custom_image.jpg")});
      if (!image) {
        return;
      }
      // 绑定shader到纹理上
      material.colorShader = shader;
      // 设置shader输入
      material.colorShader.setShaderInputs({
        "uTime": 1.0,
        "uVelocity": {x: 1.0, y: 1.0, z:-1.0, w:-1.0},
        "uTexture": image
      })
    }
  });
}
```

**MaterialType**

场景中物体材质类型枚举，定义材质的渲染方式。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHADER | 1 | 材质由着色器定义。 |
| METALLIC_ROUGHNESS20+ | 2 | 采用基于物理渲染（PBR）的金属-粗糙度模型，通过金属度与粗糙度参数，模拟更真实的材质光照效果。 |
| UNLIT23+ | 3 | 不受光照影响的材质。 |
| OCCLUSION23+ | 4 | 遮挡材质，能够遮挡场景中的其他物体但不会遮挡环境。 |

**CullMode20+**

用于设置基于物理渲染（PBR）材质的剔除模式枚举。通过控制剔除物体的正面或背面几何面片，提升渲染性能和视觉效果。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 禁用剔除。 |
| FRONT | 1 | 剔除正面几何面片。 |
| BACK | 2 | 剔除背面几何面片。 |

**Blend20+**

用于控制材质的透明效果。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 是否启用材质的透明效果模式。true表示开启透明，false表示关闭透明。 |

**RenderSort20+**

定义材质物体的渲染顺序，控制不同物体在渲染管线中的绘制先后。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| renderSortLayer | number | 否 | 是 | 渲染图层id，数值越小，渲染顺序越靠前。取值范围[0, 63]，默认图层id为32。 |
| renderSortLayerOrder | number | 否 | 是 | 同一渲染图层内，不同物体的渲染顺序，数值越小，越先渲染。取值范围[0, 255]，默认值为0。 |

**PolygonMode23+**

控制多边形绘制模式的枚举。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FILL | 0 | 绘制多边形的每个面。 |
| LINE | 1 | 仅绘制多边形线框。 |
| POINT | 2 | 仅绘制多边形顶点。 |

**Material**

材质类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| materialType | MaterialType | 是 | 否 | 材质类型。 |
| shadowReceiver20+ | boolean | 否 | 是 | 材质是否接收阴影。true表示该材质接收阴影，false表示不接收，默认值为false。 |
| cullMode20+ | CullMode | 否 | 是 | 当前材质的剔除模式设置，用于控制是否剔除背面几何面片，默认值为BACK。 |
| blend20+ | Blend | 否 | 是 | 材质是否透明，默认值为false。 |
| alphaCutoff20+ | number | 否 | 是 | 透明通道阈值，如果像素的alpha值等于或高于此阈值，则渲染该像素；如果低于此阈值，则不会渲染该像素。设置值小于1时，则开启该模式，取值范围为[0, 1]，默认值为1。 |
| renderSort20+ | RenderSort | 否 | 是 | 渲染排序设置，用于控制材质在渲染管线中的渲染顺序，渲染图层id默认值为32，同一图层内的渲染顺序默认值为0。 |
| polygonMode23+ | PolygonMode | 否 | 是 | 模型的多边形绘制模式，默认值为FILL。 |

**MaterialProperty20+**

材质属性接口，用于定义材质所使用的纹理、属性因子及纹理采样器信息。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | Image | null | 否 | 否 | 基于物理渲染（PBR）属性纹理贴图，用于表达材质的纹理信息。 |
| factor | Vec4 | 否 | 否 | 基于物理渲染（PBR）属性因子，不同属性不同含义。 |
| sampler | Sampler | 否 | 是 | 纹理贴图采样器，默认使用放大、缩小和mipmap过滤模式为线性过滤（LINEAR），纹理贴图U、V、W方向的寻址模式为重复（REPEAT）。 |

**MetallicRoughnessMaterial20+**

用于实现真实感外观的材质资源。采用基于物理渲染（PBR）的金属-粗糙度模型，通过调节金属度和粗糙度参数，可模拟金属、塑料等不同材质的表面光照与反射效果，继承自[Material](#ZH-CN_TOPIC_0000002553202193__material)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseColor | MaterialProperty | 否 | 否 | 基础颜色贴图，用于表达材质在没有光照情况下所表达的颜色信息。 |
| normal | MaterialProperty | 否 | 否 | 法线贴图，表达物体表面结构细节，使光照效果更真实，不改变几何结构。 |
| material | MaterialProperty | 否 | 否 | 金属材质参数。 粗糙度（Roughness）：表达材质因其表面细微的结构细节所导致的反光强弱程度。 金属度（Metallic）：表达材质的金属属性。 反射度（Reflectance）：材质的光反射率。 |
| ambientOcclusion | MaterialProperty | 否 | 否 | 环境光遮蔽贴图，用于模拟环境光在物体凹陷或细节部分的遮挡效果，增强局部阴影表现，提高细节真实感。 |
| emissive | MaterialProperty | 否 | 否 | 自发光颜色，表达材质自身作为光源向外发光的颜色信息。 |
| clearCoat | MaterialProperty | 否 | 否 | 透明图层，类似于车漆、碳纤、被水打湿的表面的材质需要在面上再增加一个透明的、具有一定反光特性的面。 |
| clearCoatRoughness | MaterialProperty | 否 | 否 | 透明图层粗糙度。 |
| clearCoatNormal | MaterialProperty | 否 | 否 | 透明图层法线贴图。 |
| sheen | MaterialProperty | 否 | 否 | 微纤维漫反射材质光泽，可用于表示布料和织物材料。 |
| specular | MaterialProperty | 否 | 否 | 非金属材质的高光反射，表示传统镜面反射强度。 |

**ShaderMaterial**

着色器材质，继承自[Material](#ZH-CN_TOPIC_0000002553202193__material)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorShader | Shader | 否 | 是 | 着色器，默认值为undefined。 |

**UnlitMaterial23+**

不受光照影响的材质，其着色值只与设置的基础颜色有关，与光照条件无关，继承自[Material](#ZH-CN_TOPIC_0000002553202193__material)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseColor | MaterialProperty | 否 | 否 | 基础颜色属性，用于表达材质的基础颜色信息。 |

**OcclusionMaterial23+**

遮挡材质，能够遮挡场景中的其他物体但不会遮挡环境，继承自[Material](#ZH-CN_TOPIC_0000002553202193__material)。

系统能力： SystemCapability.ArkUi.Graphics3D

**SamplerFilter20+**

采样器过滤模式枚举，定义纹理采样时的插值方法，用于控制纹理在缩放或变形时如何计算最终像素的颜色值。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEAREST | 0 | 使用最近邻插值进行采样，速度快但边缘可能锯齿明显。 |
| LINEAR | 1 | 使用线性插值进行采样，效果更平滑但性能略低。 |

**SamplerAddressMode20+**

采样器寻址模式枚举，用于控制纹理坐标超出[0, 1]范围时的处理方式。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REPEAT | 0 | 纹理坐标超出范围时，纹理会重复平铺。 |
| MIRRORED_REPEAT | 1 | 纹理坐标超出范围时，纹理以镜像方式重复。 |
| CLAMP_TO_EDGE | 2 | 纹理坐标超出范围时，贴图边缘像素会被拉伸延伸。 |

**Sampler20+**

采样器接口，用于定义纹理贴图采样时的过滤方式。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| magFilter | SamplerFilter | 否 | 是 | 放大过滤模式，控制纹理贴图被放大时的采样方式，默认值为LINEAR。 |
| minFilter | SamplerFilter | 否 | 是 | 缩小过滤模式，控制纹理贴图被缩小时的采样方式，默认值为LINEAR。 |
| mipMapMode | SamplerFilter | 否 | 是 | mipmap过滤模式，控制纹理贴图在多层不同分辨率之间的采样方式，默认值为LINEAR。 |
| addressModeU | SamplerAddressMode | 否 | 是 | 纹理贴图U方向（水平）的采样方式，默认值为REPEAT。 |
| addressModeV | SamplerAddressMode | 否 | 是 | 纹理贴图V方向（垂直）的采样方式，默认值为REPEAT。 |

**SubMesh**

子网格类型。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 名称，没有特殊格式要求。 |
| material | Material | 否 | 否 | 材质。 |
| aabb | Aabb | 是 | 否 | 轴对齐边界盒。 |

**Morpher20+**

用于控制3D模型的形变，通过调整不同形变目标的权重，实现模型的动态变形效果。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| targets | Record<string, number> | 是 | 否 | 用于存储所有形变目标的名称和对应的权重。权重值通常在[0.0, 1.0]范围内。 |

**Mesh**

网格类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subMeshes | SubMesh[] | 是 | 否 | 子网格数组。 |
| aabb | Aabb | 是 | 否 | 轴对齐包围盒。 |
| materialOverride | Material | 否 | 是 | 材质，默认为空。 |

**MeshResource18+**

网格资源，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

系统能力： SystemCapability.ArkUi.Graphics3D

**Animation**

动画类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

**属性**

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 动画是否使能。true表示可以播放动画，false表示不可以播放动画。 |
| speed20+ | number | 否 | 是 | 动画的播放速度因子。默认值为1.0，表示正常速度播放。如果设置为负值，动画将以反向速度播放。 |
| duration | number | 是 | 否 | 动画持续时间，单位为秒（s），取值范围大于等于0。 |
| running | boolean | 是 | 否 | 动画运行状态。true表示动画正在播放，false表示动画停止播放。 |
| progress | number | 是 | 否 | 动画进度状态，取值区间为[0, 1]。 |

**onFinished**

onFinished(callback: Callback<void>): void

动画播放结束时执行的回调函数，动画播放完成或者finish操作会触发这个回调。

系统能力： SystemCapability.ArkUi.Graphics3D

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数，返回值为空。 |

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function onFinished(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 注册回调函数
      anim.onFinished(()=>{
        console.info("onFinished");
      });
    }
  });
}
```

**onStarted**

onStarted(callback: Callback<void>): void

当动画开始播放时执行的回调函数，start操作以及restart操作也会触发这个回调。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数，返回值为空。 |

动画开始时会执行传入的回调函数。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function onStarted(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 注册回调函数
      anim.onStarted(()=>{
        console.info("onStarted");
      });
    }
  });
}
```

**pause**

pause(): void

将动画暂停，动画的播放进度保持在当前状态。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function pause(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 暂停动画
      anim.pause();
    }
  });
}
```

**restart**

restart(): void

从动画的起点开始播放动画。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function restart(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 重启动画
      anim.restart();
    }
  });
}
```

**seek**

seek(position: number): void

从指定位置开始播放动画。

系统能力： SystemCapability.ArkUi.Graphics3D

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 要重新播放动画的起始位置，取值区间为[0, 1]。 |

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function seek(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 指定动画的播放进度到10%
      anim.seek(0.1);
    }
  });
}
```

**start**

start(): void

基于当前进度开始播放一个动画。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function start(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 开始动画
      anim.start();
    }
  });
}
```

**stop**

stop(): void

停止播放一个动画，并将动画的进度设置到未开始状态。

系统能力： SystemCapability.ArkUi.Graphics3D

示例：

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function stop(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 停止播放动画，并将动画的进度设置到未开始状态
      anim.stop();
    }
  });
}
```

**finish**

finish(): void

直接跳转到动画的最后，并将动画的进度设置到已结束状态。

系统能力： SystemCapability.ArkUi.Graphics3D

```ets
import { Animation, Scene } from '@kit.ArkGraphics3D';

function finish(): void {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  let scene: Promise<Scene> = Scene.load($rawfile("gltf/CubeWithFloor/glTF/AnimatedCube.glb"));
  scene.then(async (result: Scene) => {
    if (result && result.animations && result.animations[0]) {
      let anim: Animation = result.animations[0];
      // 直接跳转到动画的最后，并将动画的进度设置到已结束状态。
      anim.finish();
    }
  });
}
```

**EnvironmentBackgroundType**

环境背景类型枚举，用于定义场景的背景呈现方式。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND_NONE | 0 | 无背景。 |
| BACKGROUND_IMAGE | 1 | 图片背景。 |
| BACKGROUND_CUBEMAP | 2 | 立方体贴图背景。 |
| BACKGROUND_EQUIRECTANGULAR | 3 | 等距柱状投影背景。 |

**Environment**

环境类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundType | EnvironmentBackgroundType | 否 | 否 | 环境背景类型。 |
| indirectDiffuseFactor | Vec4 | 否 | 否 | 间接散射系数。 |
| indirectSpecularFactor | Vec4 | 否 | 否 | 间接反射系数。 |
| environmentMapFactor | Vec4 | 否 | 否 | 环境地图系数。 |
| environmentImage | Image | null | 否 | 是 | 环境图片，默认为undefined。 |
| radianceImage | Image | null | 否 | 是 | 辐射图片，默认为undefined。 |
| irradianceCoefficients | Vec3[] | 否 | 是 | 辐射系数，默认为undefined。 |
| environmentRotation23+ | Quaternion | 否 | 是 | 环境光的旋转，默认为undefined，接收参数需为归一化后的四元数。 |

**Image**

图片类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 图片宽度，单位为像素（px），取值范围大于0。 |
| height | number | 是 | 否 | 图片高度，单位为像素（px），取值范围大于0。 |

**Effect21+**

特效类型，继承自[SceneResource](#ZH-CN_TOPIC_0000002553202193__sceneresource-1)。由[createEffect](Scene.md#ZH-CN_TOPIC_0000002522082230__createeffect21)接口获得。

**属性**

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 特效打开状态。true表示开启特效，false表示关闭特效。 |
| effectId | string | 是 | 否 | 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，用于特效的创建，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'。 |

**getPropertyValue23+**

getPropertyValue(propertyName: string): Object | null | undefined

获取特定特效属性的值。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ArkUi.Graphics3D

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyName | string | 是 | 特定特效属性的名称。目前支持的字符串为： -'exposure':该属性表示图像的曝光度。 -'vibrance': 该属性表示图像的自然饱和度。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Object | null | undefined | 特效属性值，如果获取失败则返回null。 |

示例：

```ets
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function getEffectProperty() {
  let scene: Promise<Scene> = Scene.load();
  scene.then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
    let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
    let effect: Effect = await sceneFactory.createEffect(params);
    effect.getPropertyValue('exposure');
  });
}
```

**setPropertyValue23+**

setPropertyValue(propertyName: string, value: Object | undefined): boolean

设置特定特效属性的值。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ArkUi.Graphics3D

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyName | string | 是 | 特定特效属性的名称。目前支持的字符串为： -'exposure':该属性表示图像的曝光度。 -'vibrance': 该属性表示图像的自然饱和度。 |
| value | Object | undefined | 是 | 要设置的特效属性值。 -'exposure'：value实际类型为number，推荐取值范围[-5, 5]。取值越大，图像越亮。 -'vibrance'：value实际类型为number，推荐取值范围 [-1, 1]。取值越大，图像颜色越鲜艳。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置特效属性值操作是否成功。true表示设置成功，false表示设置失败。 |

示例：

```ets
import { SceneResourceFactory, Scene, Effect, EffectParameters } from '@kit.ArkGraphics3D';

function setEffectProperty() {
  let scene: Promise<Scene> = Scene.load();
  scene.then(async (result: Scene | undefined) => {
    if (!result) {
      return;
    }
    let sceneFactory: SceneResourceFactory = result.getResourceFactory();
    // 特效ID，固定格式为'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'，比如'e68a7f45-2d21-4a0d-9aef-7d9c825d3f12'
    let params: EffectParameters = {effectId: "e68a7f45-2d21-4a0d-9aef-7d9c825d3f12"};
    let effect: Effect = await sceneFactory.createEffect(params);
    effect.setPropertyValue('exposure', 1);
  });
}
```