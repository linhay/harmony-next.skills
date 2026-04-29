# class (ExifMetadata)

ExifMetadata implements Metadata

Exif（Exchangeable image file format）元数据。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { image } from '@kit.ImageKit';
```

**属性**

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Multimedia.Image.Core

各属性详细取值，请参考[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002522081978__propertykey7)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| newSubfileType | number | 否 | 是 | 表示该子文件的数据类型（例如文本/图像等基本类型，而非具体存储格式）。 |
| subfileType | number | 否 | 是 | 已弃用标签，表示该子文件中的数据类型。请使用newSubfileType替代。 |
| imageWidth | number | 否 | 是 | 图像宽度。单位为像素（px）。 |
| imageLength | number | 否 | 是 | 图像长度。单位为像素（px）。 |
| bitsPerSample | number[] | 否 | 是 | 像素各分量的位数。如RGB是3分量，格式是8，8，8。 |
| compression | number | 否 | 是 | 用于图像压缩的算法标准。 |
| photometricInterpretation | number | 否 | 是 | 像素组成，如RGB（红绿蓝，Red Green Blue）和YCbCr（亮度-蓝色色差-红色色差，Luma-Chrominance）。 |
| imageDescription | string | 否 | 是 | 图像描述。 |
| make | string | 否 | 是 | 拍摄设备的品牌制造商名称。 |
| model | string | 否 | 是 | 相机型号。 |
| stripOffsets | number[] | 否 | 是 | 图像数据的分块存储偏移量，单位为字节。 为提高大图像访问效率，原始像素数据被分割为多个连续区块（称为条带）。 此标签按顺序存储每个条带在文件中的起始位置偏移量。 |
| orientation | Orientation | 否 | 是 | 图像方向。 |
| samplesPerPixel | number | 否 | 是 | 记录每个像素的颜色分量数量，适用于RGB（红绿蓝，Red Green Blue）和YCbCr（亮度-蓝色色差-红色色差，Luma-Chrominance）色彩模型。 由于这两种模型都是三分量模型（一个亮度分量加两个色度分量，或三个颜色通道），因此该标签的标准值为3。 对于JPEG压缩图像，此标签将会被对应的JPEG标记替换。 |
| rowsPerStrip | number | 否 | 是 | 每条图像数据的行数。 |
| stripByteCounts | number[] | 否 | 是 | 压缩后每个条带中的字节数。 |
| xResolution | number | 否 | 是 | 宽度方向上的图像分辨率。 |
| yResolution | number | 否 | 是 | 高度方向上的图像分辨率。 |
| planarConfiguration | number | 否 | 是 | 指示像素分量是以块状或平面格式记录。 |
| resolutionUnit | number | 否 | 是 | 用于测量宽度方向上的图像分辨率和高度方向上的图像分辨率的单位。 |
| transferFunction | string | 否 | 是 | 图像的传递函数，通常用于颜色校正。 |
| software | string | 否 | 是 | 用于生成图像的软件名称和版本。 |
| dateTime | string | 否 | 是 | 图像创建的日期和时间。 在本标准中，指文件更改的日期和时间。格式为：“YYYY:MM:DD HH:MM:SS”，时间以24小时格式显示。例如：“2025:12:15 18:44:59”。 |
| artist | string | 否 | 是 | 创建图像的人的姓名。 |
| whitePoint | number[] | 否 | 是 | 图像白点的色度。 |
| primaryChromaticities | number[] | 否 | 是 | 图像原色的色度。 |
| photoMode | number | 否 | 是 | 照片模式。 |
| jpegInterchangeFormat | number | 否 | 是 | JPEG交换格式比特流的SOI（Start of Image）标记。 |
| jpegInterchangeFormatLength | number | 否 | 是 | JPEG流的字节数。 |
| yCbCrCoefficients | number[] | 否 | 是 | 用于将RGB图像数据转换为YCbCr图像数据的变换矩阵系数。 |
| yCbCrSubSampling | number[] | 否 | 是 | 色度分量与亮度分量的采样比。 |
| yCbCrPositioning | number | 否 | 是 | 色度分量相对于亮度分量的位置。 |
| referenceBlackWhite | number[] | 否 | 是 | 参考黑点值和白点值。 |
| copyright | string | 否 | 是 | 图像的版权信息。 |
| exposureTime | number | 否 | 是 | 曝光时间。 |
| fNumber | number | 否 | 是 | 光圈值，如f/1.8。 |
| exposureProgram | number | 否 | 是 | 相机在拍摄照片时用于设置曝光的程序类。 |
| spectralSensitivity | string | 否 | 是 | 指示相机每个通道的光谱灵敏度。 |
| gpsVersionID | number[] | 否 | 是 | GPS信息的格式版本标识符。 |
| gpsLatitudeRef | string | 否 | 是 | GPS纬度参考。例如，N表示北纬，S表示南纬。 |
| gpsLatitude | number[] | 否 | 是 | GPS纬度。 纬度用三个RATIONAL（分数形式存储的数值）值表示，分别是度、分和秒，格式为dd/1、mm/1、ss/1。 当使用度数和分钟时，分钟分数最多保留两位小数，格式为dd/1，mmmm/100,0/1。 |
| gpsLongitudeRef | string | 否 | 是 | GPS经度参考。例如，E表示东经，W表示西经。 |
| gpsLongitude | number[] | 否 | 是 | GPS经度。 经度用三个RATIONAL（分数形式存储的数值）值表示，分别是度、分和秒，格式为dd/1、mm/1、ss/1。 当使用度数和分钟时，分钟分数最多保留两位小数，格式为dd/1，mmmm/100，0/1。 |
| gpsAltitudeRef | number | 否 | 是 | 用于GPS的参考高度。 |
| gpsAltitude | number | 否 | 是 | 基于GPSAltitudeRef中的参考高度。 |
| gpsTimestamp | number[] | 否 | 是 | GPS时间戳。 |
| gpsSatellites | string | 否 | 是 | 用于测量的GPS卫星。通常是它的伪随机噪声码（PRN）编号。 |
| gpsStatus | string | 否 | 是 | 记录图像时GPS接收器的状态。 |
| gpsMeasureMode | string | 否 | 是 | GPS测量模式。 |
| gpsDop | number | 否 | 是 | GPS数据精度DOP精度衰减因子（Dilution of Precision）。 |
| gpsSpeedRef | string | 否 | 是 | GPS接收器移动速度的单位。 |
| gpsSpeed | number | 否 | 是 | GPS接收器移动的速度。 |
| gpsTrackRef | string | 否 | 是 | 提供GPS接收机运动方向的参考。 |
| gpsTrack | number | 否 | 是 | GPS接收器移动的方向。 |
| gpsImgDirectionRef | string | 否 | 是 | 图像方向的参考。 |
| gpsImgDirection | number | 否 | 是 | 拍摄时图像的方向。 |
| gpsMapDatum | string | 否 | 是 | GPS接收机使用的大地测量数据。 |
| gpsDestLatitudeRef | string | 否 | 是 | 指示目标点的纬度参考。 |
| gpsDestLatitude | number[] | 否 | 是 | 目的地的纬度。 |
| gpsDestLongitudeRef | string | 否 | 是 | 指示目标点的经度参考。 |
| gpsDestLongitude | number[] | 否 | 是 | 目的地的经度。 |
| gpsDestBearingRef | string | 否 | 是 | 指向目的地的方位参考。 |
| gpsDestBearing | number | 否 | 是 | 到达目的地的方位。 |
| gpsDestDistanceRef | string | 否 | 是 | 到目标点距离的测量单位。 |
| gpsDestDistance | number | 否 | 是 | 到目的地的距离。 |
| gpsProcessingMethod | string | 否 | 是 | 记录定位方法的名称。 |
| gpsAreaInformation | string | 否 | 是 | GPS区域名称的字符串。 |
| gpsDateStamp | string | 否 | 是 | GPS日期戳。 |
| gpsDifferential | number | 否 | 是 | 是否对GPS数据应用了差分校正，这对精确定位精度至关重要。 |
| gpsHPositioningError | number | 否 | 是 | 水平定位误差。单位为米（m）。 |
| isoSpeedRatings | number | 否 | 是 | ISO 12232中指定的相机或输入设备的ISO速度和ISO纬度。 |
| photographicSensitivity | number[] | 否 | 是 | 拍摄图像时相机或输入设备的灵敏度。 |
| oecf | ArrayBuffer | 否 | 是 | ISO 14524中规定的光电转换函数（OECF）。 |
| sensitivityType | number | 否 | 是 | 灵敏度类型。 |
| standardOutputSensitivity | number | 否 | 是 | 标准输出灵敏度。 |
| recommendedExposureIndex | number | 否 | 是 | GPS测量模式。 |
| isoSpeedLatitudeyyy | number | 否 | 是 | 表示相机传感器在单次曝光中可记录的最大动态范围。单位为EV。 |
| isoSpeedLatitudezzz | number | 否 | 是 | 表示相机传感器在过曝方向保护高光细节的能力边界。单位为EV。 |
| exifVersion | string | 否 | 是 | 支持的Exif标准的版本。 |
| dateTimeOriginal | string | 否 | 是 | 生成原始图像数据的日期和时间。 对于DSC（Digital Still Camera 数码静态相机），会记录拍摄照片的日期和时间。格式为“YYYY:MM:DD HH:MM:SS”，时间以24小时格式显示。 |
| dateTimeDigitized | string | 否 | 是 | 将图像作为数字数据存储的日期和时间。 例如，如果DSC捕获了图像，并同时记录了文件，则DateTimeOriginal和DateTimeDigitized将具有相同的内容。格式为“YYYY:MM:DD HH:MM:SS”，时间以24小时格式显示。 |
| offsetTime | string | 否 | 是 | 作为DateTime标签的补充元数据，解决因地理时区变化导致的时间戳歧义问题。 |
| offsetTimeOriginal | string | 否 | 是 | 设备的地理时区位置。 |
| offsetTimeDigitized | string | 否 | 是 | 记录图像数字化时的UTC协调世界时（Coordinated Universal Time）偏移，有助于精确调整时间戳。 |
| componentsConfiguration | string | 否 | 是 | 压缩数据的信息。 |
| compressedBitsPerPixel | number | 否 | 是 | 图像压缩方案。单位为每像素比特。 |
| shutterSpeedValue | number | 否 | 是 | 快门速度，表示为摄影曝光相加系统值APEX（Additive System of Photographic Exposure）。 |
| apertureValue | number | 否 | 是 | 镜头光圈。单位为APEX。 |
| brightnessValue | number | 否 | 是 | 图像的亮度值。单位为APEX。 |
| exposureBiasValue | number | 否 | 是 | 曝光偏差值。 |
| maxApertureValue | number | 否 | 是 | 镜头的最小光圈值。 |
| subjectDistance | number | 否 | 是 | 拍照设备到被摄体的距离。单位为米（m）。 |
| meteringMode | number | 否 | 是 | 测光模式。 |
| lightSource | number | 否 | 是 | 光源。 |
| flash | number | 否 | 是 | 闪光。 |
| focalLength | number | 否 | 是 | 焦距。，单位为毫米。 |
| subjectArea | number[] | 否 | 是 | 用于指示主要对象在整个场景中的位置和区域。 |
| makerNote | ArrayBuffer | 否 | 是 | Exif/相机文件系统设计规则DCF（Design rule for Camera File system）写入器制造商记录所需信息的标签。 |
| userComment | string | 否 | 是 | 用户评论。 |
| subsecTime | string | 否 | 是 | 记录DateTime标记的秒分数的标记。 |
| subsecTimeOriginal | string | 否 | 是 | 记录DateTimeOriginal标记的秒数。 |
| subsecTimeDigitized | string | 否 | 是 | 记录DateTimeDigitized标记的秒数。 |
| flashpixVersion | string | 否 | 是 | FPXR（FlashPix Extension Resource）支持的FlashPix格式版本，用于增强设备兼容性。 |
| colorSpace | number | 否 | 是 | 颜色空间信息标签，通常记录为颜色空间说明符。 |
| pixelXDimension | number | 否 | 是 | 图像在X轴上的（二维坐标系中的Horizontal Axis）尺寸。 |
| pixelYDimension | number | 否 | 是 | 图像在Y轴上的（二维坐标系中的Vertical Axis）尺寸。 |
| relatedSoundFile | string | 否 | 是 | 与图像数据相关的音频文件的名称。 |
| flashEnergy | number | 否 | 是 | 图像捕获时的闪光灯能量。单位为光束烛光秒(BCPS，Beam Candlepower Seconds)。 |
| spatialFrequencyResponse | ArrayBuffer | 否 | 是 | 相机或输入设备空间频率表。 |
| focalPlaneXResolution | number | 否 | 是 | 传感器物理平面X轴方向上每单位物理长度的像素数量。 |
| focalPlaneYResolution | number | 否 | 是 | 传感器物理平面Y轴方向上每单位物理长度的像素数量。 |
| focalPlaneResolutionUnit | number | 否 | 是 | FocalPlaneXResolution和FocalPlaneYResolution的测量单位。 |
| subjectLocation | number[] | 否 | 是 | 图像中主体的像素坐标（基于左上角原点）。 |
| exposureIndex | number | 否 | 是 | 拍摄时选定的曝光指数。 |
| sensingMethod | number | 否 | 是 | 摄像头的图像传感器类型。 |
| fileSource | ArrayBuffer | 否 | 是 | 指示图像源。 |
| sceneType | ArrayBuffer | 否 | 是 | 场景类型。 |
| cfaPattern | ArrayBuffer | 否 | 是 | 图像传感器的滤色器阵列CFA（Color Filter Array）几何图案。 |
| customRendered | number | 否 | 是 | 表示对图像数据的特殊处理，如HDR合成、AI场景增强。 |
| exposureMode | number | 否 | 是 | 曝光模式。 |
| whiteBalance | number | 否 | 是 | 白平衡。 |
| digitalZoomRatio | number | 否 | 是 | 拍摄时的数字变焦比。 |
| focalLengthIn35mmFilm | number | 否 | 是 | 35mm胶片的焦距。 |
| sceneCaptureType | number | 否 | 是 | 拍摄的场景类型。 |
| gainControl | number | 否 | 是 | 整体图像增益调整程度。 |
| contrast | number | 否 | 是 | 相机应用的对比度优化策略。例如：标准处理、弱化对比度等。 |
| saturation | number | 否 | 是 | 相机应用的色彩饱和度调节策略。例如：标准、降饱和模式等。 |
| sharpness | number | 否 | 是 | 相机应用的边缘增强处理方式。例如：弱锐化、标准锐化等。 |
| deviceSettingDescription | ArrayBuffer | 否 | 是 | 特定相机型号的拍照条件信息。 |
| subjectDistanceRange | number | 否 | 是 | 指示到对象的距离范围。 |
| imageUniqueId | string | 否 | 是 | 为每个图像分配的唯一标识符。 |
| cameraOwnerName | string | 否 | 是 | 相机所有者的姓名。 |
| bodySerialNumber | string | 否 | 是 | 相机机身的序列号。 |
| lensSpecification | number[] | 否 | 是 | 所用镜头的规格。 |
| lensMake | string | 否 | 是 | 镜头的制造商。 |
| lensModel | string | 否 | 是 | 镜头的型号名称。 |
| lensSerialNumber | string | 否 | 是 | 镜头的序列号。 |
| compositeImage | number | 否 | 是 | 指示图像是否为合成图像。 |
| sourceImageNumberOfCompositeImage | number[] | 否 | 是 | 用于合成图像的源图像数量。 |
| sourceExposureTimesOfCompositeImage | ArrayBuffer | 否 | 是 | 合成图像的源图像的曝光时间，例如1/33秒。 |
| gamma | number | 否 | 是 | 每个组件的伽玛值。 |

**createInstance**

static createInstance(): ExifMetadata

创建一个空的[ExifMetadata](class (ExifMetadata).md)实例。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| ExifMetadata | 返回ExifMetadata的空实例。 |

示例：

```ets
async function exifMetadataCreateInstance(context: Context) {
  let exifMetadata = image.ExifMetadata.createInstance();
  if (exifMetadata != undefined) {
    console.info("createInstance success");
  }
```

**getProperties**

getProperties(key: Array<string>): Promise<Record<string, string | null>>

获取图像的元数据属性值。使用Promise异步回调。

要查询的属性的具体信息请参考[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002522081978__propertykey7)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array<string> | 是 | 要获取的值的属性名称。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回获取到的图像元数据属性值。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600202 | Unsupported metadata. Possible causes: unsupported metadata type. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    await metaData.exifMetadata.getProperties(["ImageWidth", "ImageLength"]).then((data) => {
      console.info('Get properties ',JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
```

**setProperties**

setProperties(records: Record<string, string | null>): Promise<void>

批量设置图片元数据中的指定属性的值。使用Promise异步回调。

要查询的属性的具体信息请参考[PropertyKey](Enums.md#ZH-CN_TOPIC_0000002522081978__propertykey7)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record<string, string | null> | 是 | 用户要修改的ExifMetadata对象的属性和键值对的集合。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600202 | Unsupported metadata. Possible causes: unsupported metadata type. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataSetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let setkey: Record<string, string | null> = {
      "ImageWidth": "200",
      "ImageLength": "300"
    };
    await metaData.exifMetadata.setProperties(setkey).then(async () => {
      console.info('Set properties success.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
```

**getAllProperties**

getAllProperties(): Promise<Record<string, string | null>>

获取图片中所有元数据的属性和值。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Record<string, string | null>> | Promise对象，返回元数据拥有的所有属性的值。 |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetAllProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    await metaData.exifMetadata.getAllProperties().then((data) => {
      const count = Object.keys(data).length;
      console.info('Metadata have ', count, ' properties');
      console.info(`Get metadata all properties: ${data}`);
    }).catch((error: BusinessError) => {
      console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
```

**clone**

clone(): Promise<ExifMetadata>

对Exif元数据进行克隆。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ExifMetadata> | Promise对象，成功返回Exif元数据实例。 |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let new_metadata = await metaData.exifMetadata.clone();
    new_metadata.getProperties(["ImageWidth"]).then((data1) => {
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
```

**getBlob23+**

getBlob(): Promise<ArrayBuffer>

以二进制数据的形式获取元数据。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回元数据的二进制数据。 |

示例：

```ets
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let blob = await metaData.exifMetadata.getBlob();
    if (blob != undefined) {
      console.info("get blob success");
    }
```

**setBlob23+**

setBlob(blob: ArrayBuffer): Promise<void>

使用二进制数据替换当前元数据。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Image.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blob | ArrayBuffer | 是 | 要替换的二进制数据。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码的详细介绍请参见[Image错误码](Image错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid parameter. Possible causes: The blob is empty or has a length of 0. |

示例：

```ets
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataSetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let blob = await metaData.exifMetadata.getBlob();
    if (blob != undefined) {
      console.info("get blob success");
      metaData.exifMetadata.setBlob(blob);
    }
    let new_blob = metaData.exifMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
```