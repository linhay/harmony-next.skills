# @ohos.distributedHardware.mechanicManager (机械体控制模块)

本模块提供与机械体设备交互的能力，包括设备连接状态监听、跟踪控制和跟踪状态监听功能。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { mechanicManager } from '@kit.MechanicKit';
```

#### mechanicManager.on('attachStateChange')

on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void

注册连接状态变化事件的回调监听，等待连接状态变化。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

参数名类型必填说明type'attachStateChange'是注册监听事件的类型。取值为：'attachStateChange'。callbackCallback<[AttachStateChangeInfo](#ZH-CN_TOPIC_0000002497605654__attachstatechangeinfo)>是回调函数，返回机械体设备连接变化信息。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.

**示例：**

```ets
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Register');
mechanicManager.on("attachStateChange", callback);
console.info('Register: success');
```

#### mechanicManager.off('attachStateChange')

off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void

取消注册连接状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

参数名类型必填说明type'attachStateChange'是取消注册监听事件的类型。取值为：'attachStateChange'。callbackCallback<[AttachStateChangeInfo](#ZH-CN_TOPIC_0000002497605654__attachstatechangeinfo)>否mechanicManager.off('attachStateChange')注册的回调函数。不填时默认取消所有注册的回调函数。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.

**示例：**

```ets
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
mechanicManager.off("attachStateChange", callback);
console.info('Unregister: success');
```

#### mechanicManager.getAttachedMechDevices

getAttachedMechDevices(): MechInfo[]

获取已连接的机械体设备列表。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

类型说明[MechInfo](#ZH-CN_TOPIC_0000002497605654__mechinfo)[]已连接机械体设备的列表。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.

**示例：**

```ets
console.info('Query device list');
let mechanicInfos = mechanicManager.getAttachedMechDevices();
console.info(`'device list:' ${mechanicInfos}`);
```

#### mechanicManager.setCameraTrackingEnabled

setCameraTrackingEnabled(isEnabled: boolean): void

启用或禁用当前机械体设备摄像头跟踪。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

参数名类型必填说明isEnabledboolean是是否启用摄像头跟踪， true表示启用摄像头跟踪，false表示禁用摄像头跟踪。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.33300002Device not connected.33300003Feature not supported.

**示例：**

```ets
console.info('Enable tracing');
mechanicManager.setCameraTrackingEnabled(true);
console.info('Enable Tracking Success');
```

#### mechanicManager.getCameraTrackingEnabled

getCameraTrackingEnabled(): boolean

检查当前机械体设备是否启用了摄像头跟踪。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

类型说明boolean摄像头跟踪启用状态，true表示已启用，false表示已禁用。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.33300002Device not connected.

**示例：**

```ets
console.info('Get tracking status');
let enabled = mechanicManager.getCameraTrackingEnabled();
console.info(`'current tracking status:' ${enabled}`);
```

#### mechanicManager.on('trackingStateChange')

on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void

注册跟踪状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

参数名类型必填说明type'trackingStateChange'是注册监听事件的类型。取值为：'trackingStateChange'。callbackCallback<[TrackingEventInfo](#ZH-CN_TOPIC_0000002497605654__trackingeventinfo)>是回调函数，返回跟踪事件信息。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.

**示例：**

```ets
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Register');
mechanicManager.on("trackingStateChange", callback);
console.info('Register: success');
```

#### mechanicManager.off('trackingStateChange')

off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void

取消注册跟踪状态变化事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.Mechanic.Core

**参数：**

参数名类型必填说明type'trackingStateChange'是取消注册的监听事件类型。取值为：'trackingStateChange'。callbackCallback<[TrackingEventInfo](#ZH-CN_TOPIC_0000002497605654__trackingeventinfo)>否mechanicManager.off('trackingStateChange')注册的回调函数。不填时默认取消所有注册的回调函数。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.

**示例：**

```ets
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
mechanicManager.off("trackingStateChange", callback);
console.info('Unregister: success');
```

#### mechanicManager.getCameraTrackingLayout

getCameraTrackingLayout(): CameraTrackingLayout

获取当前机械体设备摄像头跟踪布局。

**系统能力**：SystemCapability.Mechanic.Core

**返回值：**

类型说明[CameraTrackingLayout](#ZH-CN_TOPIC_0000002497605654__cameratrackinglayout)获取到的当前机械体设备摄像头跟踪布局。

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](../../errors/机械体控制模块错误码.md)。

错误码ID错误信息33300001Service exception.33300002Device not connected.

**示例：**

```ets
console.info('Query layout');
let layout = mechanicManager.getCameraTrackingLayout();
console.info(`'Query layout successful, current layout:' ${layout}`);
```

#### MechInfo

机械体设备信息。

**系统能力**：SystemCapability.Mechanic.Core

名称类型只读可选说明mechIdnumber否否机械体设备ID。mechDeviceType[MechDeviceType](#ZH-CN_TOPIC_0000002497605654__mechdevicetype)否否机械体设备的类型。mechNamestring否否机械体设备名称。

#### TrackingEventInfo

跟踪事件信息。

**系统能力**：SystemCapability.Mechanic.Core

名称类型只读可选说明event[TrackingEvent](#ZH-CN_TOPIC_0000002497605654__trackingevent)否否跟踪事件。

#### AttachStateChangeInfo

设备连接状态变化的信息。

**系统能力**：SystemCapability.Mechanic.Core

名称类型只读可选说明state[AttachState](#ZH-CN_TOPIC_0000002497605654__attachstate)否否设备连接状态。mechInfo[MechInfo](#ZH-CN_TOPIC_0000002497605654__mechinfo)否否机械体设备信息。

#### TrackingEvent

跟踪事件的枚举。

**系统能力**：SystemCapability.Mechanic.Core

名称值说明CAMERA_TRACKING_USER_ENABLED0用户启用了摄像头跟踪。CAMERA_TRACKING_USER_DISABLED1用户禁用了摄像头跟踪。CAMERA_TRACKING_LAYOUT_CHANGED2摄像头跟踪构图变更。

#### MechDeviceType

机械体设备类型的枚举。

**系统能力**：SystemCapability.Mechanic.Core

名称值说明GIMBAL_DEVICE0便携式云台设备。

#### AttachState

设备连接状态的枚举。

**系统能力**：SystemCapability.Mechanic.Core

名称值说明ATTACHED0设备已连接。DETACHED1设备已断开。

#### CameraTrackingLayout

摄像头跟踪布局的枚举。

**系统能力**：SystemCapability.Mechanic.Core

名称值说明DEFAULT0系统默认跟踪布局。LEFT1靠左布局。MIDDLE2居中布局。RIGHT3靠右布局。