# smartMobilityCommon（智慧出行场景）

作为分布式业务公共功能提供给应用，实现监听分布式业务（HiCar、超级桌面等）的状态，以及事件监听的能力。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { smartMobilityCommon } from '@kit.CarKit';
```

#### SmartMobilityEvent

公共事件。

**系统能力：**SystemCapability.CarService.DistributedEngine

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

eventName

string

否

否

事件名，由业务方自定义。

type

[SmartMobilityType](#section12883193118184)

否

否

业务类型。

data

Record<string, Object>

否

否

事件详细信息，内容由智慧出行业务和应用双方约定。

#### SmartMobilityInfo

该类为智慧出行的状态信息，定义了当前的业务类型、连接状态、业务数据。

**系统能力：**SystemCapability.CarService.DistributedEngine

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

status

[SmartMobilityStatus](#section66501518181418)

否

否

业务连接状态。

type

[SmartMobilityType](#section12883193118184)

否

否

业务类型。

data

Record<string, Object>

否

否

连接详细信息，内容由智慧出行业务和应用双方约定。

#### SmartMobilityStatus

业务连接状态枚举值。

**系统能力：**SystemCapability.CarService.DistributedEngine

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

IDLE

0

业务处于空闲态，业务未启动时，默认为该值。

RUNNING

1

业务处于运行中。

#### SmartMobilityType

业务类型枚举值。

**系统能力：**SystemCapability.CarService.DistributedEngine

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

HICAR

0

HiCar。

SUPER_LAUNCHER

1

超级桌面。

CAR_HOP

2

流转。

#### getSmartMobilityAwareness

getSmartMobilityAwareness(): SmartMobilityAwareness

用于获取智慧出行管理类。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

[SmartMobilityAwareness](#section1135959103019)

智慧出行管理类。

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';

let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
```

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

801

Capability not supported.

#### SmartMobilityAwareness

智慧出行管理类，用于调用智慧出行接口。

**系统能力：**SystemCapability.CarService.DistributedEngine

**起始版本：**5.0.0(12)

#### on('smartMobilityEvent')

on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[],callback: Callback<SmartMobilityEvent>): void

注册智慧出行业务的事件监听，例如导航流转完成后通知事件时，触发此回调执行。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

订阅类型，该位置为常量值：

'smartMobilityEvent'，表示订阅事件监听。

smartMobilityTypes

[SmartMobilityType](#section12883193118184)[]

是

业务类型数组，支持同时订阅多个业务。

callback

Callback<[SmartMobilityEvent](#section8760828151111)>

是

出行业务事件回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
  // 出行业务事件回调函数
  const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
  };
  // 注册出行业务事件监听
  awareness.on('smartMobilityEvent', types, callBack);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `on smart mobility event error, error code: ${e?.code}`);
}
```

#### off('smartMobilityEvent')

off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void

取消注册智慧出行业务的事件监听。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

订阅类型，该位置为常量值：

'smartMobilityEvent'，表示取消事件监听。

smartMobilityTypes

[SmartMobilityType](#section12883193118184)[]

是

业务类型数组，支持同时取消多个业务监听。

callback

Callback<[SmartMobilityEvent](#section8760828151111)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
  // 出行业务事件回调函数
  const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
  };

  // 解注册出行业务事件监听
  awareness.off('smartMobilityEvent', types, callBack);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `off smart mobility event error, error code: ${e?.code}`);
}
```

#### getSmartMobilityEvent

getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent

应用获取指定事件的信息。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

[SmartMobilityType](#section12883193118184)

是

业务类型。

eventName

string

是

事件名。取值有下面3种：

CAR_HOP_EVENT，流转事件。

HICAR_EVENT，HiCar事件。

SUPER_LAUNCHER_EVENT，超级桌面事件。

**返回值：**

类型

说明

[SmartMobilityEvent](#section8760828151111)

公共事件信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let type = smartMobilityCommon.SmartMobilityType.CAR_HOP;
  // 事件名称
  let eventName: string = 'CAR_HOP_EVENT';
  // 获取公共事件信息
  let event: smartMobilityCommon.SmartMobilityEvent = awareness.getSmartMobilityEvent(type, eventName);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `get smart mobility event error, error code: ${e?.code}`);
}
```

#### on('smartMobilityStatus')

on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void

注册智慧出行连接状态的监听。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

订阅类型，该位置为常量值：

'smartMobilityStatus'，表示订阅业务连接状态监听。

smartMobilityTypes

[SmartMobilityType](#section12883193118184)[]

是

业务类型数组，支持同时订阅多个业务。

callback

Callback<[SmartMobilityInfo](#section153711644737)>

是

出行连接状态回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
  // 出行连接状态回调函数
  const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
  };
  // 注册智慧出行连接状态的监听
  awareness.on('smartMobilityStatus', types, callBack);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `on smart mobility status error, error code: ${e?.code}`);
}
```

#### off('smartMobilityStatus')

off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void

取消注册智慧出行连接状态的监听。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

string

是

订阅类型，该位置为常量值：

'smartMobilityStatus'，表示取消业务连接状态监听。

smartMobilityTypes

[SmartMobilityType](#section12883193118184)[]

是

业务类型数组，支持同时取消多个业务监听。

callback

Callback<[SmartMobilityInfo](#section153711644737)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Get single instance of SmartMobilityAwareness.
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
  // 出行连接状态回调函数
  const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
  };
  // 取消注册智慧出行连接状态的监听
  awareness.off('smartMobilityStatus', types);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `off smart mobility status error, error code: ${e?.code}`);
}
```

#### getSmartMobilityStatus

getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo

获取智慧出行连接状态。

**系统能力：**SystemCapability.CarService.DistributedEngine

**设备行为差异**：该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**需要权限：**ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

type

[SmartMobilityType](#section12883193118184)

是

业务类型。

**返回值：**

类型

说明

[SmartMobilityInfo](#section153711644737)

业务状态信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified;

2. Incorrect parameter type;

3. Parameter verification failed;

4. The size of specified type is greater than 255.

801

Capability not supported.

**示例：**

```ets
import { smartMobilityCommon } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let type = smartMobilityCommon.SmartMobilityType.HICAR;
  // 获取业务状态信息
  let ret = awareness.getSmartMobilityStatus(type);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `get smart mobility status error, error code: ${e?.code}`);
}
```