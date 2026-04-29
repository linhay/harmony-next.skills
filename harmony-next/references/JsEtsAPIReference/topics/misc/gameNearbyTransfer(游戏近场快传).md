# gameNearbyTransfer(游戏近场快传)

本模块提供接入Game Service Kit的游戏近场快传能力。

起始版本： 5.1.0(18)

**导入模块**

```ets
import { gameNearbyTransfer } from '@kit.GameServiceKit';
```

**CreateParameters**

创建参数类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 否 | 模块名。字符长度范围：[1, 1024]。 |
| abilityName | string | 否 | 否 | Ability名称。字符长度范围：[1, 1024]。 |
| needShowSystemUI | boolean | 否 | 是 | 是否展示系统UI。 - true：展示 - false：不展示 默认为false。 |
| context | common.UIAbilityContext | 否 | 是 | UIAbility上下文，当needShowSystemUI为true时，该参数必传。 |
| mode | Mode | 否 | 是 | 接入模式。默认为API模式。 起始版本： 6.0.0(20)。 |
| contentType | ContentType | 否 | 是 | 内容类型。 默认值为RESOURCE_PACKAGE。 模型约束： 此接口仅可在Stage模型下使用。 起始版本： 6.1.0(23)。 |
| gameLinking | string | 否 | 是 | 游戏链接，即App Linking或Deep Linking，仅当contentType为“INSTALLATION_PACKAGE”类型时生效。如果接收端已安装该游戏，则将通过gameLinking启动该游戏。使用方式请参见使用App Linking实现应用间跳转和使用Deep Linking实现应用间跳转。 字符长度范围：[0, 2048]。 模型约束： 此接口仅可在Stage模型下使用。 起始版本： 6.1.0(23)。 |

**ConnectNotification**

连接通知类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectState | ConnectState | 否 | 否 | 连接状态。 |
| message | string | 否 | 是 | 连接结果消息。 |
| remoteDeviceName | string | 否 | 是 | 远端设备名。 |

**BindParameters**

绑定参数类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID。字符长度范围：[1, 128]。 |
| networkId | string | 否 | 否 | 设备网络ID。字符长度范围：[1, 128]。 |

**NearbyGameDevice**

近场快传设备类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceName | string | 否 | 否 | 设备名。 |
| deviceId | string | 否 | 否 | 设备ID。 |
| networkId | string | 否 | 否 | 设备网络ID。 |

**DiscoveryResult**

发现结果类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nearbyGameDevices | Array<NearbyGameDevice> | 否 | 否 | 发现的设备列表。 |

**CreateResult**

创建结果类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localDeviceName | string | 否 | 否 | 本端设备名。 |
| linkingForInstallation | string | 否 | 是 | 安装包的传输链接，仅当传输类型为安装包传输时返回。字符长度范围：[0, 2048]。 模型约束： 此接口仅可在Stage模型下使用。 起始版本： 6.1.0(23)。 |

**TransferNotification**

传输通知类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| transferState | TransferState | 否 | 否 | 传输状态。 |
| transferInfo | TransferInfo | 否 | 否 | 传输信息。 |
| fileStoragePath | string | 否 | 是 | 接收端已接收文件的存储目录沙箱路径，详情请参见应用沙箱目录，传输完成后返回。 |

**FileInfo**

文件信息类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 文件路径，使用沙箱路径，详情请参见应用沙箱目录。字符长度范围：[1, 2048]。 |
| hash | string | 否 | 是 | 文件hash值。字符长度范围：[0, 256]。 |

**PackageInfo**

包信息类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 包名。字符长度范围：[0, 2048]。 |
| version | string | 否 | 是 | 版本号，格式自定义。字符长度范围：[0, 256]。 |
| files | Array<FileInfo> | 否 | 是 | 文件列表。最多10000条。 |
| extraData | string | 否 | 是 | 扩展数据。字符长度范围：[0, 2048]。 |

**PackageFile**

传输包文件类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| srcPath | string | 否 | 否 | 源文件路径，为发送端应用沙箱路径，详情请参见应用沙箱目录。字符长度范围：[1, 2048]。完整路径。 |
| destPath | string | 否 | 否 | 目标文件路径，为接收端应用沙箱路径，详情请参见应用沙箱目录。字符长度范围：[1, 2048]。相对路径，完整路径为fileStoragePath+destPath。 |

**PackageData**

传输包数据类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 包名。字符长度范围：[0, 2048]。 |
| version | string | 否 | 是 | 版本号。字符长度范围：[0, 256]。 |
| files | Array<PackageFile> | 否 | 否 | 传输文件列表。 对于6.0.2(22)之前的版本，传输文件列表中的文件数量最多为10000条。 对于6.0.2(22)版本，文件数量最多为200000条。 对于6.0.2(22)之后的版本，文件数量最多为500000条。 |

**ReturnResult**

返回结果类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 返回码。具体取值请参考NearbyTransferErrorCode。 |
| message | string | 否 | 是 | 返回消息。 |

**PackageInfoResult**

包信息对比结果类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| packageInfoResultCode | PackageInfoResultCode | 否 | 否 | 对比结果码值。 |
| message | string | 否 | 是 | 对比结果信息。 |

**TransferInfo**

传输信息类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| expectedTime | number | 否 | 否 | 传输剩余时间，单位：s。 |
| transferredPackageSize | number | 否 | 否 | 已传输包大小，单位：Byte。 |
| totalPackageSize | number | 否 | 否 | 整包总大小，单位：Byte。 |
| rate | number | 否 | 否 | 传输速率，单位：Byte/s。 |

**RemoteInstallationInfo**

安装信息类。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| installed | boolean | 否 | 否 | 安装包在接收端是否已安装。 - true：已安装。 - false：未安装。 默认值为false。 |

**Mode**

接入模式枚举对象。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| API | 1 | API模式，即使用游戏近场快传服务接口接入。 |
| KNOCK | 2 | 碰一碰模式。详情请参考碰一碰分享。 |
| GESTURES | 3 | 隔空传送模式。详情请参考隔空传送。 模型约束： 此接口仅可在Stage模型下使用。 起始版本： 6.1.0(23)。 |

**ConnectState**

连接状态枚举对象。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTED | 0 | 连接成功。 |
| DISCONNECTED | 1 | 连接断开。 |

**TransferState**

传输状态枚举对象。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEND_START | 0 | 准备发送。 |
| SEND_PROCESS | 1 | 发送进行。 |
| SEND_FINISH | 2 | 发送完成。 |
| SEND_ERROR | 3 | 发送错误。 |
| RECEIVE_START | 4 | 接收开始。 |
| RECEIVE_PROCESS | 5 | 接收进行。 |
| RECEIVE_FINISH | 6 | 接收完成。 |
| RECEIVE_ERROR | 7 | 接收错误。 |

**PackageInfoResultCode**

包信息对比结果码值枚举对象。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR | -1 | 对比错误。 |
| PACKAGE_AVAILABLE_COMPARED | 0 | 对比后可用。 |
| PACKAGE_UNAVAILABLE_COMPARED | 1 | 对比后不可用。 |

**ContentType**

传输的内容类型枚举对象。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RESOURCE_PACKAGE | 1 | 资源包，用于在对方已安装游戏的情况下传输游戏内资源（例如游戏地图等）。 |
| INSTALLATION_PACKAGE | 2 | 安装包，用于在对方未安装游戏的情况下传输游戏安装包。 |

**NearbyTransferErrorCode**

错误码类。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL_ERROR | 1018300001 | 内部通用错误。 |
| AUTH_FAILED | 1018300002 | 鉴权失败。 |
| INVALID_REQUEST | 1018300003 | 请求不合法。 |
| NO_SERVICE_AVAILABLE | 1018300004 | 服务不可用。 |
| WLAN_BLUETOOTH_MUST_BE_ON | 1018300005 | WLAN和蓝牙必须同时开启。 |
| PUBLISH_FAILED | 1018300006 | 发布失败。 |
| DISCOVERY_FAILED | 1018300007 | 发现失败。 |
| INVALID_PARAMETER | 1018300008 | 非法参数。 起始版本： 6.0.0(20) |

**gameNearbyTransfer.on('connectNotify')**

on(type: 'connectNotify', callback: Callback<ConnectNotification>): void

订阅连接通知事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'connectNotify'，建链操作完成后触发该事件。 |
| callback | Callback<ConnectNotification> | 是 | 回调函数，返回连接通知对象。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 订阅连接通知事件
  gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
} catch (error) {
  // 订阅连接通知失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe connectNotify. Code: ${err.code}, message: ${err.message}`);
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // 获取连接状态
  hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
}
```

**gameNearbyTransfer.off('connectNotify')**

off(type: 'connectNotify', callback?: Callback<ConnectNotification>): void

取消订阅连接通知事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'connectNotify'，建链操作完成后触发该事件。 |
| callback | Callback<ConnectNotification> | 否 | 回调函数，返回连接通知对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'connectNotify'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消订阅连接通知事件
  gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe connectNotify. Code: ${err.code}, message: ${err.message}`);
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // 获取连接状态
  hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
}
```

**gameNearbyTransfer.on('discovery')**

on(type: 'discovery', callback: Callback<DiscoveryResult>): void

订阅发现结果事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'discovery'，发现设备操作完成后触发该事件。 |
| callback | Callback<DiscoveryResult> | 是 | 回调函数，返回发现结果对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 订阅发现结果
  gameNearbyTransfer.on('discovery', discoveryCallBack);
} catch (error) {
  // 订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe discovery. Code: ${err.code}, message: ${err.message}`);
}

function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
  // 获取到发现的设备 展示设备列表
  callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
  });
}
```

**gameNearbyTransfer.off('discovery')**

off(type: 'discovery', callback?: Callback<DiscoveryResult>): void

取消订阅发现结果事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'discovery'，发现设备操作完成后触发该事件。 |
| callback | Callback<DiscoveryResult> | 否 | 回调函数，返回发现结果对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'discovery'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Invalid parameter. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消订阅
  gameNearbyTransfer.off('discovery', discoveryCallBack);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe discovery. Code: ${err.code}, message: ${err.message}`);
}

function discoveryCallBack(callback: gameNearbyTransfer.DiscoveryResult) {
  // 获取到发现的设备 展示设备列表
  callback.nearbyGameDevices.forEach((device: gameNearbyTransfer.NearbyGameDevice, index: number) => {
  });
}
```

**gameNearbyTransfer.on('receivePackageInfo')**

on(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void

订阅收到包信息事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'receivePackageInfo'，收到接收方发送的自身文件信息后触发该事件。 |
| callback | Callback<PackageInfo> | 是 | 回调函数，返回包信息对象。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 订阅包信息事件
  gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
} catch (error) {
  // 订阅包信息事件失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe receivePackageInfo. Code: ${err.code}, message: ${err.message}`);
}
function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // 获取对端包信息&版本号
  hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
}
```

**gameNearbyTransfer.off('receivePackageInfo')**

off(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void

取消订阅收到包信息事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'receivePackageInfo'，收到接收方发送的自身文件信息后触发该事件。 |
| callback | Callback<PackageInfo> | 否 | 回调函数，返回包信息对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'receivePackageInfo'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消订阅包信息事件
  gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe receivePackageInfo. Code: ${err.code}, message: ${err.message}`);
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // 获取对端包信息&版本号
  hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
}
```

**gameNearbyTransfer.on('transferNotify')**

on(type: 'transferNotify', callback: Callback<TransferNotification>): void

订阅传输通知事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'transferNotify'，文件传输过程中触发该事件。 |
| callback | Callback<TransferNotification> | 是 | 回调函数，返回传输通知对象。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 订阅传输通知事件
  gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
} catch (error) {
  // 订阅传输通知失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe transferNotify. Code: ${err.code}, message: ${err.message}`);
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // 获取传输状态
  hilog.info(0x0000, 'nearby', `transferNotify. transferState: ${callback.transferState}`);
}
```

**gameNearbyTransfer.off('transferNotify')**

off(type: 'transferNotify', callback?: Callback<TransferNotification>): void

取消订阅传输通知事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'transferNotify'，文件传输过程中触发该事件。 |
| callback | Callback<TransferNotification> | 否 | 回调函数，返回传输通知对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'transferNotify'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消订阅传输通知事件
  gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe transferNotify. Code: ${err.code}, message: ${err.message}`);
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // 获取传输状态
  hilog.info(0x0000, 'nearby', `transferNotify. transferState: ${callback.transferState}`);
}
```

**gameNearbyTransfer.on('error')**

on(type: 'error', callback: Callback<ReturnResult>): void

订阅错误事件。使用callback回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'error'，内部错误时触发该事件。 |
| callback | Callback<ReturnResult> | 是 | 回调函数，返回结果信息对象。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 订阅异常事件通知
  gameNearbyTransfer.on('error', errorCallBack);
} catch (error) {
  // 订阅异常事件通知失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe error. Code: ${err.code}, message: ${err.message}`);
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  hilog.warn(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
}
```

**gameNearbyTransfer.off('error')**

off(type: 'error', callback?: Callback<ReturnResult>): void

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，支持的事件为'error'。 |
| callback | Callback<ReturnResult> | 否 | 回调函数，返回结果信息对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'error'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消订阅异常事件通知
  gameNearbyTransfer.off('error', errorCallBack);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe errorCallBack. Code: ${err.code}, message: ${err.message}`);
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  hilog.warn(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
}
```

**gameNearbyTransfer.onRemoteInstallationInfoNotify**

onRemoteInstallationInfoNotify(callback: Callback<RemoteInstallationInfo>): void

订阅近场快传远程安装包信息通知事件。使用callback回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RemoteInstallationInfo> | 是 | 回调函数，返回远程安装包结果信息对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  gameNearbyTransfer.onRemoteInstallationInfoNotify(remoteCallBack);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to subscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
}

function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
  // 对端是否已安装
  hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
}
```

**gameNearbyTransfer.offRemoteInstallationInfoNotify**

offRemoteInstallationInfoNotify(callback?: Callback<RemoteInstallationInfo>): void

取消订阅近场快传远程安装包信息通知事件。使用callback回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<RemoteInstallationInfo> | 否 | 回调函数，返回远程安装包结果信息对象。 如果该参数不为空，则取消当前callback订阅。如果该参数为空，则取消'offRemoteInstallationInfoNotify'事件的所有callback订阅。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300008 | Parameter error. Possible causes: 3. Parameter verification failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from '@kit.BasicServicesKit';

try {
  gameNearbyTransfer.offRemoteInstallationInfoNotify(remoteCallBack);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `Failed to unsubscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
}

function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
  // 对端是否已安装
  hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
}
```

**gameNearbyTransfer.create**

create(createParameters: CreateParameters): Promise<CreateResult>

创建游戏近场快传服务。使用Promise异步回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| createParameters | CreateParameters | 是 | 创建参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<CreateResult> | Promise对象。返回创建结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300002 | Authentication failed. |

资源包传输示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

@Component
struct Create {
  create() {
    // 创建资源包传输
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let initParam: gameNearbyTransfer.CreateParameters = {
      abilityName: context.abilityInfo.name,
      context: context,
      moduleName: context.abilityInfo.moduleName,
      needShowSystemUI: false // 是否显示系统UI
    };

    try {
      gameNearbyTransfer.create(initParam).then((createResult) => {
        hilog.info(0x0000, 'nearby', `create success localDeviceName ${createResult.localDeviceName}`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
      })
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'nearby', `create exception. Code: ${err.code}, message: ${err.message}`);
    }

  build() {
  }
```

安装包传输示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

@Component
struct Create {
  async create() {
    // 创建安装包传输
    let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let initParam: gameNearbyTransfer.CreateParameters = {
      abilityName: uiAbilityContext.abilityInfo.name,
      moduleName: uiAbilityContext.abilityInfo.moduleName,
      contentType: gameNearbyTransfer.ContentType.INSTALLATION_PACKAGE, // 指定传输类型为安装包
      gameLinking: "nearbytransfer://com.huawei.nearbytransferdemo?type=nearbyTransfer" // 安装包场景需要传入游戏Deeplink
    };

    try {
      let createResult = await gameNearbyTransfer.create(initParam);
      hilog.info(0x0000, '[nearby]', `create success linking: ${createResult.linkingForInstallation}`);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
    }

  build() {
  }
```

**gameNearbyTransfer.publishNearbyGame**

publishNearbyGame(): Promise<void>

发布近场快传服务。使用Promise异步回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300006 | Publishing failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  gameNearbyTransfer.publishNearbyGame().then(() => {
    hilog.info(0x0000, 'nearby', `publishNearbyGame success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `publishNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `publishNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.discoveryNearbyGame**

discoveryNearbyGame(): Promise<void>

发送端执行发现附近设备。使用Promise异步回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300007 | Discovery failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  gameNearbyTransfer.discoveryNearbyGame().then(() => {
    hilog.info(0x0000, 'nearby', `discoveryNearbyGame success.`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `discoveryNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `discoveryNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.bindNearbyGame**

bindNearbyGame(bindParameters: BindParameters): Promise<void>

发送端绑定指定近场快传服务。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bindParameters | BindParameters | 是 | 绑定参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300005 | The wireless network and Bluetooth should be enabled at the same time. |
| 1018300008 | Invalid parameter. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let bindInfo: gameNearbyTransfer.BindParameters = {
  deviceId: 'deviceId',
  networkId: 'networkId'
};
try {
  gameNearbyTransfer.bindNearbyGame(bindInfo).then(() => {
    hilog.info(0x0000, 'nearby', `bindNearbyGame success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `bindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `bindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.autoBindNearbyGame**

autoBindNearbyGame(): Promise<void>

自动绑定近场快传服务。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |
| 1018300007 | Discovery failed. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

try {
  // 自动绑定近场快传服务
  gameNearbyTransfer.autoBindNearbyGame().then(() => {
    hilog.info(0x0000, 'nearby', `autoBindNearbyGame success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `autoBindNearbyGame failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `autoBindNearbyGame exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.acceptCollaboration**

acceptCollaboration(acceptParameters: Record<string, object>): Promise<void>

接受协同。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| acceptParameters | Record<string, object> | 是 | 设置接受参数。Record数量范围：[1, 1024]。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

示例：

```ets
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { AbilityConstant, UIAbility } from "@kit.AbilityKit";
import { hilog } from "@kit.PerformanceAnalysisKit";

export default class EntryAbility extends UIAbility {
  // 协同回调
  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    try {
      // 接受协同
      gameNearbyTransfer.acceptCollaboration(wantParam).catch((err: BusinessError) => {
        hilog.error(0x0000, 'nearby', `acceptCollaboration failed. Code: ${err.code}, message: ${err.message}`);
      })
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'nearby', `acceptCollaboration exception. Code: ${err.code}, message: ${err.message}`);
    }
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
```

**gameNearbyTransfer.sendPackageInfo**

sendPackageInfo(packageInfo: PackageInfo): Promise<void>

接收端发送自身文件信息。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| packageInfo | PackageInfo | 是 | 包信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageInfo: gameNearbyTransfer.PackageInfo = {
  name: 'xxxx',
  files: [],
  version: '1.1.0', // 应用版本
  extraData: 'extraData' // 自定义信息
};
let fileInfo: gameNearbyTransfer.FileInfo = {
  path: "/xxx/xxxx/files/data.zip",
  hash: 'fileHash' // 可选
};
packageInfo.files?.push(fileInfo);
try {
  gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
    hilog.info(0x0000, 'nearby', `sendPackageInfo success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `sendPackageInfo failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `sendPackageInfo exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.replyPackageInfoResult**

replyPackageInfoResult(packageInfoResult: PackageInfoResult): Promise<void>

发送端向近场快传服务上报包信息对比结果。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| packageInfoResult | PackageInfoResult | 是 | 包信息对比结果。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
  packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE_AVAILABLE_COMPARED
};
try {
  // 上报包信息对比结果
  gameNearbyTransfer.replyPackageInfoResult(packageInfoResult).then(() => {
    hilog.info(0x0000, 'nearby', `replyPackageInfoResult success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `replyPackageInfoResult failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `replyPackageInfoResult exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.transferPackageData**

transferPackageData(packageData: PackageData): Promise<void>

开始传输包数据。使用Promise异步回调。

需要权限： ohos.permission.DISTRIBUTED_DATASYNC

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| packageData | PackageData | 是 | 待传输的包数据信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 3. Parameter verification failed. |
| 1018300001 | System internal error. |
| 1018300003 | Invalid request. |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

let packageData: gameNearbyTransfer.PackageData = {
  name: 'xxx',
  version: '1.0.1',
  files: []
};
packageData.files.push({ srcPath: "/xxx/xxxx/a.db", destPath: "xxxx/b.db" });
try {
  // 开始传输包数据
  gameNearbyTransfer.transferPackageData(packageData).then(() => {
    hilog.info(0x0000, 'nearby', `transferPackageData success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `transferPackageData failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `transferPackageData exception. Code: ${err.code}, message: ${err.message}`);
}
```

**gameNearbyTransfer.destroy**

destroy(): Promise<void>

不再使用时，销毁游戏近场快传服务。使用Promise异步回调。

系统能力： SystemCapability.GameService.GameNearby

起始版本： 5.1.0(18)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
import { hilog } from "@kit.PerformanceAnalysisKit";
import { gameNearbyTransfer } from "@kit.GameServiceKit";
import { BusinessError } from "@kit.BasicServicesKit";

// 销毁服务
try {
  gameNearbyTransfer.destroy().then(() => {
    hilog.info(0x0000, 'nearby', `destroy success`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
}
```