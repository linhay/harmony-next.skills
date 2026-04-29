# @ohos.scan (扫描)

该模块为扫描框架的js-api接口文档，提供发现和连接扫描仪的能力。

本模块首批接口从API version 20开始支持。

当前界面仅包含本模块的公开接口。

#### 导入模块

```ets
import { scan } from '@kit.BasicServicesKit';
```

#### ScanErrorCode

定义扫描错误码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_ERROR_NO_PERMISSION | 201 | 无权限。 |
| SCAN_ERROR_NOT_SYSTEM_APPLICATION | 202 | 非系统应用。 |
| SCAN_ERROR_INVALID_PARAMETER | 401 | 无效参数。 |
| SCAN_ERROR_GENERIC_FAILURE | 13100001 | 通用失败。 |
| SCAN_ERROR_RPC_FAILURE | 13100002 | RPC失败。 |
| SCAN_ERROR_SERVER_FAILURE | 13100003 | 服务失败。 |
| SCAN_ERROR_UNSUPPORTED | 13100004 | 不支持的操作。 |
| SCAN_ERROR_CANCELED | 13100005 | 操作取消。 |
| SCAN_ERROR_DEVICE_BUSY | 13100006 | 设备忙。 |
| SCAN_ERROR_INVALID | 13100007 | 无效操作。 |
| SCAN_ERROR_JAMMED | 13100008 | 卡纸。 |
| SCAN_ERROR_NO_DOCS | 13100009 | 缺纸。 |
| SCAN_ERROR_COVER_OPEN | 13100010 | 盖子打开。 |
| SCAN_ERROR_IO_ERROR | 13100011 | I/O错误。 |
| SCAN_ERROR_NO_MEMORY | 13100012 | 内存不足。 |

#### ConstraintType

定义参数限制类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_CONSTRAINT_NONE | 0 | 无限制。 |
| SCAN_CONSTRAINT_RANGE | 1 | 范围限制。 |
| SCAN_CONSTRAINT_WORD_LIST | 2 | 数字列表。 |
| SCAN_CONSTRAINT_STRING_LIST | 3 | 字符串列表。 |

#### PhysicalUnit

定义物理单位的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_UNIT_NONE | 0 | 无单位。 |
| SCAN_UNIT_PIXEL | 1 | 像素单位。 |
| SCAN_UNIT_BIT | 2 | 位单位。 |
| SCAN_UNIT_MM | 3 | 毫米单位。 |
| SCAN_UNIT_DPI | 4 | DPI单位。 |
| SCAN_UNIT_PERCENT | 5 | 百分比单位。 |
| SCAN_UNIT_MICROSECOND | 6 | 微秒单位。 |

#### OptionValueType

定义选项值类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_TYPE_BOOL | 0 | 布尔类型。 |
| SCAN_TYPE_INT | 1 | 整数类型。 |
| SCAN_TYPE_FIXED | 2 | 定点数类型。 |
| SCAN_TYPE_STRING | 3 | 字符串类型。 |

#### ScannerSyncMode

定义扫描仪同步码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UPDATE_STR | 'update' | 更新码，表示扫描仪id的变化。 |
| DELETE_STR | 'delete' | 删除码，表示扫描仪掉线。 |

#### ScannerDiscoveryMode

定义扫描仪发现方式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TCP_STR | 'TCP' | 网络扫描仪的发现模式。 |
| USB_STR | 'USB' | USB扫描仪的发现模式。 |

#### Range

定义范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minValue | number | 否 | 否 | 范围的最小值。 |
| maxValue | number | 否 | 否 | 范围的最大值。 |
| quantValue | number | 否 | 否 | 范围的量化值。 |

#### ScannerParameter

定义扫描仪参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| optionName | string | 否 | 否 | 选项名称。 |
| optionIndex | number | 否 | 否 | 选项索引。 |
| optionTitle | string | 否 | 否 | 选项标题。 |
| optionDesc | string | 否 | 否 | 选项描述。 |
| optionType | OptionValueType | 否 | 否 | 选项值类型。 |
| optionUnit | PhysicalUnit | 否 | 否 | 选项物理单位。 |
| optionConstraintType | ConstraintType | 否 | 否 | 选项约束类型。 |
| optionConstraintString | string[] | 否 | 是 | 选项字符串约束。 |
| optionConstraintInt | number[] | 否 | 是 | 选项整数约束。 |
| optionConstraintRange | Range | 否 | 是 | 选项范围约束。 |

#### ScannerOptionValue

定义扫描仪选项值的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| valueType | OptionValueType | 否 | 否 | 值类型。 |
| numValue | number | 否 | 是 | 数值。 |
| strValue | string | 否 | 是 | 字符串值。 |
| boolValue | boolean | 否 | 是 | 布尔值。 |

#### PictureScanProgress

定义图片扫描进度的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 当前进度百分比，范围从0~100。 |
| pictureFd | number | 否 | 否 | 扫描图片的文件描述符。 |
| isFinal | boolean | 否 | 否 | 是否是本次扫描的最后一张图片。true表示是最后一张图片，false表示不是最后一张图片。 |

#### ScannerDevice

定义扫描仪设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scannerId | string | 否 | 否 | 扫描仪的唯一标识符。 |
| discoveryMode | ScannerDiscoveryMode | 否 | 否 | 扫描仪的发现模式。 |
| uniqueId | string | 否 | 否 | 扫描仪的唯一ID。 |
| manufacturer | string | 否 | 否 | 扫描仪的制造商。 |
| model | string | 否 | 否 | 扫描仪的型号。 |
| deviceName | string | 否 | 否 | 扫描仪的设备名称。 |

#### ScannerSyncDevice

定义扫描仪同步设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scannerId | string | 否 | 否 | 扫描仪ID。 |
| discoveryMode | ScannerDiscoveryMode | 否 | 否 | 发现模式。 |
| uniqueId | string | 否 | 否 | 唯一ID。 |
| syncMode | ScannerSyncMode | 否 | 否 | 同步模式。 |
| oldScannerId | string | 否 | 是 | 旧的扫描仪ID，仅在syncMode为"update"时有效。 |

#### scan.init

init(): Promise<void>

初始化扫描服务。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.init().then(() => {
    console.info('scan init success');
}).catch((error: BusinessError) => {
    console.error('scan init failed: ' + JSON.stringify(error));
})
```

#### scan.exit

exit(): Promise<void>

退出扫描服务。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.exit().then(() => {
    console.info('scan exit success');
}).catch((error: BusinessError) => {
    console.error('scan exit failed: ' + JSON.stringify(error));
})
```

#### scan.startScannerDiscovery

startScannerDiscovery(): Promise<void>

开始发现扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.startScannerDiscovery().then(() => {
    console.info('start scanner discovery success');
}).catch((error: BusinessError) => {
    console.error('start scanner discovery failed: ' + JSON.stringify(error));
})
```

#### scan.openScanner

openScanner(scannerId: string): Promise<void>

打开扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 要打开的扫描仪的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.openScanner(scannerId).then(() => {
    console.info('open scanner success');
}).catch((error: BusinessError) => {
    console.error('open scanner failed: ' + JSON.stringify(error));
})
```

#### scan.closeScanner

closeScanner(scannerId: string): Promise<void>

关闭扫描仪。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 要关闭的扫描仪的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.closeScanner(scannerId).then(() => {
    console.info('close scanner success');
}).catch((error: BusinessError) => {
    console.error('close scanner failed: ' + JSON.stringify(error));
})
```

#### scan.getScannerParameter

getScannerParameter(scannerId: string): Promise<ScannerParameter[]>

获取扫描仪参数。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ScannerParameter[]> | Promise对象，返回扫描仪参数数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.getScannerParameter(scannerId).then((parameters: scan.ScannerParameter[]) => {
    console.info('get scanner parameters success: ' + JSON.stringify(parameters));
}).catch((error: BusinessError) => {
    console.error('get scanner parameters failed: ' + JSON.stringify(error));
})
```

#### scan.setScannerParameter

setScannerParameter(scannerId: string, optionIndex: number, value: ScannerOptionValue): Promise<void>

设置扫描仪参数。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要设置的选项的索引。 |
| value | ScannerOptionValue | 是 | 要设置的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
let value: scan.ScannerOptionValue = {
    valueType: scan.OptionValueType.SCAN_TYPE_INT,
    numValue: 100
};
scan.setScannerParameter(scannerId, optionIndex, value).then(() => {
    console.info('set scanner parameter success');
}).catch((error: BusinessError) => {
    console.error('set scanner parameter failed: ' + JSON.stringify(error));
})
```

#### scan.setScanAutoOption

setScanAutoOption(scannerId: string, optionIndex: number): Promise<void>

设置扫描选项为自动模式。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要设置为自动的选项的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
scan.setScanAutoOption(scannerId, optionIndex).then(() => {
    console.info('set scan auto option success');
}).catch((error: BusinessError) => {
    console.error('set scan auto option failed: ' + JSON.stringify(error));
})
```

#### scan.getScannerCurrentSetting

getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>

获取当前扫描仪设置。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| optionIndex | number | 是 | 要获取的选项的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ScannerOptionValue> | Promise对象，返回扫描仪选项值。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
scan.getScannerCurrentSetting(scannerId, optionIndex).then((value: scan.ScannerOptionValue) => {
    console.info('get scanner current setting success: ' + JSON.stringify(value));
}).catch((error: BusinessError) => {
    console.error('get scanner current setting failed: ' + JSON.stringify(error));
})
```

#### scan.startScan

startScan(scannerId: string, batchMode: boolean): Promise<void>

开始扫描。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |
| batchMode | boolean | 是 | 是否使用批处理模式。true表示使用批处理模式，false表示不使用批处理模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let batchMode: boolean = true;
scan.startScan(scannerId, batchMode).then(() => {
    console.info('start scan success');
}).catch((error: BusinessError) => {
    console.error('start scan failed: ' + JSON.stringify(error));
})
```

#### scan.cancelScan

cancelScan(scannerId: string): Promise<void>

取消扫描。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.cancelScan(scannerId).then(() => {
    console.info('cancel scan success');
}).catch((error: BusinessError) => {
    console.error('cancel scan failed: ' + JSON.stringify(error));
})
```

#### scan.getPictureScanProgress

getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>

获取图片扫描进度。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scannerId | string | 是 | 扫描仪的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PictureScanProgress> | Promise对象，返回图片扫描进度信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.getPictureScanProgress(scannerId).then((progress: scan.PictureScanProgress) => {
    console.info('get picture scan progress success: ' + JSON.stringify(progress));
}).catch((error: BusinessError) => {
    console.error('get picture scan progress failed: ' + JSON.stringify(error));
})
```

#### scan.on

on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void

注册扫描仪设备发现事件回调。使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'scanDeviceFound' | 是 | 事件类型。 |
| callback | Callback<ScannerDevice> | 是 | 回调函数，返回扫描仪设备发现信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';

scan.on('scanDeviceFound', (device: scan.ScannerDevice) => {
    console.info('scan device found: ' + JSON.stringify(device));
})
```

#### scan.off

off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void

取消注册扫描仪设备发现事件回调。使用callback异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'scanDeviceFound' | 是 | 事件类型。 |
| callback | Callback<ScannerDevice> | 否 | 回调函数，返回扫描仪设备发现信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerDevice) => {
    console.info('scan device found: ' + JSON.stringify(device));
};
scan.on('scanDeviceFound', callback);
// 取消注册
scan.off('scanDeviceFound', callback);
```

#### scan.on

on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void

注册扫描仪设备同步事件回调。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'scanDeviceSync' | 是 | 事件类型。 |
| callback | Callback<ScannerSyncDevice> | 是 | 回调函数，返回扫描仪设备同步信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';

scan.on('scanDeviceSync', (device: scan.ScannerSyncDevice) => {
    console.info('scan device sync: ' + JSON.stringify(device));
})
```

#### scan.off

off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void

取消注册扫描仪设备同步事件回调。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'scanDeviceSync' | 是 | 事件类型。 |
| callback | Callback<ScannerSyncDevice> | 否 | 回调函数，返回扫描仪设备同步信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerSyncDevice) => {
    console.info('scan device sync: ' + JSON.stringify(device));
};
scan.on('scanDeviceSync', callback);
// 取消注册
scan.off('scanDeviceSync', callback);
```