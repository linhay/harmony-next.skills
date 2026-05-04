# Interface ([ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7))

[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)类，用于获取图片相关信息。

在调用[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource)的方法前，需要先通过[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreateimagesource)构建一个ImageSource实例。

[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)的所有方法均不支持并发调用。

由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002522081974__release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。


本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedFormats | Array<string> | 是 | 否 | 支持的图片格式，包括：png、jpeg、bmp、gif、webp、dng、heic12+、wbmp23+、heifs23+、tiff23+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用image.get[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)SupportedFormats20+接口，动态查询当前设备上的解码能力。 |

#### getImageInfo

getImageInfo(index: number, callback: AsyncCallback<ImageInfo>): void

获取指定序号的图片信息。使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 创建[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。 |
| callback | AsyncCallback<ImageInfo> | 是 | 回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。 |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<ImageInfo> | 是 | 回调函数。当获取图片信息成功，err为undefined，data为获取到的图片信息；否则为错误对象。 |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 否 | 创建[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ImageInfo> | Promise对象，返回获取到的图片信息。 |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 否 | 创建[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)时的序号。默认值为0，表示第一张图片。当取值为N时，表示第N+1张图片。单帧图片场景中index取值只能为0，动图等多帧图片场景中index的取值范围为：0~（帧数-1）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImageInfo | 同步返回获取到的图片信息。 |

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
```

#### getImageProperty11+

getImageProperty(key:[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), options?: ImagePropertyOptions): Promise<string>

获取图片中给定索引处图像的指定属性键的值。用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7) | 是 | 图片属性名。 |
| options | ImagePropertyOptions | 否 | 图片属性，包括图片序号与默认属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回图片属性值，如获取失败则返回属性默认值。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码]([Image错误码](../../errors/Image错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980103 | The image data is not supported. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |

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

getImageProperties(key: Array<[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)>): Promise<Record<PropertyKey, string|null>>

批量获取图片中的指定属性键的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array<[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)> | 是 | 图片属性名的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Record<[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), string | null>> | Promise对象，返回图片属性值，如获取失败则返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980116 | Failed to decode the image. |

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

getImagePropertySync(key:[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)): string

获取图片Exif指定属性键的值，使用同步形式返回结果。


-

该方法仅支持JPEG、PNG、HEIF、WEBP23+和DNG23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

-

Exif信息是图片的元数据，包含拍摄时间、相机型号、光圈、焦距、ISO等。

-

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7) | 是 | 图片属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回图片Exif中指定属性键的值（如获取失败则返回属性默认值），各个数据值作用请参考[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7)。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, key is not supported. |

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

modifyImageProperty(key: [PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), value: string): Promise<void>

通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7) | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |
| 62980123 | The image does not support EXIF decoding. |
| 62980133 | The EXIF data is out of range. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

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

modifyImageProperties(records: Record<[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), string|null>): Promise<void>

批量通过指定的键修改图片属性的值。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


调用modifyImageProperties修改属性会改变属性字节长度，使用buffer创建的[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)调用modifyImageProperties会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<[PropertyKey](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__propertykey7), string | null> | 是 | 包含图片属性名和属性值的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 62980123 | The image does not support EXIF decoding. |
| 62980135 | The EXIF value is invalid. |
| 62980146 | The EXIF data failed to be written to the file. |

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


- 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreateimagesource7)实例或通过传入的uri创建[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreateimagesource)实例。

- 该方法在内存中完成批量数据修改后会一次性写入文件，相比[modifyImageProperties](#ZH-CN_TOPIC_0000002522081974__modifyimageproperties12)更高效。

- 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 包含图片属性名和属性值的键值对集合。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. For example, the property key is not supported, or the property value is invalid. |
| 7700304 | Failed to write image properties to the file. |

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

**readImageMetadata23+**

readImageMetadata(propertyKeys?: string[], index?: number): Promise<ImageMetadata>

读取图像源的元数据，使用propertyKeys指定元数据字段。使用Promise异步回调。

该接口仅支持JPEG、PNG、HEIF、WEBP和DNG（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


读取DNG格式图片时，该接口对部分propertyKeys有特殊处理。以下字段的字符串取值请参考[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002522081978__propertykey7)中的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| propertyKeys | string[] | 否 | 图片属性名的数组。若未指定propertyKeys，则返回所有支持的元数据。 |
| index | number | 否 | 感兴趣的索引，默认值为0。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ImageMetadata> | Promise对象，返回ImageMetadata对象，其中含有图片属性名对应的metadata对象，通过ImageMetadata中的metadata对象可以获取图片属性值。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. |
| 7700204 | Invalid parameter. Possible causes: 1. The index is negative. 2. The index is greater than or equal to the number of frames in the image. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadImageMetadata(imageSourceObj : image.ImageSource) {
  let propertyKeys = ["ImageWidth", "HwMnoteIsXmageSupported"];
  await imageSourceObj.readImageMetadata(propertyKeys).then((metaData: image.ImageMetadata) => {
    if (metaData != undefined && metaData.exifMetadata != undefined &&
      metaData.makerNoteHuaweiMetadata != undefined) {
      console.info("ImageWidth: " + metaData.exifMetadata.imageWidth +
        " HwMnoteIsXmageSupported: " + metaData.makerNoteHuaweiMetadata.isXmageSupported);
    }
  }).catch((error: BusinessError) => {
    console.error(`ReadImageMetadata failed error.code is ${error.code}, error.message is ${error.message}`);
  })
}
```

**writeImageMetadata23+**

writeImageMetadata(imageMetadata: ImageMetadata): Promise<void>

批量修改图片属性。使用Promise异步回调。


- 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreateimagesource7)实例或通过传入的uri创建[image.createImageSource](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreateimagesource)实例。

- 该方法在内存中完成批量数据修改后会一次性写入文件，相比[modifyImageProperties](#ZH-CN_TOPIC_0000002522081974__modifyimageproperties12)更高效。

- 支持修改JPEG、PNG和HEIF文件类型的图片属性，图片需要包含Exif信息。修改属性前，先通过supportedFormats属性查询设备是否支持HEIF格式的Exif读写。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageMetadata | ImageMetadata | 是 | 图像的元数据集。若imageMetadata中的属性值都为空，则清空所有Exif元数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700102 | Unsupported MIME type. |
| 7700202 | Unsupported metadata. |
| 7700204 | Invalid parameter. Possible causes: The imageSource object is released. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function WriteImageMetadata(imageSourceObj : image.ImageSource) {
  let propertyKeys = ["ImageWidth", "HwMnoteIsXmageSupported"];
  let metaData = await imageSourceObj.readImageMetadata(propertyKeys);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    metaData.exifMetadata.imageLength = 3072;
  }
  await imageSourceObj.writeImageMetadata(metaData).then(() => {
    console.info(`write image metadata success.`);
  }).catch((error: BusinessError) => {
    console.error(`writeImageMetadata failed error.code is ${error.code}, error.message is ${error.message}`);
  });
}
```

#### updateData9+

updateData(buf: ArrayBuffer, isFinished: boolean, offset: number, length: number): Promise<void>

更新增量数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 存放增量数据的buffer。 |
| isFinished | boolean | 是 | true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。 |
| offset | number | 是 | 即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。 |
| length | number | 是 | 当前buffer的长度。单位：字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buf | ArrayBuffer | 是 | 存放增量数据的buffer。 |
| isFinished | boolean | 是 | true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。 |
| offset | number | 是 | 即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。 |
| length | number | 是 | 当前buffer的长度。单位：字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当更新增量数据成功，err为undefined，否则为错误对象。 |

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

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](Interface (Picture).md#ZH-CN_TOPIC_0000002553361895__release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptionsForPicture | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Picture> | Promise对象，返回Picture。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified.2.Incorrect parameter types; 3.Parameter verification failed. |
| 7700301 | Failed to decode image. |

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
```

#### createPictureAtIndex20+

createPictureAtIndex(index: number): Promise<Picture>

通过指定序号的图片（目前仅支持GIF和HEIF23+图像序列格式）创建Picture对象。使用Promise异步回调。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](Interface (Picture).md#ZH-CN_TOPIC_0000002553361895__release13)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 解码图片序号。图片序号有效的取值范围为：[0，帧数-1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Picture> | Promise对象，返回Picture。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7700101 | Bad source. |
| 7700102 | Unsupported MIME type. |
| 7700103 | Image too large. |
| 7700203 | Unsupported options. For example, index is invalid. |
| 7700301 | Decoding failed. |

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
```

#### createPixelMap7+

createPixelMap(options?: DecodingOptions): Promise<PixelMap>

通过图片解码参数创建PixelMap对象。使用Promise异步回调。

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002522081974__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002522081978__allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PixelMap> | Promise对象，返回PixelMap。 |

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

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002522081974__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002522081978__allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<PixelMap> | 是 | 回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

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

从API version 15开始，推荐使用[createPixelMapUsingAllocator](#ZH-CN_TOPIC_0000002522081974__createpixelmapusingallocator15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002522081978__allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 是 | 解码参数。 |
| callback | AsyncCallback<PixelMap> | 是 | 回调函数，当创建PixelMap对象成功，err为undefined，data为获取到的PixelMap对象；否则为错误对象。 |

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

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

从API version 15开始，推荐使用[createPixelMapUsingAllocatorSync](#ZH-CN_TOPIC_0000002522081974__createpixelmapusingallocatorsync15)，该接口可以指定输出pixelMap的内存类型[AllocatorType](Enums.md#ZH-CN_TOPIC_0000002522081978__allocatortype15)，详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。


该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | 用于同步返回创建结果。 |

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
```

#### createPixelMapList10+

createPixelMapList(options?: DecodingOptions): Promise<Array<PixelMap>>

通过图片解码参数创建PixelMap数组。使用Promise异步回调。

针对动态图（如Gif、Webp），该接口会返回每帧图片数据；针对静态图，该接口会返回唯一的一帧图片数据。


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 否 | 解码参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<PixelMap>> | 异步返回PixelMap数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

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


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<PixelMap>> | 是 | 回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

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


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 是 | 解码参数。 |
| callback | AsyncCallback<Array<PixelMap>> | 是 | 回调函数，当创建PixelMap对象数组成功，err为undefined，data为获取到的PixelMap对象数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980099 | The shared memory data is abnormal. |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980109 | Failed to crop the image. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980137 | Invalid media operation. |
| 62980173 | The DMA memory does not exist. |
| 62980174 | The DMA memory data is abnormal. |

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

createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: [AllocatorType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15)): Promise<PixelMap>

使用指定的分配器根据图像解码参数异步创建PixelMap对象。使用Promise异步回调。接口使用详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。


- 该方法为非线程安全的方法，不支持在同一个[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例上并发调用。

- 由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 否 | 解码参数。 |
| allocatorType | [AllocatorType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15) | 否 | 用于图像解码的内存类型。默认值为AllocatorType.AUTO。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PixelMap> | Promise对象，返回PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

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
```

#### createPixelMapUsingAllocatorSync15+

createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: [AllocatorType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15)): PixelMap

根据指定的分配器同步创建一个基于图像解码参数的PixelMap对象。接口使用详情请参考[图片解码内存优化(ArkTS)](../../guides/图片解码内存优化.md)。

由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](Interface (PixelMap).md#ZH-CN_TOPIC_0000002522241972__release7)方法，及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

该方法为同步方法，调用时会阻塞当前线程，不建议在主线程中调用，否则可能导致应用卡顿、掉帧或响应延迟。具体场景参考[耗时任务并发场景简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview)。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DecodingOptions | 否 | 解码参数。 |
| allocatorType | [AllocatorType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285837__allocatortype15) | 否 | 用于图像解码的内存类型。默认值为AllocatorType.AUTO。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | 用于同步返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types;3.Parameter verification failed. |
| 7700101 | Bad source. e.g.,1. Image has invalid width or height. 2. Image source incomplete. 3. Read image data failed. 4. Codec create failed. |
| 7700102 | Unsupported mimetype. |
| 7700103 | Image too large. This status code is thrown when an error occurs during the process of checking size. |
| 7700201 | Unsupported allocator type, e.g., use share memory to decode a HDR image as only DMA supported hdr metadata. |
| 7700203 | Unsupported options, e.g., cannot convert image into desired pixel format. |
| 7700301 | Failed to decode image. |
| 7700302 | Failed to allocate memory. |

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
```

#### getDelayTimeList10+

getDelayTimeList(callback: AsyncCallback<Array<number>>): void

获取图像延迟时间数组。使用callback异步回调。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，当获取图像延迟时间数组成功，err为undefined，data为获取到的图像延时时间数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回延迟时间数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980110 | The image source data is incorrect. |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980149 | Invalid MIME type for the image source. |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，当获取图像帧数成功，err为undefined，data为获取到的图像帧数；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回图像帧数。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980111 | The image source data is incomplete. |
| 62980112 | The image format does not match. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid image parameter. |
| 62980116 | Failed to decode the image. |
| 62980118 | Failed to create the image plugin. |
| 62980122 | Failed to decode the image header. |
| 62980137 | Invalid media operation. |

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

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回帧过渡模式数组。 |

**错误码：**

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980137 | Invalid media operation. |
| 62980149 | Invalid MIME type for the image source. |

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

释放[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例。使用callback异步回调。

由于图片占用内存较大，所以当[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当资源释放成功，err为undefined，否则为错误对象。 |

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

释放[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例。使用Promise异步回调。

由于图片占用内存较大，所以当[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002522081974__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| options | GetImagePropertyOptions | 否 | 图片属性，包括图片序号与默认属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回图片属性值，如获取失败则返回属性默认值。 |

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

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002522081974__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| callback | AsyncCallback<string> | 是 | 回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。 |

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

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


从API version 7开始支持，从API version 11废弃，建议使用[getImageProperty](#ZH-CN_TOPIC_0000002522081974__getimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| options | GetImagePropertyOptions | 是 | 图片属性，包括图片序号与默认属性值。 |
| callback | AsyncCallback<string> | 是 | 回调函数，当获取图片属性值成功，err为undefined，data为获取到的图片属性值；否则为错误对象。 |

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

该接口仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](#ZH-CN_TOPIC_0000002522081974__modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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

仅支持JPEG、PNG、HEIF12+和WEBP23+（不同硬件设备支持情况不同）文件，且需要包含Exif信息。


调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

从API version 9开始支持，从API version 11废弃，建议使用[modifyImageProperty](#ZH-CN_TOPIC_0000002522081974__modifyimageproperty11)代替。

**系统能力：** SystemCapability.Multimedia.Image.[ImageSource](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreateimagesource7)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 图片属性名。 |
| value | string | 是 | 属性值。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当修改图片属性值成功，err为undefined，否则为错误对象。 |

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