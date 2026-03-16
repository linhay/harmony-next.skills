# Interface (AuxiliaryPicture)

AuxiliaryPicture类，用于读取或写入图像的辅助图数据以及获取图像的辅助图信息。目前支持的辅助图类型可参考[AuxiliaryPictureType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13)。

在调用AuxiliaryPicture的方法前，需要通过[image.createAuxiliaryPicture](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateauxiliarypicture13)或Picture的[getAuxiliaryPicture](Interface (Picture).md#ZH-CN_TOPIC_0000002529445809__getauxiliarypicture13)创建一个AuxiliaryPicture实例。

由于图片占用内存较大，所以当AuxiliaryPicture对象使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497605842__release13)方法及时释放对象。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该对象。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 13开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### writePixelsFromBuffer13+

writePixelsFromBuffer(data: ArrayBuffer): Promise<void>

读取ArrayBuffer中的辅助图片数据，并将数据写入AuxiliaryPicture对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明dataArrayBuffer是辅助图像素数据。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

**示例:**

```ets
async function WritePixelsFromBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    let auxBuffer: ArrayBuffer = await auxPictureObj.readPixelsToBuffer();
    await auxPictureObj.writePixelsFromBuffer(auxBuffer);
    console.info('Write pixels from buffer success.');
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

#### readPixelsToBuffer13+

readPixelsToBuffer(): Promise<ArrayBuffer>

读取图像像素映射数据并将数据写入ArrayBuffer。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<ArrayBuffer>Promise对象。返回辅助图像素数据。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // 需要支持hdr的图片。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
      console.info('Read pixels to buffer success.' );
    }).catch((error: BusinessError) => {
      console.error(`Read pixels to buffer failed error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

#### getType13+

getType(): AuxiliaryPictureType

获取辅助图的类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[AuxiliaryPictureType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__auxiliarypicturetype13)操作成功，返回辅助图的类型。

**示例：**

```ets
async function GetAuxiliaryPictureType(auxPictureObj : image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let type: image.AuxiliaryPictureType = auxPictureObj.getType();
    console.info('Success get auxiliary picture type ' +  JSON.stringify(type));
  } else {
    console.error('Failed get auxiliary picture type ');
  }
}
```

#### setMetadata13+

setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>

设置辅助图元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明metadataType[MetadataType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13)是元数据的类型，用于设置对应的元数据。metadata[Metadata](Interface (Metadata).md)是元数据对象。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.7600202Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 图片包含exif metadata。
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

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error(`Set metadata failed.error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}
```

#### getMetadata13+

getMetadata(metadataType: MetadataType): Promise<Metadata>

从辅助图中获取元数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明metadataType[MetadataType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__metadatatype13)是元数据类型，用于获取对应类型的元数据。

**返回值：**

类型说明Promise<[Metadata](Interface (Metadata).md)>Promise对象，返回元数据的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.7600202Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type.

**示例：**

```ets
async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Get AuxPictureObj Metadata success' );
    } else {
      console.error('Get AuxPictureObj Metadata failed');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}
```

#### getAuxiliaryPictureinfo13+

getAuxiliaryPictureInfo(): AuxiliaryPictureInfo

获取有关此辅助图的图像信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明[AuxiliaryPictureInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__auxiliarypictureinfo13)返回辅助图图像信息。

**示例：**

```ets
async function GetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
  if(auxPictureObj != null) {
    let auxinfo: image.AuxiliaryPictureInfo = auxPictureObj.getAuxiliaryPictureInfo();
    console.info('GetAuxiliaryPictureInfo Type: ' + auxinfo.auxiliaryPictureType +
      ' height: ' + auxinfo.size.height + ' width: ' + auxinfo.size.width +
      ' rowStride: ' +  auxinfo.rowStride +  ' pixelFormat: ' + auxinfo.pixelFormat +
      ' colorSpace: ' +  auxinfo.colorSpace);
  } else {
    console.error('Get auxiliary picture information failed');
  }
}
```

#### setAuxiliaryPictureinfo13+

setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void

设置辅助图的图像信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明info[AuxiliaryPictureInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__auxiliarypictureinfo13)是辅助图的图像信息。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](../../errors/Image错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
import { colorSpaceManager } from '@kit.ArkGraphics2D';

async function SetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
  if(auxPictureObj != null) {
    let colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
    let info: image.AuxiliaryPictureInfo = {
      auxiliaryPictureType: image.AuxiliaryPictureType.GAINMAP,
      size: {height: 100, width: 200},
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      rowStride: 0,
      colorSpace: colorSpaceManager.create(colorSpaceName),
    };
    auxPictureObj.setAuxiliaryPictureInfo(info);
  }
}
```

#### release13+

release():void

释放辅助图对象，无返回值。

由于图片占用内存较大，所以当AuxiliaryPicture对象使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**示例：**

```ets
async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```