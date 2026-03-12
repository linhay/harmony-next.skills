# Interface (ImageSource)

ImageSource类，用于获取图片相关信息。

在调用ImageSource的方法前，需要先通过[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource)构建一个ImageSource实例。

ImageSource的所有方法均不支持并发调用。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497445864__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

名称类型只读可选说明supportedFormatsArray<string>是否支持的图片格式，包括：png，jpeg，bmp，gif，webp，dng，heic12+（不同硬件设备支持情况不同）。

#### getImageInfo

getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void

获取指定序号的图片信息。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明indexnumber是创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。callbackAsyncCallback<[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>是回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0, (error: BusinessError, imageInfo: image.ImageInfo) => {
    if (error) {
      console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}
```

#### getImageInfo

getImageInfo(callback: AsyncCallback<ImageInfo>): void

获取图片信息。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>是回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo((err: BusinessError, imageInfo: image.ImageInfo) => {
    if (err) {
      console.error(`Failed to obtain the image information.code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('Succeeded in obtaining the image information.');
    }
  })
}
```

#### getImageInfo

getImageInfo(index?: number): Promise<ImageInfo>

获取图片信息。使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明indexnumber否创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。

**返回值：**

类型说明Promise<[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)>Promise对象，返回获取到的图片信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageInfo(0)
    .then((imageInfo: image.ImageInfo) => {
      console.info('Succeeded in obtaining the image information.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to obtain the image information.code is ${error.code}, message is ${error.message}`);
    })
}
```

#### getImageInfoSync12+

getImageInfoSync(index?: number): ImageInfo

获取指定序号的图片信息，使用同步形式返回图片信息。

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明indexnumber否创建ImageSource时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。

**返回值：**

类型说明[ImageInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imageinfo)同步返回获取到的图片信息。

**示例：**

```ets
function GetImageInfoSync(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let imageInfo = imageSource.getImageInfoSync(0);
  if (imageInfo == undefined) {
    console.error('Failed to obtain the image information.');
  } else {
    console.info('Succeeded in obtaining the image information.');
    console.info('imageInfo.size.height:' + imageInfo.size.height);
    console.info('imageInfo.size.width:' + imageInfo.size.width);
  }
}
```

#### getImageProperty11+

getImageProperty(key:PropertyKey, options?: ImagePropertyOptions): Promise<string>

获取图片中给定索引处图像的指定属性键的值。用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明key[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)是图片属性名。options[ImagePropertyOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__imagepropertyoptions11)否图片属性，包括图片序号与默认属性值。

**返回值：**

类型说明Promise<string>Promise对象，返回图片属性值，如获取失败则返回属性默认值。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed;62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980103The image data is not supported.62980110The image source data is incorrect.62980111The image source data is incomplete.62980112The image format does not match.62980113Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted.62980115Invalid image parameter.62980118Failed to create the image plugin.62980122Failed to decode the image header.62980123The image does not support EXIF decoding.62980135The EXIF value is invalid.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  let options: image.ImagePropertyOptions = { index: 0, defaultValue: '9999' }
  imageSourceObj.getImageProperty(image.PropertyKey.BITS_PER_SAMPLE, options)
    .then((data: string) => {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }).catch((error: BusinessError) => {
    console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
  })
}
```

#### getImageProperties12+

getImageProperties(key: Array<PropertyKey>): Promise<Record<PropertyKey, string|null>>

批量获取图片中的指定属性键的值。使用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keyArray<[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)>是图片属性名的数组。

**返回值：**

类型说明Promise<Record<[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), string | null>>Promise对象，返回图片属性值，如获取失败则返回null。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed;62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980110The image source data is incorrect.62980113Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted.62980116Failed to decode the image.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperties(imageSourceObj : image.ImageSource) {
  let key = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
  imageSourceObj.getImageProperties(key).then((data) => {
    console.info(JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(JSON.stringify(err));
  });
}
```

#### getImagePropertySync20+

getImagePropertySync(key:PropertyKey): string

获取图片exif指定属性键的值，使用同步形式返回结果。

-

该方法仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含exif信息。

-

exif信息是图片的元数据，包含拍摄时间、相机型号、光圈、焦距、ISO等。

-

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明key[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)是图片属性名。

**返回值：**

类型说明string返回图片exif中指定属性键的值（如获取失败则返回属性默认值），各个数据值作用请参考[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7700101Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed.7700102Unsupported MIME type.7700202Unsupported metadata. For example, key is not supported.

**示例：**

```ets
function GetImagePropertySync(context : Context) {
  let resourceMgr = context.resourceManager;
  if (resourceMgr == null) {
    return;
  }
  let fd = resourceMgr.getRawFdSync("example.jpg");

  const imageSourceObj = image.createImageSource(fd);
  console.info("getImagePropertySync");
  let bits_per_sample = imageSourceObj.getImagePropertySync(image.PropertyKey.BITS_PER_SAMPLE);
  console.info("bits_per_sample : " + bits_per_sample);
}
```

#### modifyImageProperty11+

modifyImageProperty(key: PropertyKey, value: string): Promise<void>

通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明key[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)是图片属性名。valuestring是属性值。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;62980123The image does not support EXIF decoding.62980133The EXIF data is out of range.62980135The EXIF value is invalid.62980146The EXIF data failed to be written to the file.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty(image.PropertyKey.IMAGE_WIDTH, "120").then(() => {
    imageSourceObj.getImageProperty(image.PropertyKey.IMAGE_WIDTH).then((width: string) => {
      console.info(`ImageWidth is :${width}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}`);
  })
}
```

#### modifyImageProperties12+

modifyImageProperties(records: Record<PropertyKey, string|null>): Promise<void>

批量通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

调用modifyImageProperties修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperties会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明recordsRecord<[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), string | null>是包含图片属性名和属性值的数组。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed;62980123The image does not support EXIF decoding.62980135The EXIF value is invalid.62980146The EXIF data failed to be written to the file.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperties(imageSourceObj : image.ImageSource) {
  let keyValues: Record<PropertyKey, string|null> = {
    [image.PropertyKey.IMAGE_WIDTH] : "1024",
    [image.PropertyKey.IMAGE_LENGTH] : "1024"
  };
  let checkKey = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
  imageSourceObj.modifyImageProperties(keyValues).then(() => {
    imageSourceObj.getImageProperties(checkKey).then((data) => {
      console.info(`Image Width and Image Height:${data}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
  });
}
```

#### modifyImagePropertiesEnhanced22+

modifyImagePropertiesEnhanced(records: Record<string, string | null>): Promise<void>

批量修改图片属性。使用Promise异步回调。

- 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[ImageSource](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例或通过传入的uri创建[ImageSource](Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource)实例。
- 该方法在内存中完成批量数据修改后会一次性写入文件，相比[modifyImageProperties](#ZH-CN_TOPIC_0000002497445864__modifyimageproperties12)更高效。
- 支持修改JPEG、PNG和HEIF文件类型的图片属性，图片需要包含exif信息。修改属性前，先通过supportedFormats属性查询设备是否支持HEIF格式的exif读写。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明recordsRecord<string, string | null>是包含图片属性名和属性值的键值对集合。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7700102Unsupported MIME type.7700202Unsupported metadata. For example, the property key is not supported, or the property value is invalid.7700304Failed to write image properties to the file.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImagePropertiesEnhanced(imageSourceObj : image.ImageSource) {
  let keyValues: Record<string, string|null> = {
    "ImageWidth" : "1024",
    "ImageLength" : "1024"
  };
  let checkKey = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH];
  imageSourceObj.modifyImagePropertiesEnhanced(keyValues).then(() => {
    imageSourceObj.getImageProperties(checkKey).then((data) => {
      console.info(`Image Width and Image Height:${data}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to modify the Image Width and Image Height, error.code ${err.code}, error.message ${err.message}`);
  });
}
```

#### updateData9+

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>

更新增量数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是存放增量数据的buffer。isFinishedboolean是true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。offsetnumber是即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。lengthnumber是当前buffer的长度。单位：字节。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function UpdateDatay(imageSourceObj : image.ImageSource) {
  const array: ArrayBuffer = new ArrayBuffer(100);
  imageSourceObj.updateData(array, false, 0, 10).then(() => {
    console.info('Succeeded in updating data.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update data.code is ${err.code},message is ${err.message}`);
  })
}
```

#### updateData9+

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number, callback: AsyncCallback<void>): void

更新增量数据。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明bufArrayBuffer是存放增量数据的buffer。isFinishedboolean是true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。offsetnumber是即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。lengthnumber是当前buffer的长度。单位：字节。callbackAsyncCallback<void>是回调函数，当更新增量数据成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function UpdateDatay(imageSourceObj : image.ImageSource) {
  const array: ArrayBuffer = new ArrayBuffer(100);
  imageSourceObj.updateData(array, false, 0, 10, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update data.code is ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in updating data.');
    }
  })
}
```

#### createPicture13+

createPicture(options?: DecodingOptionsForPicture): Promise<Picture>

通过图片解码参数创建Picture对象。使用Promise异步回调。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](Interface (Picture).md#ZH-CN_TOPIC_0000002529445809__release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptionsForPicture](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptionsforpicture13)否解码参数。

**返回值：**

类型说明Promise<[Picture](Interface (Picture).md)>Promise对象，返回Picture。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.2.Incorrect parameter types; 3.Parameter verification failed.7700301Failed to decode image.

**示例：**

```ets
async function CreatePicture(imageSourceObj : image.ImageSource) {
  let options: image.DecodingOptionsForPicture = {
    desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP] // GAINMAP为需要解码的辅助图类型。
  };
  let pictureObj: image.Picture = await imageSourceObj.createPicture(options);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }
}
```

#### createPictureAtIndex20+

createPictureAtIndex(index: number): Promise<Picture>

通过指定序号的图片（目前仅支持GIF格式）创建Picture对象。使用Promise异步回调。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](Interface (Picture).md#ZH-CN_TOPIC_0000002529445809__release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明indexnumber是解码图片序号。图片序号有效的取值范围为：[0，帧数-1]。

**返回值：**

类型说明Promise<[Picture](Interface (Picture).md)>Promise对象，返回Picture。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息7700101Bad source.7700102Unsupported MIME type.7700103Image too large.7700203Unsupported options. For example, index is invalid.7700301Decoding failed.

**示例：**

```ets
async function CreatePictures(imageSourceObj : image.ImageSource) {
  let frameCount: number = await imageSourceObj.getFrameCount();
  for (let index = 0; index < frameCount; index++) {
    try {
      let pictureObj: image.Picture = await imageSourceObj.createPictureAtIndex(index);
      console.info('Create picture succeeded for frame: ' + index);
    } catch (e) {
      console.error('Create picture failed for frame: ' + index);
    }
  }
}
```

#### createPixelMap7+

createPixelMap(options?: DecodingOptions): Promise<PixelMap>

通过图片解码参数创建PixelMap对象。使用Promise异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002497445864__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](zh-cn_topic_0000002529285837.html#ZH-CN_TOPIC_0000002529285837__allocatortype15)，详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMap().then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelMap object through image decoding parameters.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelMap object through image decoding parameters, error.code ${error.code}, error.message ${error.message}`);
  })
}
```

#### createPixelMap7+

createPixelMap(callback: AsyncCallback<PixelMap>): void

通过默认参数创建PixelMap对象。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002497445864__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](zh-cn_topic_0000002529285837.html#ZH-CN_TOPIC_0000002529285837__allocatortype15)，详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<[PixelMap](Interface (PixelMap).md)>是回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMap((err: BusinessError, pixelMap: image.PixelMap) => {
    if (err) {
      console.error(`Failed to create pixelMap.code is ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in creating pixelMap object.');
    }
  })
}
```

#### createPixelMap7+

createPixelMap(options: DecodingOptions, callback: AsyncCallback<PixelMap>): void

通过图片解码参数创建PixelMap对象。使用callback异步回调。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002497445864__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](zh-cn_topic_0000002529285837.html#ZH-CN_TOPIC_0000002529285837__allocatortype15)，详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)是解码参数。callbackAsyncCallback<[PixelMap](Interface (PixelMap).md)>是回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap(imageSourceObj : image.ImageSource) {
  let decodingOptions: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 1, height: 2 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  imageSourceObj.createPixelMap(decodingOptions, (err: BusinessError, pixelMap: image.PixelMap) => {
    if (err) {
      console.error(`Failed to create pixelMap.code is ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in creating pixelMap object.');
    }
  })
}
```

#### createPixelMapSync12+

createPixelMapSync(options?: DecodingOptions): PixelMap

通过图片解码参数同步创建PixelMap对象。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocatorSync](#ZH-CN_TOPIC_0000002497445864__createpixelmapusingallocatorsync15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](zh-cn_topic_0000002529285837.html#ZH-CN_TOPIC_0000002529285837__allocatortype15)，详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)用于同步返回创建结果。

**示例：**

```ets
function CreatePixelMapSync(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 1, height: 2 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

#### createPixelMapList10+

createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>

通过图片解码参数创建PixelMap数组。使用Promise异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。

**返回值：**

类型说明Promise<Array<[PixelMap](Interface (PixelMap).md)>>异步返回PixelMap数组。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980099The shared memory data is abnormal.62980101The image data is abnormal.62980103The image data is not supported.62980106The image data is too large. This status code is thrown when an error occurs during the process of checking size.62980109Failed to crop the image.62980111The image source data is incomplete.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980137Invalid media operation.62980173The DMA memory does not exist.62980174The DMA memory data is abnormal.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  let decodeOpts: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 198, height: 202 },
    rotate: 0,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    index: 0,
  };
  imageSourceObj.createPixelMapList(decodeOpts).then((pixelMapList: Array<image.PixelMap>) => {
    console.info('Succeeded in creating pixelMapList object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create pixelMapList object, error code is ${err}`);
  })
}
```

#### createPixelMapList10+

createPixelMapList(callback: AsyncCallback<Array<PixelMap>>): void

通过默认参数创建PixelMap数组。使用callback异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[PixelMap](Interface (PixelMap).md)>>是回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980099The shared memory data is abnormal.62980101The image data is abnormal.62980103The image data is not supported.62980106The image data is too large. This status code is thrown when an error occurs during the process of checking size.62980109Failed to crop the image.62980111The image source data is incomplete.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980137Invalid media operation.62980173The DMA memory does not exist.62980174The DMA memory data is abnormal.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  imageSourceObj.createPixelMapList((err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
    if (err) {
      console.error(`Failed to create pixelMapList object, error code is ${err}`);
    } else {
      console.info('Succeeded in creating pixelMapList object.');
    }
  })
}
```

#### createPixelMapList10+

createPixelMapList(options: DecodingOptions, callback: AsyncCallback<Array<PixelMap>>): void

通过图片解码参数创建PixelMap数组。使用callback异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)是解码参数。callbackAsyncCallback<Array<[PixelMap](Interface (PixelMap).md)>>是回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980099The shared memory data is abnormal.62980101The image data is abnormal.62980103The image data is not supported.62980106The image data is too large. This status code is thrown when an error occurs during the process of checking size.62980109Failed to crop the image.62980111The image source data is incomplete.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980137Invalid media operation.62980173The DMA memory does not exist.62980174The DMA memory data is abnormal.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapList(imageSourceObj : image.ImageSource) {
  let decodeOpts: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 198, height: 202 },
    rotate: 0,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    index: 0,
  };
  imageSourceObj.createPixelMapList(decodeOpts, (err: BusinessError, pixelMapList: Array<image.PixelMap>) => {
    if (err) {
      console.error(`Failed to create pixelMapList object, error code is ${err}`);
    } else {
      console.info('Succeeded in creating pixelMapList object.');
    }
  })
}
```

#### createPixelMapUsingAllocator15+

createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>

使用指定的分配器根据图像解码参数异步创建PixelMap对象。使用Promise异步回调。接口使用详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。allocatorType[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15)否用于图像解码的内存类型。默认值为AllocatorType.AUTO。

**返回值：**

类型说明Promise<[PixelMap](Interface (PixelMap).md)>Promise对象，返回PixelMap。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed.7700101Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed.7700102Unsupported mimetype.7700103Image too large. This status code is thrown when an error occurs during the process of checking size.7700201Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata.7700203Unsupported options, e.g., cannot convert image into desired pixel format.7700301Failed to decode image.7700302Failed to allocate memory.

**示例：**

```ets
async function CreatePixelMapUsingAllocator(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocator(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

#### createPixelMapUsingAllocatorSync15+

createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap

根据指定的分配器同步创建一个基于图像解码参数的PixelMap对象。接口使用详情请参考[申请图片解码内存(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type)。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002497605846__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明options[DecodingOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__decodingoptions7)否解码参数。allocatorType[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15)否用于图像解码的内存类型。默认值为AllocatorType.AUTO。

**返回值：**

类型说明[PixelMap](Interface (PixelMap).md)用于同步返回创建结果。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息401Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed.7700101Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed.7700102Unsupported mimetype.7700103Image too large. This status code is thrown when an error occurs during the process of checking size.7700201Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata.7700203Unsupported options, e.g., cannot convert image into desired pixel format.7700301Failed to decode image.7700302Failed to allocate memory.

**示例：**

```ets
async function CreatePixelMapUsingAllocator(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocatorSync(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

#### getDelayTimeList10+

getDelayTimeList(callback: AsyncCallback<Array<number>>): void

获取图像延迟时间数组。使用callback异步回调。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<number>>是回调函数，当获取图像延迟时间数组成功，err为undefined，data为获取到的图像延时时间数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980110The image source data is incorrect.62980111The image source data is incomplete.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980122Failed to decode the image header.62980149Invalid MIME type for the image source.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDelayTimeList((err: BusinessError, delayTimes: Array<number>) => {
    if (err) {
      console.error(`Failed to get delayTimes object.code is ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting delayTimes object.');
    }
  })
}
```

#### getDelayTimeList10+

getDelayTimeList(): Promise<Array<number>>

获取图像延迟时间数组。使用Promise异步回调。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明Promise<Array<number>>Promise对象，返回延迟时间数组。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980110The image source data is incorrect.62980111The image source data is incomplete.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980122Failed to decode the image header.62980149Invalid MIME type for the image source.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetDelayTimeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDelayTimeList().then((delayTimes: Array<number>) => {
    console.info('Succeeded in getting delayTimes object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get delayTimes object.code is ${err.code},message is ${err.message}`);
  })
}
```

#### getFrameCount10+

getFrameCount(callback: AsyncCallback<number>): void

获取图像帧数。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数，当获取图像帧数成功，err为undefined，data为获取到的图像帧数；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980111The image source data is incomplete.62980112The image format does not match.62980113Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980122Failed to decode the image header.62980137Invalid media operation.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetFrameCount(imageSourceObj : image.ImageSource) {
  imageSourceObj.getFrameCount((err: BusinessError, frameCount: number) => {
    if (err) {
      console.error(`Failed to get frame count.code is ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting frame count.');
    }
  })
}
```

#### getFrameCount10+

getFrameCount(): Promise<number>

获取图像帧数。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明Promise<number>Promise对象，返回图像帧数。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980111The image source data is incomplete.62980112The image format does not match.62980113Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted.62980115Invalid image parameter.62980116Failed to decode the image.62980118Failed to create the image plugin.62980122Failed to decode the image header.62980137Invalid media operation.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetFrameCount(imageSourceObj : image.ImageSource) {
  imageSourceObj.getFrameCount().then((frameCount: number) => {
    console.info('Succeeded in getting frame count.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get frame count.code is ${err.code},message is ${err.message}`);
  })
}
```

#### getDisposalTypeList12+

getDisposalTypeList(): Promise<Array<number>>

获取图像帧过渡模式数组。使用Promise异步回调。此接口仅用于gif图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

类型说明Promise<Array<number>>Promise对象，返回帧过渡模式数组。

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

错误码ID错误信息62980096The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory.62980101The image data is abnormal.62980137Invalid media operation.62980149Invalid MIME type for the image source.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetDisposalTypeList(imageSourceObj : image.ImageSource) {
  imageSourceObj.getDisposalTypeList().then((disposalTypes: Array<number>) => {
    console.info('Succeeded in getting disposalTypes object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get disposalTypes object.code ${err.code},message is ${err.message}`);
  })
}
```

#### release

release(callback: AsyncCallback<void>): void

释放ImageSource实例。使用callback异步回调。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数，当资源释放成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
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

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
  })
}
```

#### getImageProperty(deprecated)

getImageProperty(key:string, options?: GetImagePropertyOptions): Promise<string>

获取图片中给定索引处图像的指定属性键的值。使用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002497445864__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keystring是图片属性名。options[GetImagePropertyOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__getimagepropertyoptionsdeprecated)否图片属性，包括图片序号与默认属性值。

**返回值：**

类型说明Promise<string>Promise对象，返回图片属性值，如获取失败则返回属性默认值。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageProperty("BitsPerSample")
    .then((data: string) => {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }).catch((error: BusinessError) => {
    console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
  })
}
```

#### getImageProperty(deprecated)

getImageProperty(key:string, callback: AsyncCallback<string>): void

获取图片中给定索引处图像的指定属性键的值。使用callback异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002497445864__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keystring是图片属性名。callbackAsyncCallback<string>是回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.getImageProperty("BitsPerSample", (error: BusinessError, data: string) => {
    if (error) {
      console.error('Failed to get the value of the specified attribute key of the image.');
    } else {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }
  })
}
```

#### getImageProperty(deprecated)

getImageProperty(key:string, options: GetImagePropertyOptions, callback: AsyncCallback<string>): void

获取图片指定属性键的值。使用callback异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002497445864__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keystring是图片属性名。options[GetImagePropertyOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__getimagepropertyoptionsdeprecated)是图片属性，包括图片序号与默认属性值。callbackAsyncCallback<string>是回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageProperty(imageSourceObj : image.ImageSource) {
  let property: image.GetImagePropertyOptions = { index: 0, defaultValue: '9999' }
  imageSourceObj.getImageProperty("BitsPerSample", property, (error: BusinessError, data: string) => {
    if (error) {
      console.error('Failed to get the value of the specified attribute key of the image.');
    } else {
      console.info('Succeeded in getting the value of the specified attribute key of the image.');
    }
  })
}
```

#### modifyImageProperty(deprecated)

modifyImageProperty(key: string, value: string): Promise<void>

通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](#ZH-CN_TOPIC_0000002497445864__modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keystring是图片属性名。valuestring是属性值。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty("ImageWidth", "120").then(() => {
    imageSourceObj.getImageProperty("ImageWidth").then((width: string) => {
      console.info(`ImageWidth is :${width}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get the Image Width, error.code ${error.code}, error.message ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to modify the Image Width, error.code ${error.code}, error.message ${error.message}`);
  })
}
```

#### modifyImageProperty(deprecated)

modifyImageProperty(key: string, value: string, callback: AsyncCallback<void>): void

通过指定的键修改图片属性的值。使用callback异步回调。

仅支持JPEG、PNG和HEIF12+（不同硬件设备支持情况不同）文件，且需要包含exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的exif读写。

调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](#ZH-CN_TOPIC_0000002497445864__modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

参数名类型必填说明keystring是图片属性名。valuestring是属性值。callbackAsyncCallback<void>是回调函数，当修改图片属性值成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ModifyImageProperty(imageSourceObj : image.ImageSource) {
  imageSourceObj.modifyImageProperty("ImageWidth", "120", (err: BusinessError) => {
    if (err) {
      console.error(`Failed to modify the Image Width.code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('Succeeded in modifying the Image Width.');
    }
  })
}
```