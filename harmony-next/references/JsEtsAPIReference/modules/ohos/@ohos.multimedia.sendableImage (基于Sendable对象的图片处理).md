# @ohos.multimedia.sendableImage (基于Sendable对象的图片处理)

本模块基于Sendable对象，提供图片处理效果，包括通过属性创建PixelMap、读取图像像素数据、读取区域内的图片数据等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sendableImage } from '@kit.ImageKit';
```

#### sendableImage.createPixelMap

createPixelMap(colors: ArrayBuffer, options: image.InitializationOptions): Promise<PixelMap>

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是默认按照BGRA_8888格式处理的颜色数组。options[image.InitializationOptions](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。

**返回值：**

类型说明Promise<[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)>

返回PixelMap。

当创建的PixelMap大小超过原图大小时，返回原图PixelMap大小。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo() {
    const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
    let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
    sendableImage.createPixelMap(color, opts).then((pixelMap: sendableImage.PixelMap) => {
        console.info('Succeeded in creating pixelmap.');
    }).catch((error: BusinessError) => {
        console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
    })
}
```

#### sendableImage.createPixelMapFromParcel

createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap

从MessageSequence中获取PixelMap。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是保存有PixelMap信息的MessageSequence。

**返回值：**

类型说明[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980096Operation failed62980097IPC error62980115Invalid input parameter62980105Failed to get the data62980177Abnormal API environment62980178Failed to create the PixelMap62980179Abnormal buffer size62980180FD mapping failed62980246Failed to read the PixelMap

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  pixel_map: sendableImage.PixelMap;
  constructor(conPixelmap: sendableImage.PixelMap) {
    this.pixel_map = conPixelmap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    try {
      this.pixel_map = sendableImage.createPixelMapFromParcel(messageSequence);
    } catch(e) {
      let error = e as BusinessError;
      console.error(`createPixelMapFromParcel error. code is ${error.code}, message is ${error.message}`);
      return false;
    }
    return true;
  }
}
async function Demo() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 4,
    size: { height: 4, width: 6 },
    alphaType: 3
  }
  let pixelMap: sendableImage.PixelMap | undefined = undefined;
  await sendableImage.createPixelMap(color, opts).then((srcPixelMap: sendableImage.PixelMap) => {
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

    // 获取到PixelMap。
    let newPixelMap = ret.pixel_map;
  }
}
```

#### sendableImage.createPixelMapFromSurface

createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>

根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8).size指定。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明surfaceIdstring是对应Surface的ID，可通过预览组件获取，如[XComponent](../../topics/components/XComponent.md)组件。region[image.Region](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先获取整个画面，再使用[crop](#ZH-CN_TOPIC_0000002497605848__crop)截取所需区域。

**返回值：**

类型说明Promise<[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)>成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980115If the image parameter invalid.62980105Failed to get the data62980178Failed to create the PixelMap

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  sendableImage.createPixelMapFromSurface(surfaceId, region).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
  });
}
```

#### sendableImage.createPixelMapSync

createPixelMapSync(colors: ArrayBuffer, options: image.InitializationOptions): PixelMap

通过属性创建PixelMap，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是BGRA_8888格式的颜色数组。options[image.InitializationOptions](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。

**返回值：**

类型说明[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo() {
    const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
    let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
    let pixelMap : sendableImage.PixelMap = sendableImage.createPixelMapSync(color, opts);
    return pixelMap;
}
```

#### sendableImage.convertFromPixelMap

convertFromPixelMap(pixelmap: image.PixelMap): PixelMap

通过image下的PixelMap创建出一个sendableImage下的PixelMap，同步返回PixelMap结果。原PixelMap的方法均不可再调用。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明pixelmap[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)是image下的非sendable的PixelMap。

**返回值：**

类型说明[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)成功同步返回sendable的PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401If the image parameter invalid. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.62980104Failed to initialize the internal object.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
  let sendablePixelMap : sendableImage.PixelMap = sendableImage.convertFromPixelMap(pixelMap);
  return sendablePixelMap;
}
```

#### sendableImage.convertToPixelMap

convertToPixelMap(pixelmap: PixelMap): image.PixelMap

通过sendableImage下的PixelMap创建出一个image下的PixelMap，同步返回PixelMap结果。原PixelMap的方法均不可再调用。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明pixelmap[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)是sendableImage下的PixelMap。

**返回值：**

类型说明[image.PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回image下的非sendable的PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401If the image parameter invalid. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.62980104Failed to initialize the internal object.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  let sendablePixelMap : sendableImage.PixelMap = sendableImage.createPixelMapSync(color, opts);
  let pixelMap : image.PixelMap = sendableImage.convertToPixelMap(sendablePixelMap);
  return pixelMap;
}
```

#### ISendable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**系统能力：** SystemCapability.Multimedia.Image.Core

类型说明[lang.ISendable](../other/@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002497444768__langisendable)所有Sendable类型的父类型。

#### PixelMap

图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](#ZH-CN_TOPIC_0000002497605848__sendableimagecreatepixelmap)创建一个PixelMap实例。目前pixelmap序列化大小最大128MB，超过会送显失败。大小计算方式为(宽*高*每像素占用字节数)。

sendableImage下的PixelMap支持sendable属性，支持worker线程共享。sendableImage下的PixelMap，可以利用[Convert](#ZH-CN_TOPIC_0000002497605848__sendableimageconverttopixelmap)方法与image下的PixelMap进行互相转换。转换后，原对象的方法均不允许再调用，否则将报错501 无法调用接口。跨线程处理PixelMap时，需要考虑多线程问题。

在调用PixelMap的方法前，需要先通过[sendableImage.createPixelMap](#ZH-CN_TOPIC_0000002497605848__sendableimagecreatepixelmap)构建一个PixelMap对象。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明isEditableboolean是否

true表示图像像素可被编辑，false表示不可被编辑。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isStrideAlignmentboolean是否true表示图像内存为DMA内存，false表示非DMA内存。DMA内存的PixelMap会做256字节内存对齐，行末会存在padding区域。

#### readPixelsToBuffer

readPixelsToBuffer(dst: ArrayBuffer): Promise<void>

读取图像像素数据，结果写入ArrayBuffer里。使用Promise异步回调。

该接口指定BGRA_8888格式创建pixelmap，读取的像素数据与原数据保持一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dstArrayBuffer是缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605848__getpixelbytesnumber)接口获取。

**返回值：**

类型说明Promise<void>Promise实例，用于获取结果，失败时返回错误信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### readPixelsToBufferSync

readPixelsToBufferSync(dst: ArrayBuffer): void

以同步方法读取PixelMap到Buffer里。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dstArrayBuffer是缓冲区，函数执行结束后获取的图像像素数据写入到该内存区域内。缓冲区大小由[getPixelBytesNumber](#ZH-CN_TOPIC_0000002497605848__getpixelbytesnumber)接口获取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap: sendableImage.PixelMap) {
  const bufferSize = pixelMap.getPixelBytesNumber();
  const readBuffer: ArrayBuffer = new ArrayBuffer(bufferSize);
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBufferSync(readBuffer);
  }
}
```

#### readPixels

readPixels(area: image.PositionArea): Promise<void>

读取区域内的图片数据。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[image.PositionArea](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域大小，根据区域读取。

**返回值：**

类型说明Promise<void>Promise实例，用于获取读取结果，失败时返回错误信息。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // 符合条件则进入。
    }).catch((error: BusinessError) => {
      console.error(`Failed to read the image data in the area. code is ${error.code}, message is ${error.message}`);// 不符合条件则进入。
    })
  }
}
```

#### readPixelsSync

readPixelsSync(area: image.PositionArea): void

读取区域内的图片数据并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[image.PositionArea](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域大小，根据区域读取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### writePixels

writePixels(area: image.PositionArea): Promise<void>

将PixelMap写入指定区域内。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[image.PositionArea](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域，根据区域写入。

**返回值：**

类型说明Promise<void>Promise实例，用于获取写入结果，失败时返回错误信息。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded to write pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to write pixelmap into the specified area. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### writePixelsSync

writePixelsSync(area: image.PositionArea): void

以同步方法将PixelMap写入指定区域内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明area[image.PositionArea](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__positionarea7)是区域，根据区域写入。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### writeBufferToPixels

writeBufferToPixels(src: ArrayBuffer): Promise<void>

读取缓冲区中的图片数据，结果写入PixelMap中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明srcArrayBuffer是图像像素数据。

**返回值：**

类型说明Promise<void>Promise实例，用于获取结果，失败时返回错误信息。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### writeBufferToPixelsSync

writeBufferToPixelsSync(src: ArrayBuffer): void

读取缓冲区中的图片数据，结果写入PixelMap并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明srcArrayBuffer是图像像素数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap: sendableImage.PixelMap) {
  const bufferSize = pixelMap.getPixelBytesNumber();
  const color : ArrayBuffer = new ArrayBuffer(bufferSize);
  let bufferArr : Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixelsSync(color);
  }
}
```

#### getImageInfo

getImageInfo(): Promise<image.ImageInfo>

获取图像像素信息。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<[image.ImageInfo](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>Promise实例，用于异步获取图像像素信息，失败时返回错误信息。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
      if (imageInfo != undefined) {
        console.info("Succeeded in obtaining the image pixel map information."+ imageInfo.size.height);
      }
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### getImageInfoSync

getImageInfoSync(): image.ImageInfo

以同步方法获取图像像素信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明[image.ImageInfo](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)图像像素信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息501Resource Unavailable

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  if (pixelMap != undefined) {
    let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
  }
}
```

#### getBytesNumberPerRow

getBytesNumberPerRow(): number

获取图像像素每行字节数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的行字节数。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let rowCount: number = pixelMap.getBytesNumberPerRow();
}
```

#### getPixelBytesNumber

getPixelBytesNumber(): number

获取图像像素的总字节数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的总字节数。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
}
```

#### getDensity

getDensity():number

获取当前图像像素的密度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明number图像像素的密度，单位为ppi。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let getDensity: number = pixelMap.getDensity();
}
```

#### opacity

opacity(rate: number): Promise<void>

通过设置透明比率来让PixelMap达到对应的透明效果。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明ratenumber是透明比率的值，取值范围是(0,1]。

**返回值：**

类型说明Promise<void>Promise实例，用于获取结果，失败时返回错误信息。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### opacitySync

opacitySync(rate: number): void

设置PixelMap的透明比率，初始化PixelMap。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明ratenumber是透明比率的值，取值范围是(0,1]。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let rate : number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacitySync(rate);
  }
}
```

#### createAlphaPixelmap

createAlphaPixelmap(): Promise<PixelMap>

根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的PixelMap，可用于阴影效果。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)>Promise实例，返回PixelMap。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap().then((alphaPixelMap: sendableImage.PixelMap) => {
      console.info('Succeeded in creating alpha pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### createAlphaPixelmapSync

createAlphaPixelmapSync(): PixelMap

根据Alpha通道的信息，生成一个仅包含Alpha通道信息的PixelMap，可用于阴影效果，同步返回PixelMap类型的结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let resPixelMap : sendableImage.PixelMap = pixelMap.createAlphaPixelmapSync();
  return resPixelMap;
}
```

#### scale

scale(x: number, y: number): Promise<void>

根据输入的宽高对图片进行缩放。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### scaleSync

scaleSync(x: number, y: number): void

以同步方法根据输入的宽高对图片进行缩放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY);
  }
}
```

#### translate

translate(x: number, y: number): Promise<void>

根据输入的坐标对图片进行位置变换。使用Promise异步回调。

translate后的图片尺寸改变为：width+X，height+Y，建议translate后的图片尺寸宽高不超过屏幕的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是区域横坐标。单位：像素。ynumber是区域纵坐标。单位：像素。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### translateSync

translateSync(x: number, y: number): void

根据输入的坐标对图片进行位置变换并同步返回结果。

translate后的图片尺寸改变为：width+X，height+Y，建议translate后的图片尺寸宽高不超过屏幕的宽高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明xnumber是宽度的缩放倍数。ynumber是高度的缩放倍数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let translateX : number = 50.0;
  let translateY : number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translateSync(translateX, translateY);
  }
}
```

#### rotate

rotate(angle: number): Promise<void>

根据输入的角度对图片进行旋转。使用Promise异步回调。

- 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动校正。例如，-100度与260度效果相同。
- 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明anglenumber是图片旋转的角度。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### rotateSync

rotateSync(angle: number): void

根据输入的角度对图片进行旋转并同步返回结果。

- 图片旋转的角度取值范围：[0, 360]。超出取值范围时，根据圆周360度自动校正。例如，-100度与260度效果相同。
- 如果图片旋转的角度不是90的整数倍，旋转后图片的尺寸会发生改变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明anglenumber是图片旋转的角度。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let angle : number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotateSync(angle);
  }
}
```

#### flip

flip(horizontal: boolean, vertical: boolean): Promise<void>

根据输入的条件对图片进行翻转。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明horizontalboolean是true表示进行水平翻转，false表示不进行水平翻转。verticalboolean是true表示进行垂直翻转，false表示不进行垂直翻转。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### flipSync

flipSync(horizontal: boolean, vertical: boolean): void

根据输入的条件对图片进行翻转并同步返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明horizontalboolean是true表示进行水平翻转，false表示不进行水平翻转。verticalboolean是true表示进行垂直翻转，false表示不进行垂直翻转。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let horizontal : boolean = true;
  let vertical : boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flipSync(horizontal, vertical);
  }
}
```

#### crop

crop(region: image.Region): Promise<void>

根据输入的尺寸对图片进行裁剪。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[image.Region](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的尺寸。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
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

#### cropSync

cropSync(region: image.Region): void

根据输入的尺寸裁剪图片。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明region[image.Region](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)是裁剪的尺寸。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.501Resource Unavailable.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.cropSync(region);
  }
}
```

#### getColorSpace

getColorSpace(): colorSpaceManager.ColorSpaceManager

获取图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)图像广色域信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980101If the image data abnormal.62980103If the image data unsupport.62980115If the image parameter invalid.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
  if (pixelMap != undefined) {
    let csm = pixelMap.getColorSpace();
  }
}
```

#### setColorSpace

setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void

设置图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorSpace[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)是图像广色域信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980111If the operation invalid.62980115If the image parameter invalid.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

async function Demo(pixelMap : sendableImage.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
  let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    pixelMap.setColorSpace(csm);
  }
}
```

#### applyColorSpace

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>

根据输入的目标色彩空间对图像像素颜色进行色彩空间转换。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明targetColorSpace[colorSpaceManager.ColorSpaceManager](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspacemanager)是目标色彩空间，支持SRGB、DCI_P3、DISPLAY_P3、ADOBE_RGB_1998。

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.62980104Failed to initialize the internal object.62980108Failed to convert the color space.62980115Invalid image parameter.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(pixelMap : sendableImage.PixelMap) {
    let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // colorSpaceManager.ColorSpace该对象当前仅支持2in1/PC设备使用。
    let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
    pixelMap.applyColorSpace(targetColorSpace).then(() => {
        console.info('Succeeded in applying color space for pixelmap object.');
    }).catch((error: BusinessError) => {
        console.error(`Failed to apply color space for pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
}
```

#### marshalling

marshalling(sequence: rpc.MessageSequence): void

将PixelMap序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是新创建的MessageSequence。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980115Invalid image parameter.62980097IPC error.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: sendableImage.PixelMap;
  constructor(conPixelMap : sendableImage.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence : rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    sendableImage.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: sendableImage.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: sendableImage.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info("unmarshalling information h:" + imageInfo.size.height + "w:" + imageInfo.size.width);
        })
      })
    });
    return true;
  }
}

async function Demo() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 4,
    size: { height: 4, width: 6 },
    alphaType: 3
  }
  let pixelMap: sendableImage.PixelMap | undefined = undefined;
  await sendableImage.createPixelMap(color, opts).then((srcPixelMap: sendableImage.PixelMap) => {
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

#### unmarshalling

unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>

从MessageSequence中获取PixelMap。使用Promise异步回调。

如需使用同步方式创建PixelMap可使用：[createPixelMapFromParcel](#ZH-CN_TOPIC_0000002497605848__sendableimagecreatepixelmapfromparcel)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是保存有PixelMap信息的MessageSequence。

**返回值：**

类型说明Promise<[PixelMap](#ZH-CN_TOPIC_0000002497605848__pixelmap)>Promise实例，用于异步获取结果，失败时返回错误信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980115Invalid image parameter.62980097IPC error.62980096The operation failed.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: sendableImage.PixelMap;
  constructor(conPixelMap: sendableImage.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    sendableImage.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : sendableImage.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : sendableImage.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
          console.info("unmarshalling information h:" + imageInfo.size.height + "w:" + imageInfo.size.width);
        })
      })
    });
    return true;
  }
}

async function Demo() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 4,
    size: { height: 4, width: 6 },
    alphaType: 3
  }
  let pixelMap: sendableImage.PixelMap | undefined = undefined;
  await sendableImage.createPixelMap(color, opts).then((srcPixelMap : sendableImage.PixelMap) => {
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

#### release

release():Promise<void>

释放PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<void>Promise实例，异步返回释放结果。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap: sendableImage.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

#### Size

表示图片尺寸。

继承自[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明heightnumber否否输出图片的高，单位：像素。widthnumber否否输出图片的宽，单位：像素。

#### Region

表示区域信息。

继承自[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明size[Size](#ZH-CN_TOPIC_0000002497605848__size)否否区域大小。xnumber否否区域横坐标。单位：像素。ynumber否否区域纵坐标。单位：像素。

#### sendableImage.createImageSource

createImageSource(uri: string): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明uristring是

图片路径，当前仅支持应用沙箱路径。

当前支持格式有：.jpg .png .gif .bmp .webp .dng [SVG](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__svg标签说明) .ico。

**返回值：**

类型说明[ImageSource](#ZH-CN_TOPIC_0000002497605848__imagesource)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
}
```

#### sendableImage.createImageSource

createImageSource(fd: number): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明fdnumber是文件描述符fd。

**返回值：**

类型说明[ImageSource](#ZH-CN_TOPIC_0000002497605848__imagesource)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  let file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(file.fd);
}
```

#### sendableImage.createImageSource

createImageSource(buf: ArrayBuffer): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[sendableImage.createPixelMap](#ZH-CN_TOPIC_0000002497605848__sendableimagecreatepixelmap)这一类方法。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是图像缓冲区数组。

**返回值：**

类型说明[ImageSource](#ZH-CN_TOPIC_0000002497605848__imagesource)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';

async function Demo() {
  const buf: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(buf);
}
```

#### sendableImage.createImageReceiver

createImageReceiver(size: image.Size, format: image.ImageFormat, capacity: number): ImageReceiver

通过图片大小、图片格式、容量创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-3)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明size[image.Size](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)是图像的默认大小。format[image.ImageFormat](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__imageformat9)是图像格式，取值为image.ImageFormat常量，目前仅支持 ImageFormat:JPEG。capacitynumber是同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**返回值：**

类型说明[ImageReceiver](#ZH-CN_TOPIC_0000002497605848__imagereceiver)如果操作成功，则返回ImageReceiver实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401The parameter check failed.

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo() {
    let size: image.Size = {
        height: 8192,
        width: 8
    }
    let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
}
```

#### ImageSource

ImageSource类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过[sendableImage.createImageSource](#ZH-CN_TOPIC_0000002497605848__sendableimagecreateimagesource)构建一个ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-1)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

#### createPixelMap

createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>

通过图片解码参数创建PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[image.DecodingOptions](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。

**返回值：**

类型说明Promise<[PixelMap]>Promise实例，用于异步返回创建结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
  sendableImageSourceObj.createPixelMap().then((pixelMap: sendableImage.PixelMap) => {
    console.info('Succeeded in creating pixelMap object through image decoding parameters.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelMap object through image decoding parameters. code ${error.code}, message is ${error.message}`);
  })
}
```

#### release

release(): Promise<void>

释放ImageSource实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明Promise<void>Promise实例，异步返回结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
  sendableImageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance. code ${error.code}, message is ${error.message}`);
  })
}
```

#### Image

提供基本的图像操作，包括获取图像信息、读写图像数据。调用[readNextImage](#ZH-CN_TOPIC_0000002497605848__readnextimage)和[readLatestImage](#ZH-CN_TOPIC_0000002497605848__readlatestimage)接口时会返回Image。继承自[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605848__release-2)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明clipRect[Region](#ZH-CN_TOPIC_0000002497605848__region)否否要裁剪的图像区域。size[Size](#ZH-CN_TOPIC_0000002497605848__size)是否

图像大小。

如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。

如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。

Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的是previewOutput还是captureOutput。

相机预览与拍照最佳实践请参考[双路预览(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview)与[拍照实践(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting-case)。

formatnumber是否图像格式，参考[OH_NativeBuffer_Format](../../capi/headers/buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)。timestamp12+number是否图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过[getImageProperty](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageproperty11)接口读取相关的EXIF信息。

#### getComponent

getComponent(componentType: image.ComponentType): Promise<image.Component>

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。getComponent是线程不安全的。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明componentType[image.ComponentType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__componenttype9)是图像的组件类型。

**返回值：**

类型说明Promise<[image.Component](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__component9)>Promise实例，用于异步返回组件缓冲区。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  let img = await receiver.readNextImage();
  img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
    console.info('getComponent succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`getComponent failed code ${error.code}, message is ${error.message}`);
  })
}
```

#### release

release(): Promise<void>

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<void>promise返回操作结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  let img = await receiver.readNextImage();
  img.release().then(() => {
    console.info('release succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`release failed. code ${error.code}, message is ${error.message}`);
  })
}
```

#### ImageReceiver

图像接收类，用于获取组件surface id，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

在调用以下方法前需要先创建ImageReceiver实例。

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

名称类型只读可选说明size[image.Size](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)是否图片大小。capacitynumber是否同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。format[image.ImageFormat](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__imageformat9)是否图像格式。

#### getReceivingSurfaceId

getReceivingSurfaceId(): Promise<string>

用于获取一个surface id供Camera或其他组件使用。使用promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<string>异步返回surface id。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.getReceivingSurfaceId().then((id: string) => {
    console.info('Succeeded in getting the ReceivingSurfaceId.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the ReceivingSurfaceId.code ${error.code}, message is ${error.message}`);
  })
}
```

#### readLatestImage

readLatestImage(): Promise<Image>

从ImageReceiver读取最新的图片。使用promise异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605848__on)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](#ZH-CN_TOPIC_0000002497605848__image)对象使用完毕后需要调用[release](#ZH-CN_TOPIC_0000002497605848__release-2)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<[Image](#ZH-CN_TOPIC_0000002497605848__image)>异步返回最新图片。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.readLatestImage().then((img: image.Image) => {
    console.info('readLatestImage succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`readLatestImage failed. code ${error.code}, message is ${error.message}`);
  })
}
```

#### readNextImage

readNextImage(): Promise<Image>

从ImageReceiver读取下一张图片。使用promise异步回调。

此接口需要在[on](#ZH-CN_TOPIC_0000002497605848__on)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](#ZH-CN_TOPIC_0000002497605848__image)对象使用完毕后需要调用[release](#ZH-CN_TOPIC_0000002497605848__release-2)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<[Image](#ZH-CN_TOPIC_0000002497605848__image)>异步返回下一张图片。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.readNextImage().then((img: image.Image) => {
    console.info('readNextImage succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`readNextImage failed. code ${error.code}, message is ${error.message}`);
  })
}
```

#### on

on(type: 'imageArrival', callback: AsyncCallback<void>): void

接收图片时注册。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明typestring是注册事件的类型，固定为'imageArrival'，接收图片时触发。callbackAsyncCallback<void>是注册的事件回调。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.on('imageArrival', () => {
    // 接收到图片，实现回调函数逻辑。
  })
}
```

#### release

release(): Promise<void>

释放ImageReceiver实例。使用promise异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

类型说明Promise<void>异步返回操作结果。

**示例：**

```ets
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.release().then(() => {
    console.info('release succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`release failed. code ${error.code}, message is ${error.message}`);
  })
}
```