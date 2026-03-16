# gamePerformance (游戏场景感知)

本模块提供接入Game Service Kit的游戏场景感知能力。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { gamePerformance } from '@kit.GameServiceKit';
```

#### DeviceInfo

设备信息类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

tempLevel

number

否

否

温控档位，档位越高表示温度越高。不同档位及其建议如下：

- 1：无需处理。
- 2：建议降低无感知业务规格，例如后台更新降速或延迟运行。
- 3：建议暂停无感知业务，降低游戏非核心业务的规格，例如前台更新降速。
- 4：建议减少游戏特效，降低分辨率，画质。
- 5：建议降低全场景规格，进一步降低分辨率、画质等。
- 6：建议游戏降至最低规格。

gpuInfo

[GpuInfo](#section12288563197)

否

是

GPU性能信息。

thermalInfo

[ThermalInfo](#section55661711201613)

否

是

温度变化趋势数据。

**起始版本：**5.0.1(13)。

#### GpuInfo

GPU性能信息类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

gpuLoadLevel

number

否

是

GPU负载整体等级。10个等级，负载程度从1到10递增。

vertexLoadLevel

number

否

是

顶点处理负载等级。10个等级，负载程度从1到10递增。

fragmentLoadLevel

number

否

是

片元处理负载等级。10个等级，负载程度从1到10递增。

textureLoadLevel

number

否

是

纹理处理负载等级。10个等级，负载程度从1到10递增。

bandwidthLoadLevel

number

否

是

带宽负载等级。10个等级，负载程度从1到10递增。

currentFrequency

number

否

是

GPU当前频点，单位：KHz。

**起始版本：**5.0.2(14)。

#### ThermalInfo

温度变化趋势数据类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**名称**

**类型**

只读

可选

**说明**

thermalMargin

number

否

是

时间裕量，温控到达指定档位的时间，单位：秒（s）。

 说明：

- 该数值超过60时，可信度降低。
- 0：已达到查询的温控档位。
- -1：表示不能到达。
- -2：查询的档位低于当前档位。

thermalTrend

number

否

是

温升趋势，取值范围为[-100,100]，负号代表降温，数值越大说明当前温度变化越快。

#### BaseGameInfo

游戏基本信息类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

messageType

number

否

否

信息类型。

- 0：标识一个游戏包体消息，对应[GamePackageInfo](#section3844175954711)。
- 1：标识一个游戏设置消息，对应[GameConfigInfo](#section10841101134814)。
- 2：标识一个游戏场景消息，对应[GameSceneInfo](#section1535311105717)。
- 3：标识一个游戏网络状态消息，对应[GameNetInfo](#section138783245711)。
- 4：标识一个游戏玩家信息，对应[GamePlayerInfo](#section2401441273)。

extra

string

否

是

扩展参数，JSON字符串，用于传递游戏拓展信息，字符长度范围：[0, 128]。

#### GamePackageInfo

游戏包信息类，继承[BaseGameInfo](#section116223815415)。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bundleName

string

否

否

游戏包名。字符长度范围：[1, 128]。

appVersion

string

否

否

游戏版本号。字符长度范围：[1, 64]。

engineType

number

否

是

游戏引擎类型。

- 1：UNITY
- 2：UNREAL4
- 3：MESSIAH
- 4：COCOS
- 200：OTHERS

engineVersion

string

否

是

游戏引擎版本号。字符长度范围：[0, 64]。

gameType

number

否

是

游戏类型。

- 1：MOBA（多人在线战术竞技）
- 2：RPG（角色扮演）
- 3：FPS（第一人称射击类）
- 4：FTG（格斗游戏）
- 5：RAC（竞速游戏）
- 200：OTHERS（其他）

vulkanSupported

boolean

否

是

是否支持Vulkan。

- true：支持
- false：不支持

默认为false。

#### GameConfigInfo

游戏配置信息类，继承[BaseGameInfo](#section116223815415)。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

maxPictureQualityLevel

number

否

否

支持的画质最高等级。

- 1：流畅
- 2：均衡
- 3：高清
- 4：HDR高清
- 5：超高清

currentPictureQualityLevel

number

否

否

画质的当前等级。

- 1：流畅
- 2：均衡
- 3：高清
- 4：HDR高清
- 5：超高清

maxFrameRate

number

否

否

支持的最高帧率。

currentFrameRate

number

否

否

当前设置的帧率。取值范围为[1, 144]。

maxResolution

string

否

否

支持的最高分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。

currentResolution

string

否

否

当前设置的分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。

antiAliasing

boolean

否

否

是否开启抗锯齿。

- true：开启
- false：不开启

默认为false。

shadow

boolean

否

否

当前是否开启阴影。

- true：开启
- false：不开启

默认为false。

multithreading

boolean

否

否

是否开启多线程。

- true：开启
- false：不开启

默认为false。

particle

boolean

否

否

是否开启粒子效果。

- true：开启
- false：不开启

默认为false。

hdMode

boolean

否

否

是否开启高清模式。

- true：开启
- false：不开启

默认为false。

#### GameSceneInfo

游戏场景信息类，继承[BaseGameInfo](#section116223815415)。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

sceneID

number

否

否

游戏场景ID。

- 0：回切场景标识结束
- 1：游戏启动
- 2：游戏内更新
- 3：登录过程
- 4：主界面
- 5：加载一局游戏（自己加载）
- 6：加载一局游戏（自己加载完毕，等待其他玩家）
- 7：游戏中
- 8：观战模式

（游戏特殊场景编码：从100开始自定义）

 说明：

游戏自定义场景推荐使用subSceneID传入。

description

string

否

是

游戏场景描述（自定义描述）。字符长度范围：[0, 128]。

subSceneID

number

否

是

游戏子场景ID（自定义）。

subDescription

string

否

是

游戏子场景描述（自定义描述）。字符长度范围：[0, 128]。

importanceLevel

number

否

否

游戏场景重要程度，5个等级，重要程度从1到5递增。

sceneFrequency

number

否

是

该场景在一局游戏中出现的次数。

sceneTime

number

否

是

该场景持续的时间，单位：毫秒（ms）。

recommendedCpuLevel

number

否

是

游戏推荐的该场景下的CPU等级。

- 1：Low（低）
- 2：Middle（中）
- 3：High（高）

recommendedGpuLevel

number

否

是

游戏推荐的该场景下的GPU等级。

- 1：Low（低）
- 2：Middle（中）
- 3：High（高）

recommendedDdrLevel

number

否

是

游戏推荐的该场景下的DDR等级。

- 1：Low（低）
- 2：Middle（中）
- 3：High（高）

recommendedFps

number

否

是

游戏推荐的该场景下的目标帧率。

maxFps

number

否

是

该场景的最大帧率。

currentFps

number

否

是

该场景的当前帧率。

keyThread

string

否

是

该场景下的关键线程。

- render：渲染线程
- logic：逻辑线程
- net：网络线程

按照 render|xxx|logic|xxx 格式传入。字符长度范围：[0, 32]。

drawCallCount

number

否

是

该场景下每帧的平均Drawcall数。

vertexCount

number

否

是

该场景下每帧的平均模型顶点数。

triangleCount

number

否

是

该场景下每帧的平均模型三角形数。

shaderCount

number

否

是

该场景下每帧的平均shader数量。

textureCount

number

否

是

该场景下每帧的平均纹理数量。

meshCount

number

否

是

该场景下每帧的平均mesh数量。

channelCount

number

否

是

该场景下每帧渲染的通道数。

participantCount

number

否

是

在该场景下的同屏人数。

#### GameNetInfo

游戏网络信息类，继承[BaseGameInfo](#section116223815415)。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

netLatency

string

否

否

游戏场景中网络时延，包含整体、上行、下行和服务器处理时间。

单位：毫秒（ms），字符长度范围：[1, 128]。

 说明：

格式：10,20,30,40（允许10或10,20或10,20,30），按照固定顺序解析：total,up,down,server。

netLoad

number

否

是

游戏网络负载等级。

- 1：轻度负载
- 2：中度负载
- 3：重度负载

#### GamePlayerInfo

游戏玩家信息类，继承[BaseGameInfo](#section116223815415)。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。

**名称**

**类型**

只读

可选

**说明**

gamePlayerId

string

否

是

游戏玩家ID。字符长度范围：[0, 256]。

teamPlayerId

string

否

是

团队玩家ID。字符长度范围：[0, 256]。

thirdOpenId

string

否

是

游戏官方账号ID。字符长度范围：[0, 128]。

#### DeviceInfoParameter

设备状态信息参数类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**名称**

**类型**

只读

可选

**说明**

deviceInfoType

[DeviceInfoType](#section13891254145017)

否

否

设备状态信息类型。

 说明：

- 若deviceInfoType传参为DeviceInfoType.GPU，则parameters须为空。
- 若deviceInfoType传参为DeviceInfoType.THERMAL，parameters可为空，也可传值。

parameters

Record<string, string>

否

是

设备状态信息参数。

 说明：

当前deviceInfoType传参为DeviceInfoType.THERMAL时支持传入。key固定为[DeviceInfoParameterKey](#section1346841562510).THERMAL_TEMP_LEVEL，value为指定的温控档位值，取值参见[温控档位](#section1033653365917)。若不传值则指定为系统默认温控档位。

#### DeviceInfoType

设备状态信息类型枚举对象。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**名称**

**值**

**说明**

THERMAL

1

温度变化趋势数据。

GPU

2

GPU负载。

#### DeviceInfoParameterKey

设备状态信息参数键值枚举对象。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**名称**

**值**

**说明**

THERMAL_TEMP_LEVEL

tempLevel

温控档位。

#### GameCustomTag

游戏自定义数据的标签枚举对象。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

CRASH

1

崩溃。

#### GamePerformanceErrorCode

Game Service Kit错误码类。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

**名称**

值

**说明**

INTERNAL_ERROR

1010300001

游戏内部通用错误。

AUTH_FAILED

1010300002

鉴权失败。

INVALID_REQUEST

1010300003

非法请求。

#### gamePerformance.init

init(gamePackageInfo: GamePackageInfo): Promise<void>

游戏启动时，需要对游戏场景感知模块进行初始化。使用Promise异步回调。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

**必填**

**说明**

gamePackageInfo

[GamePackageInfo](#section3844175954711)

是

游戏包信息类。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

1010300002

Auth failed.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gamePackageInfo: gamePerformance.GamePackageInfo = {
  messageType: 0,
  bundleName: "com.example.demo", // 仅示例，请替换为实际的游戏包名
  appVersion: "1.0"
}
try {
  gamePerformance.init(gamePackageInfo).then(() => {
    // 初始化成功
    hilog.info(0x0001, 'demo', `Succeeded in initializing.`);
  })
} catch (error) {
  // 初始化失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to initialize. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.updateGameInfo

updateGameInfo<T extends BaseGameInfo>(gameInfo: T): Promise<void>

更新游戏信息。使用Promise异步回调。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

**必填**

**说明**

gameInfo

[BaseGameInfo](#section116223815415)

是

游戏基本信息。

**返回值**：

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

1010300003

Invalid request.

**示例**：

```ets
// 以更新游戏场景信息为例
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gameSceneInfo: gamePerformance.GameSceneInfo = {
  messageType: 2,
  sceneID: 7,
  importanceLevel: 4
}
try {
  gamePerformance.updateGameInfo(gameSceneInfo).then(() => {
    // 更新游戏场景信息成功
    hilog.info(0x0001, 'demo', `Succeeded in updating.`);
  });
} catch (error) {
  // 更新游戏场景信息失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to update. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.on('deviceStateChanged')

on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>): void

订阅设备状态变化。使用callback回调。

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

**必填**

**说明**

type

string

是

监听的事件类型，目前仅支持监听deviceStateChanged（设备状态变化）事件。

callback

Callback<[DeviceInfo](#section1033653365917)>

是

回调函数，返回设备信息。

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // 设备信息详情
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 订阅deviceStateChanged事件
try {
  gamePerformance.on('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // 订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to subscribe. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.on('deviceStateChanged')

on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void

按需订阅设备状态变化。使用callback回调。

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**参数**：

**参数名**

**类型**

**必填**

**说明**

type

string

是

监听的事件类型，目前仅支持监听deviceStateChanged（设备状态变化）事件。

callback

Callback<[DeviceInfo](#section1033653365917)>

是

回调函数，返回设备信息。

scope

Array<[DeviceInfoType](#section13891254145017)>

是

需要订阅的设备状态信息类型。

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

1010300003

Invalid request.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // 设备信息详情
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 订阅deviceStateChanged事件
try {
  let types:Array<gamePerformance.DeviceInfoType> = [gamePerformance.DeviceInfoType.GPU];
  gamePerformance.on('deviceStateChanged', onDeviceStateChange,types);
} catch (error) {
  // 订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to subscribe. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.off('deviceStateChanged')

off(type: 'deviceStateChanged', callback?: Callback<DeviceInfo>): void

取消订阅设备状态变化。使用callback回调。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.0(12)

**参数**：

**参数名**

**类型**

**必填**

**说明**

type

string

是

监听的事件类型，目前仅支持监听deviceStateChanged（设备状态变化）事件。

callback

Callback<[DeviceInfo](#section1033653365917)>

否

回调函数，返回设备信息。

如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消deviceStateChanged事件的所有callback订阅。

**错误码**：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // 设备信息详情
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 取消订阅deviceStateChanged事件
try {
  gamePerformance.off('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
}

// 取消deviceStateChanged事件的全部订阅
try {
  gamePerformance.off("deviceStateChanged");
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.getDeviceInfoByScope

getDeviceInfoByScope(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo>

查询设备状态信息。使用Promise异步回调。

Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.0.1(13)

**参数**：

**参数名**

**类型**

**必填**

**说明**

scope

Array<[DeviceInfoParameter](#section12485171912281)>

是

设备状态信息参数。

**返回值**：

类型

说明

Promise<[DeviceInfo](#section1033653365917)>

Promise对象。返回设备状态信息。

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

The parameter check failed.

1010300003

Invalid request.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 查询设备状态
try {
  let gpuParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.GPU
  }
  let thermalParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.THERMAL
  }
  let gameInfos: Array<gamePerformance.DeviceInfoParameter> = [gpuParam, thermalParam];
  gamePerformance.getDeviceInfoByScope(gameInfos).then((deviceInfo:gamePerformance.DeviceInfo) => {
    hilog.info(0x0001, 'demo', `Succeeded in querying device info. tempLevel is ${deviceInfo.tempLevel}`);
  });
} catch (error) {
  // 查询失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to query. Code: ${err.code}, message: ${err.message}`);
}
```

#### gamePerformance.addGameCustomData

addGameCustomData(data: Record<string, string>, tag: GameCustomTag): void

上报带标签的游戏自定义数据。

**系统能力：**SystemCapability.GameService.GamePerformance

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

**必填**

**说明**

data

Record<string, string>

是

自定义数据。键的字符长度范围：[0, 128]，值的字符长度范围：[0, 1024]，单次上报Record数量范围：[1, 100]。

 说明：

可多次上报数据，已上报数据的键与值长度总和不能超过128000个字符。

tag

[GameCustomTag](#section51091113529)

是

自定义标签。

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息

401

Parameter error. Possible causes: 3. Parameter verification failed.

1010300003

Invalid request.

**示例**：

```ets
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 上报带崩溃标签的游戏自定义数据
try {
  let data:Record<string, string> = {'custom':'gaming'};
  gamePerformance.addGameCustomData(data, gamePerformance.GameCustomTag.CRASH);
} catch (error) {
  // 上报自定义数据失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to add custom data. Code: ${err.code}, message: ${err.message}`);
}
```