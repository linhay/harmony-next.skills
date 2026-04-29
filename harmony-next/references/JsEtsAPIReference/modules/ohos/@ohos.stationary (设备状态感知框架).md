# @ohos.stationary (设备状态感知框架)

设备状态感知框架提供设备状态感知能力，包括绝对静止和相对静止。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块不支持x86模拟器。

#### 导入模块

```ets
import { stationary } from '@kit.MultimodalAwarenessKit';
```

#### ActivityResponse

服务响应抽象接口。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | ActivityState | 否 | 否 | 设备状态变化返回值。 |

#### ActivityType

type ActivityType = 'still' | 'relativeStill'

设备状态类型。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 类型 | 说明 |
| --- | --- |
| 'still' | 绝对静止。 |
| 'relativeStill' | 相对静止。 |

#### ActivityEvent

设备状态事件。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 进入。 |
| EXIT | 2 | 退出。 |
| ENTER_EXIT | 3 | 进入和退出。 |

#### ActivityState

设备状态返回值。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTER | 1 | 进入。 |
| EXIT | 2 | 退出。 |

#### stationary.on('still' | 'relativeStill')

on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void

设备状态管理，订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | ActivityType | 是 | 设备状态能力类型。 |
| event | ActivityEvent | 是 | 事件类型。 |
| reportLatencyNs | number | 是 | 报告延时(取值范围1000000000-3000000000)。 |
| callback | Callback<ActivityResponse> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```ets
let reportLatencyNs = 1000000000;
stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

#### stationary.once('still' | 'relativeStill')

once(activity: ActivityType, callback: Callback<ActivityResponse>): void

设备状态管理，查询设备状态。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | ActivityType | 是 | 设备状态能力类型。 |
| callback | Callback<ActivityResponse> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```ets
stationary.once('still', (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

#### stationary.off('still' | 'relativeStill')

off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void

设备状态管理，取消订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| activity | ActivityType | 是 | 设备状态能力类型。 |
| event | ActivityEvent | 是 | 事件类型。 |
| callback | Callback<ActivityResponse> | 否 | 回调函数，接收上报状态变化事件，如果没有传递callback参数或者传递的类型是undefined，会移除该进程下订阅该类型的所有callback。 |

**示例：**

```ets
stationary.off('still', stationary.ActivityEvent.ENTER);
```