# arViewController（AR场景管理能力）

本模块提供AR Engine（AR引擎服务）的arViewController（AR场景管理能力）相关接口。

基础核心能力包括AR会话管理、空间对象管理与场景化管理。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

起始版本： 5.1.0(18)

**导入模块**

```ets
import { arEngine, arViewController } from '@kit.AREngine';
```

**LandmarkType**

人脸关键点类别。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT_EYE | 0 | 左眼。 |
| LEFT_SIDE_OF_MOUTH | 1 | 嘴巴左侧。 |
| RIGHT_EYE | 2 | 右眼。 |
| RIGHT_SIDE_OF_MOUTH | 3 | 嘴巴右侧。 |
| TIP_OF_NOSE | 4 | 鼻尖。 |
| CENTER_OF_FACE | 5 | 人脸中心。 |

**ARViewContext**

ARView上下文，用于AR场景管理，包括初始化、暂停、恢复及销毁。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

**ARViewContext.init**

init(): Promise<void>

初始化[ARViewContext](#ZH-CN_TOPIC_0000002522082116__arviewcontext)，初始化AR会话和设置AR渲染场景等。使用Promise异步回调。

需要权限： ohos.permission.CAMERA and ohos.permission.GYROSCOPE and ohos.permission.ACCELEROMETER

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中调用会返回801错误码，可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permissions not granted, such as the camera permission. |
| 801 | Device not compatible. |
| 1009200001 | Failure. |
| 1009200007 | Configuration not supported. |
| 1009200008 | Resource exhausted. |
| 1009200009 | Service unavailable. |
| 1009200010 | Camera unavailable. |
| 1009200201 | ARView invalid operation. |
| 1009200202 | Graphics3D AR scene required. |
| 1009200203 | AREngine config required. |
| 1009200204 | AR session setup failed. |
| 1009200205 | AR scene camera setup failed. |

示例：

```ets
import { arViewController } from '@kit.AREngine';
import { BusinessError } from '@kit.BasicServicesKit';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.init().then(() => {
  console.info('Initialization successful.');
}).catch((error: BusinessError) => {
  console.error(`Initialization failed. error code: ${error.code}`);
})
```

**ARViewContext.pause**

pause(): void

暂停相机跟踪与AR场景渲染。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

示例：

```ets
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.pause();
```

**ARViewContext.destroy**

destroy(): Promise<void>

销毁[ARViewContext](#ZH-CN_TOPIC_0000002522082116__arviewcontext)，释放ARView使用资源，包括AR会话与呈现场景销毁，在退出ARView时使用。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

示例：

```ets
import { arViewController } from '@kit.AREngine';
import { BusinessError } from '@kit.BasicServicesKit';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.destroy().then(() => {
  console.info('Destruction successful.');
}).catch((error: BusinessError) => {
  console.error(`Destruction failed. error code: ${error.code}`);
})
```

**ARViewContext.resume**

resume(): void

用于恢复暂停的相机跟踪与AR场景渲染。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |
| 1009200010 | Camera unavailable. |
| 1009200201 | ARView invalid operation. |
| 1009200204 | AR session setup failed. |

示例：

```ets
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.resume();
```

**ARViewContext.scene**

set scene(scene: Scene)

设置ARView的AR场景。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | Scene | 是 | AR呈现场景，用于管理空间节点。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

Scene.load().then((scene: Scene) => {
  let context: arViewController.ARViewContext = new arViewController.ARViewContext();
  context.scene = scene;
})
```

**ARViewContext.scene**

get scene(): Scene

获得的AR呈现场景，用于管理空间节点。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Scene | AR呈现场景，用于管理空间节点。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let scene: Scene = context.scene;
```

**ARViewContext.session**

get session(): arEngine.ARSession | undefined

获取AR会话，用于获取相关AR环境跟踪、相机跟踪、命中检测等能力，如相机位姿、平面信息、创建锚点等。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| arEngine.ARSession | undefined | 获得的AR会话内容，AR会话正常设置之后返回为arEngine.ARSession，异常设置或异常操作导致ARViewContext未初始化成功，返回undefined。 |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let arSession: arEngine.ARSession | undefined = context.session;
```

**ARViewContext.config**

set config(conf: arEngine.ARConfig)

设置AR会话的配置文件，如北向坐标、性能模式等。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| conf | arEngine.ARConfig | 是 | ARSession的功能配置参数。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.config = {
  type: arEngine.ARType.WORLD,
  poseMode: arEngine.ARPoseMode.GRAVITY_AND_HEADING,
  powerMode: arEngine.ARPowerMode.POWER_SAVING,
  depthMode: arEngine.ARDepthMode.AUTOMATIC
}
```

**ARViewContext.loadAsset**

loadAsset(resourcePath: ResourceStr, landmark: LandmarkType): Promise<void>

在指定的关键点处放置模型。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourcePath | ResourceStr | 是 | 存储模型的路径。 |
| landmark | LandmarkType | 是 | 指定想要放置模型的关键点。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
// 此处为用户本地存放模型路径
let resourcePath:ResourceStr = $rawfile('xxxx/xxxx');
context.loadAsset(resourcePath, arViewController.LandmarkType.LEFT_EYE);
```

**ARViewContext.removeAsset**

removeAsset(landmark: LandmarkType):Promise<void>

在指定的关键点移除已放置的模型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| landmark | LandmarkType | 是 | 指定想要移除模型的关键点。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.removeAsset(arViewController.LandmarkType.LEFT_EYE);
```

**ARViewContext.clearResource**

clearResource():Promise<void>

清除所有放置的模型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

示例：

```ets
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.clearResource();
```

**ARViewContext.setBlendShapeWeight**

setBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType, weight: number): boolean

设置指定Node里特定微表情的权重，用于渲染表情。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | Node | 是 | 新建锚点对应的AR场景节点。 说明： Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见AR Engine重力对齐世界坐标系与AGP世界坐标系。 |
| type | arEngine.ARBlendShapeType | 是 | 微表情类型。 |
| weight | number | 是 | 微表情权重，范围是0到1。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 微表情权重设置结果。true代表成功，false代表失败 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    ctx.setBlendShapeWeight(node, arEngine.ARBlendShapeType.EYE_BLINK_LEFT, 0.1);
  }
```

**ARViewContext.getBlendShapeWeight**

getBlendShapeWeight(node: Node, type: arEngine.ARBlendShapeType): number | null

获取指定Node里特定微表情的权重。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | Node | 是 | 新建锚点对应的AR场景节点。 说明： Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见AR Engine重力对齐世界坐标系与AGP世界坐标系。 |
| type | arEngine.ARBlendShapeType | 是 | 微表情类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | null | 当前微表情的权重，若传入的node或type有误，则返回null。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    ctx.getBlendShapeWeight(node, arEngine.ARBlendShapeType.EYE_BLINK_LEFT);
  }
```

**ARViewContext.transformPose**

transformPose(position: Vec3, rotation: Quaternion): arEngine.ARPose | null

将位姿信息从AR坐标系转换为AGP渲染引擎坐标系。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | Vec3 | 是 | 位姿坐标信息 |
| rotation | Quaternion | 是 | 位姿朝向信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| arEngine.ARPose | null | 转换后的位姿信息，若传入参数无效或创建ARPose对象失败则返回null。 |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Vec3, Quaternion } from '@kit.ArkGraphics3D';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let pose: Vec3 =  {x: 1.0, y: -1.0, z: -0.5};
let rot: Quaternion =  {x: -0.1, y: 0.2, z: -0.3, w: 0.5};
let agpPose: arEngine.ARPose | null = context.transformPose(pose, rot);
```

**ARViewContext.callback**

set callback(callback: ARViewCallback);

回调函数，可根据回调功能实现对应业务逻辑。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ARViewCallback | 是 | ARViewCallback抽象类，声明ARView的回调接口。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200201 | ARView invalid operation. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

class ARViewCallbackImpl extends arViewController.ARViewCallback {

  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    console.info('onAnchorAdd');
    console.info(`add anchor id = ${String(anchor.id)}`);
    console.info(`add anchor translation = ${anchor.getPose().translation}`);
    console.info(`add node pose = ${node.position}`);
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    console.info('onAnchorUpdate');
    console.info(`update anchor id = ${String(anchor.id)}`);
    console.info(`update anchor translation = ${anchor.getPose().translation}`);
    console.info(`update node pose = ${node.position}`);
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    let arSession: arEngine.ARSession | undefined = ctx.session;
    if (arSession) {
      let frame: arEngine.ARFrame = arSession.getFrame();
      if (!frame) {
        console.error('Failed to get arSession.frame, it is undefined or null');
      } else {
        console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
        await frame.release();
      }
    } else {
      console.error('Failed to get arSession, arSession is undefined');
    }

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.callback = new ARViewCallbackImpl();
```

**ARViewCallback**

ARViewCallback抽象类，声明ARView的回调接口。

开发者需继承此类并且根据业务逻辑实现回调子类。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

**ARViewCallback.onAnchorAdd**

abstract onAnchorAdd(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

当AR会话检测到新平面时，平面自动创建锚点以及对应的场景节点，并在帧刷新逻辑中自动触发此回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | ARViewContext | 是 | 当前ARView的上下文信息（ARViewContext）。 |
| node | Node | 是 | 新建锚点对应的AR场景节点。 说明： Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见AR Engine重力对齐世界坐标系与AGP世界坐标系。 |
| anchor | arEngine.ARAnchor | 是 | 新平面对应的新创建的锚点。 说明： ARAnchor的位姿使用了AR Engine重力对齐世界坐标系。具体参见AR Engine重力对齐世界坐标系。 |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // 其他操作
}
```

**ARViewCallback.onAnchorUpdate**

abstract onAnchorUpdate(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

更新AR会话中的锚点时，ARView自动检测该锚点对应的场景节点，并调用该回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | ARViewContext | 是 | 当前ARView的上下文信息（ARViewContext）。 |
| node | Node | 是 | 新建锚点对应的AR场景节点。 说明： Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见AR Engine重力对齐世界坐标系与AGP世界坐标系。 |
| anchor | arEngine.ARAnchor | 是 | 更新锚点。 说明： ARAnchor的位姿使用了AR Engine重力对齐世界坐标系。具体参见AR Engine重力对齐世界坐标系。 |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // 其他操作
}
```

**ARViewCallback.onFrameUpdate**

abstract onFrameUpdate(ctx: ARViewContext, sysBootTs: number): void

AR场景每帧刷新前会自动触发该回调，开发者可以基于此回调进行AR实体摆放位姿调整、动画调整以及相机位姿调整等。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[arViewController.isARTypeSupported](arViewController（AR场景管理能力）.md#ZH-CN_TOPIC_0000002522082116__arviewcontrollerisartypesupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | ARViewContext | 是 | 当前ARView的上下文信息。 |
| sysBootTs | number | 是 | 时间戳，单位为us。 |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
  let arSession: arEngine.ARSession | undefined = ctx.session;
  if (arSession) {
    let frame: arEngine.ARFrame = arSession.getFrame();
    if (!frame){
      console.error('Failed to get arSession.frame, it is undefined or null');
    } else {
      console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
      await frame.release();
    }
  } else {
    console.error('Failed to get arSession, arSession is undefined');
  }
```

**arViewController.isARTypeSupported**

isARTypeSupported(type: arEngine.ARFeatureType): boolean

在ARViewController中调用此接口来判断AR特性是否支持在当前设备上运行。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AREngine.Core

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | ARFeatureType | 是 | 表示想要检查能否正常运行的AR特性。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | AR特性检查结果。true表示该设备支持，false则表示该设备不支持。 |

错误码：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009200001 | Failure. |

示例：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
```