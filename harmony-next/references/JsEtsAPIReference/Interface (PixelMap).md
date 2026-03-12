# Interface (PixelMap)

图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[image.createPixelMap](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmap8)创建一个PixelMap实例。目前pixelmap序列化大小最大128MB，超过会送显失败。大小计算方式为(宽*高*每像素占用字节数)。

从API version 11开始，PixelMap支持通过worker跨线程调用。当PixelMap通过[Worker](@ohos.worker (启动一个Worker).md)跨线程后，原线程的PixelMap的所有接口均不能调用，否则将报错501 服务器不具备完成请求的功能。

在调用PixelMap的方法前，可以通过[image.createPixelMap](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmap8)传入像素数据创建一个PixelMap对象，也可以通过[ImageSource](Interface (ImageSource).md)进行图片解码创建PixelMap对象。

开发元服务请通过[ImageSource](Interface (ImageSource).md)构建PixelMap对象。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 7开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明isEditable7+boolean是否

图像像素是否可被编辑。true表示可被编辑，false表示不可被编辑。为false时，图像的渲染和传输性能更好。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

isStrideAlignment11+boolean是否图像的行数据是否已进行内存对齐。true表示已进行内存对齐，每行数据的末尾可能有空白字节填充以满足对齐要求；false表示未进行内存对齐，每行数据紧密排列，末尾无空白字节填充。

#### readPixelsToBuffer7+

readPixelsToBuffer(dst: ArrayBuffer): Promise<void>

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dstArrayBuffer是缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info('Succeeded in reading image pixel data.'); // 符合条件则进入。
    }).catch((error: BusinessError) => {
      console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
    })
  }
}
```

#### readPixelsToBuffer7+

readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dstArrayBuffer是缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。callbackAsyncCallback<void>是回调函数。当读取像素数据到ArrayBuffer成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer, (error: BusinessError, res: void) => {
      if(error) {
        console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
        return;
      } else {
        console.info('Succeeded in reading image pixel data.');  // 符合条件则进入。
      }
    })
  }
}
```

#### readPixelsToBufferSync12+

readPixelsToBufferSync(dst: ArrayBuffer): void

按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，同步返回结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dstArrayBuffer是缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function ReadPixelsToBufferSync(pixelMap : image.PixelMap) {
  const bufferSize = pixelMap.getPixelBytesNumber();
  const readBuffer = new ArrayBuffer(bufferSize);
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBufferSync(readBuffer);
  }
}
```

#### readPixels7+

readPixels(area: PositionArea): Promise<void>

固定按照BGRA_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定。使用Promise异步回调。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width * height}）* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width * height}）* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域大小，根据区域读取。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
      console.info('RGBA data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// 不符合条件则进入。
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
      console.info('YUV data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// 不符合条件则进入。
    })
  }
}
```

#### readPixels7+

readPixels(area: PositionArea, callback: AsyncCallback<void>): void

固定按照BGRA_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定，使用callback形式返回。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width * height}）* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width * height}）* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域大小，根据区域读取。callbackAsyncCallback<void>是回调函数。当读取区域内的图片数据成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('RGBA data is ', new Uint8Array(area.pixels));
      }
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('YUV data is ', new Uint8Array(area.pixels));
      }
    })
  }
}
```

#### readPixelsSync12+

readPixelsSync(area: PositionArea): void

固定按照BGRA_8888格式，读取PixelMap指定区域内的图像像素数据，并写入[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定，同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域大小，根据区域读取。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function ReadPixelsSync(pixelMap : image.PixelMap) {
  const area : image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixelsSync(area);
  }
}
```

#### writePixels7+

writePixels(area: PositionArea): Promise<void>

固定按照BGRA_8888格式，读取[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定。使用Promise异步回调。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width * height}）* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width * height}）* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域，根据区域写入。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width *1.5。
    offset: 0,
    stride: 8, // PixelMap为yuv格式时，writePixels函数不使用该变量。
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}
```

#### writePixels7+

writePixels(area: PositionArea, callback: AsyncCallback<void>): void

固定按照BGRA_8888格式，读取[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定，使用callback形式返回。

可用公式计算PositionArea需要申请的内存大小。

YUV的区域计算公式：读取区域（region.size{width * height}）* 1.5 （1倍的Y分量+0.25倍U分量+0.25倍V分量）

RGBA的区域计算公式：读取区域（region.size{width * height}）* 4 （1倍的R分量+1倍G分量+1倍B分量+1倍A分量）

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域，根据区域写入。callbackAsyncCallback<void>是回调函数，当写入成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(8), // 8为需要创建的像素buffer大小，取值为：height * width *4。
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(6), // 6为需要创建的像素buffer大小，取值为：height * width * 1.5。
    offset: 0,
    stride: 8, // PixelMap为yuv格式时，writePixels函数不使用该变量。
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}
```

#### writePixelsSync12+

writePixelsSync(area: PositionArea): void

固定按照BGRA_8888格式，读取[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7).region指定，同步返回结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[PositionArea](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域，根据区域写入。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function WritePixelsSync(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixelsSync(area);
  }
}
```

#### writeBufferToPixels7+

writeBufferToPixels(src: ArrayBuffer): Promise<void>

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明srcArrayBuffer是缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color).then(() => {
      console.info("Succeeded in writing data from a buffer to a PixelMap.");
    }).catch((error: BusinessError) => {
      console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### writeBufferToPixels7+

writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明srcArrayBuffer是缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。callbackAsyncCallback<void>是回调函数。当缓冲区中的图像像素数据写入PixelMap成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96);  // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
        return;
      } else {
        console.info("Succeeded in writing data from a buffer to a PixelMap.");
      }
    })
  }
}
```

#### writeBufferToPixelsSync12+

writeBufferToPixelsSync(src: ArrayBuffer): void

按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap，同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明srcArrayBuffer是缓冲区，函数执行时会将该缓冲区中的图像像素数据写入到PixelMap。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605846__getpixelbytesnumber7)接口获取。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function WriteBufferToPixelsSync(pixelMap:image.PixelMap) {
  const color : ArrayBuffer = new ArrayBuffer(96);  // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr : Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixelsSync(color);
  }
}
```

#### getImageInfo7+

getImageInfo(): Promise<ImageInfo>

获取图像像素信息。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>Promise对象，返回图像像素信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
      if (imageInfo != undefined) {
        console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
      }
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### getImageInfo7+

getImageInfo(callback: AsyncCallback<ImageInfo>): void

获取图像像素信息，使用callback形式返回获取的图像像素信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>是回调函数。当获取图像像素信息成功，err为undefined，data为获取到的图像像素信息；否则为错误对象。

**示例:**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function GetImageInfoSync(pixelMap : image.PixelMap){
  if (pixelMap != undefined) {
    pixelMap.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
      if (error) {
        console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
        return;
      } else {
        console.info(`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}`);
      }
    })
  }
}
```

#### getImageInfoSync12+

getImageInfoSync(): ImageInfo

以同步方法获取图像像素信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)图像像素信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息501Resource Unavailable

**示例：**

```ets
function GetImageInfoSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
    return imageInfo;
  }
  return undefined;
}
```

#### getBytesNumberPerRow7+

getBytesNumberPerRow(): number

获取图像像素每行字节数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的行字节数。

**示例：**

```ets
function GetBytesNumberPerRow(pixelMap: image.PixelMap) {
  let rowCount: number = pixelMap.getBytesNumberPerRow();
}
```

#### getPixelBytesNumber7+

getPixelBytesNumber(): number

获取图像像素的总字节数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的总字节数。

**示例：**

```ets
function GetPixelBytesNumber(pixelMap: image.PixelMap) {
  let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
}
```

#### getDensity9+

getDensity():number

获取当前图像像素的密度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的密度，单位为ppi。

**示例：**

```ets
function GetDensity(pixelMap: image.PixelMap) {
  let getDensity: number = pixelMap.getDensity();
}
```

#### opacity9+

opacity(rate: number, callback: AsyncCallback<void>): void

通过设置透明比率来让PixelMap达到对应的透明效果，yuv图片不支持设置透明度，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明ratenumber是透明比率的值，取值范围是(0,1]。callbackAsyncCallback<void>是回调函数。当设置透明比率成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in setting opacity.");
      }
    })
  }
}
```

#### opacity9+

opacity(rate: number): Promise<void>

通过设置透明比率来让PixelMap达到对应的透明效果，yuv图片不支持设置透明度。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明ratenumber是透明比率的值，取值范围是(0,1]。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate).then(() => {
      console.info('Succeeded in setting opacity.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set opacity. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### opacitySync12+

opacitySync(rate: number): void

设置PixelMap的透明比率，yuv图片不支持设置透明度，初始化PixelMap并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明ratenumber是透明比率的值，取值范围是(0,1]。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function OpacitySync(pixelMap:image.PixelMap) {
  let rate : number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacitySync(rate);
  }
}
```

#### createAlphaPixelmap9+

createAlphaPixelmap(): Promise<PixelMap>

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的pixelmap，可用于阴影效果，yuv格式不支持此接口。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating alpha pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### createAlphaPixelmap9+

createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的pixelmap，可用于阴影效果，yuv格式不支持此接口，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[PixelMap](Interface (PixelMap).md)>是回调函数，当创建PixelMap成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap((err: BusinessError, alphaPixelMap: image.PixelMap) => {
      if (alphaPixelMap == undefined) {
        console.error(`Failed to obtain new pixel map. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in obtaining new pixel map.');
      }
    })
  }
}
```

#### createAlphaPixelmapSync12+

createAlphaPixelmapSync(): PixelMap

根据Alpha通道的信息，生成一个仅包含Alpha通道信息的PixelMap，可用于阴影效果，yuv格式不支持此接口，同步返回PixelMap类型的结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function CreateAlphaPixelmapSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let pixelmap : image.PixelMap = pixelMap.createAlphaPixelmapSync();
    return pixelmap;
  }
  return undefined;
}
```

#### scale9+

scale(x: number, y: number, callback: AsyncCallback<void>): void

根据输入的宽高的缩放倍数对图片进行缩放，使用callback形式返回。

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
1. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。callbackAsyncCallback<void>是回调函数。当对图片进行缩放成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in scaling pixelmap.");
      }
    })
  }
}
```

#### scale9+

scale(x: number, y: number): Promise<void>

根据输入的宽高的缩放倍数对图片进行缩放。使用Promise异步回调。

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
1. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### scaleSync12+

scaleSync(x: number, y: number): void

根据输入的宽高的缩放倍数对图片进行缩放，同步返回结果。

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
1. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY);
  }
}
```

#### scale12+

scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>

根据指定的缩放算法和输入的宽高的缩放倍数对图片进行缩放。使用Promise异步回调。

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
1. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)是采用的缩放算法。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function ScaleSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### scaleSync12+

scaleSync(x: number, y: number, level: AntiAliasingLevel): void

根据指定的缩放算法和输入的宽高的缩放倍数对图片进行缩放，同步返回结果。

1. 建议宽高的缩放倍数取非负数，否则会产生翻转效果。
1. 宽高的缩放倍数 = 缩放后的图片宽高 / 缩放前的图片宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)是采用的缩放算法。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}
```

#### createScaledPixelMap18+

createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

根据指定的缩放算法和输入的宽高的缩放倍数，创建一个新的缩放后的图片。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)否采用的缩放算法。

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateScaledPixelMap(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
      pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating scaledPixelMap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to create scaledPixelMap. Error code is ${error.code}, error message is ${error.message}`);
    })
  }
}
```

#### createScaledPixelMapSync18+

createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap

根据指定的缩放算法和输入的宽高的缩放倍数，创建一个新的缩放后的图片，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)否采用的缩放算法。

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function CreateScaledPixelMapSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}
```

#### createCroppedAndScaledPixelMap22+

createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

根据指定的裁剪区域、宽高的缩放倍数和缩放算法，创建一个新的裁剪并缩放后的图片。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的区域。取值范围不能超过图片的宽和高（单位：像素）。xnumber是宽度的缩放倍数。不能为0。ynumber是高度的缩放倍数。不能为0。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)否采用的缩放算法。默认值是AntiAliasingLevel.NONE。

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7600201The PixelMap has been released.7600204Invalid region.7600205Unsupported memory format or pixel format.7600301Memory alloc failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMap(pixelMap: PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
    .then((croppedAndScaled: PixelMap) => {
      console.info('PixelMap crop and scale succeeded.');
    })
    .catch((error: BusinessError) => {
      console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
    });
}
```

#### createCroppedAndScaledPixelMapSync22+

createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap

根据指定的裁剪区域、宽高的缩放倍数和缩放算法，创建一个新的裁剪并缩放后的图片。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的区域。取值范围不能超过图片的宽和高（单位：像素）。xnumber是宽度的缩放倍数。不能为0。ynumber是高度的缩放倍数。不能为0。level[AntiAliasingLevel](Enums.md#ZH-CN_TOPIC_0000002529285837__antialiasinglevel12)否采用的缩放算法。默认值是AntiAliasingLevel.NONE。

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)成功则同步返回PixelMap对象，失败则抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7600201The PixelMap has been released.7600204Invalid region.7600205Unsupported memory format or pixel format.7600301Memory alloc failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMapSync(pixelMap: PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  try {
    const croppedAndScaled = pixelMap.createCroppedAndScaledPixelMapSync(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH);
  } catch (e) {
    const error = e as BusinessError;
    console.error(`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}`);
  }
}
```

#### clone18+

clone(): Promise<PixelMap>

拷贝一份当前Pixelmap对象。使用Promise异步回调。

**系统能力：**: SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息501Resource unavailable.62980102Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data.62980103Image YUV And ASTC types are not supported.62980104Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap.62980106The image data is too large. This status code is thrown when an error occurs during the process of checking size.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.clone().then((clonePixelMap: image.PixelMap) => {
      console.info('Succeeded clone pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to clone pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### cloneSync18+

cloneSync(): PixelMap

拷贝一份当前Pixelmap对象, 同步返回结果。

**系统能力：**: SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息501Resource unavailable.62980102Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data.62980103Image YUV And ASTC types are not supported.62980104Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap.62980106The image data is too large. This status code is thrown when an error occurs during the process of checking size.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function CloneSync(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      let clonedPixelMap:image.PixelMap = pixelMap.cloneSync();
    } catch(e) {
      let error = e as BusinessError;
      console.error(`clone pixelmap error. code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

#### translate9+

translate(x: number, y: number, callback: AsyncCallback<void>): void

根据输入的坐标对图片进行位置变换，使用callback形式返回。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是区域横坐标。单位：像素。ynumber是区域纵坐标。单位：像素。callbackAsyncCallback<void>是回调函数。当对图片进行位置变换成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in translating pixelmap.");
      }
    })
  }
}
```

#### translate9+

translate(x: number, y: number): Promise<void>

根据输入的坐标对图片进行位置变换。使用Promise异步回调。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是区域横坐标。单位：像素。ynumber是区域纵坐标。单位：像素。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY).then(() => {
      console.info('Succeeded in translating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### translateSync12+

translateSync(x: number, y: number): void

根据输入的坐标对图片进行位置变换，同步返回结果。

translate后的图片尺寸改变为：width+X ，height+Y，建议translate后的图片尺寸宽高不要超过屏幕的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是区域横坐标。单位：像素。ynumber是区域纵坐标。单位：像素。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function TranslateSync(pixelMap:image.PixelMap) {
  let translateX : number = 50.0;
  let translateY : number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translateSync(translateX, translateY);
  }
}
```

#### rotate9+

rotate(angle: number, callback: AsyncCallback<void>): void

根据输入的角度对图片进行旋转，使用callback形式返回。

1. 图片旋转的角度取值范围：0-360。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
1. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明anglenumber是图片旋转的角度。callbackAsyncCallback<void>是回调函数。当对图片进行旋转成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in rotating pixelmap.");
      }
    })
  }
}
```

#### rotate9+

rotate(angle: number): Promise<void>

根据输入的角度对图片进行旋转。使用Promise异步回调。

1. 图片旋转的角度取值范围：0-360。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
1. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明anglenumber是图片旋转的角度。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle).then(() => {
      console.info('Succeeded in rotating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### rotateSync12+

rotateSync(angle: number): void

根据输入的角度对图片进行旋转，同步返回结果。

1. 图片旋转的角度取值范围：0-360。超出取值范围时，根据圆周360度自动矫正。例如，-100度与260度效果相同。
1. 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明anglenumber是图片旋转的角度。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
function RotateSync(pixelMap: image.PixelMap) {
  let angle : number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotateSync(angle);
  }
}
```

#### flip9+

flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void

根据输入的条件对图片进行翻转，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明horizontalboolean是true表示进行水平翻转，false表示不进行水平翻转。verticalboolean是true表示进行垂直翻转，false表示不进行垂直翻转。callbackAsyncCallback<void>是回调函数，当对图片翻转成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in flipping pixelmap.");
      }
    })
  }
}
```

#### flip9+

flip(horizontal: boolean, vertical: boolean): Promise<void>

根据输入的条件对图片进行翻转。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明horizontalboolean是true表示进行水平翻转，false表示不进行水平翻转。verticalboolean是true表示进行垂直翻转，false表示不进行垂直翻转。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical).then(() => {
      console.info('Succeeded in flipping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}`);
    })
  }
}
```

#### flipSync12+

flipSync(horizontal: boolean, vertical: boolean): void

根据输入的条件对图片进行翻转并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明horizontalboolean是true表示进行水平翻转，false表示不进行水平翻转。verticalboolean是true表示进行垂直翻转，false表示不进行垂直翻转。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function FlipSync(pixelMap:image.PixelMap) {
  let horizontal : boolean = true;
  let vertical : boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flipSync(horizontal, vertical);
  }
}
```

#### crop9+

crop(region: Region, callback: AsyncCallback<void>): void

根据输入的尺寸对图片进行裁剪，使用callback形式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的尺寸。取值范围不能超过图片的宽高。callbackAsyncCallback<void>是回调函数。当对图片进行裁剪成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info("Succeeded in cropping pixelmap.");
      }
    })
  }
}
```

#### crop9+

crop(region: Region): Promise<void>

根据输入的尺寸对图片进行裁剪。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的尺寸。取值范围不能超过图片的宽高。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region).then(() => {
      console.info('Succeeded in cropping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}`);

    });
  }
}
```

#### cropSync12+

cropSync(region: Region): void

根据输入的尺寸裁剪图片。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的尺寸。取值范围不能超过图片的宽高。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed501Resource Unavailable

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function CropSync(pixelMap:image.PixelMap) {
  let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.cropSync(region);
  }
}
```

#### getColorSpace10+

getColorSpace(): colorSpaceManager.ColorSpaceManager

获取图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)图像广色域信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980101If the image data abnormal.62980103If the image data unsupport.62980115If the image parameter invalid.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function GetColorSpace(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let csm = pixelMap.getColorSpace();
  }
}
```

#### setColorSpace10+

setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void

设置图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorSpace[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)是图像广色域信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980111The image source data is incomplete.62980115If the image parameter invalid.

**示例：**

```ets
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function SetColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
  let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    pixelMap.setColorSpace(csm);
  }
}
```

#### applyColorSpace11+

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void

根据输入的目标色彩空间对图像像素颜色进行色彩空间转换，使用callback形式返回。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明targetColorSpace[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)是目标色彩空间，支持SRGB、DCI_P3、DISPLAY_P3、ADOBE_RGB_1998。callbackAsyncCallback<void>是回调函数。当对图像像素颜色进行色彩空间转换成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980104Failed to initialize the internal object.62980108Failed to convert the color space.62980115Invalid image parameter.

**示例：**

```ets
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    try {
      pixelMap.applyColorSpace(targetColorSpace, (error: BusinessError) => {
        if (error) {
          console.error(`ApplyColorSpace failed. code is ${error.code}, message is ${error.message}`);
          return;
        } else {
          console.info("Succeeded ApplyColorSpace.");
        }
      });
    } catch (error) {
      console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
      return;
    }
    console.info('Succeeded in applying color space for pixelmap object.');
  }
}
```

#### applyColorSpace11+

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>

根据输入的目标色彩空间对图像像素颜色进行色彩空间转换。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明targetColorSpace[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)是目标色彩空间，支持SRGB、DCI_P3、DISPLAY_P3、ADOBE_RGB_1998。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980104Failed to initialize the internal object.62980108Failed to convert the color space.62980115Invalid image parameter.

**示例：**

```ets
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
      pixelMap.applyColorSpace(targetColorSpace).then(() => {
      console.info('Succeeded in applying color space for pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to apply color space for pixelmap object, error code is ${error}`);
      return;
    });
  }
}
```

#### toSdr12+

toSdr(): Promise<void>

将HDR的图像内容转换为SDR的图像内容。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980137Invalid image operation.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ToSdr(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地hdr图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    pixelmap.toSdr().then(() => {
      let imageInfo = pixelmap.getImageInfoSync();
      console.info("after toSdr ,imageInfo isHdr:" + imageInfo.isHdr);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set sdr. code is ${err.code}, message is ${err.message}`);
    });
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

#### getMetadata12+

getMetadata(key: HdrMetadataKey): HdrMetadataValue

从PixelMap中获取元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明key[HdrMetadataKey](Enums.md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)是HDR元数据的关键字，可用于查询对应值。

**返回值：**

类型说明[HdrMetadataValue](Types.md#ZH-CN_TOPIC_0000002529445811__hdrmetadatavalue12)返回元数据的值。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource unavailable.62980173The DMA memory does not exist.62980302Memory copy failed. Possibly caused by invalid metadata value.

**示例：**

```ets
async function GetMetadata(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地hdr图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    try {
      let staticMetadata = pixelmap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info(`getMetadata:${staticMetadata}`);
    } catch (e) {
      console.error('pixelmap create failed' + e);
    }
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

#### setMetadata12+

setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>

设置PixelMap元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明key[HdrMetadataKey](Enums.md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)是HDR元数据的关键字，用于设置对应值。value[HdrMetadataValue](Types.md#ZH-CN_TOPIC_0000002529445811__hdrmetadatavalue12)是元数据的值。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource unavailable.62980173The DMA memory does not exist.62980302Memory copy failed. Possibly caused by invalid metadata value.

**示例：**

创建DMA_ALLOC内存的PixelMap方法请参考: [系统默认的内存分配方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#系统默认的内存分配方式)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import {image} from '@kit.ImageKit';

function SetMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方链接。
  let staticMetadata: image.HdrStaticMetadata = {
    displayPrimariesX: [1.1, 1.1, 1.1],
    displayPrimariesY: [1.2, 1.2, 1.2],
    whitePointX: 1.1,
    whitePointY: 1.2,
    maxLuminance: 2.1,
    minLuminance: 1.0,
    maxContentLightLevel: 2.1,
    maxFrameAverageLightLevel: 2.1,
  };
  pixelMap.setMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA, staticMetadata).then(() => {
    console.info('Succeeded in setting pixelMap metadata.');
  }).catch((error: BusinessError) => {
    console.error("Failed to set the metadata.code ", error);
  })
}
```

#### setTransferDetached12+

setTransferDetached(detached: boolean): void

pixelmap在跨线程传输时，断开原线程的引用。适用于需立即释放pixelmap的场景。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明detachedboolean是true表示断开原线程引用，false表示不断开原线程引用。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息501Resource Unavailable

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
// 子线程方法。
async function loadPixelMap(rawFileDescriptor: number): Promise<PixelMap> {
  // 创建imageSource。
  const imageSource = image.createImageSource(rawFileDescriptor);
  // 创建pixelMap。
  const pixelMap = imageSource.createPixelMapSync();
  // 释放imageSource。
  imageSource.release();
  // 使pixelMap在跨线程传输完成后，断开原线程的引用。
  pixelMap.setTransferDetached(true);
  // 返回pixelMap给主线程。
  return pixelMap;
}

@Entry
@Component
struct Demo {
  @State pixelMap: PixelMap | undefined = undefined;
  // 主线程方法。
  private loadImageFromThread(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr = context.resourceManager;
    // 此处‘example.jpg’仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
    resourceMgr.getRawFd('example.jpg').then(rawFileDescriptor => {
      taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
        if (pixelMap) {
          this.pixelMap = pixelMap as PixelMap;
          console.log('Succeeded in creating pixelMap.');
          // 主线程释放pixelMap。由于子线程返回pixelMap时已调用setTransferDetached，所以此处能够立即释放pixelMap。
          this.pixelMap.release();
        } else {
          console.error('Failed to create pixelMap.');
        }
      });
    });
  }
  build() {
    // ...
  }
}
```

#### marshalling10+

marshalling(sequence: rpc.MessageSequence): void

将PixelMap序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是新创建的MessageSequence。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980115Invalid image parameter.62980097IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory.

**示例：**

```ets
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelMap : image.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence : rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
        })
      })
    });
    return true;
  }
}
async function Marshalling() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let ret: MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}
```

#### unmarshalling10+

unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>

从MessageSequence中获取PixelMap，如需使用同步方式创建PixelMap可使用：[createPixelMapFromParcel](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromparcel11)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是保存有PixelMap信息的MessageSequence。

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980115Invalid image parameter.62980097IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory.62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.

**示例：**

```ets
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelMap: image.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : image.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
          console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
        })
      })
    });
    return true;
  }
}
async function Unmarshalling() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap : image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data : rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let ret : MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}
```

#### release7+

release(): Promise<void>

释放PixelMap对象（释放后，任何访问该对象内部数据的方法调用都会失败）。使用Promise异步回调。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### release7+

release(callback: AsyncCallback<void>): void

释放PixelMap对象（释放后，任何访问该对象内部数据的方法调用都会失败）。使用callback形式返回释放结果。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当对PixelMap对象释放成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.release((err: BusinessError) => {
      if (err) {
        console.error(`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in releasing pixelmap object.');
      }
    })
  }
}
```

#### convertPixelFormat12+

convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>

YUV和RGB类型互转。使用Promise异步回调。

支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB_P010/YCBCR_P010与RGBA1010102互转。

从API18开始，可用于ASTC_4x4类型转为RGBA_8888类型，目前仅支持ASTC_4x4转为RGBA_8888。

仅在ASTC_4x4格式的图像需要进行像素访问时，建议调用此接口将ASTC_4x4类型转为RGBA_8888类型。由于使用ASTC_4x4反解为RGBA_8888时延较高，其余情况下不推荐使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明targetPixelFormat[PixelMapFormat](Enums.md#ZH-CN_TOPIC_0000002529285837__pixelmapformat7)是目标像素格式，用于YUV和RGB类型互转，或者ASTC_4x4类型转为RGBA_8888类型。目前仅支持NV12/NV21与RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16互转，YCRCB_P010/YCBCR_P010与RGBA1010102互转，ASTC_4x4转为RGBA_8888。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980111The image source data is incomplete.62980115Invalid input parameter.62980178Failed to create the pixelmap.62980274The conversion failed62980276The type to be converted is an unsupported target pixel format

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ConvertPixelFormat(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    // 设置目标像素格式为NV12。
    let targetPixelFormat = image.PixelMapFormat.NV12;
    pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
      // pixelMap转换成NV12格式成功。
      console.info('PixelMapFormat convert Succeeded');
    }).catch((error: BusinessError) => {
      // pixelMap转换成NV12格式失败。
      console.error(`PixelMapFormat convert Failed. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### setMemoryNameSync13+

setMemoryNameSync(name: string): void

设置PixelMap内存标识符。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明namestring是pixelmap内存标识符，只允许DMA和ASHMEM内存形式的pixelmap设置。DMA内存设置名字长度取值范围为[1, 255]，ASHMEM内存设置名字长度取值范围为[1, 244]，单位字节。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.The length of the input parameter is too long. 2.Parameter verification failed.501Resource unavailable.62980286Memory format not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function SetMemoryNameSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      pixelMap.setMemoryNameSync("PixelMapName Test");
    } catch(e) {
      let error = e as BusinessError;
      console.error(`setMemoryNameSync error. code is ${error.code}, message is ${error.message}`);
    }
  }
}
```

#### getUniqueId22+

getUniqueId(): number

获取PixelMap的唯一ID。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number唯一ID。取值为正整数。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7600201The PixelMap has been released.

**示例：**

```ets
function DemoGetUniqueId(pixelMap: PixelMap) {
  const uniqueId: number = pixelMap.getUniqueId();
}
```

#### isReleased22+

isReleased(): boolean

检查PixelMap对象是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失败。

释放指的是ArkTS对象释放与之关联的native对象的管理权。仅当所有管理该native对象的ArkTS对象都被释放时，native对象占用的内存才会被回收。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明booleanPixelMap是否已被释放。返回true表示已被释放，否则返回false。

**示例：**

```ets
async function DemoIsReleased(pixelMap: PixelMap) { // 未释放的PixelMap。
  pixelMap.isReleased(); // 返回false。
  await pixelMap.release();
  pixelMap.isReleased(); // 返回true。
}
```