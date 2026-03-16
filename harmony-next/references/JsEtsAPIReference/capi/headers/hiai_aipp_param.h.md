# hiai_aipp_param.h

#### 概述

模型推理时动态AIPP对象创建，参数设置和查询的接口。

**库：** libhiai_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：**[CANN](../../topics/misc/CANN.md)

#### 汇总

#### 类型定义

名称

描述

typedef struct [HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam)[HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam)

AIPP参数对象。

#### 枚举

名称

描述

[HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) {

HIAI_YUV420SP_U8 = 0,

HIAI_XRGB8888_U8 = 1,

HIAI_YUV400_U8 = 2,

HIAI_ARGB8888_U8 = 3,

HIAI_YUYV_U8 = 4,

HIAI_YUV422SP_U8 = 5,

HIAI_AYUV444_U8 = 6,

HIAI_RGB888_U8 = 7,

HIAI_BGR888_U8 = 8,

HIAI_YUV444SP_U8 = 9,

HIAI_YVU444SP_U8 = 10,

HIAI_IMAGE_FORMAT_INVALID = 255

}

CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。

[HiAI_ImageColorSpace](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imagecolorspace) {

HIAI_JPEG = 0,

HIAI_BT_601_NARROW = 1,

HIAI_BT_601_FULL = 2,

HIAI_BT_709_NARROW = 3,

HIAI_IMAGE_COLOR_SPACE_INVALID = 4

}

图像色域空间类型。

#### 函数

名称

描述

[HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) * [HMS_HiAIAippParam_Create](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_create) (uint32_t batchNum)

根据batchNum创建动态AippParam对象。

void * [HMS_HiAIAippParam_GetData](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getdata) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

获取AippParam申请的内存地址。

uint32_t [HMS_HiAIAippParam_GetDataSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getdatasize) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

获取AippParam申请的内存大小。

int [HMS_HiAIAippParam_GetInputIndex](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getinputindex) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

查询AippParam对象所在输入的索引。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetInputIndex](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setinputindex) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t inputIndex)

设置AippParam在输入上的索引。

int [HMS_HiAIAippParam_GetInputAippIndex](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getinputaippindex) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

查询AippParam对象在该输入的多个输出分支上的索引。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetInputAippIndex](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setinputaippindex) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t inputAippIndex)

设置AippParam对象作用于该输入的多个输出分支上的索引。

void [HMS_HiAIAippParam_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_destroy) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) **aippParam)

释放AippParam对象。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetInputFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setinputformat) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, [HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) inputFormat)

设置AippParam对象的输入图像格式。

[HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat)[HMS_HiAIAippParam_GetInputFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getinputformat) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

查询AippParam对象的输入图像格式。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetInputShape](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setinputshape) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t srcImageW, uint32_t srcImageH)

设置AippParam对象的输入图像宽高。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetInputShape](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getinputshape) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t *srcImageW, uint32_t *srcImageH)

查询AippParam对象的输入图像宽高。

uint32_t [HMS_HiAIAippParam_GetBatchCount](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getbatchcount) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

查询AippParam对象的图像数量。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetCscConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setcscconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, [HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) inputFormat, [HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) outputFormat, [HiAI_ImageColorSpace](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imagecolorspace) space)

设置AippParam对象的CSC色域转换参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetCscConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getcscconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, [HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) *inputFormat, [HiAI_ImageFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imageformat) *outputFormat, [HiAI_ImageColorSpace](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_imagecolorspace) *space)

查询AippParam对象的CSC色域转换相关参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetChannelSwapConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setchannelswapconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)

设置AippParam对象的ChannelSwap通道交换参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetChannelSwapConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getchannelswapconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, bool *rbuvSwapSwitch, bool *axSwapSwitch)

查询AippParam对象的ChannelSwap通道交换参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetSingleBatchMultiCrop](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setsinglebatchmulticrop) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, bool singleBatchMultiCrop)

设置AippParam对象的SingleBatchMultiCrop标识。

bool [HMS_HiAIAippParam_GetSingleBatchMultiCrop](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getsinglebatchmulticrop) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam)

查询AippParam对象的SingleBatchMultiCrop标识。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetCropConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setcropconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH)

设置AippParam对象的裁剪参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetCropConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getcropconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t *startPosW, uint32_t *startPosH, uint32_t *croppedW, uint32_t *croppedH)

查询AippParam对象的裁剪参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetResizeConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setresizeconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH)

设置AippParam对象的图像缩放参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetResizeConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getresizeconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t *resizedW, uint32_t *resizedH)

查询AippParam对象的图像缩放参数。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetPadConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setpadconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize)

设置AippParam对象的输入图像的填充像素数。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetPadConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getpadconfig) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t *leftPadSize, uint32_t *rightPadSize, uint32_t *topPadSize, uint32_t *bottomPadSize)

查询AippParam对象的输入图像的填充像素数。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetChannelPadding](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setchannelpadding) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)

设置AippParam对象的通道padding填充值。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetChannelPadding](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getchannelpadding) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)

查询AippParam对象的通道padding填充值。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetRotationAngle](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setrotationangle) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float rotationAngle)

设置AippParam对象的旋转角度。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetRotationAngle](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getrotationangle) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float *rotationAngle)

查询AippParam对象的图像旋转角度。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetDtcMeanPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setdtcmeanpixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)

设置AippParam对象的数据类型转换通道像素平均值。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetDtcMeanPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getdtcmeanpixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)

查询AippParam对象的数据类型转换通道像素平均值。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetDtcMinPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setdtcminpixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)

设置AippParam对象的数据类型转换通道像素最小值。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetDtcMinPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getdtcminpixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)

查询AippParam对象的数据类型转换通道像素最小值。

OH_NN_ReturnCode [HMS_HiAIAippParam_SetDtcVarReciPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_setdtcvarrecipixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)

设置AippParam对象的数据类型转换通道像素方差。

OH_NN_ReturnCode [HMS_HiAIAippParam_GetDtcVarReciPixel](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaiaippparam_getdtcvarrecipixel) ([HiAI_AippParam](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_aippparam) *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)

查询AippParam对象的数据类型转换通道像素方差。