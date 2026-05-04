# detectBarcode (图像识码)

本模块提供本地图片识码和图像数据识码能力，支持对图像中的条形码、二维码、MULTIFUNCTIONAL CODE进行识别。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts)接入。

起始版本： 4.1.0(11)

**导入模块**

```ets
import { detectBarcode } from '@kit.ScanKit';
```

**InputImage**

待识别的图片信息。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 图片路径，例如file://media/Photo/x/xxx.jpg。 |

示例：

推荐使用[picker](../../guides/使用Picker选择媒体库资源.md)获取图片路径。

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
photoSelectOptions.isPhotoTakingSupported = false;
photoSelectOptions.isEditSupported = false;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoSelectOptions).then((result: photoAccessHelper.PhotoSelectResult) => {
  if (!result || (result.photoUris && result.photoUris.length === 0)) {
    hilog.error(0x0001, 'picker', 'Failed to get PhotoSelectResult by promise');
    return;
  }
  hilog.info(0x0001, 'picker', `Succeeded in getting PhotoSelectResult by promise.`);
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${error.code}`);
});
```

**detectBarcode.decode**

decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>

通过配置参数调用图片识码，使用Promise异步回调返回识码结果。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | InputImage | 是 | 待识别的图片信息。 |
| options | scanBarcode.ScanOptions | 否 | 启动图片识码参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<scanBarcode.ScanResult>> | Promise对象，返回识码结果对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

示例：

```ets
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义识码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
// 通过picker拉起图库并选择图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // 定义识码参数inputImage，其中uri为picker选择图片
  let inputImage: detectBarcode.InputImage = { uri: result.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, options).then((result: Array<scanBarcode.ScanResult>) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${error.code}, message: ${error.message}`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${error.code}.`);
});
```

**detectBarcode.decode**

decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

通过配置参数调用图片识码，使用Callback异步回调返回识码结果。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | InputImage | 是 | 待识别的图片信息。 |
| options | scanBarcode.ScanOptions | 是 | 启动图片识码参数。 |
| callback | AsyncCallback<Array<scanBarcode.ScanResult>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.ScanResult>，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

示例：

```ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义识码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true }
// 通过选择模式拉起photoPicker界面，用户可以选择一个图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // 定义识码参数inputImage，其中uri为picker选择图片
  let inputImage: detectBarcode.InputImage = { uri: result.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, options, (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error && error.code) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${error.code}, message: ${error.message}`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${error.code}`);
});
```

**detectBarcode.decode**

decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

图片识码，使用Callback异步回调返回识码结果。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | InputImage | 是 | 待识别的图片信息。 |
| callback | AsyncCallback<Array<scanBarcode.ScanResult>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.ScanResult>，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

示例：

```ets
import { scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 通过picker拉起图库并选择图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // 定义识码参数inputImage，其中uri为picker选择图片
  let inputImage: detectBarcode.InputImage = { uri: result.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error && error.code) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
    });
  } catch (error) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${error.code}, message: ${error.message}`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${error.code}`);
});
```

**ByteImage**

待识别的图像数据。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| byteBuffer | ArrayBuffer | 否 | 否 | 图像数据。 |
| width | number | 否 | 否 | 图像宽度，单位：px。 |
| height | number | 否 | 否 | 图像高度，单位：px。 |
| format | ImageFormat | 否 | 否 | 图像数据类型。 |

示例：

```ets
import { detectBarcode } from '@kit.ScanKit';

// YUV图像的buffer, height, width数据，可通过相机预览流数据获取，比如获取宽高是1920*1080时
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: buffer,
  width: 1920,
  height: 1080,
  format: detectBarcode.ImageFormat.NV21
};
```

**ImageFormat**

枚举，图像数据类型。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NV21 | 0 | 图像格式为NV21。 |

**DetectResult**

识别结果。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanResults | Array<scanBarcode.ScanResult> | 否 | 否 | 扫码结果。 |
| zoomValue | number | 否 | 否 | 相机可变焦距比，通过setZoomRatio控制相机实现变焦功能。 说明： 1. 使用Camera Kit getZoomRatio接口获取相机当前变焦比zoomRatio。 2. 使用Camera Kit setZoomRatio接口设置targetRatio，目标值为zoomRatio * zoomValue。 |

**detectBarcode.decodeImage**

decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise<DetectResult>

通过配置参数调用图像数据识码能力，使用Promise异步回调返回识码结果。

系统能力： SystemCapability.Multimedia.Scan.ScanBarcode

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ByteImage | 是 | 待识别的图像数据。 |
| options | scanBarcode.ScanOptions | 否 | 启动图像数据识码参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<DetectResult> | Promise对象，返回图像数据识码结果对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

示例：

```ets
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 优先获取图像的YUVByteBuffer, YUVHeight, YUVWidth数据，比如获取宽高是1920*1080时
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: YUVByteBuffer,
  width: 1920,
  height: 1080,
  format: detectBarcode.ImageFormat.NV21
};
let options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: false
};
try {
  detectBarcode.decodeImage(byteImg, options).then((result: detectBarcode.DetectResult) => {
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting DetectResult by promise with options, result is ${JSON.stringify(result)}`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to get DetectResult by promise with options. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to decode Image. Code: ${error.code}, message: ${error.message}`);
}
```

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

不支持并行调用。