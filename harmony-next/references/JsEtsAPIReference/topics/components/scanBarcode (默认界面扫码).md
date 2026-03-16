# scanBarcode (默认界面扫码)

本模块提供默认界面扫码能力。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts)接入。

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { scanBarcode } from '@kit.ScanKit';
```

#### ScanResult

扫码结果。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

**可选**

**说明**

scanType

scanCore.[ScanType](../misc/scanCore (扫码公共信息).md#section113371139123212)

否

否

码类型。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

originalValue

string

否

否

码识别内容结果。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

scanCodeRect

[ScanCodeRect](#section1456184716188)

否

是

码识别位置信息。

**起始版本：**4.1.0(11)

cornerPoints

Array<[Point](#section9634457911)>

否

是

码识别角点位置信息，返回QR Code四个角点。此参数仅图像识码接口[detectBarcode.decodeImage](detectBarcode (图像识码).md#section387381185013)返回。

**起始版本：**5.0.0(12)

isGS1

boolean

否

是

码图是否携带GS1（Global Standards 1）数据。

true表示码图携带GS1数据；false表示码图不携带GS1数据。默认值是false。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**起始版本：**6.0.2(22)

source

scanCore.[ScanSource](../misc/scanCore (扫码公共信息).md#section152115548134)

否

是

扫码结果来源。此参数仅默认界面扫码接口返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**起始版本：**6.0.2(22)

#### ScanCodeRect

码的位置信息。使用默认扫码接口（startScan和startScanForResult）不返回码位置。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

**可选**

**说明**

left

number

否

否

码外接矩形左上角的x坐标。单位：px。

top

number

否

否

码外接矩形左上角的y坐标。单位：px。

right

number

否

否

码外接矩形右下角的x坐标。单位：px。

bottom

number

否

否

码外接矩形右下角的y坐标。单位：px。

自定义界面扫码返回的坐标单位与传入参数[ViewControl](../misc/customScan (自定义界面扫码).md#section8604949165313)中width、height单位一致。

#### Point

点坐标，该坐标系左上角为{0，0}，此坐标系是以设备充电口在右侧时的横向设备方向为基准的。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

**可选**

**说明**

x

number

否

否

X轴坐标，单位：px。

y

number

否

否

Y轴坐标，单位：px。

#### ScanOptions

扫码、识码参数。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.0.0(10)

**名称**

**类型**

只读

**可选**

**说明**

scanTypes

Array<scanCore.[ScanType](../misc/scanCore (扫码公共信息).md#section113371139123212)>

否

是

设置扫码类型，默认扫码ALL（全部码类型）。

enableMultiMode

boolean

否

是

是否开启多码识别，默认false。

- true：多码识别。
- false：单码识别。

enableAlbum

boolean

否

是

是否开启相册，默认true。

- true：开启相册扫码。
- false：关闭相册扫码。

此参数只控制默认界面扫码能力中的相册识码且相册识码只支持单码识别。

**示例：**

```ets
import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((result: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${error.code}, message: ${error.message}`);
  }
}
```

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，使用Promise异步回调返回解码结果。需要在页面和组件的生命周期内调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

应用上下文。

options

[ScanOptions](#section1285191073117)

否

启动扫码参数。

**返回值：**

**类型**

**说明**

Promise<[ScanResult](#section10614317162112)>

Promise对象，返回扫码结果对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

1000500002

The user canceled the barcode scanning.

**示例：**

```ets
import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((result: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${error.code}, message: ${error.message}`);
  }
}
```

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，使用Callback异步回调返回解码结果。需要在页面和组件的生命周期内调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

应用上下文。

callback

AsyncCallback<[ScanResult](#section10614317162112)>

是

回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](#section10614317162112)；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

1000500002

The user canceled the barcode scanning.

**示例：**

```ets
import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 启动扫码，拉起扫码界面
function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), (error: BusinessError, result: scanBarcode.ScanResult) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to startScanForResult. Code: ${error.code}, message: ${error.message}`);
  }
}
```

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，使用Callback异步回调返回解码结果。需要在页面和组件的生命周期内调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

应用上下文。

options

[ScanOptions](#section1285191073117)

是

启动扫码参数。

callback

AsyncCallback<[ScanResult](#section10614317162112)>

是

回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](#section10614317162112)；否则为错误对象。

**错误码**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

1000500002

The user canceled the barcode scanning.

**示例：**

```ets
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
// 启动扫码，拉起扫码界面
function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options, (error: BusinessError, result: scanBarcode.ScanResult) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to startScanForResult. Code: ${error.code}, message: ${error.message}`);
  }
}
```

#### scanBarcode.startScan(deprecated)

startScan(options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，使用Promise异步回调返回扫码结果。

**废弃说明：**从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scanBarcode (默认界面扫码).md#section829511911349)替代。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.0.0(10)

**参数：**

**参数名**

**类型**

必填

**说明**

options

[ScanOptions](#section1285191073117)

否

启动扫码参数。

**返回值：**

**类型**

**说明**

Promise<[ScanResult](#section10614317162112)>

Promise对象，返回扫码结果对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

**示例：**

```ets
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造启动扫码的入参options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options).then((result: scanBarcode.ScanResult) => {
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}`);
  }).catch((error: BusinessError) => {
    // 当扫码过程中出现错误打印报错并返回
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### scanBarcode.startScan(deprecated)

startScan(callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，使用Callback异步回调返回扫码结果。

**废弃说明：**从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scanBarcode (默认界面扫码).md#section399311216327)替代。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.0.0(10)

**参数：**

**参数名**

**类型**

必填

**说明**

callback

AsyncCallback<[ScanResult](#section10614317162112)>

是

回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](#section10614317162112)；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

**示例：**

```ets
import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  scanBarcode.startScan((error: BusinessError, result: scanBarcode.ScanResult) => {
    // error回调监听，当扫码过程中出现错误打印报错并返回
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### scanBarcode.startScan(deprecated)

startScan(options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，使用Callback异步回调返回扫码结果。

**废弃说明：**从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scanBarcode (默认界面扫码).md#section1738211373353)替代。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.0.0(10)

**参数：**

**参数名**

**类型**

**必填**

**说明**

options

[ScanOptions](#section1285191073117)

是

启动扫码参数。

callback

AsyncCallback<[ScanResult](#section10614317162112)>

是

回调函数，当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](#section10614317162112)；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

**示例：**

```ets
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造启动扫码的入参options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options, (error: BusinessError, result: scanBarcode.ScanResult) => {
    // error回调监听，当扫码过程中出现错误打印报错并返回
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}`);
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${error.code}, message: ${error.message}`);
}
```