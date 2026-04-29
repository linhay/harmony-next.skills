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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'attachStateChange' | 是 | 注册监听事件的类型。取值为：'attachStateChange'。 |
| callback | Callback<AttachStateChangeInfo> | 是 | 回调函数，返回机械体设备连接变化信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码]([机械体控制模块错误码](../../errors/机械体控制模块错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'attachStateChange' | 是 | 取消注册监听事件的类型。取值为：'attachStateChange'。 |
| callback | Callback<AttachStateChangeInfo> | 否 | mechanicManager.off('attachStateChange')注册的回调函数。不填时默认取消所有注册的回调函数。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

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

| 类型 | 说明 |
| --- | --- |
| MechInfo[] | 已连接机械体设备的列表。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否启用摄像头跟踪， true表示启用摄像头跟踪，false表示禁用摄像头跟踪。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |
| 33300003 | Feature not supported. |

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

| 类型 | 说明 |
| --- | --- |
| boolean | 摄像头跟踪启用状态，true表示已启用，false表示已禁用。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'trackingStateChange' | 是 | 注册监听事件的类型。取值为：'trackingStateChange'。 |
| callback | Callback<TrackingEventInfo> | 是 | 回调函数，返回跟踪事件信息。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'trackingStateChange' | 是 | 取消注册的监听事件类型。取值为：'trackingStateChange'。 |
| callback | Callback<TrackingEventInfo> | 否 | mechanicManager.off('trackingStateChange')注册的回调函数。不填时默认取消所有注册的回调函数。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |

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

| 类型 | 说明 |
| --- | --- |
| CameraTrackingLayout | 获取到的当前机械体设备摄像头跟踪布局。 |

**错误码：**

以下的错误码的详细介绍请参见[机械体控制模块错误码](机械体控制模块错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

**示例：**

```ets
console.info('Query layout');
let layout = mechanicManager.getCameraTrackingLayout();
console.info(`'Query layout successful, current layout:' ${layout}`);
```

#### MechInfo

机械体设备信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mechId | number | 否 | 否 | 机械体设备ID。 |
| mechDeviceType | MechDeviceType | 否 | 否 | 机械体设备的类型。 |
| mechName | string | 否 | 否 | 机械体设备名称。 |

#### TrackingEventInfo

跟踪事件信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | TrackingEvent | 否 | 否 | 跟踪事件。 |

#### AttachStateChangeInfo

设备连接状态变化的信息。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | AttachState | 否 | 否 | 设备连接状态。 |
| mechInfo | MechInfo | 否 | 否 | 机械体设备信息。 |

#### TrackingEvent

跟踪事件的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA_TRACKING_USER_ENABLED | 0 | 用户启用了摄像头跟踪。 |
| CAMERA_TRACKING_USER_DISABLED | 1 | 用户禁用了摄像头跟踪。 |
| CAMERA_TRACKING_LAYOUT_CHANGED | 2 | 摄像头跟踪构图变更。 |

#### MechDeviceType

机械体设备类型的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GIMBAL_DEVICE | 0 | 便携式云台设备。 |

#### AttachState

设备连接状态的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTACHED | 0 | 设备已连接。 |
| DETACHED | 1 | 设备已断开。 |

#### CameraTrackingLayout

摄像头跟踪布局的枚举。

**系统能力**：SystemCapability.Mechanic.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 系统默认跟踪布局。 |
| LEFT | 1 | 靠左布局。 |
| MIDDLE | 2 | 居中布局。 |
| RIGHT | 3 | 靠右布局。 |