# image_common.h

#### 概述

声明图像接口使用的公共枚举和结构体。

**引用文件：** <multimedia/image_framework/image/image_common.h>

**库：** libimage_common.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：**[Image_NativeModule](../../topics/graphics/Image_NativeModule.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Image_Size](../../topics/graphics/Image_Size.md)Image_Size图像大小结构体。[Image_Region](../../topics/graphics/Image_Region.md)Image_Region待解码的图像源区域结构体。[Image_PositionArea](../../topics/graphics/Image_PositionArea.md)Image_PositionArea要读取或写入的图像像素区域。[Image_Scale](../../topics/graphics/Image_Scale.md)Image_Scale图像缩放倍数。[Image_String](../../topics/graphics/Image_String.md)Image_String/Image_MimeType字符串结构。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md)-声明用于Picture的元数据。

#### 枚举

名称typedef关键字描述[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)Image_ErrorCode错误码。[Image_MetadataType](#ZH-CN_TOPIC_0000002497445872__image_metadatatype)Image_MetadataType定义元数据类型。[IMAGE_ALLOCATOR_MODE](#ZH-CN_TOPIC_0000002497445872__image_allocator_mode)IMAGE_ALLOCATOR_MODEpixelmap内存分配类型。

#### 函数

名称描述[Image_ErrorCode OH_PictureMetadata_Create(Image_MetadataType metadataType, OH_PictureMetadata **metadata)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_create)创建OH_PictureMetadata指针。[Image_ErrorCode OH_PictureMetadata_GetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_getproperty)根据key获取Metadata的单条属性。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。[Image_ErrorCode OH_PictureMetadata_SetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_setproperty)根据key修改Metadata的单条属性。[Image_ErrorCode OH_PictureMetadata_GetPropertyWithNull(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_getpropertywithnull)获取图片元数据的属性值。输出的value.data以字符串结束符'\0'结尾。[Image_ErrorCode OH_PictureMetadata_Release(OH_PictureMetadata *metadata)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_release)释放OH_PictureMetadata指针。[Image_ErrorCode OH_PictureMetadata_Clone(OH_PictureMetadata *oldMetadata, OH_PictureMetadata **newMetadata)](#ZH-CN_TOPIC_0000002497445872__oh_picturemetadata_clone)拷贝元数据。

#### 变量

名称描述static const char * MIME_TYPE_BMP = "image/bmp"

bmp图片格式。

**起始版本：** 12

static const char * MIME_TYPE_JPEG = "image/jpeg"

jpeg图片格式。

**起始版本：** 12

static const char * MIME_TYPE_HEIC = "image/heic"

heic图片格式。

**起始版本：** 12

static const char * MIME_TYPE_PNG = "image/png"

png图片格式。

**起始版本：** 12

static const char * MIME_TYPE_WEBP = "image/webp"

webp图片格式。

**起始版本：** 12

static const char * MIME_TYPE_GIF = "image/gif"

gif图片格式。

**起始版本：** 12

static const char * MIME_TYPE_ICON = "image/x-icon"

ico图片格式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_BITS_PER_SAMPLE = "BitsPerSample"

每个像素比特数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ORIENTATION = "Orientation"

图片方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_IMAGE_LENGTH = "ImageLength"

图片长度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_IMAGE_WIDTH = "ImageWidth"

图片宽度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_LATITUDE = "GPSLatitude"

图片纬度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_LONGITUDE = "GPSLongitude"

图片经度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_LATITUDE_REF = "GPSLatitudeRef"

纬度引用，例如N或S。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_LONGITUDE_REF = "GPSLongitudeRef"

经度引用，例如W或E。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DATE_TIME_ORIGINAL = "DateTimeOriginal"

拍摄时间，例如2022:09:06 15:48:00。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_EXPOSURE_TIME = "ExposureTime"

曝光时间，例如1/33 sec。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SCENE_TYPE = "SceneType"

拍摄场景模式，例如人像、风光、运动、夜景等。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ISO_SPEED_RATINGS = "ISOSpeedRatings"

ISO感光度，例如400。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_F_NUMBER = "FNumber"

光圈值，例如f/1.8。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COMPRESSED_BITS_PER_PIXEL = "CompressedBitsPerPixel"

用于压缩图像的压缩模式，单位为每像素位数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COMPRESSION = "Compression"

图像压缩方案。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_PHOTOMETRIC_INTERPRETATION = "PhotometricInterpretation"

像素构成，例如RGB或YCbCr。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_STRIP_OFFSETS = "StripOffsets"

每个strip的字节偏移量。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SAMPLES_PER_PIXEL = "SamplesPerPixel"

每个像素的分量数。由于该标准适用于RGB和YCbCr图像，因此该标签的值设置为3。在JPEG压缩数据中，使用JPEG标记代替该标签。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ROWS_PER_STRIP = "RowsPerStrip"

每个strip的图像数据行数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_STRIP_BYTE_COUNTS = "StripByteCounts"

每个图像数据带的总字节数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_X_RESOLUTION = "XResolution"

图像宽度方向的分辨率。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_Y_RESOLUTION = "YResolution"

图像高度方向的分辨率。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_PLANAR_CONFIGURATION = "PlanarConfiguration"

表示像素组件的记录格式，chunky格式或是planar格式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_RESOLUTION_UNIT = "ResolutionUnit"

用于测量XResolution和YResolution的单位。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_TRANSFER_FUNCTION = "TransferFunction"

图像的传递函数，通常用于颜色校正。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SOFTWARE = "Software"

用于生成图像的软件的名称和版本。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ARTIST = "Artist"

创建图像的用户名称。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_WHITE_POINT = "WhitePoint"

图像的白点色度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_PRIMARY_CHROMATICITIES = "PrimaryChromaticities"

图像的主要颜色的色度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_YCBCR_COEFFICIENTS = "YCbCrCoefficients"

从RGB到YCbCr图像数据的转换矩阵系数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_YCBCR_SUB_SAMPLING = "YCbCrSubSampling"

色度分量与亮度分量的采样比率。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_YCBCR_POSITIONING = "YCbCrPositioning"

色度分量相对于亮度分量的位置。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_REFERENCE_BLACK_WHITE = "ReferenceBlackWhite"

参考黑点值和参考白点值。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COPYRIGHT = "Copyright"

图像的版权信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_JPEG_INTERCHANGE_FORMAT = "JPEGInterchangeFormat"

JPEG压缩缩略图数据开始字节（SOI）的偏移。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_JPEG_INTERCHANGE_FORMAT_LENGTH = "JPEGInterchangeFormatLength"

JPEG压缩缩略图数据的字节数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_EXPOSURE_PROGRAM = "ExposureProgram"

拍照时相机用来设置曝光的程序的类别。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SPECTRAL_SENSITIVITY = "SpectralSensitivity"

表示所用相机的每个通道的光谱灵敏度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_OECF = "OECF"

表示ISO 14524中规定的光电转换函数（OECF）。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_EXIF_VERSION = "ExifVersion"

支持的Exif标准版本。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DATE_TIME_DIGITIZED = "DateTimeDigitized"

图像作为数字数据存储的日期和时间，格式为YYYY:MM:DD HH:MM:SS。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COMPONENTS_CONFIGURATION = "ComponentsConfiguration"

压缩数据的特定信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SHUTTER_SPEED_VALUE = "ShutterSpeedValue"

快门速度，以APEX（摄影曝光的加法系统）值表示。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_BRIGHTNESS_VALUE = "BrightnessValue"

图像的亮度值，以APEX单位表示。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_MAX_APERTURE_VALUE = "MaxApertureValue"

最小F数镜头。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBJECT_DISTANCE = "SubjectDistance"

测量单位为米的主体距离。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBJECT_AREA = "SubjectArea"

该标签指示整个场景中主要主体的位置和区域。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_MAKER_NOTE = "MakerNote"

Exif/DCF制造商使用的标签，用于记录任何所需信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBSEC_TIME = "SubsecTime"

用于为DateTime标签记录秒的分数的标签。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBSEC_TIME_ORIGINAL = "SubsecTimeOriginal"

用于为DateTimeOriginal标签记录秒的分数的标签。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBSEC_TIME_DIGITIZED = "SubsecTimeDigitized"

用于为DateTimeDigitized标签记录秒的分数的标签。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FLASHPIX_VERSION = "FlashpixVersion"

该标签表示FPXR文件支持的Flashpix格式版本，增强了设备兼容性。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COLOR_SPACE = "ColorSpace"

色彩空间信息标签，通常记录为色彩空间指定符。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_RELATED_SOUND_FILE = "RelatedSoundFile"

与图像数据相关的音频文件的名称。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FLASH_ENERGY = "FlashEnergy"

图像捕获时的闪光能量，以BCPS表示。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SPATIAL_FREQUENCY_RESPONSE = "SpatialFrequencyResponse"

相机或输入设备的空间频率表。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FOCAL_PLANE_X_RESOLUTION = "FocalPlaneXResolution"

图像宽度中每FocalPlaneResolutionUnit的像素。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FOCAL_PLANE_Y_RESOLUTION = "FocalPlaneYResolution"

图像高度中每FocalPlaneResolutionUnit的像素。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FOCAL_PLANE_RESOLUTION_UNIT = "FocalPlaneResolutionUnit"

测量FocalPlaneXResolution和FocalPlaneYResolution的单位。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBJECT_LOCATION = "SubjectLocation"

主要对象相对于左边缘的位置。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_EXPOSURE_INDEX = "ExposureIndex"

捕获时选定的曝光指数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SENSING_METHOD = "SensingMethod"

相机上的图像传感器类型。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FILE_SOURCE = "FileSource"

表明图像来源。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_CFA_PATTERN = "CFAPattern"

图像传感器的色彩滤光片（CFA）几何图案。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_CUSTOM_RENDERED = "CustomRendered"

指示图像数据上的特殊处理。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_EXPOSURE_MODE = "ExposureMode"

拍摄时设置的曝光模式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DIGITAL_ZOOM_RATIO = "DigitalZoomRatio"

捕获时的数字变焦比率。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SCENE_CAPTURE_TYPE = "SceneCaptureType"

捕获的场景类型。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GAIN_CONTROL = "GainControl"

整体图像增益调整的程度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_CONTRAST = "Contrast"

相机应用的对比度处理方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SATURATION = "Saturation"

相机应用的饱和度处理方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SHARPNESS = "Sharpness"

相机应用的锐度处理方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DEVICE_SETTING_DESCRIPTION = "DeviceSettingDescription"

特定相机模型的拍照条件信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBJECT_DISTANCE_RANGE = "SubjectDistanceRange"

表示主体到相机的距离范围。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_IMAGE_UNIQUE_ID = "ImageUniqueID"

为每张图片唯一分配的标识符。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_VERSION_ID = "GPSVersionID"

GPSInfoIFD的版本。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_ALTITUDE_REF = "GPSAltitudeRef"

用于GPS高度的参照高度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_ALTITUDE = "GPSAltitude"

基于GPSAltitudeRef的高度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_SATELLITES = "GPSSatellites"

用于测量的GPS卫星。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_STATUS = "GPSStatus"

录制图像时GPS接收器的状态。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_MEASURE_MODE = "GPSMeasureMode"

GPS测量模式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DOP = "GPSDOP"

GPS DOP（数据精度等级）。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_SPEED_REF = "GPSSpeedRef"

用来表示GPS接收器移动速度的单位。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_SPEED = "GPSSpeed"

GPS接收器的移动速度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_TRACK_REF = "GPSTrackRef"

GPS接收机移动方向的参照。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_TRACK = "GPSTrack"

GPS接收机的移动方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_IMG_DIRECTION_REF = "GPSImgDirectionRef"

图像方向的参照。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_IMG_DIRECTION = "GPSImgDirection"

拍摄时图像的方向。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_MAP_DATUM = "GPSMapDatum"

GPS接收器使用的大地测量数据。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_LATITUDE_REF = "GPSDestLatitudeRef"

目的地点的纬度参照。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_LATITUDE = "GPSDestLatitude"

目的地点的纬度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_LONGITUDE_REF = "GPSDestLongitudeRef"

目的地点的经度参照。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_PROCESSING_METHOD = "GPSProcessingMethod"

记录定位方法名的字符串。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_AREA_INFORMATION = "GPSAreaInformation"

记录GPS区域名的字符串。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DIFFERENTIAL = "GPSDifferential"

此字段表示GPS数据是否应用了差分校正，对于精确的位置准确性至关重要。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_BODY_SERIAL_NUMBER = "BodySerialNumber"

相机机身的序列号。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_CAMERA_OWNER_NAME = "CameraOwnerName"

相机所有者的姓名。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_COMPOSITE_IMAGE = "CompositeImage"

表示图像是否为合成图像。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DNG_VERSION = "DNGVersion"

DNG版本标签编码了符合DNG规范的四级版本号。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_LONGITUDE = "GPSDestLongitude"

目的地点的经度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_BEARING_REF = "GPSDestBearingRef"

指向目的地点的方位参照。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_BEARING = "GPSDestBearing"

目的地方位。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_DISTANCE_REF = "GPSDestDistanceRef"

目标点距离的测量单位。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_DEST_DISTANCE = "GPSDestDistance"

到目的地点的距离。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_DEFAULT_CROP_SIZE = "DefaultCropSize"

DefaultCropSize指定了原始坐标中的最终图像大小，考虑了额外的边缘像素。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GAMMA = "Gamma"

表示系数伽马的值。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ISO_SPEED_LATITUDEYYY = "ISOSpeedLatitudeyyy"

该标签指示摄像机或输入设备的ISO速度纬度yyy值，该值在ISO 12232中定义。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_ISO_SPEED_LATITUDEZZZ = "ISOSpeedLatitudezzz"

该标签指示摄像机或输入设备的ISO速度纬度zzz值，该值在ISO 12232中定义。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_LENS_MAKE = "LensMake"

镜头的制造商。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_LENS_MODEL = "LensModel"

镜头的型号名称。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_LENS_SERIAL_NUMBER = "LensSerialNumber"

镜头的序列号。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_LENS_SPECIFICATION = "LensSpecification"

使用的镜头规格。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_NEW_SUBFILE_TYPE = "NewSubfileType"

在Exif中，"NewSubfileType"字段用于标识子文件的数据类型，如全分辨率图像、缩略图或多帧图像的一部分。其值是位掩码，0代表全分辨率图像，1代表缩略图，2代表多帧图像的一部分。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_OFFSET_TIME = "OffsetTime"

在Exif中，OffsetTime字段表示与UTC（协调世界时）的时间偏移，格式为±HH:MM，用于确定照片拍摄的本地时间。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_OFFSET_TIME_DIGITIZED = "OffsetTimeDigitized"

此标签记录图像数字化时的UTC偏移量，有助于准确调整时间戳。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_OFFSET_TIME_ORIGINAL = "OffsetTimeOriginal"

此标签记录原始图像创建时的UTC偏移量，对于时间敏感的应用至关重要。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SOURCE_EXPOSURE_TIMES_OF_COMPOSITE_IMAGE = "SourceExposureTimesOfCompositeImage"

合成图像的源图像曝光时间。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SOURCE_IMAGE_NUMBER_OF_COMPOSITE_IMAGE = "SourceImageNumberOfCompositeImage"

用于合成图像的源图像数量。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SUBFILE_TYPE = "SubfileType"

此标签指示此子文件中的数据类型。标签已弃用，请使用NewSubfileType替代。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GPS_H_POSITIONING_ERROR = "GPSHPositioningError"

此标签指示水平定位误差，单位为米。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_PHOTOGRAPHIC_SENSITIVITY = "PhotographicSensitivity"

此标签指示拍摄图像时相机或输入设备的灵敏度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_BURST_NUMBER = "HwMnoteBurstNumber"

连拍次数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_CONF = "HwMnoteFaceConf"

人脸置信度。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_LEYE_CENTER = "HwMnoteFaceLeyeCenter"

左眼中心。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_MOUTH_CENTER = "HwMnoteFaceMouthCenter"

嘴中心。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_POINTER = "HwMnoteFacePointer"

脸部指针。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_RECT = "HwMnoteFaceRect"

脸部矩形。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_REYE_CENTER = "HwMnoteFaceReyeCenter"

右眼中心。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_SMILE_SCORE = "HwMnoteFaceSmileScore"

FaceCount张人脸的笑脸分数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FACE_VERSION = "HwMnoteFaceVersion"

人脸算法版本信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_FRONT_CAMERA = "HwMnoteFrontCamera"

是否是前置相机自拍。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SCENE_POINTER = "HwMnoteScenePointer"

场景指针。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_SCENE_VERSION = "HwMnoteSceneVersion"

场景算法版本信息。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_IS_XMAGE_SUPPORTED = "HwMnoteIsXmageSupported"

是否支持XMAGE。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_XMAGE_MODE = "HwMnoteXmageMode"

XMAGE水印模式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_XMAGE_LEFT = "HwMnoteXmageLeft"

水印区域X1坐标。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_XMAGE_TOP = "HwMnoteXmageTop"

水印区域Y1坐标。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_XMAGE_RIGHT = "HwMnoteXmageRight"

水印区域X2坐标

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_XMAGE_BOTTOM = "HwMnoteXmageBottom"

水印区域Y2坐标。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_CLOUD_ENHANCEMENT_MODE = "HwMnoteCloudEnhancementMode"

云增强模式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_WIND_SNAPSHOT_MODE = "HwMnoteWindSnapshotMode"

运动快拍模式。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_GIF_LOOP_COUNT = "GIFLoopCount"

GIF图片循环次数。

**起始版本：** 12

static const char * OHOS_IMAGE_PROPERTY_X_IN_ORIGINAL = "XInOriginal"

水印裁剪图左上角在原始图中的X坐标。

**起始版本：** 13

static const char * OHOS_IMAGE_PROPERTY_Y_IN_ORIGINAL = "YInOriginal"

水印裁剪图左上角在原始图中的Y坐标。

**起始版本：** 13

static const char * OHOS_IMAGE_PROPERTY_FRAGMENT_WIDTH = "FragmentImageWidth"

水印裁剪图的宽。

**起始版本：** 13

static const char * OHOS_IMAGE_PROPERTY_FRAGMENT_HEIGHT = "FragmentImageHeight"

水印裁剪图的高。

**起始版本：** 13

static const char * IMAGE_PROPERTY_GIF_DELAY_TIME = "GifDelayTime"

GIF图片的每帧播放时长（单位为毫秒）。

**起始版本：** 20

static const char * IMAGE_PROPERTY_GIF_DISPOSAL_TYPE = "GifDisposalType"

GIF图片每帧的帧过渡模式。

**起始版本：** 20

#### 枚举类型说明

#### Image_ErrorCode

```ets
enum Image_ErrorCode
```

**描述**

错误码。

**起始版本：** 12

枚举项描述IMAGE_SUCCESS = 0操作成功。IMAGE_BAD_PARAMETER = 401无效参数。IMAGE_UNSUPPORTED_MIME_TYPE = 7600101不支持的MIME类型。IMAGE_UNKNOWN_MIME_TYPE = 7600102未知的MIME类型。IMAGE_TOO_LARGE = 7600103过大的数据或图片。IMAGE_DMA_NOT_EXIST = 7600173内存不是DMA内存。IMAGE_DMA_OPERATION_FAILED = 7600174DMA内存操作失败。IMAGE_UNSUPPORTED_OPERATION = 7600201不支持的操作。IMAGE_UNSUPPORTED_METADATA = 7600202不支持的metadata。IMAGE_UNSUPPORTED_CONVERSION = 7600203不支持的转换。IMAGE_INVALID_REGION = 7600204无效区域。IMAGE_UNSUPPORTED_MEMORY_FORMAT = 7600205

不支持的内存格式。

**起始版本：** 13

IMAGE_INVALID_PARAMETER = 7600206

无效参数。

**起始版本：** 19

IMAGE_UNSUPPORTED_DATA_FORMAT = 7600207

不支持的数据格式。

**起始版本：** 22

IMAGE_ALLOC_FAILED = 7600301申请内存失败。IMAGE_COPY_FAILED = 7600302内存拷贝失败。IMAGE_LOCK_UNLOCK_FAILED = 7600303

内存加锁或解锁失败。

**起始版本：** 15

IMAGE_INIT_FAILED = 7600304

初始化失败。

**起始版本：** 22

IMAGE_CREATE_PIXELMAP_FAILED = 7600305

创建PixelMap失败。

**起始版本：** 22

IMAGE_ALLOCATOR_MODE_UNSUPPORTED = 7600501

不支持的内存分配器类型。例如，使用共享内存创建hdr图像。

 DMA内存支持hdr元数据。

**起始版本：** 20

IMAGE_UNKNOWN_ERROR = 7600901未知错误。IMAGE_BAD_SOURCE = 7700101解码数据源异常。IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE = 7700102

图片解码中不支持的MIME类型。

**起始版本：** 15

IMAGE_SOURCE_TOO_LARGE = 7700103

图像过大。

**起始版本：** 15

IMAGE_SOURCE_UNSUPPORTED_ALLOCATOR_TYPE = 7700201

不支持的分配器类型。例如，DMA支持HDR元数据，可以使用共享内存解码HDR图像。

**起始版本：** 15

IMAGE_SOURCE_UNSUPPORTED_OPTIONS = 7700203

不支持的选项。例如，无法将图像转换为所需的像素格式。

**起始版本：** 15

IMAGE_SOURCE_INVALID_PARAMETER = 7700204

ImageSource的无效参数。

**起始版本：** 19

IMAGE_DECODE_FAILED = 7700301解码失败。IMAGE_SOURCE_ALLOC_FAILED = 7700302

内存申请失败。

**起始版本：** 15

IMAGE_PACKER_INVALID_PARAMETER = 7800202

ImagePacker的无效参数。

**起始版本：** 19

IMAGE_ENCODE_FAILED = 7800301编码失败。IMAGE_RECEIVER_INVALID_PARAMETER = 7900201

ImageReceiver的无效参数。

**起始版本：** 20

#### Image_MetadataType

```ets
enum Image_MetadataType
```

**描述**

定义元数据类型。

**起始版本：** 13

枚举项描述EXIF_METADATA = 1EXIF元数据。FRAGMENT_METADATA = 2水印裁剪图元数据。GIF_METADATA = 5

GIF图片元数据。

**起始版本：** 20

#### IMAGE_ALLOCATOR_MODE

```ets
enum IMAGE_ALLOCATOR_MODE
```

**描述**

pixelmap内存分配类型。

**起始版本：** 20

枚举项描述IMAGE_ALLOCATOR_MODE_AUTO = 0系统决定创建pixelmap时分配内存的类型。IMAGE_ALLOCATOR_MODE_DMA = 1分配DMA类型的内存Buffer。IMAGE_ALLOCATOR_MODE_SHARED_MEMORY = 2使用共享内存创建pixelmap。

#### 函数说明

#### OH_PictureMetadata_Create()

```ets
Image_ErrorCode OH_PictureMetadata_Create(Image_MetadataType metadataType, OH_PictureMetadata **metadata)
```

**描述**

创建OH_PictureMetadata指针。

**起始版本：** 13

**参数：**

参数项描述[Image_MetadataType](#ZH-CN_TOPIC_0000002497445872__image_metadatatype) metadataType元数据的类型。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) **metadata被操作的OH_PictureMetadata指针。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureMetadata_GetProperty()

```ets
Image_ErrorCode OH_PictureMetadata_GetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

根据key获取Metadata的单条属性。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata被操作的OH_PictureMetadata指针。[Image_String](../../topics/graphics/Image_String.md) *key属性的键。[Image_String](../../topics/graphics/Image_String.md) *value属性的值。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。

#### OH_PictureMetadata_SetProperty()

```ets
Image_ErrorCode OH_PictureMetadata_SetProperty(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

根据key修改Metadata的单条属性。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata被操作的OH_PictureMetadata指针。[Image_String](../../topics/graphics/Image_String.md) *key属性的键。[Image_String](../../topics/graphics/Image_String.md) *value属性的值。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。

#### OH_PictureMetadata_GetPropertyWithNull()

```ets
Image_ErrorCode OH_PictureMetadata_GetPropertyWithNull(OH_PictureMetadata *metadata, Image_String *key, Image_String *value)
```

**描述**

获取图片元数据的属性值。输出的value.data以字符串结束符'\0'结尾。

**起始版本：** 19

**参数：**

参数项描述[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata将被操作的PictureMetadata指针。[Image_String](../../topics/graphics/Image_String.md) *key属性键指针。[Image_String](../../topics/graphics/Image_String.md) *value属性值指针。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_INVALID_PARAMETER：metadata、key或value为空。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型，或元数据类型与辅助图片类型不匹配。

#### OH_PictureMetadata_Release()

```ets
Image_ErrorCode OH_PictureMetadata_Release(OH_PictureMetadata *metadata)
```

**描述**

释放OH_PictureMetadata指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata被操作的OH_PictureMetadata指针。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureMetadata_Clone()

```ets
Image_ErrorCode OH_PictureMetadata_Clone(OH_PictureMetadata *oldMetadata, OH_PictureMetadata **newMetadata)
```

**描述**

拷贝元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *oldMetadata被操作的OH_PictureMetadata指针。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) **newMetadata拷贝得到的OH_PictureMetadata指针。

**返回：**

类型说明[Image_ErrorCode](#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_ALLOC_FAILED：内存分配失败。

 IMAGE_COPY_FAILED：内存拷贝失败。