# hiai_aipp_param.h

**概述**

模型推理时动态AIPP对象创建，参数设置和查询的接口。

引用文件： <CANNKit/hiai_aipp_param.h>

库： libhiai_foundation.so

系统能力： SystemCapability.AI.HiAIFoundation

起始版本： 4.1.0(11)

相关模块： [CANN](CANN.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct HiAI_AippParam HiAI_AippParam | AIPP参数对象。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| HiAI_ImageFormat { HIAI_YUV420SP_U8 = 0, HIAI_XRGB8888_U8 = 1, HIAI_YUV400_U8 = 2, HIAI_ARGB8888_U8 = 3, HIAI_YUYV_U8 = 4, HIAI_YUV422SP_U8 = 5, HIAI_AYUV444_U8 = 6, HIAI_RGB888_U8 = 7, HIAI_BGR888_U8 = 8, HIAI_YUV444SP_U8 = 9, HIAI_YVU444SP_U8 = 10, HIAI_IMAGE_FORMAT_INVALID = 255 } | CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。 |
| HiAI_ImageColorSpace { HIAI_JPEG = 0, HIAI_BT_601_NARROW = 1, HIAI_BT_601_FULL = 2, HIAI_BT_709_NARROW = 3, HIAI_IMAGE_COLOR_SPACE_INVALID = 4 } | 图像色域空间类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| HiAI_AippParam * HMS_HiAIAippParam_Create (uint32_t batchNum) | 根据batchNum创建动态AippParam对象。 |
| void * HMS_HiAIAippParam_GetData (HiAI_AippParam *aippParam) | 获取AippParam申请的内存地址。 |
| uint32_t HMS_HiAIAippParam_GetDataSize (HiAI_AippParam *aippParam) | 获取AippParam申请的内存大小。 |
| int HMS_HiAIAippParam_GetInputIndex (HiAI_AippParam *aippParam) | 查询AippParam对象所在输入的索引。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputIndex (HiAI_AippParam *aippParam, uint32_t inputIndex) | 设置AippParam在输入上的索引。 |
| int HMS_HiAIAippParam_GetInputAippIndex (HiAI_AippParam *aippParam) | 查询AippParam对象在该输入的多个输出分支上的索引。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputAippIndex (HiAI_AippParam *aippParam, uint32_t inputAippIndex) | 设置AippParam对象作用于该输入的多个输出分支上的索引。 |
| void HMS_HiAIAippParam_Destroy (HiAI_AippParam **aippParam) | 释放AippParam对象。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat (HiAI_AippParam *aippParam, HiAI_ImageFormat inputFormat) | 设置AippParam对象的输入图像格式。 |
| HiAI_ImageFormat HMS_HiAIAippParam_GetInputFormat (HiAI_AippParam *aippParam) | 查询AippParam对象的输入图像格式。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape (HiAI_AippParam *aippParam, uint32_t srcImageW, uint32_t srcImageH) | 设置AippParam对象的输入图像宽高。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetInputShape (HiAI_AippParam *aippParam, uint32_t *srcImageW, uint32_t *srcImageH) | 查询AippParam对象的输入图像宽高。 |
| uint32_t HMS_HiAIAippParam_GetBatchCount (HiAI_AippParam *aippParam) | 查询AippParam对象的图像数量。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig (HiAI_AippParam *aippParam, HiAI_ImageFormat inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space) | 设置AippParam对象的CSC色域转换参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetCscConfig (HiAI_AippParam *aippParam, HiAI_ImageFormat *inputFormat, HiAI_ImageFormat *outputFormat, HiAI_ImageColorSpace *space) | 查询AippParam对象的CSC色域转换相关参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelSwapConfig (HiAI_AippParam *aippParam, bool rbuvSwapSwitch, bool axSwapSwitch) | 设置AippParam对象的ChannelSwap通道交换参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelSwapConfig (HiAI_AippParam *aippParam, bool *rbuvSwapSwitch, bool *axSwapSwitch) | 查询AippParam对象的ChannelSwap通道交换参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetSingleBatchMultiCrop (HiAI_AippParam *aippParam, bool singleBatchMultiCrop) | 设置AippParam对象的SingleBatchMultiCrop标识。 |
| bool HMS_HiAIAippParam_GetSingleBatchMultiCrop (HiAI_AippParam *aippParam) | 查询AippParam对象的SingleBatchMultiCrop标识。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetCropConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH) | 设置AippParam对象的裁剪参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetCropConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t *startPosW, uint32_t *startPosH, uint32_t *croppedW, uint32_t *croppedH) | 查询AippParam对象的裁剪参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetResizeConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH) | 设置AippParam对象的图像缩放参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetResizeConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t *resizedW, uint32_t *resizedH) | 查询AippParam对象的图像缩放参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetPadConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize) | 设置AippParam对象的输入图像的填充像素数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetPadConfig (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t *leftPadSize, uint32_t *rightPadSize, uint32_t *topPadSize, uint32_t *bottomPadSize) | 查询AippParam对象的输入图像的填充像素数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount) | 设置AippParam对象的通道padding填充值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelPadding (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount) | 查询AippParam对象的通道padding填充值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle (HiAI_AippParam *aippParam, uint32_t batchIndex, float rotationAngle) | 设置AippParam对象的旋转角度。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetRotationAngle (HiAI_AippParam *aippParam, uint32_t batchIndex, float *rotationAngle) | 查询AippParam对象的图像旋转角度。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素平均值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMeanPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素平均值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素最小值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMinPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素最小值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素方差。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcVarReciPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素方差。 |