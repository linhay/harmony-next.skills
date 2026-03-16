# customScan (自定义界面扫码)

本模块提供自定义界面扫码能力。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts)接入。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { customScan } from '@kit.ScanKit';
```

#### ViewControl

相机控制参数。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

**可选**

**说明**

width

number

否

否

[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件的宽，默认使用单位为vp，支持px、lpx和vp。

height

number

否

否

XComponent组件的高，默认使用单位为vp，支持px、lpx和vp。

surfaceId

string

否

否

XComponent持有surface的ID。

1. ViewControl的width和height需和XComponent的保持一致，start接口根据设置宽高值会匹配最接近相机分辨率，当未匹配到合适分辨率，接口会返回1000500001内部错误。XComponent组件为预览流提供的Surface，而XComponent的能力由UI提供，相关介绍可参见[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)。
1. 当开发设备为折叠屏时，折叠态切换时需自行调整XComponent的宽高，start接口会重新适配相机分辨率比例。

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct customScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'onLoad is called')
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, 'viewControl', `onLoad surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '[Scan Sample]',
                `Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}`);
            }).catch((error: BusinessError) => {
              hilog.error(0x0001, '[Scan Sample]',
                `Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}`);
            })
          } catch (error) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

#### ScanFrame

相机预览流（YUV）。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

**可选**

**说明**

byteBuffer

ArrayBuffer

否

否

相机预览流的ArrayBuffer数组。

width

number

否

否

相机预览流的宽度，单位：px。

height

number

否

否

相机预览流的高度，单位：px。

scanCodeRects

Array<scanBarcode.[ScanCodeRect](../components/scanBarcode (默认界面扫码).md#section1456184716188)>

否

是

相机预览流的码图检测位置信息。

**设备行为差异：**该属性在带有Kirin NPU（Neural-network Processing Unit，神经网络处理器）的设备可正常返回，在不带有Kirin NPU的设备上返回null。

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct customScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  private callback: AsyncCallback<scanBarcode.ScanResult[]> =
    async (error: BusinessError, result: scanBarcode.ScanResult[]) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
    }
  // 回调获取ScanFrame
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    async (error: BusinessError, frameResult: customScan.ScanFrame) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      // byteBuffer相机YUV图像数组
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanFrame.byteBuffer.byteLength:  ${frameResult.byteBuffer.byteLength}`);
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanFrame.scanCodeRect: ${JSON.stringify(frameResult.scanCodeRects)}`);
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (error) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

1. scanCodeRects返回为横向预览流中的码图位置检测信息，如需后续处理，需要将位置转换为纵向坐标系，数组中每一个元素left、top、right、bottom参数转换逻辑，以手机设备竖屏、充电口向下为例，以scanCodeRects第一个元素为例：

```ets
// start接口frameCallback回调返回frameResult数据
import { customScan, scanBarcode } from '@kit.ScanKit';
// 模拟相机预览流返回数据frameResult: customScan.ScanFrame
let frameResult: customScan.ScanFrame = {
  "width": 1920,
  "height": 1080,
  // buffer 为相机流
"byteBuffer": buffer,
  "scanCodeRects": [{
    "left": 84,
    "top": 142,
    "right": 1695,
    "bottom": 996
  }]
};
if (frameResult && frameResult.scanCodeRects) {
  let rect: scanBarcode.ScanCodeRect = frameResult.scanCodeRects[0];
  // 预览流尺寸转换为显示组件XComponent尺寸比例，例如设置的scanWidth为360vp
  let scanWidth = 360;
  let ratio = scanWidth / frameResult.height;
  let left = (frameResult.height - rect.bottom) * ratio;
  let top = rect.left * ratio;
  let right = (frameResult.height - rect.top) * ratio;
  let bottom = rect.right * ratio;
}
```

1. 对应的二维码区域位置可以使用固定定位position({x: left, y: top})，宽度width: right - left，高度height: bottom - top，画出二维码实际区域范围。

#### customScan.init

init(options?: scanBarcode.ScanOptions): void

初始化自定义界面扫码。

**需要权限：**ohos.permission.CAMERA

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

options

scanBarcode.[ScanOptions](../components/scanBarcode (默认界面扫码).md#section1285191073117)

否

自定义界面扫码参数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

从5.0.2(14)开始，customScan模块的init接口新增错误码201。

- 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块init接口，返回错误码1000500001。
- 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块init接口，返回错误码201。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

**示例：**

```ets
import { scanBarcode, scanCore, customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: true
};
try {
  customScan.init(options);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to init customScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.start

start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>

启动扫码相机流，使用Promise异步回调获取扫码结果。

此接口需要在init接口调用后才能使用。

**需要权限：**ohos.permission.CAMERA

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

viewControl

[ViewControl](#section8604949165313)

是

相机控制参数。

**返回值：**

**类型**

**说明**

Promise<Array<scanBarcode.[ScanResult](../components/scanBarcode (默认界面扫码).md#section10614317162112)>>

Promise对象，返回启动相机流扫码结果对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

从5.0.2(14)开始，customScan模块的start接口新增错误码201。

- 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
- 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块start接口，返回错误码201。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct customScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '[Scan Sample]',
                `Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}`);
            }).catch((error: BusinessError) => {
              hilog.error(0x0001, '[Scan Sample]',
                `Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}`);
            });
          } catch (error) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

#### customScan.start

start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void

启动扫码相机流，使用Callback异步回调获取扫码结果、相机预览流（YUV-图像格式NV21基于4:2:0采样）。

此接口需要在init接口调用后才能使用。

**需要权限：**ohos.permission.CAMERA

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

viewControl

[ViewControl](#section8604949165313)

是

相机控制参数。

callback

AsyncCallback<Array<scanBarcode.[ScanResult](../components/scanBarcode (默认界面扫码).md#section10614317162112)>>

是

回调函数，当启动相机流扫码成功，err为undefined，data为获取到的Array<scanBarcode.[ScanResult](../components/scanBarcode (默认界面扫码).md#section10614317162112)>；否则为错误对象。

frameCallback

AsyncCallback<[ScanFrame](#section1670633211200)>

否

回调函数，当启动相机流成功，err为undefined，data为获取到的相机预览流（YUV）[ScanFrame](#section1670633211200)；否则为错误对象。

**起始版本：**5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

从5.0.2(14)开始，customScan模块的start接口新增错误码201。

- 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
- 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块start接口，返回错误码201。

错误码ID

错误信息

201

Permission denied.

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct customScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // 返回自定义扫描结果的回调
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    async (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
    }
  // 回调获取ScanFrame
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    async (error: BusinessError, scanFrame: customScan.ScanFrame) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanFrame by callback, scanFrame is ${JSON.stringify(scanFrame)}`);
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (error) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

#### customScan.getFlashLightStatus

getFlashLightStatus(): boolean

获取当前相机闪光灯状态。

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**返回值：**

**类型**

**说明**

boolean

返回当前相机闪光灯状态。true代表开启，false代表关闭。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // 根据当前闪光灯状态，选择打开或关闭闪光灯
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${error.code}, message: ${error.message}`);
    }
  }
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.openFlashLight

openFlashLight(): void

开启相机闪光灯。

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // 根据当前闪光灯状态，选择打开或关闭闪光灯
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${error.code}, message: ${error.message}`);
    }
  }
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.closeFlashLight

closeFlashLight(): void

关闭相机闪光灯。

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}`);
}
// 根据当前闪光灯状态，选择打开或关闭闪光灯
if (flashLightStatus) {
  try {
    customScan.closeFlashLight();
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}`);
  }
} else {
  try {
    customScan.openFlashLight();
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${error.code}, message: ${error.message}`);
  }
}
```

#### customScan.setZoom

setZoom(zoomValue: number): void

设置变焦比。变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

本接口必须在启动相机流start接口后使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

**必填**

**说明**

zoomValue

number

是

相机变焦比，精度最高为小数点后两位（例如1.45）。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 设置变焦比
let zoomValue = 2.0;
try {
  customScan.setZoom(zoomValue);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setZoom. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.getZoom

getZoom(): number

获取当前的变焦比。

本接口必须在启动相机流start接口后使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**返回值：**

**类型**

**说明**

number

返回当前的变焦比。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

try {
  // 获取变焦比
  let zoomValue = customScan.getZoom();
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting zoomValue, zoomValue is ${zoomValue}`);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to get zoomValue. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.setFocusPoint

setFocusPoint(point: scanBarcode.Point): void

设置相机焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

本接口必须在启动相机流start接口后使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

**必填**

**说明**

point

scanBarcode.[Point](../components/scanBarcode (默认界面扫码).md#section9634457911)

是

焦点。x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 设置对焦点
  customScan.setFocusPoint({ x: 0.5, y: 0.5 });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setFocusPoint. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.resetFocus

resetFocus(): void

设置连续自动对焦模式。

本接口必须在启动相机流start接口后使用。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 设置连续自动对焦模式
  customScan.resetFocus();
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to resetFocus. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.on('lightingFlash')

on(type: 'lightingFlash', callback: AsyncCallback<boolean>): void

订阅闪光灯状态监听事件，当环境昏、亮状态变化时，使用callback异步回调返回打开时机。

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

**必填**

**说明**

type

string

是

事件回调类型，固定为'lightingFlash'，当环境亮度发生变时触发。可用于提示用户打开或关闭闪光灯。

callback

AsyncCallback<boolean>

是

回调函数。返回true表示当前环境暗，可以提示用户打开闪光灯，false表示环境亮，可以提示用户关闭闪光灯。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (error: BusinessError, bool: boolean) => {
  if (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to light Flash by callback. Code: ${error.code}, message: ${error.message}`);
    return;
  }
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in lighting Flash by callback, bool is ${bool}`);
}

try {
  customScan.on('lightingFlash', callback);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to listen lightingFlash. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.off('lightingFlash')

off(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void

注销闪光灯状态监听事件。

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

type

string

是

事件回调类型，固定为'lightingFlash'，当环境亮度发生变化时触发，可用于提示用户打开或关闭闪光灯。

callback

AsyncCallback<boolean>

否

需要被注销的回调函数，若callback不填，则注销所有绑定在'lightingFlash'上的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (error: BusinessError, bool: boolean) => {
  if (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to cancel Flash by callback. Code: ${error.code}, message: ${error.message}`);
    return;
  }
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in cancelling Flash by callback, bool is ${bool}`);
}
// 可以不填callback，取消lightingFlash所有监听。填写callback，必须保持和customScan.on中监听的事件保持一致
try {
  customScan.off('lightingFlash', callback);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to listen lightingFlash. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.rescan

rescan(): void

触发一次重新扫码。如果扫描结果不是预期结果，可以调用此接口触发下一次扫描。

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出内部错误的异常。

仅对start接口的Callback异步回调有效，Promise异步回调接口无效。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct customScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // 返回自定义扫描结果的回调
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    async (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
      // 重新触发扫码。如需不重启相机并重新触发一次扫码，可以在start接口的Callback异步回调中，调用rescan接口。
      try {
        customScan.rescan();
      } catch (error) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to rescan customScan. Code: ${error.code}, message: ${error.message}`);
      }
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback);
          } catch (error) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

#### customScan.setAutoZoomEnabled

setAutoZoomEnabled(enabled: boolean): void

设置自动变焦能力的开启和关闭。未调用时默认开启自动变焦。

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

enabled

boolean

是

是否开启自动变焦能力。true代表开启，false代表关闭。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 开启或关闭自动变焦能力，true为开启，false为关闭
  customScan.setAutoZoomEnabled(false);
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setAutoZoomEnabled. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.stop

stop(): Promise<void>

暂停扫码相机流，使用Promise异步回调。

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**返回值：**

**类型**

**说明**

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop().then(() => {
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by promise');
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to stop scan by promise. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to stop customScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.stop

stop(callback: AsyncCallback<void>): void

暂停扫码相机流，使用Callback异步回调。

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

callback

AsyncCallback<void>

是

回调函数。当暂停相机流成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop((error: BusinessError) => {
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to stop scan by callback. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by callback');
  })
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to stop customScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.release

release(): Promise<void>

释放扫码相机流，使用Promise异步回调。

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**返回值：**

**类型**

**说明**

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release().then(() => {
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by promise');
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to release scan by promise. Code: ${error.code}, message: ${error.message}`);
  })
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to release customScan. Code: ${error.code}, message: ${error.message}`);
}
```

#### customScan.release

release(callback: AsyncCallback<void>): void

释放扫码相机流，使用Callback异步回调。

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：**SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

**必填**

**说明**

callback

AsyncCallback<void>

是

回调函数。当释放相机流成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1000500001

Internal error.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release((error: BusinessError) => {
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to release scan by callback. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by callback');
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to release customScan. Code: ${error.code}, message: ${error.message}`);
}
```