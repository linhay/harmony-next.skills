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

**名称****值****说明**SCAN_ERROR_NO_PERMISSION201无权限。SCAN_ERROR_NOT_SYSTEM_APPLICATION202非系统应用。SCAN_ERROR_INVALID_PARAMETER401无效参数。SCAN_ERROR_GENERIC_FAILURE13100001通用失败。SCAN_ERROR_RPC_FAILURE13100002RPC失败。SCAN_ERROR_SERVER_FAILURE13100003服务失败。SCAN_ERROR_UNSUPPORTED13100004不支持的操作。SCAN_ERROR_CANCELED13100005操作取消。SCAN_ERROR_DEVICE_BUSY13100006设备忙。SCAN_ERROR_INVALID13100007无效操作。SCAN_ERROR_JAMMED13100008卡纸。SCAN_ERROR_NO_DOCS13100009缺纸。SCAN_ERROR_COVER_OPEN13100010盖子打开。SCAN_ERROR_IO_ERROR13100011I/O错误。SCAN_ERROR_NO_MEMORY13100012内存不足。

#### ConstraintType

定义参数限制类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**SCAN_CONSTRAINT_NONE0无限制。SCAN_CONSTRAINT_RANGE1范围限制。SCAN_CONSTRAINT_WORD_LIST2数字列表。SCAN_CONSTRAINT_STRING_LIST3字符串列表。

#### PhysicalUnit

定义物理单位的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**SCAN_UNIT_NONE0无单位。SCAN_UNIT_PIXEL1像素单位。SCAN_UNIT_BIT2位单位。SCAN_UNIT_MM3毫米单位。SCAN_UNIT_DPI4DPI单位。SCAN_UNIT_PERCENT5百分比单位。SCAN_UNIT_MICROSECOND6微秒单位。

#### OptionValueType

定义选项值类型的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**SCAN_TYPE_BOOL0布尔类型。SCAN_TYPE_INT1整数类型。SCAN_TYPE_FIXED2定点数类型。SCAN_TYPE_STRING3字符串类型。

#### ScannerSyncMode

定义扫描仪同步码的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**UPDATE_STR'update'更新码，表示扫描仪id的变化。DELETE_STR'delete'删除码，表示扫描仪掉线。

#### ScannerDiscoveryMode

定义扫描仪发现方式的枚举。

**系统能力：** SystemCapability.Print.PrintFramework

**名称****值****说明**TCP_STR'TCP'网络扫描仪的发现模式。USB_STR'USB'USB扫描仪的发现模式。

#### Range

定义范围的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**minValuenumber否否范围的最小值。maxValuenumber否否范围的最大值。quantValuenumber否否范围的量化值。

#### ScannerParameter

定义扫描仪参数的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**optionNamestring否否选项名称。optionIndexnumber否否选项索引。optionTitlestring否否选项标题。optionDescstring否否选项描述。optionType[OptionValueType](#ZH-CN_TOPIC_0000002529445473__optionvaluetype)否否选项值类型。optionUnit[PhysicalUnit](#ZH-CN_TOPIC_0000002529445473__physicalunit)否否选项物理单位。optionConstraintType[ConstraintType](#ZH-CN_TOPIC_0000002529445473__constrainttype)否否选项约束类型。optionConstraintStringstring[]否是选项字符串约束。optionConstraintIntnumber[]否是选项整数约束。optionConstraintRange[Range](#ZH-CN_TOPIC_0000002529445473__range)否是选项范围约束。

#### ScannerOptionValue

定义扫描仪选项值的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**valueType[OptionValueType](#ZH-CN_TOPIC_0000002529445473__optionvaluetype)否否值类型。numValuenumber否是数值。strValuestring否是字符串值。boolValueboolean否是布尔值。

#### PictureScanProgress

定义图片扫描进度的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**progressnumber否否当前进度百分比，范围从0~100。pictureFdnumber否否扫描图片的文件描述符。isFinalboolean否否是否是本次扫描的最后一张图片。true表示是最后一张图片，false表示不是最后一张图片。

#### ScannerDevice

定义扫描仪设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**scannerIdstring否否扫描仪的唯一标识符。discoveryMode[ScannerDiscoveryMode](#ZH-CN_TOPIC_0000002529445473__scannerdiscoverymode)否否扫描仪的发现模式。uniqueIdstring否否扫描仪的唯一ID。manufacturerstring否否扫描仪的制造商。modelstring否否扫描仪的型号。deviceNamestring否否扫描仪的设备名称。

#### ScannerSyncDevice

定义扫描仪同步设备的接口。

**系统能力：** SystemCapability.Print.PrintFramework

**属性：**

**名称****类型****只读****可选****说明**scannerIdstring否否扫描仪ID。discoveryMode[ScannerDiscoveryMode](#ZH-CN_TOPIC_0000002529445473__scannerdiscoverymode)否否发现模式。uniqueIdstring否否唯一ID。syncMode[ScannerSyncMode](#ZH-CN_TOPIC_0000002529445473__scannersyncmode)否否同步模式。oldScannerIdstring否是旧的扫描仪ID，仅在syncMode为"update"时有效。

#### scan.init

init(): Promise<void>

初始化扫描服务。使用Promise异步回调。

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是要打开的扫描仪的ID。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是要关闭的扫描仪的ID。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。

**返回值：**

**类型****说明**Promise<[ScannerParameter](#ZH-CN_TOPIC_0000002529445473__scannerparameter)[]>Promise对象，返回扫描仪参数数组。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。optionIndexnumber是要设置的选项的索引。value[ScannerOptionValue](#ZH-CN_TOPIC_0000002529445473__scanneroptionvalue)是要设置的值。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。optionIndexnumber是要设置为自动的选项的索引。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。optionIndexnumber是要获取的选项的索引。

**返回值：**

**类型****说明**Promise<[ScannerOptionValue](#ZH-CN_TOPIC_0000002529445473__scanneroptionvalue)>Promise对象，返回扫描仪选项值。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。batchModeboolean是是否使用批处理模式。true表示使用批处理模式，false表示不使用批处理模式。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。

**返回值：**

**类型****说明**Promise<void>Promise对象，无返回结果。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**scannerIdstring是扫描仪的ID。

**返回值：**

**类型****说明**Promise<[PictureScanProgress](#ZH-CN_TOPIC_0000002529445473__picturescanprogress)>Promise对象，返回图片扫描进度信息。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**type'scanDeviceFound'是事件类型。callbackCallback<[ScannerDevice](#ZH-CN_TOPIC_0000002529445473__scannerdevice)>是回调函数，返回扫描仪设备发现信息。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**type'scanDeviceFound'是事件类型。callbackCallback<[ScannerDevice](#ZH-CN_TOPIC_0000002529445473__scannerdevice)>否回调函数，返回扫描仪设备发现信息。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**type'scanDeviceSync'是事件类型。callbackCallback<[ScannerSyncDevice](#ZH-CN_TOPIC_0000002529445473__scannersyncdevice)>是回调函数，返回扫描仪设备同步信息。

**错误码：**

错误码ID错误信息201Permission denied.

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

**参数名****类型****必填****说明**type'scanDeviceSync'是事件类型。callbackCallback<[ScannerSyncDevice](#ZH-CN_TOPIC_0000002529445473__scannersyncdevice)>否回调函数，返回扫描仪设备同步信息。

**错误码：**

错误码ID错误信息201Permission denied.

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