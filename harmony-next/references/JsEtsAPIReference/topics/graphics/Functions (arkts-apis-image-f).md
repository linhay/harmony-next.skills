[]()[]()

# Functions

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

[]()[]()

#### image.createPicture13+

createPicture(mainPixelmap : PixelMap): Picture

通过主图的pixelmap创建一个Picture对象。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](../../types/interfaces/Interface (Picture).md#ZH-CN_TOPIC_0000002529445809__release13)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明mainPixelmap[PixelMap](../../types/interfaces/Interface (PixelMap).md)是主图的pixelmap。

**返回值：**

类型说明[Picture](../../types/interfaces/Interface (Picture).md)返回Picture对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed.

**示例：**

```ets
async function CreatePicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }
}
```

[]()[]()

#### image.createPictureFromParcel13+

createPictureFromParcel(sequence: rpc.MessageSequence): Picture

从MessageSequence中获取Picture。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](../../types/interfaces/Interface (Picture).md#ZH-CN_TOPIC_0000002529445809__release13)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](../../modules/ohos/@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是保存有Picture信息的MessageSequence。

**返回值：**

类型说明[Picture](../../types/interfaces/Interface (Picture).md)返回Picture对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed.62980097IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory.

**示例：**

```ets
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  picture: image.Picture | null = null;
  constructor(conPicture: image.Picture) {
    this.picture = conPicture;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    if(this.picture != null) {
      this.picture.marshalling(messageSequence);
      console.info('Marshalling success !');
      return true;
    } else {
      console.error('Marshalling failed !');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }).catch((error: BusinessError) => {
      console.error(`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}`);
    });
    return true;
  }
}

async function Marshalling_UnMarshalling(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // 序列化。
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // 反序列化。
    data.readParcelable(ret);
  } else {
    console.error('PictureObj is null');
  }
}
```

[]()[]()

#### image.createPixelMap8+

createPixelMap(colors: ArrayBuffer, options: InitializationOptions): Promise<PixelMap>

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是

图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8).srcPixelFormat指定。

**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。

options[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。

**返回值：**

类型说明Promise<[PixelMap](../../types/interfaces/Interface (PixelMap).md)>

Promise对象，返回PixelMap。

当创建的pixelMap大小超过原图大小时，返回原图pixelMap大小。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
  })
}
```

[]()[]()

#### image.createPixelMap8+

createPixelMap(colors: ArrayBuffer, options: InitializationOptions, callback: AsyncCallback<PixelMap>): void

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是

图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8).srcPixelFormat指定。

**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。

options[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。callbackAsyncCallback<[PixelMap](../../types/interfaces/Interface (PixelMap).md)>是回调函数，当创建PixelMap成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts, (error: BusinessError, pixelMap: image.PixelMap) => {
    if(error) {
      console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
      return;
    } else {
      console.info('Succeeded in creating pixelmap.');
    }
  })
}
```

[]()[]()

#### image.createPixelMapUsingAllocator20+

createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>

通过属性创建以及指定内存类型创建PixelMap，默认采用BGRA_8888格式处理数据。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是

图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8).srcPixelFormat指定。

**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。

param[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。allocatorType[AllocatorType](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__allocatortype15)否

指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。

 1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN、YCBCR_P010、YCRCB_P010和ASTC_4x4。RGBA_1010102默认申请DMA内存。其他格式（RGB_565、RGBA_8888、BGRA_8888和RGBAF_16）尺寸大于512*512默认申请DMA内存，否则申请共享内存。

2. image.AllocatorType.DMA：RGBA_1010102、RGB_565、RGBA_8888、BGRA_8888和RGBAF_16支持DMA内存类型，其余格式不支持。

3. image.AllocatorType.SHARED：UNKNOWN、RGBA_1010102、YCBCR_P010、YCRCB_P010和ASTC_4x4不支持共享内存，其余格式支持。

**返回值：**

类型说明Promise<[PixelMap](../../types/interfaces/Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息7600201Unsupported operation.7600301Memory alloc failed.7600302Memory copy failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapUseAllocator() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, srcPixelFormat: image.PixelMapFormat.RGBA_8888, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.AUTO).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelmap.');
  }).catch((error: BusinessError) => {
    console.error("Failed to create pixelmap. code is ", error.code);
  })
}
```

[]()[]()

#### image.createPixelMapFromParcel11+

createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap

从MessageSequence中获取PixelMap。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明sequence[rpc.MessageSequence](../../modules/ohos/@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__messagesequence9)是保存有PixelMap信息的MessageSequence。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980097IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory.62980115Invalid input parameter.62980105Failed to get the data.62980177Abnormal API environment.62980178Failed to create the PixelMap.62980179Abnormal buffer size.62980180FD mapping failed. Possible cause: 1. Size and address does not match. 2. Memory map in memalloc failed.62980246Failed to read the PixelMap.

**示例：**

```ets
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelmap: image.PixelMap) {
    this.pixel_map = conPixelmap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    try {
      this.pixel_map = image.createPixelMapFromParcel(messageSequence);
    } catch(e) {
      let error = e as BusinessError;
      console.error(`createPixelMapFromParcel error. code is ${error.code}, message is ${error.message}`);
      return false;
    }
    return true;
  }
}
async function CreatePixelMapFromParcel() {
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

    // 获取到pixelmap。
    let newPixelmap = ret.pixel_map;
  }
}
```

[]()[]()

#### image.createPixelMapFromSurface11+

createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>

根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__region8).size指定。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

当设备为折叠屏，且折叠状态切换时，可能因Surface自带旋转角度导致接口创建失败。需将宽高适配旋转角度。推荐使用[image.createPixelMapFromSurface](#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromsurface15)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明surfaceIdstring是对应Surface的ID，可通过预览组件获取，如[XComponent](../components/XComponent.md)组件。region[Region](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__region8)是截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先使用[image.createPixelMapFromSurface](#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromsurface15)获取整个画面，再使用[crop](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__crop9)截取所需区域。

**返回值：**

类型说明Promise<[PixelMap](../../types/interfaces/Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息62980115If the image parameter invalid.62980105Failed to get the data.62980178Failed to create the PixelMap.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapFromSurface(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  image.createPixelMapFromSurface(surfaceId, region).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
  });
}
```

[]()[]()

#### image.createPixelMapFromSurfaceSync12+

createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap

以同步方式，根据Surface ID和区域信息创建一个PixelMap对象。该区域的大小由[Region](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__region8).size指定。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

当设备为折叠屏，且折叠状态切换时，可能因Surface自带旋转角度导致接口创建失败。需将宽高适配旋转角度。推荐使用[image.createPixelMapFromSurfaceSync](#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromsurfacesync15)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明surfaceIdstring是对应Surface的ID，可通过预览组件获取，如[XComponent](../components/XComponent.md)组件。region[Region](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__region8)是截取的画面区域。仅支持从画面左上角开始截取部分或整个画面，即Region中的x和y必须为0，Region.size中width和height的取值范围分别为[1, 预览流宽度]和[1, 预览流高度]。如需截取任意区域，可先使用[image.createPixelMapFromSurfaceSync](#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromsurfacesync15)获取整个画面，再使用[cropSync](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__cropsync12)截取所需区域。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.62980105Failed to get the data.62980178Failed to create the PixelMap.

**示例：**

```ets
async function Demo(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  let pixelMap: image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region);
  return pixelMap;
}
```

[]()[]()

#### image.createPixelMapFromSurface15+

createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>

从Surface ID创建一个PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明surfaceIdstring是对应Surface的ID，可通过预览组件获取，如[XComponent](../components/XComponent.md)组件。

**返回值：**

类型说明Promise<[PixelMap](../../types/interfaces/Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980105Failed to get the data62980178Failed to create the PixelMap

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapFromSurface(surfaceId: string) {
  image.createPixelMapFromSurface(surfaceId).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
  });
}
```

[]()[]()

#### image.createPixelMapFromSurfaceSync15+

createPixelMapFromSurfaceSync(surfaceId: string): PixelMap

从Surface ID创建一个PixelMap对象，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明surfaceIdstring是对应Surface的ID，可通过预览组件获取，如[XComponent](../components/XComponent.md)组件。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980105Failed to get the data62980178Failed to create the PixelMap

**示例：**

```ets
async function CreatePixelMapFromSurfaceSync(surfaceId: string) {
  let pixelMap : image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId);
  return pixelMap;
}
```

[]()[]()

#### image.createPixelMapSync12+

createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，同步返回结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是

图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8).srcPixelFormat指定。

**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。

options[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed

**示例：**

```ets
function CreatePixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
  return pixelMap;
}
```

[]()[]()

#### image.createPixelMapSync12+

createPixelMapSync(options: InitializationOptions): PixelMap

通过属性创建PixelMap，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明options[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度，尺寸，缩略值，像素格式和是否可编辑。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed

**示例：**

```ets
function CreatePixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(opts);
  return pixelMap;
}
```

[]()[]()

#### image.createPixelMapUsingAllocatorSync20+

createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

通过指定属性以及内存类型创建PixelMap，默认采用BGRA_8888格式处理数据，同步返回结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明colorsArrayBuffer是

图像像素数据的缓冲区，用于初始化PixelMap的像素。初始化前，缓冲区中的像素格式需要由[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8).srcPixelFormat指定。

**说明：** 图像像素数据的缓冲区长度：length = width * height * 单位像素字节数。

param[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。allocatorType[AllocatorType](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__allocatortype15)否

指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。

 1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN、YCBCR_P010、YCRCB_P010和ASTC_4x4。RGBA_1010102默认申请DMA内存。其他格式（RGB_565、RGBA_8888、BGRA_8888和RGBAF_16）尺寸大于512*512默认申请DMA内存，否则申请共享内存。

2. image.AllocatorType.DMA：RGBA_1010102、RGB_565、RGBA_8888、BGRA_8888和RGBAF_16支持DMA内存类型，其余格式不支持。

3. image.AllocatorType.SHARED：UNKNOWN、RGBA_1010102、YCBCR_P010、YCRCB_P010和ASTC_4x4不支持共享内存，其余格式支持。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息7600201Unsupported operation.7600301Memory alloc failed.7600302Memory copy failed.

**示例：**

```ets
function CreatePixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, srcPixelFormat: image.PixelMapFormat.RGBA_8888, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(color, opts, image.AllocatorType.AUTO);
  return pixelMap;
}
```

[]()[]()

#### image.createPixelMapUsingAllocatorSync20+

createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

通过属性创建PixelMap，同步返回PixelMap结果。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明param[InitializationOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__initializationoptions8)是创建像素的属性，包括透明度、尺寸、缩略值、像素格式和是否可编辑。allocatorType[AllocatorType](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__allocatortype15)否

指定创建pixelmap的内存类型，默认内存类型是AllocatorType.AUTO。

 1. image.AllocatorType.AUTO：不支持该内存类型的格式有UNKNOWN和ASTC_4x4。RGBA_1010102、YCBCR_P010、YCRCB_P010格式默认申请DMA内存。其他格式（RGB_565, RGBA_8888, BGRA_8888, RGBAF_16）尺寸大于512*512默认申请DMA内存，否则申请共享内存。

2. image.AllocatorType.DMA：RGB_565、RGBA_8888、BGRA_8888、RGBAF_16、RGBA_1010102、YCBCR_P010和YCRCB_P010支持DMA内存类型，其余格式不支持。

3. image.AllocatorType.SHARED：UNKNOWN、RGBA_1010102、YCBCR_P010、YCRCB_P010和ASTC_4x4不支持共享内存，其余格式支持。

**返回值：**

类型说明[PixelMap](../../types/interfaces/Interface (PixelMap).md)成功同步返回PixelMap对象，失败抛出异常。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息7600201Unsupported operation.7600301Memory alloc failed.

**示例：**

```ets
function CreatePixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(opts, image.AllocatorType.AUTO);
  return pixelMap;
}
```

[]()[]()

#### image.createPremultipliedPixelMap12+

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

将PixelMap的透明通道非预乘模式转变为预乘模式，转换后的数据存入目标PixelMap。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明src[PixelMap](../../types/interfaces/Interface (PixelMap).md)是源PixelMap对象。dst[PixelMap](../../types/interfaces/Interface (PixelMap).md)是目标PixelMap对象。callbackAsyncCallback<void>是回调函数，当创建PixelMap成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980103The image data is not supported62980246Failed to read the pixelMap62980248Pixelmap not allow modify

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i+1] = 255;
    bufferArr[i+2] = 122;
    bufferArr[i+3] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
    if(error) {
      console.error(`Failed to convert pixelmap, error code is ${error}`);
      return;
    } else {
      console.info('Succeeded in converting pixelmap.');
    }
  })
}
```

[]()[]()

#### image.createPremultipliedPixelMap12+

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

将PixelMap数据按照透明度非预乘格式转为预乘格式，转换后的数据存入另一个PixelMap。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明src[PixelMap](../../types/interfaces/Interface (PixelMap).md)是源PixelMap对象。dst[PixelMap](../../types/interfaces/Interface (PixelMap).md)是目标PixelMap对象。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980103The image data is not supported62980246Failed to read the pixelMap62980248Pixelmap not allow modify

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i+1] = 255;
    bufferArr[i+2] = 122;
    bufferArr[i+3] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
    console.info('Succeeded in converting pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to convert pixelmap, error code is ${error}`);
  })
}
```

[]()[]()

#### image.createUnpremultipliedPixelMap12+

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

将PixelMap的透明通道预乘模式转变为非预乘模式，转换后的数据存入目标PixelMap。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明src[PixelMap](../../types/interfaces/Interface (PixelMap).md)是源PixelMap对象。dst[PixelMap](../../types/interfaces/Interface (PixelMap).md)是目标PixelMap对象。callbackAsyncCallback<void>是回调函数，当创建PixelMap成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed62980103The image data is not supported62980246Failed to read the pixelMap62980248Pixelmap not allow modify

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateUnpremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i+1] = 255;
    bufferArr[i+2] = 122;
    bufferArr[i+3] = 122;
  }
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForPre);
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForUnpre);
  image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
    if(error) {
      console.error(`Failed to convert pixelmap, error code is ${error}`);
      return;
    } else {
      console.info('Succeeded in converting pixelmap.');
    }
  })
}
```

[]()[]()

#### image.createUnpremultipliedPixelMap12+

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

将PixelMap的透明通道预乘模式转变为非预乘模式，转换后的数据存入目标PixelMap。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](../../types/interfaces/Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明src[PixelMap](../../types/interfaces/Interface (PixelMap).md)是源PixelMap对象。dst[PixelMap](../../types/interfaces/Interface (PixelMap).md)是目标PixelMap对象。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.62980103The image data is not supported.62980246Failed to read the pixelMap.62980248Pixelmap not allow modify.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateUnpremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16为需要创建的像素buffer大小，取值为：height * width *4。
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr[i] = 255;
    bufferArr[i+1] = 255;
    bufferArr[i+2] = 122;
    bufferArr[i+3] = 122;
  }
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForPre);
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForUnpre);
  image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
    console.info('Succeeded in converting pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to convert pixelmap, error code is ${error}`);
  })
}
```

[]()[]()

#### image.createImageSource

createImageSource(uri: string): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明uristring是

图片路径，当前仅支持应用沙箱路径。

当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic12+（不同硬件设备支持情况不同） [.svg10+](#ZH-CN_TOPIC_0000002529445805__svg标签说明) .ico11+。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
async function CreateImageSource(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const path: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
}
```

[]()[]()

#### image.createImageSource9+

createImageSource(uri: string, options: SourceOptions): ImageSource

通过传入的uri创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明uristring是

图片路径，当前仅支持应用沙箱路径。

当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic12+（不同硬件设备支持情况不同）[.svg10+](#ZH-CN_TOPIC_0000002529445805__svg标签说明) .ico11+。

options[SourceOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__sourceoptions9)是图片属性，包括图片像素密度、像素格式和图片尺寸。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 此处'test.png'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const path: string = context.filesDir + "/test.png";
  let imageSourceObj: image.ImageSource = image.createImageSource(path, sourceOptions);
}
```

[]()[]()

#### image.createImageSource7+

createImageSource(fd: number): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明fdnumber是文件描述符fd。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd);
}
```

[]()[]()

#### image.createImageSource9+

createImageSource(fd: number, options: SourceOptions): ImageSource

通过传入文件描述符来创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明fdnumber是文件描述符fd。options[SourceOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__sourceoptions9)是图片属性，包括图片像素密度、像素格式和图片尺寸。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  const filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd, sourceOptions);
}
```

[]()[]()

#### image.createImageSource9+

createImageSource(buf: ArrayBuffer): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[image.createPixelMapSync](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__createpixelmapsync12)这一类接口。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是图像缓冲区数组。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
async function CreateImageSource() {
  const buf: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  const imageSourceObj: image.ImageSource = image.createImageSource(buf);
}
```

[]()[]()

#### image.createImageSource9+

createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource

通过缓冲区创建ImageSource实例。buf数据是未解码的数据，不可以传入类似于RBGA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用[image.createPixelMapSync](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__createpixelmapsync12)这一类接口。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是图像缓冲区数组。options[SourceOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__sourceoptions9)是图片属性，包括图片像素密度、像素格式和图片尺寸。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
async function CreateImageSource() {
  const data: ArrayBuffer = new ArrayBuffer(112);
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  const imageSourceObj: image.ImageSource = image.createImageSource(data, sourceOptions);
}
```

[]()[]()

#### image.createImageSource11+

createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource

通过图像资源文件的RawFileDescriptor创建ImageSource实例。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明rawfile[resourceManager.RawFileDescriptor](../../modules/ohos/@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__rawfiledescriptor9)是图像资源文件的RawFileDescriptor。options[SourceOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__sourceoptions9)否图片属性，包括图片像素密度、像素格式和图片尺寸。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource类实例，失败时返回undefined。

**示例：**

```ets
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateImageSource(context : Context) {
  // 获取resourceManager资源管理器。
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  resourceMgr.getRawFd('test.jpg').then((rawFileDescriptor: resourceManager.RawFileDescriptor) => {
    const imageSourceObj: image.ImageSource = image.createImageSource(rawFileDescriptor);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get RawFileDescriptor.code is ${error.code}, message is ${error.message}`);
  })
}
```

[]()[]()

#### image.CreateIncrementalSource9+

CreateIncrementalSource(buf: ArrayBuffer): ImageSource

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

以增量方式创建的ImageSource实例，仅支持使用以下功能，同步、异步callback、异步Promise均支持。

- 获取图片信息：指定序号-[getImageInfo](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageinfo)、直接获取-[getImageInfo](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageinfo-1)
- 获取图片中给定索引处图像的指定属性键的值：[getImageProperty](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageproperty11)
- 批量获取图片中的指定属性键的值：[getImageProperties](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageproperties12)
- 更新增量数据：[updateData](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__updatedata9)
- 创建PixelMap对象：通过图片解码参数创建-[createPixelMap](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__createpixelmap7)、通过默认参数创建-[createPixelMap](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__createpixelmap7-1) 、通过图片解码参数-[createPixelMap](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__createpixelmap7-2)
- 释放ImageSource实例：[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是增量数据。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource，失败时返回undefined。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateIncrementalImageSource(context : Context) {
  let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // 获取图像资源。
  // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageArray创建失败会导致后续无法正常执行。
  let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // 分片。
  let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
  const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength));
  imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
    imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
      let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
      let imageInfo = pixelMap.getImageInfoSync();
      console.info('Succeeded in creating pixelMap');
    }).catch((error : BusinessError) => {
      console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
    })
  }).catch((error : BusinessError) => {
    console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
  })
}
```

[]()[]()

#### image.CreateIncrementalSource9+

CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。

此接口支持的功能与[CreateIncrementalSource(buf: ArrayBuffer): ImageSource](#ZH-CN_TOPIC_0000002529445805__imagecreateincrementalsource9)所生成的实例支持的功能相同。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是增量数据。options[SourceOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__sourceoptions9)否图片属性，包括图片像素密度、像素格式和图片尺寸。

**返回值：**

类型说明[ImageSource](../../types/interfaces/Interface (ImageSource).md)返回ImageSource，失败时返回undefined。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreateIncrementalImageSource(context : Context) {
  let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // 获取图像资源。
  // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageArray创建失败会导致后续无法正常执行。
  let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // 分片。
  let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
  let sourceOptions: image.SourceOptions = { sourceDensity: 120};

  const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength), sourceOptions);
  imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
    imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
      let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
      let imageInfo = pixelMap.getImageInfoSync();
      console.info('Succeeded in creating pixelMap');
    }).catch((error : BusinessError) => {
      console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
    })
  }).catch((error : BusinessError) => {
    console.error(`Failed to updateData error code is ${error.code}, message is ${error.message}`);
  })
}
```

[]()[]()

#### image.getImageSourceSupportedFormats20+

getImageSourceSupportedFormats(): string[]

获取支持解码的图片格式，图片格式以mime type表示。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明string[]支持解码的图片格式（mime type）列表。

**示例：**

```ets
async function GetImageSourceSupportedFormats() {
    let formats = image.getImageSourceSupportedFormats();
    console.info('formats:', formats);
}
```

[]()[]()

#### image.createImagePacker

createImagePacker(): ImagePacker

创建ImagePacker实例。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImagePacker).md#ZH-CN_TOPIC_0000002529445807__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

类型说明[ImagePacker](../../types/interfaces/Interface (ImagePacker).md)返回ImagePacker实例。

**示例：**

```ets
async function CreateImagePacker() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
}
```

[]()[]()

#### image.getImagePackerSupportedFormats20+

getImagePackerSupportedFormats(): string[]

获取支持编码的图片格式，图片格式以mime type表示。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

类型说明string[]支持编码的图片格式（mime type）列表。

**示例：**

```ets
async function GetImagePackerSupportedFormats() {
    let formats = image.getImagePackerSupportedFormats();
    console.info('formats:', formats);
}
```

[]()[]()

#### image.createAuxiliaryPicture13+

createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture

通过ArrayBuffer图片数据、辅助图尺寸、辅助图类型创建AuxiliaryPicture实例。该接口仅支持传入BGRA的连续像素数据，会创建出RGBA的辅助图。

由于图片占用内存较大，所以当AuxiliaryPicture实例使用完成后，应主动调用[release](../../types/interfaces/Interface (AuxiliaryPicture).md#ZH-CN_TOPIC_0000002497605842__release13)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明bufferArrayBuffer是以buffer形式存放的图像数据。size[Size](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__size)是辅助图的尺寸。单位：像素。type[AuxiliaryPictureType](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13)是辅助图类型。

**返回值：**

类型说明[AuxiliaryPicture](../../types/interfaces/Interface (AuxiliaryPicture).md)如果操作成功，则返回AuxiliaryPicture实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
async function CreateAuxiliaryPicture(context: Context) {
  let funcName = "CreateAuxiliaryPicture";
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
  let auxBuffer: ArrayBuffer = rawFile.buffer as ArrayBuffer;
  let auxSize: Size = {
    height: 180,
    width: 240
  };
  let auxType: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
  let auxPictureObj: image.AuxiliaryPicture | null = image.createAuxiliaryPicture(auxBuffer, auxSize, auxType);
  if(auxPictureObj != null) {
    let type: image.AuxiliaryPictureType = auxPictureObj.getType();
    console.info(funcName, `CreateAuxiliaryPicture succeeded this.Aux_picture.type ${type}`);
  } else {
    console.error(funcName, 'CreateAuxiliaryPicture failed');
  }
}
```

[]()[]()

#### image.createImageReceiver11+

createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver

通过图片大小、图片格式、容量创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](../../types/interfaces/Interface (CameraManager).md#ZH-CN_TOPIC_0000002497445800__createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageReceiver).md#ZH-CN_TOPIC_0000002497605844__release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明size[Size](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__size)是图像的默认大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。format[ImageFormat](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__imageformat9)是图像格式，取值为[ImageFormat](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。capacitynumber是同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**返回值：**

类型说明[ImageReceiver](../../types/interfaces/Interface (ImageReceiver).md)如果操作成功，则返回ImageReceiver实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;

**示例：**

```ets
let size: image.Size = {
  height: 8192,
  width: 8192
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
```

[]()[]()

#### image.createImageCreator11+

createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator

通过图片大小、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageCreator).md)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明size[Size](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__size)是图像的默认大小。format[ImageFormat](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__imageformat9)是图像格式，如YCBCR_422_SP，JPEG。capacitynumber是同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**返回值：**

类型说明[ImageCreator](../../types/interfaces/Interface (ImageCreator).md)如果操作成功，则返回ImageCreator实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;

**示例：**

```ets
let size: image.Size = {
  height: 8192,
  width: 8192
}
let creator: image.ImageCreator = image.createImageCreator(size, image.ImageFormat.JPEG, 8);
```

[]()[]()

#### image.createImageReceiver(deprecated)

createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver

通过宽、高、图片格式、容量创建ImageReceiver实例。ImageReceiver做为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](../../types/interfaces/Interface (CameraManager).md#ZH-CN_TOPIC_0000002497445800__createpreviewoutput)。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageReceiver).md#ZH-CN_TOPIC_0000002497605844__release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

从API version 9开始支持，从API version 11废弃，建议使用[createImageReceiver](#ZH-CN_TOPIC_0000002529445805__imagecreateimagereceiver11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

参数名类型必填说明widthnumber是图像的默认宽度。单位：像素。该参数不会影响接收到的图片宽度，实际宽度由生产者决定，如相机。heightnumber是图像的默认高度。单位：像素。该参数不会影响接收到的图片高度，实际高度由生产者决定，如相机。formatnumber是图像格式，取值为[ImageFormat](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。capacitynumber是同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**返回值：**

类型说明[ImageReceiver](../../types/interfaces/Interface (ImageReceiver).md)如果操作成功，则返回ImageReceiver实例。

**示例：**

```ets
let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);
```

[]()[]()

#### image.createImageCreator(deprecated)

createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator

通过宽、高、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](../../types/interfaces/Interface (ImageCreator).md)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

从API version 9开始支持，从API version 11废弃，建议使用[createImageCreator](#ZH-CN_TOPIC_0000002529445805__imagecreateimagecreator11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

参数名类型必填说明widthnumber是图像的默认宽度。单位：像素。heightnumber是图像的默认高度。单位：像素。formatnumber是图像格式，如YCBCR_422_SP，JPEG。capacitynumber是同时访问的最大图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**返回值：**

类型说明[ImageCreator](../../types/interfaces/Interface (ImageCreator).md)如果操作成功，则返回ImageCreator实例。

**示例：**

```ets
let creator: image.ImageCreator = image.createImageCreator(8192, 8192, image.ImageFormat.JPEG, 8);
```

[]()[]()

#### SVG标签说明

从API version 10开始支持SVG标签，使用版本为(SVG) 1.1，SVG标签需设置width，height。SVG文件可添加xml声明，应以“<?xml”开头，当前支持的标签列表有：

- a
- circle
- clipPath
- defs
- ellipse
- feBlend
- feColorMatrix
- feComposite
- feDiffuseLighting
- feDisplacementMap
- feDistantLight
- feFlood
- feGaussianBlur
- feImage
- feMorphology
- feOffset
- fePointLight
- feSpecularLighting
- feSpotLight
- feTurbulence
- filter
- g
- image
- line
- linearGradient
- mask
- path
- pattern
- polygon
- polyline
- radialGradient
- rect
- stop
- svg
- text
- textPath
- tspan
- use