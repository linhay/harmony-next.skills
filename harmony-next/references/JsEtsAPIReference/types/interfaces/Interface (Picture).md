# Interface (Picture)

Picture类，一些包含特殊信息的图片可以解码为Picture（也可以称为多图对象）。多图对象一般包含主图、辅助图和元数据。其中主图包含图像的大部分信息，主要用于显示图像内容；辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息；元数据一般用来存储关于图像文件的信息。多图对象类用于读取或写入多图对象。在调用Picture的方法前，需要先通过[image.createPicture](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreatepicture13)创建一个Picture实例。

由于图片占用内存较大，所以当Picture实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002553361895__release13)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。


- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 13开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### getMainPixelmap13+

getMainPixelmap(): PixelMap

获取主图的pixelmap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | 同步返回PixelMap对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetMainPixelmap(pictureObj : image.Picture) {
  let funcName = "getMainPixelmap";
  if (pictureObj != null) {
    let mainPixelmap: image.PixelMap = pictureObj.getMainPixelmap();
    if (mainPixelmap != null) {
      mainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info('GetMainPixelmap information height:' + imageInfo.size.height + ' width:' + imageInfo.size.width);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
```

#### getHdrComposedPixelmap13+

getHdrComposedPixelmap(): Promise<PixelMap>

合成HDR图并获取HDR图的pixelmap。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PixelMap> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码]([Image错误码](../../errors/Image错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600901 | Inner unknown error. Please check the logs for detailed information. |
| 7600201 | Unsupported operation. e.g.,1. The picture does not has a gainmap. 2. MainPixelMap's allocator type is not DMA. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmap(pictureObj : image.Picture) {
  let funcName = "getHdrComposedPixelmap";
  if (pictureObj != null) { // 图片包含Hdr图。
    let hdrComposedPixelmap: image.PixelMap = await pictureObj.getHdrComposedPixelmap();
    if (hdrComposedPixelmap != null) {
      hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`GetHdrComposedPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
```

**getHdrComposedPixelmapWithOptions23+**

getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>

合成HDR图像并返回HDR图像的PixelMap，支持传入合成参数（如PixelMapFormat等）。使用Promise异步回调。

调用该接口的Picture对象中必须包含主图、增益图和元数据。

模型约束：此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | HdrComposeOptions | 否 | 合成HDR的选项。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PixelMap | undefined> | Promise对象，返回PixelMap或undefined。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600201 | Unsupported operation. |

示例：

```ets
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmapWithOptions(picture : image.Picture) {
  if (picture == null) {
    console.error('picture is null');
    return;
  }

  let opt: image.HdrComposeOptions = {
    desiredPixelFormat: image.PixelMapFormat.RGBA_1010102
  };
  let hdrComposedPixelmap: image.PixelMap | undefined = await picture.getHdrComposedPixelmapWithOptions(opt);
  if (hdrComposedPixelmap == null || hdrComposedPixelmap == undefined) {
    console.error(`GetHdrComposedPixelmapWithOptions failed`);
    return;
  }

  hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
    if (imageInfo !== null) {
      console.info(`GetHdrComposedPixelmapWithOptions information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }
  }).catch((error: BusinessError) => {
    console.error(`GetHdrComposedPixelmapWithOptions information failed error.code: ${error.code} ,error.message: ${error.message}`);
  });
}
```

#### getGainmapPixelmap13+

getGainmapPixelmap(): PixelMap | null

获取增益图的pixelmap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | null | 返回Pixelmap对象，如果没有则返回null。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetGainmapPixelmap(pictureObj : image.Picture) {
  let funcName = "getGainmapPixelmap";
  if (pictureObj != null) { // 图片包含增益图。
    let gainPixelmap: image.PixelMap | null = pictureObj.getGainmapPixelmap();
    if (gainPixelmap != null) {
      gainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`GetGainmapPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
        } else {
          console.error('GainPixelmap is null');
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    } else {
      console.info('GainPixelmap is null');
    }
  } else {
    console.error('PictureObj is null');
  }
```

#### setAuxiliaryPicture13+

setAuxiliaryPicture(type: [AuxiliaryPictureType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13), auxiliaryPicture: AuxiliaryPicture): void

设置辅助图。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13) | 是 | 辅助图类型。 |
| auxiliaryPicture | AuxiliaryPicture | 是 | 辅助图对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
async function SetAuxiliaryPicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg");// 需要支持hdr的图片。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let pixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(pixelMap);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
    if (auxPictureObj != null) {
      pictureObj.setAuxiliaryPicture(type, auxPictureObj);
    }
```

#### getAuxiliaryPicture13+

getAuxiliaryPicture(type: [AuxiliaryPictureType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13)): AuxiliaryPicture | null

根据类型获取辅助图。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13) | 是 | 辅助图类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AuxiliaryPicture | null | 返回AuxiliaryPicture对象，如果没有则返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
async function GetAuxiliaryPicture(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
  }
```

#### setMetadata13+

setMetadata(metadataType: [MetadataType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13), metadata: Metadata): Promise<void>

设置主图的元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13) | 是 | 元数据类型。 |
| metadata | Metadata | 是 | 元数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function SetPictureObjMetadata(exifContext: Context) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 含有exif metadata的图片。
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error('Failed to set metadata. error.code: ' +JSON.stringify(error.code) + ' ,error.message:' + JSON.stringify(error.message));
    });
  } else {
    console.error('exifPictureOb is null');
  }
```

#### getMetadata13+

getMetadata(metadataType: [MetadataType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13)): Promise<Metadata>

获取主图的元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13) | 是 | 元数据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Metadata> | Promise对象。返回元数据。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例：**

```ets
async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('get picture metadata success');
    } else {
      console.error('get picture metadata is failed');
    }
  } else {
    console.error(" pictureObj is null");
  }
```

#### marshalling13+

marshalling(sequence: rpc.MessageSequence): void

将picture序列化后写入MessageSequence。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | 是 | 新创建的MessageSequence。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

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
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }).catch((error: BusinessError) => {
      console.error(`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}`);
    });
    return true;
}

async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
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
```

#### release13+

release(): void

释放picture对象。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**示例：**

```ets
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
```