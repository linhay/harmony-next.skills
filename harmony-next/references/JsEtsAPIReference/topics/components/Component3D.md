# Component3D

3D渲染组件，用于将ArkGraphics 3D场景或glTF（.gltf文件和.glb文件）模型渲染到ArkUI界面中，支持自定义场景模式与自动场景模式，并提供自定义渲染管线能力。


该组件从API Version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

Component3D(sceneOptions?: [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1)Options)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneOptions | [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1)Options | 否 | 3D场景配置选项。 说明： 3D场景配置选项在控件创建后不支持动态修改。 |

#### [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1)Options对象说明

Component3D组件配置选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | Scene | 否 | 是 | 3D模型资源文件或场景对象，默认值为undefined。 当传入glTF（.gltf文件和.glb文件）模型时，组件以自动场景模式运行，框架会自动创建基础相机、光源和默认手势交互（旋转、缩放），其相关参数由框架内部管理，不支持外部修改，开发者仅可通过Component3D的属性对展示效果进行配置。 当传入Scene对象时，组件以自定义场景模式运行，相机、光源及交互由开发者通过ArkGraphics 3D API自行创建和管理。 当不填写此参数时，组件仅作为自定义渲染管线（shader/customRender）的输出容器使用。 说明： 自定义场景模式下未内置相机控制器，因此不会自动响应拖拽或缩放手势；如需交互，请开发者接入手势并更新相机的位置与旋转。 |
| modelType | ModelType | 否 | 是 | 3D场景显示合成方式。 默认值：ModelType.SURFACE 说明： 设置为ModelType.TEXTURE时通过GPU合成显示。 设置为ModelType.SURFACE时通过专有硬件合成显示。 一般开发者可以使用默认值而无需关心此项设置。 |

#### ModelType枚举说明

渲染合成模式类型枚举，用于指定3D场景的渲染输出方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXTURE | 0 | 使用GPU合成显示3D场景。 |
| SURFACE | 1 | 使用专有硬件显示3D场景。 |

#### [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1)12+

type [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1) = Scene

设置3D场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 类型 | 说明 |
| --- | --- |
| [Scene](../graphics/Scene.md#ZH-CN_TOPIC_0000002529446039__scene-1) | 用于设置场景。 |

#### 属性

除支持[通用属性]([通用属性](../misc/通用属性.md).md)外，还支持以下属性：

#### environment

environment(uri: [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr))

设置3D环境资源。目前仅支持GLTF格式资源，模型资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 3D环境资源。 |

#### customRender

customRender(uri: [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr), selfRenderUpdate: boolean)

设置三维场景渲染的渲染管线。管线配置及自渲染属性在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 自定义渲染管线的配置文件。 |
| selfRenderUpdate | boolean | 是 | 当设置为true时外部UI没有更新时也能触发动效渲染。 当设置为false时只有外部UI更新才能触发渲染。 |

#### shader

shader(uri: [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr))

设置自定义渲染的shader文件资源。自定义渲染的shader文件资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 自定义渲染的shader文件资源。详细.shader文件格式请参考.shader资源文件格式要求。 |

#### shaderImageTexture

shaderImageTexture(uri: [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr))

设置自定义渲染用到的纹理资源。若自定义渲染用到多个纹理资源则调用多次，绑定点与调用顺序一致，不支持纹理更换。纹理资源在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | [ResourceStr](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) | 是 | 自定义渲染用到的纹理资源。 |

#### shaderInputBuffer

shaderInputBuffer(buffer: Array<number>)

设置自定义渲染用到的动效参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | Array<number> | 是 | 自定义渲染用到的动效参数，数组长度范围为[0, 1048576]。 |

#### renderWidth

renderWidth(value: [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10))

设置3D渲染分辨率的宽度。渲染分辨率的长宽可以不同于控件的长宽，若渲染分辨率与控件分辨率长宽不一致时会上采样或下采样到控件长宽。

不调用此属性时默认渲染分辨率。

渲染分辨率在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 是 | 3D渲染分辨率的宽度，当前仅支持设置Dimension.Percentage，取值范围是[0, 100%]。 |

#### renderHeight

renderHeight(value: [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10))

设置3D渲染分辨率的长度。渲染分辨率的长宽可以不同于控件的长宽，若渲染分辨率与控件分辨率长宽不一致时会上采样或下采样到控件长宽。

不调用此属性时默认渲染分辨率。

渲染分辨率在控件创建后不支持动态修改。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 是 | 3D渲染分辨率的长度，当前仅支持设置Dimension.Percentage，取值范围是[0, 100%]。 |

#### 事件

支持[通用事件]([通用事件](../misc/通用事件.md).md)。

#### 示例

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

GLTF模型加载示例。

```ets
// xxx.ets
@Entry
@Component
struct Index {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  scene: SceneOptions = { scene: $rawfile('gltf/DamagedHelmet/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};
  build() {
    Row() {
      Column() {
        Text('GLTF Example')
        Component3D( this.scene )
        // 绑定环境资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
          .environment($rawfile('gltf/Environment/glTF/Environment.gltf'))
          .renderWidth('90%').renderHeight('90%')
      }.width('100%')
    }
    .height('100%')
  }
```

自定义渲染示例。

```ets
import { AnimatorResult } from '@kit.ArkUI';

class EngineTime {
  totalTimeUs = 0;
  deltaTimeUs = 0;
};

let engineTime = new EngineTime();
let frameCount: number = 0;

function TickFrame() {
  if (frameCount == 10) {
    engineTime.totalTimeUs += 1.0;
    engineTime.deltaTimeUs += 1.0;
    frameCount = 0;
  } else {
    frameCount++;
}

@Entry
@Component
struct Index {
  // 加载场景资源，支持.gltf和.glb格式，路径和文件名可根据项目实际资源自定义
  scene: SceneOptions = { scene: $rawfile('gltf/DamagedHelmet/glTF/DamagedHelmet.gltf'), modelType: ModelType.SURFACE};
  backAnimator: AnimatorResult = this.getUIContext().createAnimator({
    duration: 2000,
    easing: "ease",
    delay: 0,
    fill: "none",
    direction: "normal",
    iterations: -1,
    begin: 100,
    end: 200,
  });
  @State timeDelta: number[] = [1.0, 2.0];
  create() {
    this.backAnimator.onFinish = () => {
      console.info('backAnimator onfinish');
    }
    this.backAnimator.onFrame = (value: number) => {
      TickFrame();
      this.timeDelta[0] = engineTime.deltaTimeUs;
    }

  }
  build() {
    Row() {
      Column() {
        Text('custom rendering')
        Component3D()
          // 绑定自定义shader脚本，路径和文件名可根据项目实际资源自定义
          .shader($rawfile('assets/app/shaders/shader/London.shader'))
          // 绑定贴图资源作为shader输入纹理，路径和文件名可根据项目实际资源自定义
          .shaderImageTexture($rawfile('assets/London.jpg'))
          .shaderInputBuffer(this.timeDelta)
          // 绑定自定义渲染流程文件（如.rng），路径和文件名可根据项目实际资源自定义
          .customRender($rawfile('assets/app/rendernodegraphs/London.rng'), true)
          .renderWidth('90%').renderHeight('90%')
          .onAppear(() => {
            this.create();
            this.backAnimator.play();
          }).width('50%').height('50%')
      }.width('100%')
    }
    .height('100%')
  }
```
