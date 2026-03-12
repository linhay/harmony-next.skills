# arViewController（AR场景管理能力）

本模块提供AR Engine（AR引擎服务）的arViewController（AR场景管理能力）相关接口。

基础核心能力包括AR会话管理、空间对象管理与场景化管理。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { arEngine, arViewController } from '@kit.AREngine';
```

#### ARViewContext

ARView上下文，用于AR场景管理，包括初始化、暂停、恢复及销毁。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### ARViewContext.init

init(): Promise<void>

初始化[ARViewContext](#section12681656121519)，初始化AR会话和设置AR渲染场景等。

使用Promise异步回调。

**需要权限：**ohos.permission.CAMERA and ohos.permission.GYROSCOPE and ohos.permission.ACCELEROMETER

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](zh-cn_topic_0000002500306238.md)。

错误码ID

错误信息

201

Permissions not granted, such as the camera permission.

801

Device not compatible.

1009200001

Failure.

1009200007

Configuration not supported.

1009200008

Resource exhausted.

1009200009

Service unavailable.

1009200010

Camera unavailable.

1009200201

ARView invalid operation.

1009200202

Graphics3D AR scene required.

1009200203

AREngine config required.

1009200204

AR session setup failed.

1009200205

AR scene camera setup failed.

**示例**：

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

#### ARViewContext.pause

pause(): void

暂停相机跟踪与AR场景渲染。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

1009200201

ARView invalid operation.

1009200204

AR session setup failed.

**示例**：

```ets
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.pause();
```

#### ARViewContext.destroy

destroy(): Promise<void>

销毁[ARViewContext](#section12681656121519)，释放ARView使用资源，包括AR会话与呈现场景销毁，在退出ARView时使用。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

1009200201

ARView invalid operation.

1009200204

AR session setup failed.

**示例**：

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

#### ARViewContext.resume

resume(): void

用于恢复暂停的相机跟踪与AR场景渲染。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

1009200010

Camera unavailable.

1009200201

ARView invalid operation.

1009200204

AR session setup failed.

**示例**：

```ets
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.resume();
```

#### ARViewContext.scene

set scene(scene: Scene)

设置ARView的AR场景。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

参数名

类型

必填

说明

scene

[Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene#scene-1)

是

AR呈现场景，用于管理空间节点。

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200201

ARView invalid operation.

**示例**：

```ets
import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

Scene.load().then(async (scene: Scene) => {
  let context: arViewController.ARViewContext = new arViewController.ARViewContext();
  context.scene = scene;
})
```

#### ARViewContext.scene

get scene(): Scene

获得的AR呈现场景，用于管理空间节点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值**:

类型

说明

[Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene#scene-1)

AR呈现场景，用于管理空间节点。

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200201

ARView invalid operation.

**示例**：

```ets
import { Scene } from '@kit.ArkGraphics3D';
import { arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let scene: Scene = context.scene;
```

#### ARViewContext.session

get session(): arEngine.ARSession | undefined

获取AR会话，用于获取相关AR环境跟踪、相机跟踪、命中检测等能力，如相机位姿、平面信息、创建锚点等。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值**:

类型

说明

[arEngine](arEngine（AR增强现实能力）.md).[ARSession](arEngine（AR增强现实能力）.md#section19193165314510) | undefined

获得的AR会话内容，AR会话正常设置之后返回为arEngine.ARSession，异常设置或异常操作导致ARViewContext未初始化成功，返回undefined。

**示例**：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
let arSession: arEngine.ARSession | undefined = context.session;
```

#### ARViewContext.config

set config(conf: arEngine.ARConfig)

设置AR会话的配置文件，如北向坐标、性能模式等。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

参数名

类型

必填

说明

conf

[arEngine](arEngine（AR增强现实能力）.md).[ARConfig](arEngine（AR增强现实能力）.md#section1262116345111)

是

[ARSession](arEngine（AR增强现实能力）.md#section19193165314510)的功能配置参数。

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200201

ARView invalid operation.

**示例**：

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

#### ARViewContext.callback

set callback(callback: ARViewCallback);

回调函数，可根据回调功能实现对应业务逻辑。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

参数名

类型

必填

说明

callback

[ARViewCallback](#section9396615174614)

是

ARViewCallback抽象类，声明ARView的回调接口。

**错误码**：

以下错误码的详细介绍请参见[AR Engine错误码](AR Engine错误码.md)。

错误码ID

错误信息

1009200201

ARView invalid operation.

**示例**：

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

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    let arSession: arEngine.ARSession | undefined = ctx.session;
    if (arSession) {
      let frame = arSession.getFrame();
      if (!frame) {
        console.error('Failed to get arSession.frame, it is undefined or null');
      } else {
        console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
        frame.release();
      }
    } else {
      console.error('Failed to get arSession, arSession is undefined');
    }
  }
}

let context: arViewController.ARViewContext = new arViewController.ARViewContext();
context.callback = new ARViewCallbackImpl();
```

#### ARViewCallback

ARViewCallback抽象类，声明ARView的回调接口。

开发者需继承此类并且根据业务逻辑实现回调子类。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### ARViewCallback.onAnchorAdd

abstract onAnchorAdd(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

当AR会话检测到新平面时，平面自动创建锚点以及对应的场景节点，并在帧刷新逻辑中自动触发此回调函数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

参数名

类型

必填

说明

ctx

[ARViewContext](#section12681656121519)

是

当前ARView的上下文信息（ARViewContext）。

node

[Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)

是

新建锚点对应的AR场景节点。

 注意：

Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)与[AGP世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section7594451483)。

anchor

[arEngine](arEngine（AR增强现实能力）.md).[ARAnchor](arEngine（AR增强现实能力）.md#section106411242143016)

是

新平面对应的新创建的锚点。

 注意：

[ARAnchor](arEngine（AR增强现实能力）.md#section106411242143016)的位姿使用了AR Engine重力对齐世界坐标系。具体参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)。

**示例**：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // 其他操作
}
```

#### ARViewCallback.onAnchorUpdate

abstract onAnchorUpdate(ctx: ARViewContext, node: Node, anchor: arEngine.ARAnchor): void

更新AR会话中的锚点时，ARView自动检测该锚点对应的场景节点，并调用该回调函数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

参数名

类型

必填

说明

ctx

[ARViewContext](#section12681656121519)

是

当前ARView的上下文信息（ARViewContext）。

node

[Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#node)

是

新建锚点对应的AR场景节点。

 注意：

Node属于AGP（Ark Graphics Platform）渲染引擎能力，使用了AGP齐世界坐标系，与AR Engine所使用的的重力对齐世界坐标系不一致，与anchor参数一同使用时需注意区分。具体参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)与[AGP世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section7594451483)。

anchor

[arEngine](arEngine（AR增强现实能力）.md).[ARAnchor](arEngine（AR增强现实能力）.md#section106411242143016)

是

更新锚点。

 注意：

[ARAnchor](arEngine（AR增强现实能力）.md#section106411242143016)的位姿使用了AR Engine重力对齐世界坐标系。具体参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)。

**示例**：

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  // 其他操作
}
```

#### ARViewCallback.onFrameUpdate

abstract onFrameUpdate(ctx: ARViewContext, sysBootTs: number): void

AR场景每帧刷新前会自动触发该回调，开发者可以基于此回调进行AR实体摆放位姿调整、动画调整以及相机位姿调整等。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

ctx

[ARViewContext](#section12681656121519)

是

当前ARView的上下文信息。

sysBootTs

number

是

时间戳，单位为us。

**示例**：

```ets
import { arEngine, arViewController } from '@kit.AREngine';

// 参考ARViewContext.callback接口示例代码创建callback类再实现该接口
onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
  let arSession: arEngine.ARSession | undefined = ctx.session;
  if (arSession) {
    let frame = arSession.getFrame();
    if (!frame){
      console.error('Failed to get arSession.frame, it is undefined or null');
    } else {
      console.info(`Succeeded in getting arSession.frame = ${frame.timestamp}`);
      frame.release();
    }
  } else {
    console.error('Failed to get arSession, arSession is undefined');
  }
}
```