# CANN

#### 概述

提供CANN Kit模型推理的相关接口。

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)


CANN Kit的模型编译、加载、推理等基础功能接口已抽取放在[neural_network_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h)中，此处重点描述高阶功能。

#### 汇总

#### 文件

| 名称 | 描述 |
| --- | --- |
| [hiai_aipp_param.h](hiai_aipp_param.h.md) | 模型推理时动态AIPP对象创建，参数设置和查询的接口。 |
| [hiai_helper.h](hiai_helper.h.md) | 查询CANN Kit版本以及检查模型支持情况的接口。 |
| [hiai_options.h](hiai_options.h.md) | 选项参数的接口。 |
| [hiai_single_op.h](hiai_single_op.h.md) | 定义CANN Kit单算子接口，用于单算子的创建、计算以及Tensor和Buffer的管理。 |
| [hiai_tensor.h](hiai_tensor.h.md) | 模型推理时使用的输入输出内存相关的辅助接口。 |

#### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [HiAISingleOpDescriptor_ConvolutionParam](HiAISingleOpDescriptor_ConvolutionParam.md) | HMS_HiAISingleOpDescriptor_CreateConvolution输入参数。 |
| struct [HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md) | HMS_HiAISingleOpExecutor_CreateConvolution输入参数。 |
| struct [HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) | HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation输入参数。 |

#### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct HiAI_AippParam HiAI_AippParam | AIPP参数对象。 |
| typedef struct [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) HiAI_SingleOpTensorDesc | 单算子Tensor描述的句柄。 |
| typedef struct HiAI_SingleOpBuffer HiAI_SingleOpBuffer | 单算子Buffer句柄。 |
| typedef struct HiAI_SingleOpTensor HiAI_SingleOpTensor | 单算子Tensor句柄。 |
| typedef struct HiAI_SingleOpOptions HiAI_SingleOpOptions | 单算子选项句柄。 |
| typedef struct HiAI_SingleOpDescriptor HiAI_SingleOpDescriptor | 单算子的算子描述句柄。 |
| typedef struct [HiAISingleOpDescriptor_ConvolutionParam](HiAISingleOpDescriptor_ConvolutionParam.md) | HMS_HiAISingleOpDescriptor_CreateConvolution输入参数。 |
| typedef struct [HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md) | HMS_HiAISingleOpExecutor_CreateConvolution输入参数。 |
| typedef struct [HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) | HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation输入参数。 |
| typedef struct HiAI_SingleOpExecutor HiAI_SingleOpExecutor | 单算子执行器句柄。 |

#### 枚举

| 名称 | 描述 |
| --- | --- |
| HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format { HIAI_YUV420SP_U8 = 0, HIAI_XRGB8888_U8 = 1, HIAI_YUV400_U8 = 2, HIAI_ARGB8888_U8 = 3, HIAI_YUYV_U8 = 4, HIAI_YUV422SP_U8 = 5, HIAI_AYUV444_U8 = 6, HIAI_RGB888_U8 = 7, HIAI_BGR888_U8 = 8, HIAI_YUV444SP_U8 = 9, HIAI_YVU444SP_U8 = 10, HIAI_IMAGE_FORMAT_INVALID = 255 } | CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。 |
| HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)ColorSpace { HIAI_JPEG = 0, HIAI_BT_601_NARROW = 1, HIAI_BT_601_FULL = 2, HIAI_BT_709_NARROW = 3, HIAI_IMAGE_COLOR_SPACE_INVALID = 4 } | 图像色域空间类型。 |
| HiAI_Compatibility { HIAI_COMPATIBILITY_COMPATIBLE = 0, HIAI_COMPATIBILITY_INCOMPATIBLE = 1 } | 编译后模型兼容性结果。 |
| HiAI_FormatMode { HIAI_FORMAT_MODE_NCHW = 0, HIAI_FORMAT_MODE_ORIGIN = 1 } | 模型编译时数据的排列格式。 |
| HiAI_DynamicShapeStatus { HIAI_DYNAMIC_SHAPE_DISABLED = 0, HIAI_DYNAMIC_SHAPE_ENABLED = 1 } | 是否使能编译前可变shape。 |
| HiAI_DynamicShapeCacheMode { HIAI_DYNAMIC_SHAPE_CACHE_BUILT_MODEL = 0, HIAI_DYNAMIC_SHAPE_CACHE_LOADED_MODEL = 1 } | 编译前可变shape支持的模式。 |
| HiAI_ExecuteDevice { HIAI_EXECUTE_DEVICE_NPU = 0, HIAI_EXECUTE_DEVICE_CPU = 1, HIAI_EXECUTE_DEVICE_GPU = 2 } | 模型运行时支持的设备类型。 |
| HiAI_FallbackMode { HIAI_FALLBACK_ENABLED = 0, HIAI_FALLBACK_DISABLED = 1 } | 指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。 |
| HiAI_DeviceMemoryReusePlan { HIAI_DEVICE_MEMORY_REUSE_PLAN_UNSET = 0, HIAI_DEVICE_MEMORY_REUSE_PLAN_LOW = 1, HIAI_DEVICE_MEMORY_REUSE_PLAN_HIGH = 2 } | 设备内存复用配置选项。 |
| HiAI_TuningStrategy { HIAI_TUNING_STRATEGY_OFF = 0, HIAI_TUNING_STRATEGY_ON_DEVICE_TUNING = 1, HIAI_TUNING_STRATEGY_ON_DEVICE_PREPROCESS_TUNING = 2, HIAI_TUNING_STRATEGY_ON_CLOUD_TUNING = 3 } | 模型优化策略配置选项。 |
| HiAI_TuningMode { HIAI_TUNING_MODE_UNSET = 0, HIAI_TUNING_MODE_AUTO = 1, HIAI_TUNING_MODE_HETER = 2 } | 辅助调优模式。 |
| HiAI_BandMode { HIAI_BANDMODE_UNSET = 0, HIAI_BANDMODE_LOW = 1, HIAI_BANDMODE_NORMAL = 2, HIAI_BANDMODE_HIGH = 3 } | 定义硬件之间带宽模式。 |
| HiAI_OmType { HIAI_OM_TYPE_OFF = 0, HIAI_OM_TYPE_PROFILING = 1, HIAI_OM_TYPE_DUMP = 2 } | 维测类型定义。 |
| HiAI_SingleOpDataType { HIAI_SINGLEOP_DT_FLOAT = 0, HIAI_SINGLEOP_DT_FLOAT16 = 1, HIAI_SINGLEOP_DT_UNDEFINED = 17 } | 单算子张量数据类型枚举。 |
| HiAI_SingleOpFormat { HIAI_SINGLEOP_FORMAT_NCHW = 0, HIAI_SINGLEOP_FORMAT_NHWC = 1, HIAI_SINGLEOP_FORMAT_ND = 2, HIAI_SINGLEOP_FORMAT_NC1HWC0 = 3, HIAI_SINGLEOP_FORMAT_NC4HW4 = 28, HIAI_SINGLEOP_FORMAT_NC8HW8 = 31, HIAI_SINGLEOP_FORMAT_RESERVED = 255 } | 单算子张量排布格式枚举。 |
| HiAI_SingleOpConvMode { HIAI_SINGLEOP_CONV_MODE_COMMON = 0, HIAI_SINGLEOP_CONV_MODE_TRANSPOSED = 1, HIAI_SINGLEOP_CONV_MODE_DEPTHWISE = 2 } | 单算子卷积模式枚举。 |
| HiAI_SingleOpPadMode { HIAI_SINGLEOP_PAD_MODE_SPECIFIC = 0, HIAI_SINGLEOP_PAD_MODE_SAME = 1, HIAI_SINGLEOP_PAD_MODE_SAME_UPPER = 2, HIAI_SINGLEOP_PAD_MODE_SAME_LOWER = 3, HIAI_SINGLEOP_PAD_MODE_VALID = 4 } | 单算子填充模式枚举。 |
| HiAI_SingleOpActivationType { HIAI_SINGLEOP_ACTIVATION_TYPE_RELU = 0, HIAI_SINGLEOP_ACTIVATION_TYPE_RELU6 = 1 } | 单算子激活模式枚举。 |
| HiAI_SingleOpSupportStatus { HIAI_SINGLEOP_OPTIMIZED = 0, HIAI_SINGLEOP_COMMON = 1, HIAI_SINGLEOP_UNSUPPORTED = 2 } | 单算子支持状态枚举。 |

#### 函数

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
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat (HiAI_AippParam *aippParam, HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format inputFormat) | 设置AippParam对象的输入图像格式。 |
| HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format HMS_HiAIAippParam_GetInputFormat (HiAI_AippParam *aippParam) | 查询AippParam对象的输入图像格式。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape (HiAI_AippParam *aippParam, uint32_t src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)W, uint32_t srcImageH) | 设置AippParam对象的输入图像宽高。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetInputShape (HiAI_AippParam *aippParam, uint32_t *src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)W, uint32_t *srcImageH) | 查询AippParam对象的输入图像宽高。 |
| uint32_t HMS_HiAIAippParam_GetBatchCount (HiAI_AippParam *aippParam) | 查询AippParam对象的图像数量。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig (HiAI_AippParam *aippParam, HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space) | 设置AippParam对象的CSC色域转换参数。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetCscConfig (HiAI_AippParam *aippParam, HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format *inputFormat, HiAI_ImageFormat *outputFormat, HiAI_ImageColorSpace *space) | 查询AippParam对象的CSC色域转换相关参数。 |
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
| OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t [padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)Values[], uint32_t channelCount) | 设置AippParam对象的通道padding填充值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelPadding (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t [padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)Values[], uint32_t channelCount) | 查询AippParam对象的通道padding填充值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle (HiAI_AippParam *aippParam, uint32_t batchIndex, float rotationAngle) | 设置AippParam对象的旋转角度。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetRotationAngle (HiAI_AippParam *aippParam, uint32_t batchIndex, float *rotationAngle) | 查询AippParam对象的图像旋转角度。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素平均值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMeanPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素平均值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素最小值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMinPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素最小值。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount) | 设置AippParam对象的数据类型转换通道像素方差。 |
| OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcVarReciPixel (HiAI_AippParam *aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount) | 查询AippParam对象的数据类型转换通道像素方差。 |
| const char * HMS_HiAI_GetVersion (void) | 获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。 |
| HiAI_Compatibility HMS_HiAICompatibility_CheckFromFile (const char *file) | 查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| HiAI_Compatibility HMS_HiAICompatibility_CheckFromBuffer (const void *data, size_t size) | 查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetInputTensorShapes (OH_NNCompilation *compilation, NN_TensorDesc *inputTensorDescs[], size_t shapeCount) | 编译时更新模型输入shape。 |
| size_t HMS_HiAIOptions_GetInputTensorShapeSize (const OH_NNCompilation *compilation) | 查询选项参数中shape描述的个数。 |
| NN_TensorDesc * HMS_HiAIOptions_GetInputTensorShape (const OH_NNCompilation *compilation, size_t index) | 查询选项参数中指定索引的shape描述。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetFormatMode (OH_NNCompilation *compilation, HiAI_FormatMode formatMode) | 设置模型编译时的数据排列格式。 |
| HiAI_FormatMode HMS_HiAIOptions_GetFormatMode (const OH_NNCompilation *compilation) | 查询模型编译参数中的数据排列格式。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeStatus (OH_NNCompilation *compilation, HiAI_DynamicShapeStatus status) | 设置编译前可变shape配置中的EnableMode参数。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeMaxCache (OH_NNCompilation *compilation, size_t maxCacheCount) | 设置编译前可变shape配置中的最大缓存编译后模型数量。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeCacheMode (OH_NNCompilation *compilation, HiAI_DynamicShapeCacheMode mode) | 设置编译前可变shape配置中的缓存模式参数。 |
| HiAI_DynamicShapeStatus HMS_HiAIOptions_GetDynamicShapeStatus (const OH_NNCompilation *compilation) | 查询编译前可变shape配置中的状态参数。 |
| size_t HMS_HiAIOptions_GetDynamicShapeMaxCache (const OH_NNCompilation *compilation) | 查询编译前可变shape配置中的最大缓存数量。 |
| HiAI_DynamicShapeCacheMode HMS_HiAIOptions_GetDynamicShapeCacheMode (const OH_NNCompilation *compilation) | 查询编译前可变shape配置中的cacheMode参数。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetOperatorDeviceOrder (OH_NNCompilation *compilation, const char *operatorName, HiAI_ExecuteDevice *executeDevices, size_t deviceCount) | 设置算子级调优配置中算子执行设备列表。 |
| size_t HMS_HiAIOptions_GetOperatorDeviceCount (const OH_NNCompilation *compilation, const char *operatorName) | 查询算子级调优配置中指定算子的执行设备个数。 |
| HiAI_ExecuteDevice * HMS_HiAIOptions_GetOperatorDeviceOrder (const OH_NNCompilation *compilation, const char *operatorName) | 查询算子级调优配置中指定算子的执行设备列表。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetModelDeviceOrder (OH_NNCompilation *compilation, HiAI_ExecuteDevice *executeDevices, size_t deviceCount) | 设置模型级调优配置中模型执行设备列表。 |
| size_t HMS_HiAIOptions_GetModelDeviceCount (const OH_NNCompilation *compilation) | 查询模型级调优配置中模型的执行设备个数。 |
| HiAI_ExecuteDevice * HMS_HiAIOptions_GetModelDeviceOrder (const OH_NNCompilation *compilation) | 查询模型级调优配置中模型的执行设备列表。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetFallbackMode (OH_NNCompilation *compilation, HiAI_FallbackMode fallbackMode) | 设置调优配置中的回滚模式。 |
| HiAI_FallbackMode HMS_HiAIOptions_GetFallbackMode (const OH_NNCompilation *compilation) | 查询调优配置中的回滚模式。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetDeviceMemoryReusePlan (OH_NNCompilation *compilation, HiAI_DeviceMemoryReusePlan deviceMemoryReusePlan) | 设置调优配置中的设备内存复用参数。 |
| HiAI_DeviceMemoryReusePlan HMS_HiAIOptions_GetDeviceMemoryReusePlan (const OH_NNCompilation *compilation) | 查询调优配置中的设备内存复用参数。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetTuningStrategy (OH_NNCompilation *compilation, HiAI_TuningStrategy tuningStrategy) | 设置模型编译时的模型优化策略。 |
| HiAI_TuningStrategy HMS_HiAIOptions_GetTuningStrategy (const OH_NNCompilation *compilation) | 查询模型优化策略。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetQuantConfig (OH_NNCompilation *compilation, void *data, size_t size) | 设置模型编译时量化配置。 |
| void * HMS_HiAIOptions_GetQuantConfigData (const OH_NNCompilation *compilation) | 查询量化配置的数据地址。 |
| size_t HMS_HiAIOptions_GetQuantConfigSize (const OH_NNCompilation *compilation) | 查询量化配置的数据大小。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetTuningMode (OH_NNCompilation *compilation, HiAI_TuningMode tuningMode) | 选择辅助调优模式。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetTuningCacheDir (OH_NNCompilation *compilation, const char *cacheDir) | 设置辅助调优的缓存目录。 |
| HiAI_TuningMode HMS_HiAIOptions_GetTuningMode (const OH_NNCompilation *compilation) | 查询辅助调优模式。 |
| const char * HMS_HiAIOptions_GetTuningCacheDir (const OH_NNCompilation *compilation) | 查询辅助调优的缓存目录。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetBandMode (OH_NNCompilation *compilation, HiAI_BandMode bandMode) | 设置NPU与周边硬件IO资源的带宽模式。 |
| HiAI_BandMode HMS_HiAIOptions_GetBandMode (const OH_NNCompilation *compilation) | 查询带宽模式。 |
| OH_NN_ReturnCode HMS_HiAIOptions_SetOmOptions (OH_NNCompilation *compilation, HiAI_OmType type, const char *outputDir) | 设置模型加载时的维测选项信息。 |
| [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * HMS_HiAISingleOpTensorDesc_Create (const int64_t *dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual) | 创建HiAI_SingleOpTensorDesc对象。 |
| size_t HMS_HiAISingleOpTensorDesc_GetDimensionCount (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc) | 查询HiAI_SingleOpTensorDesc的维度数量。 |
| int64_t HMS_HiAISingleOpTensorDesc_GetDimension (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc, size_t index) | 查询HiAI_SingleOpTensorDesc指定索引的维度长度。 |
| HiAI_SingleOpDataType HMS_HiAISingleOpTensorDesc_GetDataType (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc) | 查询HiAI_SingleOpTensorDesc的数据类型。 |
| HiAI_SingleOpFormat HMS_HiAISingleOpTensorDesc_GetFormat (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc) | 查询HiAI_SingleOpTensorDesc的排布格式。 |
| bool HMS_HiAISingleOpTensorDesc_IsVirtual (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc) | 查询HiAI_SingleOpTensorDesc是否为虚拟张量。 |
| size_t HMS_HiAISingleOpTensorDesc_GetByteSize (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc) | 查询基于HiAI_SingleOpTensorDesc的维度和数据类型计算的数据占用字节数。 |
| void HMS_HiAISingleOpTensorDesc_Destroy ([HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) **tensorDesc) | 释放HiAI_SingleOpTensorDesc对象。 |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpBuffer_Create (size_t dataSize) | 按照指定的内存大小创建HiAI_SingleOpBuffer对象。 |
| size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer *buffer) | 查询HiAI_SingleOpBuffer的字节大小。 |
| void * HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer *buffer) | 查询HiAI_SingleOpBuffer的内存地址。 |
| OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer **buffer) | 释放HiAI_SingleOpBuffer对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromTensorDesc (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc) | 根据HiAI_SingleOpTensorDesc创建HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc, void *data, size_t dataSize) | 根据HiAI_SingleOpTensorDesc、HiAI_SingleOpBuffer的内存地址和数据大小创建HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromConst (const [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc, void *data, size_t dataSize) | 根据HiAI_SingleOpTensorDesc、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建HiAI_SingleOpTensor对象。 |
| [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor *tensor) | 获取HiAI_SingleOpTensor的Tensor描述。 |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor *tensor) | 获取HiAI_SingleOpTensor的Buffer。 |
| OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor **tensor) | 释放HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpOptions * HMS_HiAISingleOpOptions_Create (void) | 创建HiAI_SingleOpOptions对象。 |
| void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions **options) | 释放HiAI_SingleOpOptions对象。 |
| HiAI_SingleOpDescriptor * HMS_HiAISingleOpDescriptor_CreateConvolution ([HiAISingleOpDescriptor_ConvolutionParam](HiAISingleOpDescriptor_ConvolutionParam.md) param) | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。 |
| HiAI_SingleOpDescriptor * HMS_HiAISingleOpDescriptor_CreateActivation (HiAI_SingleOpActivationType activationType, float coef) | 创建激活函数类的描述符对象。 |
| void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor **opDesc) | 释放HiAI_SingleOpDescriptor对象。 |
| HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckConvolution ([HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md) param) | 预查询卷积算子的支持状态。 |
| HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation ([HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) param) | 预查询卷积和激活融合算子的支持状态。 |
| HiAI_SingleOpExecutor * HMS_HiAISingleOpExecutor_CreateConvolution ([HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md) param) | 创建卷积类算子对应的HiAI_SingleOpExecutor对象。 |
| HiAI_SingleOpExecutor * HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation ([HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) param) | 创建卷积和激活融合算子对应的HiAI_SingleOpExecutor对象。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc (const HiAI_SingleOpExecutor *executor, uint32_t index, [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *output) | 更新HiAI_SingleOpExecutor的输出tensor描述。 |
| size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor *executor) | 查询HiAI_SingleOpExecutor所需的ION内存工作空间的字节大小。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor *executor, void *workspace, size_t workspaceSize) | 加载HiAI_SingleOpExecutor。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor *executor, HiAI_SingleOpTensor *input[], int32_t inputNum, HiAI_SingleOpTensor *output[], int32_t outputNum) | 执行同步运算推理。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor **executor) | 销毁HiAI_SingleOpExecutor对象，释放执行器占用的内存。 |
| size_t HMS_HiAITensor_GetSizeWith[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format (NN_TensorDesc *desc, HiAI_ImageFormat format) | 根据NN_TensorDesc和HiAI_ImageFormat计算申请tensor的大小。 |
| OH_NN_ReturnCode HMS_HiAITensor_SetAippParams (NN_Tensor *tensor, HiAI_AippParam *aippParams[], size_t aippNum) | 给NN_Tensor设置AippParams。 |

#### 类型定义说明

#### HiAI_AippParam

```ets
typedef struct HiAI_AippParam HiAI_AippParam
```

**描述**

AIPP参数对象。

**起始版本：** 4.1.0(11)

#### HiAI_SingleOpBuffer

```ets
typedef struct HiAI_SingleOpBuffer HiAI_SingleOpBuffer
```

**描述**

单算子Buffer句柄。

**起始版本：** 5.0.0(12)

#### HiAI_SingleOpDescriptor

```ets
typedef struct HiAI_SingleOpDescriptor HiAI_SingleOpDescriptor
```

**描述**

单算子的算子描述句柄。

**起始版本：** 5.0.0(12)

#### [HiAISingleOpDescriptor_ConvolutionParam](HiAISingleOpDescriptor_ConvolutionParam.md)

```ets
typedef struct HiAISingleOpDescriptor_ConvolutionParam
```

**描述**

[HMS_HiAISingleOpDescriptor_CreateConvolution](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopdescriptor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

#### HiAI_SingleOpExecutor

```ets
typedef struct HiAI_SingleOpExecutor HiAI_SingleOpExecutor
```

**描述**

单算子执行器句柄。

**起始版本：** 5.0.0(12)

#### [HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md)

```ets
typedef struct HiAI_SingleOpExecutorConvolutionParam
```

**描述**

[HMS_HiAISingleOpExecutor_CreateConvolution](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

#### [HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md)

```ets
typedef struct HiAI_SingleOpExecutorFusedConvolutionActivationParam
```

**描述**

[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

**起始版本：** 5.0.0(12)

#### HiAI_SingleOpOptions

```ets
typedef struct HiAI_SingleOpOptions HiAI_SingleOpOptions
```

**描述**

单算子选项句柄。

**起始版本：** 5.0.0(12)

#### HiAI_SingleOpTensor

```ets
typedef struct HiAI_SingleOpTensor HiAI_SingleOpTensor
```

**描述**

单算子Tensor句柄。

**起始版本：** 5.0.0(12)

#### [HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)

```ets
typedef struct HiAI_SingleOpTensorDesc HiAI_SingleOpTensorDesc
```

**描述**

单算子Tensor描述的句柄。

**起始版本：** 5.0.0(12)

#### 枚举类型说明

#### HiAI_BandMode

```ets
enum HiAI_BandMode
```

**描述**

定义硬件之间带宽模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_BANDMODE_UNSET | 不设置，由系统调节。 |
| HIAI_BANDMODE_LOW | 低级带宽模式。 |
| HIAI_BANDMODE_NORMAL | 中级带宽模式。 |
| HIAI_BANDMODE_HIGH | 高级带宽模式。 |

#### HiAI_Compatibility

```ets
enum HiAI_Compatibility
```

**描述**

编译后模型兼容性结果。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_COMPATIBILITY_COMPATIBLE | 模型兼容。 |
| HIAI_COMPATIBILITY_INCOMPATIBLE | 模型不兼容。 |

#### HiAI_DeviceMemoryReusePlan

```ets
enum HiAI_DeviceMemoryReusePlan
```

**描述**

设备内存复用配置选项。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_DEVICE_MEMORY_REUSE_PLAN_UNSET | 不使用，默认值。 |
| HIAI_DEVICE_MEMORY_REUSE_PLAN_LOW | 低内存复用率，模型申请的内存较多但模型推理性能相对较优。 |
| HIAI_DEVICE_MEMORY_REUSE_PLAN_HIGH | 高内存复用率，模型申请的内存较少但模型推理性能相对较差。 |

#### HiAI_DynamicShapeCacheMode

```ets
enum HiAI_DynamicShapeCacheMode
```

**描述**

编译前可变shape支持的模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_DYNAMIC_SHAPE_CACHE_BUILT_MODEL | 缓存编译后的模型，内存占用较小，默认值。 |
| HIAI_DYNAMIC_SHAPE_CACHE_LOADED_MODEL | 缓存加载后的模型，性能较优。 |

#### HiAI_DynamicShapeStatus

```ets
enum HiAI_DynamicShapeStatus
```

**描述**

是否使能编译前可变shape。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_DYNAMIC_SHAPE_DISABLED | 不使能编译前可变shape，默认值。 |
| HIAI_DYNAMIC_SHAPE_ENABLED | 使能编译前可变shape。 |

#### HiAI_ExecuteDevice

```ets
enum HiAI_ExecuteDevice
```

**描述**

模型运行时支持的设备类型。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_EXECUTE_DEVICE_NPU | NPU，默认值。 |
| HIAI_EXECUTE_DEVICE_CPU | CPU。 |
| HIAI_EXECUTE_DEVICE_GPU | GPU。 |

#### HiAI_FallbackMode

```ets
enum HiAI_FallbackMode
```

**描述**

指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_FALLBACK_ENABLED | 允许，默认值。 |
| HIAI_FALLBACK_DISABLED | 不允许。 |

#### HiAI_FormatMode

```ets
enum HiAI_FormatMode
```

**描述**

模型编译时数据的排列格式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_FORMAT_MODE_NCHW | 格式为NCHW，默认值。 |
| HIAI_FORMAT_MODE_ORIGIN | 格式为原始模型格式。 |

#### HiAI_ImageColorSpace

```ets
enum HiAI_ImageColorSpace
```

**描述**

图像色域空间类型。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_JPEG | JPEG色域空间类型。 |
| HIAI_BT_601_NARROW | BT.601 video range色域空间类型。 |
| HIAI_BT_601_FULL | BT.601 full range色域空间类型。 |
| HIAI_BT_709_NARROW | BT.709 video range色域空间类型。 |
| HIAI_IMAGE_COLOR_SPACE_INVALID | 无效图像色域类型。 |

#### HiAI_ImageFormat

```ets
enum HiAI_ImageFormat
```

**描述**

CANN Kit推理支持的输入和输出Tensor的图片格式的枚举。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_YUV420SP_U8 | YUV420SP_U8格式的图片。 |
| HIAI_XRGB8888_U8 | XRGB8888_U8格式的图片。 |
| HIAI_YUV400_U8 | YUV400_U8格式的图片。 |
| HIAI_ARGB8888_U8 | ARGB8888_U8格式的图片。 |
| HIAI_YUYV_U8 | YUYV_U8格式的图片。 |
| HIAI_YUV422SP_U8 | YUV422SP_U8格式的图片。 |
| HIAI_AYUV444_U8 | AYUV444_U8格式的图片。 |
| HIAI_RGB888_U8 | RGB888_U8格式的图片。 |
| HIAI_BGR888_U8 | BGR888_U8格式的图片。 |
| HIAI_YUV444SP_U8 | YUV444SP格式的图片。 |
| HIAI_YVU444SP_U8 | YVU444SP格式的图片。 |
| HIAI_IMAGE_FORMAT_INVALID | 不支持的图片格式。 |

#### HiAI_OmType

```ets
enum HiAI_OmType
```

**描述**

维测类型定义。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_OM_TYPE_OFF | 关闭维测。 |
| HIAI_OM_TYPE_PROFILING | Profiling维测类型。 |
| HIAI_OM_TYPE_DUMP | Dump维测类型。 起始版本：6.0.0(20) |

#### HiAI_SingleOpActivationType

```ets
enum HiAI_SingleOpActivationType
```

**描述**

单算子激活模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_ACTIVATION_TYPE_RELU | ReLU激活函数。 |
| HIAI_SINGLEOP_ACTIVATION_TYPE_RELU6 | ReLU6激活函数。 |

#### HiAI_SingleOpConvMode

```ets
enum HiAI_SingleOpConvMode
```

**描述**

单算子卷积模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_CONV_MODE_COMMON | 普通卷积。 |
| HIAI_SINGLEOP_CONV_MODE_TRANSPOSED | 转置卷积。 |
| HIAI_SINGLEOP_CONV_MODE_DEPTHWISE | 深度卷积。 |

#### HiAI_SingleOpDataType

```ets
enum HiAI_SingleOpDataType
```

**描述**

单算子张量数据类型枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_DT_FLOAT | 张量数据类型为float。 |
| HIAI_SINGLEOP_DT_FLOAT16 | 张量数据类型为float16。 |
| HIAI_SINGLEOP_DT_UNDEFINED | 张量数据类型未定义。 |

#### HiAI_SingleOpFormat

```ets
enum HiAI_SingleOpFormat
```

**描述**

单算子张量排布格式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_FORMAT_NCHW | 张量按照NCHW格式排布。 |
| HIAI_SINGLEOP_FORMAT_NHWC | 张量按照NHWC格式排布。 |
| HIAI_SINGLEOP_FORMAT_ND | 张量按照ND格式排布。暂不支持用户使用ND格式排布的单算子Tensor。 |
| HIAI_SINGLEOP_FORMAT_NC1HWC0 | 张量按照NC1HWC0格式排布。 |
| HIAI_SINGLEOP_FORMAT_NC4HW4 | 张量按照NC4HW4格式排布。 |
| HIAI_SINGLEOP_FORMAT_NC8HW8 | 张量按照NC8HW8格式排布。 |
| HIAI_SINGLEOP_FORMAT_RESERVED | 张量排布格式未定义。 |

#### HiAI_SingleOpPadMode

```ets
enum HiAI_SingleOpPadMode
```

**描述**

单算子填充模式枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_PAD_MODE_SPECIFIC | 如果填充算法未设置，将根据参数pads采用显示填充。 |
| HIAI_SINGLEOP_PAD_MODE_SAME | 对输入进行填充使输出维度与输入维度相同。输出维度由ceil(输入维度 / 步长)确定。 |
| HIAI_SINGLEOP_PAD_MODE_SAME_UPPER | 使用SAME_UPPER填充模式，当填充长度为奇数时，起始的填充长度小于等于末尾的填充长度。 |
| HIAI_SINGLEOP_PAD_MODE_SAME_LOWER | 使用SAME_LOWER填充模式，当填充长度为奇数时，起始的填充长度大于等于末尾的填充长度。 |
| HIAI_SINGLEOP_PAD_MODE_VALID | 不填充，输出维度由ceil((输入维度 - 滤波器维度 + 1) / 步长)确定。 |

#### HiAI_SingleOpSupportStatus

```ets
enum HiAI_SingleOpSupportStatus
```

**描述**

单算子支持状态枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_SINGLEOP_OPTIMIZED | 使用单算子性能已优化。推荐用户使用单算子执行器，执行单算子推理计算。 |
| HIAI_SINGLEOP_COMMON | 使用单算子性能普通。支持该算子，但使用单算子可能性能收益小。 |
| HIAI_SINGLEOP_UNSUPPORTED | 不支持该单算子。若创建该单算子执行器将会失败。 |

#### HiAI_TuningMode

```ets
enum HiAI_TuningMode
```

**描述**

辅助调优模式。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_TUNING_MODE_UNSET | 关闭调优模式。 |
| HIAI_TUNING_MODE_AUTO | 自动调优模式，推荐选择的模式，内部算法控制调优。 |
| HIAI_TUNING_MODE_HETER | 异构调优模式。 |

#### HiAI_TuningStrategy

```ets
enum HiAI_TuningStrategy
```

**描述**

模型优化策略配置选项。

**起始版本：** 4.1.0(11)

| 枚举值 | 描述 |
| --- | --- |
| HIAI_TUNING_STRATEGY_OFF | 不支持深度融合场景，也不支持编译前可变shape，默认值。 |
| HIAI_TUNING_STRATEGY_ON_DEVICE_TUNING | 支持编译前可变shape场景深度融合优化模型。 |
| HIAI_TUNING_STRATEGY_ON_DEVICE_PREPROCESS_TUNING | NPU算子库动态升级场景深度融合优化模型。 |
| HIAI_TUNING_STRATEGY_ON_CLOUD_TUNING | 未来场景的预留，目前不使用。 |

#### 函数说明

#### HMS_HiAI_GetVersion()

```ets
const char* HMS_HiAI_GetVersion (void)
```

**描述**

获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。

**起始版本：** 4.1.0(11)

**返回：**

成功返回CANN Kit版本号，失败返回空指针。

#### HMS_HiAIAippParam_Create()

```ets
HiAI_AippParam* HMS_HiAIAippParam_Create (uint32_t batchNum)
```

**描述**

根据batchNum创建动态AippParam对象。

本方法用于创建动态AippParam对象，根据传入的batchNum申请相应的内存，用于存储动态AIPP参数。 不需要[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)指针实例时，需要调用[HMS_HiAIAippParam_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_destroy)进行释放，否则会出现内存泄漏。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| batchNum | 模型输入的batch大小，取值范围为(0, 127]。 |

**返回：**

成功时返回[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)指针实例，失败返回空指针。

#### HMS_HiAIAippParam_Destroy()

```ets
void HMS_HiAIAippParam_Destroy (HiAI_AippParam ** aippParam)
```

**描述**

释放AippParam对象。

本方法用于释放通过[HMS_HiAIAippParam_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_create)创建的[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |

#### HMS_HiAIAippParam_GetBatchCount()

```ets
uint32_t HMS_HiAIAippParam_GetBatchCount (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的图像数量。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询推理AippParam设置图像数量。 在单batch多crop场景为一张图像多个crop的子图像的数量。在多batch单crop场景为输入的batch值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |

**返回：**

成功返回图像数量，失败返回0。

#### HMS_HiAIAippParam_GetChannelPadding()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelPadding (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)
```

**描述**

查询AippParam对象的通道padding填充值。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的通道padding的填充值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| [padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)Values[] | 通道填充值数组，填充值范围[-65504, 65504]，默认填充值为0。 |
| channelCount | 通道填充数，当前支持[1, 4]，例如channelCount=3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetChannelSwapConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetChannelSwapConfig (HiAI_AippParam * aippParam, bool * rbuvSwapSwitch, bool * axSwapSwitch)
```

**描述**

查询AippParam对象的ChannelSwap通道交换参数。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询通道交换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| rbuvSwapSwitch | 返回真为RB/UV通道交换已使能，返回假为RB/UV通道交换未使能。 |
| axSwapSwitch | 返回真为AX通道交换已使能，返回假为AX通道交换未使能。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetCropConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetCropConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * startPosW, uint32_t * startPosH, uint32_t * croppedW, uint32_t * croppedH)
```

**描述**

查询AippParam对象的裁剪参数。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的裁剪参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应即将crop出来的图像索引。 |
| startPosW | 裁剪起始位置水平方向坐标。 |
| startPosH | 裁剪起始位置垂直方向坐标。 |
| croppedW | 裁剪出的图像宽度，单位为像素。 |
| croppedH | 裁剪出的图像高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetCscConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetCscConfig (HiAI_AippParam * aippParam, HiAI_ImageFormat * inputFormat, HiAI_ImageFormat * outputFormat, HiAI_ImageColorSpace * space)
```

**描述**

查询AippParam对象的CSC色域转换相关参数。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询推理AippParam色域转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| inputFormat | 图像输入格式，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |
| outputFormat | 图像输出格式，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |
| space | 图像颜色空间类型，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)ColorSpace。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetData()

```ets
void* HMS_HiAIAippParam_GetData (HiAI_AippParam * aippParam)
```

**描述**

获取AippParam申请的内存地址。

本方法用于获取通过[HMS_HiAIAippParam_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_create)申请的[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)的data内存地址。 data指向申请的AIPP参数的内存。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返空指针。 |

**返回：**

成功时返回AippParam申请的内存地址，失败返回空指针。

#### HMS_HiAIAippParam_GetDataSize()

```ets
uint32_t HMS_HiAIAippParam_GetDataSize (HiAI_AippParam * aippParam)
```

**描述**

获取AippParam申请的内存大小。

本方法用于获取通过[HMS_HiAIAippParam_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_create)申请的[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)的size大小。 size为申请的AIPP参数的内存大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回0。 |

**返回：**

成功时返回AippParam申请的内存大小，失败返回0。

#### HMS_HiAIAippParam_GetDtcMeanPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMeanPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素平均值。

该方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的数据类型转换像素平均值。 该方法需配合[HMS_HiAIAippParam_GetDtcMinPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcminpixel)、[HMS_HiAIAippParam_GetDtcVarReciPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcvarrecipixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| meanPixel[] | 通道像素平均值数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetDtcMinPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcMinPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素最小值。

该方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的数据类型转换像素最小值。 该方法需配合[HMS_HiAIAippParam_GetDtcMeanPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcmeanpixel)、[HMS_HiAIAippParam_GetDtcVarReciPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcvarrecipixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| minPixel[] | 通道像素最小值数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetDtcVarReciPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetDtcVarReciPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)
```

**描述**

查询AippParam对象的数据类型转换通道像素方差。

该方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的数据类型转换像素方差值。 该方法需配合[HMS_HiAIAippParam_GetDtcMeanPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcmeanpixel)、[HMS_HiAIAippParam_GetDtcMinPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getdtcminpixel)共同使用，来获取所有数据类型转换参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| varReciPixel[] | 通道像素方差数组，数组size为channelCount。 |
| channelCount | 通道数量，取值范围为[1, 4]，对应从chn0开始。例如channelCount等于3则对应查询通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetInputAippIndex()

```ets
int HMS_HiAIAippParam_GetInputAippIndex (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象在该输入的多个输出分支上的索引。

本方法用于在data节点有多个索引时，查询AippParam对象在data节点上的索引。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回-1。 |

**返回：**

成功时返回该AippParam对象在data节点上的索引，失败返回-1。

#### HMS_HiAIAippParam_GetInputFormat()

```ets
HiAI_ImageFormat HMS_HiAIAippParam_GetInputFormat (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的输入图像格式。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询输入图像格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回HIAI_IMAGE_FORMAT_INVALID。 |

**返回：**

成功返回[HiAI_ImageFormat](#ZH-CN_TOPIC_0000002553362477__hiai_imageformat)，失败返回HIAI_IMAGE_FORMAT_INVALID。

#### HMS_HiAIAippParam_GetInputIndex()

```ets
int HMS_HiAIAippParam_GetInputIndex (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象所在输入的索引。

本方法用于在多个输入情况下，查询AippParam对象所在输入的索引。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回-1。 |

**返回：**

成功时返回该AippParam对象所在输入的索引，失败返回-1。

#### HMS_HiAIAippParam_GetInputShape()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetInputShape (HiAI_AippParam * aippParam, uint32_t * srcImageW, uint32_t * srcImageH)
```

**描述**

查询AippParam对象的输入图像宽高。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询输入图像宽高。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)W | 输入图像的宽度，单位为像素。 |
| src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)H | 输入图像的高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetPadConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetPadConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * leftPadSize, uint32_t * rightPadSize, uint32_t * topPadSize, uint32_t * bottomPadSize)
```

**描述**

查询AippParam对象的输入图像的填充像素数。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的对输入图像的填充像素数。 当需要查询channel上的填充值时，需与[HMS_HiAIAippParam_GetChannelPadding](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_getchannelpadding)一起使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| leftPadSize | 图像左侧Padding像素数。 |
| rightPadSize | 图像右侧Padding像素数。 |
| topPadSize | 图像上侧Padding像素数。 |
| bottomPadSize | 图像下侧Padding像素数。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetResizeConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetResizeConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t * resizedW, uint32_t * resizedH)
```

**描述**

查询AippParam对象的图像缩放参数。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的缩放后图像宽高值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| resizedW | 缩放后图像宽度，单位为像素。 |
| resizedH | 缩放后图像高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetRotationAngle()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_GetRotationAngle (HiAI_AippParam * aippParam, uint32_t batchIndex, float * rotationAngle)
```

**描述**

查询AippParam对象的图像旋转角度。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询对应索引的图像旋转角度。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| rotationAngle | 旋转角度。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_GetSingleBatchMultiCrop()

```ets
bool HMS_HiAIAippParam_GetSingleBatchMultiCrop (HiAI_AippParam * aippParam)
```

**描述**

查询AippParam对象的SingleBatchMultiCrop标识。

本方法用于动态AIPP推理时，根据[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象查询是否为单batch多crop场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |

**返回：**

返回真为单batch多crop场景，返回假为非单batch多crop场景。

#### HMS_HiAIAippParam_SetChannelPadding()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelPadding (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t paddingValues[], uint32_t channelCount)
```

**描述**

设置AippParam对象的通道padding填充值。

本方法用于动态AIPP推理时，设置AIPP通道padding的填充值到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| [padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)Values[] | 通道填充值数组，填充值范围[-65504, 65504]，默认填充值为0。 |
| channelCount | 通道填充数，当前支持[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetChannelSwapConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetChannelSwapConfig (HiAI_AippParam * aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)
```

**描述**

设置AippParam对象的ChannelSwap通道交换参数。

本方法用于动态AIPP推理时，设置AippParam通道交换参数到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 AIPP支持两种类型的通道交换：RB/UV通道交换和AX通道交换。 RB/UV通道交换丰富了输入图像的格式，开启RB/UV通道交换后，AIPP支持的图像输入格式比可配置的输入类型丰富了一倍。

| 配置类型 | 可接受图像类型 |
| --- | --- |
| YUV420SP_U8 | YUV420SP_U8，YVU420 + rbuv_swap_switch |
| XRGB8888_U8 | XRGB8888_U8，XBGR + rbuv_swap_switch |
| ARGB8888_U8 | ARGB8888_U8，ABGR + rbuv_swap_switch |
| RGB888_U8 | BGR888_U8 + rbuv_swap_switch |
| BGR888_U8 | RGB888_U8 + rbuv_swap_switch |
| YUYV_U8 | YUYV_U8，YVYU_U8 + rbuv_swap_switch |
| YUV422SP_U8 | YUV422SP_U8，YVU422_U8 + rbuv_swap_switch |
| AYUV444_U8 | AYUV444_U8 + rbuv_swap_switch |

YUV400_U8是灰度图，不支持通道交换。

当配置的图像输入格式为XRGB、ARGB或AYUV时，支持开启AX通道交换。开启后，图像第一个通道的输入被搬移到第四个通道上，即当XRGB、ARGB和AYUV开启AX通道交换后，转变为RGBX、RGBA和YUVA。 当模型训练集为RGB格式的图像，而推理时的图像输入为XRGB或者ARGB时，可以通过使能AX通道交换，将RGB通道前移，实现兼容。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| rbuvSwapSwitch | 参数真为使能RB/UV通道交换，参数假为不使能RB/UV通道交换。 |
| axSwapSwitch | 参数真为使能AX通道交换，参数假为不使能AX通道交换。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetCropConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetCropConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t startPosW, uint32_t startPosH, uint32_t croppedW, uint32_t croppedH)
```

**描述**

设置AippParam对象的裁剪参数。

本方法用于动态AIPP推理时，设置裁剪参数到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 YUV类型的图像受图像自身类型的限制，当输入图像类型为YUV420SP、YUYV、YUV422SP和AYUV444时，裁剪的起始坐标和裁剪的宽高需为是偶数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应即将crop出来的图像索引。 |
| startPosW | 裁剪起始位置水平方向坐标，startPosW小于输入图像的宽度，单位为像素。 |
| startPosH | 裁剪起始位置垂直方向坐标，startPosH小于输入图像的高度，单位为像素。 |
| croppedW | 裁剪出的图像宽度，startPosW与cropSizeW之和小于等于输入图像的宽度，单位为像素。 |
| croppedH | 裁剪出的图像高度，startPosH与cropSizeH之和小于等于输入图像的高度，单位为像素。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetCscConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetCscConfig (HiAI_AippParam * aippParam, HiAI_ImageFormat inputFormat, HiAI_ImageFormat outputFormat, HiAI_ImageColorSpace space)
```

**描述**

设置AippParam对象的CSC色域转换参数。

本方法用于动态AIPP推理时，设置AippParam色域转换参数到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 色域转换（Color Space Conversion，以下简称CSC），特指在YUV444和RGB888两种图像格式之间进行转换。 输入为YUV格式图像(YUV420/YUYV/YUV422SP/AYUV444)，模型训练集可为RGB,BGR，灰度图（YUV400_U8）。 输入为RGB格式图像(XRGB8888/ARGB8888)，模型训练集可为YUV444SP，YVU444SP，灰度图（YUV400_U8）。 不支持从YUV400到RGB或BGR的转换。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| inputFormat | 图像输入格式，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |
| outputFormat | 图像输出格式，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |
| space | 图像颜色空间类型，可参考HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)ColorSpace。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetDtcMeanPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMeanPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t meanPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素平均值。

数据类型转换（Data Type Conversion，简称DTC），用于将输入图像中像素值转换为模型训练时的数据类型。设置DTC参数，使得转换之后的数据在一个预期的范围，避免强制转换。 数据类型转化功能，将输入的图像数据类型通过转化公式转换为FP16类型送给后续模块计算，实际为依次执行减均值、减最小值和乘方差操作。

计算公式为：U8->FP16: pixelOutChn(i) = [pixelInChn(i)–meanChn(i)–minChn(i)] * varReciChn(i), i ∈ [0, 4) 其中：pixelOutChn(i)为DTC模块的每个通道的输出值，pixelInChn(i)为DTC模块的每个通道的输入值，meanChn(i)为用户输入的每个通道的均值， minChn(i)为用户输入的每个通道的最小值， varReciChn(i)为用户输入的每个通道的方差。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素平均值到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 该方法需配合[HMS_HiAIAippParam_SetDtcMinPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcminpixel)、[HMS_HiAIAippParam_SetDtcVarReciPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcvarrecipixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| meanPixel[] | 通道像素平均值数组，数组size为channelCount，默认值为0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetDtcMinPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcMinPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float minPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素最小值。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素最小值到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 该方法需配合[HMS_HiAIAippParam_SetDtcMeanPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcmeanpixel)、[HMS_HiAIAippParam_SetDtcVarReciPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcvarrecipixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| minPixel[] | 通道像素最小值数组，数组size为channelCount，默认值为0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetDtcVarReciPixel()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetDtcVarReciPixel (HiAI_AippParam * aippParam, uint32_t batchIndex, float varReciPixel[], uint32_t channelCount)
```

**描述**

设置AippParam对象的数据类型转换通道像素方差。

该方法用于动态AIPP推理时，设置DTC数据类型转换像素方差到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 该方法需配合[HMS_HiAIAippParam_SetDtcMeanPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcmeanpixel)、[HMS_HiAIAippParam_SetDtcMinPixel](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setdtcminpixel)共同使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| varReciPixel[] | 通道像素方差数组，数组size为channelCount，默认值为1.0。 |
| channelCount | 通道数量，取值范围为[1, 4]，例如channelCount=3则对应配置通道chn0, chn1, chn2的数据。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetInputAippIndex()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputAippIndex (HiAI_AippParam * aippParam, uint32_t inputAippIndex)
```

**描述**

设置AippParam对象作用于该输入的多个输出分支上的索引。

本方法用于在data有多个输出分支时，设置AippParam对象作用域该输入的第几个输出分支。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |
| inputAippIndex | 用于标识AIPP配置参数在输入Data有多个输出分支时作用于第几个分支，从0开始计数。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetInputFormat()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputFormat (HiAI_AippParam * aippParam, HiAI_ImageFormat inputFormat)
```

**描述**

设置AippParam对象的输入图像格式。

本方法用于动态AIPP推理时，设置AIPP的输入图像格式到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 AIPP可配置的图像格式为[HiAI_ImageFormat](#ZH-CN_TOPIC_0000002553362477__hiai_imageformat)所支持的范围。 图像像素点为Uint8类型，范围为0到255。当图像的输入为YUV类型时，无论是YUV420还是YUV422或者YUYV，AIPP自动将图像数据补齐为YUV444格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| inputFormat | 输入图像的格式HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetInputIndex()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputIndex (HiAI_AippParam * aippParam, uint32_t inputIndex)
```

**描述**

设置AippParam在输入上的索引。

本方法用于在多个输入情况下，设置索引以确定该AippParam对象作用于第几个输入。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空。 |
| inputIndex | 用于标识此AIPP参数作用于模型的第几个输入，从0开始计数。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetInputShape()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetInputShape (HiAI_AippParam * aippParam, uint32_t srcImageW, uint32_t srcImageH)
```

**描述**

设置AippParam对象的输入图像宽高。

本方法用于动态AIPP推理时，设置输入图像宽高到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)W | 输入图像的宽度，单位为像素，取值范围[16, 4096]。 |
| src[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)H | 输入图像的高度，单位为像素，取值范围[16, 4096]。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetPadConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetPadConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t leftPadSize, uint32_t rightPadSize, uint32_t topPadSize, uint32_t bottomPadSize)
```

**描述**

设置AippParam对象的输入图像的填充像素数。

本方法用于动态AIPP推理时，设置对输入图像的填充像素数到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。包含图像左右上下侧的Padding像素数。 当需要设置channel上的填充值时，需与[HMS_HiAIAippParam_SetChannelPadding](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_setchannelpadding)一起使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| leftPadSize | 图像左侧Padding像素数，经过[padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)后的图像宽度，需与原始模型维度中宽度保持一致。 |
| rightPadSize | 图像右侧Padding像素数，经过[padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)后的图像宽度，需与原始模型维度中宽度保持一致。 |
| topPadSize | 图像上侧Padding像素数，经过[padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)后的图像高度，需与原始模型维度中高度保持一致。 |
| bottomPadSize | 图像下侧Padding像素数，经过[padding](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__padding)后的图像高度，需与原始模型维度中高度保持一致。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetResizeConfig()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetResizeConfig (HiAI_AippParam * aippParam, uint32_t batchIndex, uint32_t resizedW, uint32_t resizedH)
```

**描述**

设置AippParam对象的图像缩放参数。

本方法用于动态AIPP推理时，设置图像缩放参数到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。Resize的类型为双线性插值。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| resizedW | 缩放后图像宽度，单位为像素，取值范围[16, 448]，图像宽度缩放倍数的范围[1/16, 16]。 |
| resizedH | 缩放后图像高度，单位为像素，取值范围[16, 4096]，图像高度缩放倍数的范围[1/16, 16]。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetRotationAngle()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetRotationAngle (HiAI_AippParam * aippParam, uint32_t batchIndex, float rotationAngle)
```

**描述**

设置AippParam对象的旋转角度。

本方法用于动态AIPP推理时，设置旋转角度到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| batchIndex | 对于多batch单crop场景，对应输入的图像索引；对于单batch多crop场景，对应crop出来的图像索引。 |
| rotationAngle | 旋转角度，仅支持0, 90, 180, 270。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIAippParam_SetSingleBatchMultiCrop()

```ets
OH_NN_ReturnCode HMS_HiAIAippParam_SetSingleBatchMultiCrop (HiAI_AippParam * aippParam, bool singleBatchMultiCrop)
```

**描述**

设置AippParam对象的SingleBatchMultiCrop标识。

本方法用于动态AIPP推理时，设置AippParam单batch多crop标识到[HiAI_AippParam](#ZH-CN_TOPIC_0000002553362477__hiai_aippparam)对象。 对于单个batch的图像输入的场景，支持一次性传入多组crop等AIPP参数，一次推理即能得到全部人脸等的关键点信息。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| aippParam | HiAI_AippParam指针实例，非空，否则返回失败。 |
| singleBatchMultiCrop | 参数真为单batch多crop场景，参数假为非单batch多crop场景。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAICompatibility_CheckFromBuffer()

```ets
HiAI_Compatibility HMS_HiAICompatibility_CheckFromBuffer (const void * data, size_t size)
```

**描述**

查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| data | 编译后模型数据地址，非空，否则返回不兼容。 |
| size | 编译后模型数据大小，非空，否则返回不兼容。 |

**返回：**

成功返回 [HiAI_Compatibility](#ZH-CN_TOPIC_0000002553362477__hiai_compatibility)，失败返回不兼容。

#### HMS_HiAICompatibility_CheckFromFile()

```ets
HiAI_Compatibility HMS_HiAICompatibility_CheckFromFile (const char * file)
```

**描述**

查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| file | 编译后模型文件路径及名称，要求用户进程对文件有访问权限，非空，否则返回不兼容。 |

**返回：**

成功返回 [HiAI_Compatibility](#ZH-CN_TOPIC_0000002553362477__hiai_compatibility)，失败返回不兼容。

#### HMS_HiAIOptions_GetBandMode()

```ets
HiAI_BandMode HMS_HiAIOptions_GetBandMode (const OH_NNCompilation * compilation)
```

**描述**

查询带宽模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回带宽模式[HiAI_BandMode](#ZH-CN_TOPIC_0000002553362477__hiai_bandmode)，失败返回默认值。

#### HMS_HiAIOptions_GetDeviceMemoryReusePlan()

```ets
HiAI_DeviceMemoryReusePlan HMS_HiAIOptions_GetDeviceMemoryReusePlan (const OH_NNCompilation * compilation)
```

**描述**

查询调优配置中的设备内存复用参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI_DeviceMemoryReusePlan](#ZH-CN_TOPIC_0000002553362477__hiai_devicememoryreuseplan)，失败返回默认值。

#### HMS_HiAIOptions_GetDynamicShapeCacheMode()

```ets
HiAI_DynamicShapeCacheMode HMS_HiAIOptions_GetDynamicShapeCacheMode (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的cacheMode参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI_DynamicShapeCacheMode](#ZH-CN_TOPIC_0000002553362477__hiai_dynamicshapecachemode)，失败返回默认值。

#### HMS_HiAIOptions_GetDynamicShapeMaxCache()

```ets
size_t HMS_HiAIOptions_GetDynamicShapeMaxCache (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的最大缓存数量。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功时返回最大缓存数量，失败返回0。

#### HMS_HiAIOptions_GetDynamicShapeStatus()

```ets
HiAI_DynamicShapeStatus HMS_HiAIOptions_GetDynamicShapeStatus (const OH_NNCompilation * compilation)
```

**描述**

查询编译前可变shape配置中的状态参数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI_DynamicShapeStatus](#ZH-CN_TOPIC_0000002553362477__hiai_dynamicshapestatus)，失败返回默认值。

#### HMS_HiAIOptions_GetFallbackMode()

```ets
HiAI_FallbackMode HMS_HiAIOptions_GetFallbackMode (const OH_NNCompilation * compilation)
```

**描述**

查询调优配置中的回滚模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功时返回[HiAI_FallbackMode](#ZH-CN_TOPIC_0000002553362477__hiai_fallbackmode)，失败返回默认值。

#### HMS_HiAIOptions_GetFormatMode()

```ets
HiAI_FormatMode HMS_HiAIOptions_GetFormatMode (const OH_NNCompilation * compilation)
```

**描述**

查询模型编译参数中的数据排列格式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回[HiAI_FormatMode](#ZH-CN_TOPIC_0000002553362477__hiai_formatmode)，失败返回默认值。

#### HMS_HiAIOptions_GetInputTensorShape()

```ets
NN_TensorDesc* HMS_HiAIOptions_GetInputTensorShape (const OH_NNCompilation * compilation, size_t index)
```

**描述**

查询选项参数中指定索引的shape描述。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回空指针。 |
| index | 输入shape的索引，取值为[0, HMS_HiAIOptions_GetInputTensorShapeSize)。 |

**返回：**

成功返回选项参数中的shape描述，失败返回空指针。

#### HMS_HiAIOptions_GetInputTensorShapeSize()

```ets
size_t HMS_HiAIOptions_GetInputTensorShapeSize (const OH_NNCompilation * compilation)
```

**描述**

查询选项参数中shape描述的个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功返回选项参数中shape描述的个数，失败返回0。

#### HMS_HiAIOptions_GetModelDeviceCount()

```ets
size_t HMS_HiAIOptions_GetModelDeviceCount (const OH_NNCompilation * compilation)
```

**描述**

查询模型级调优配置中模型的执行设备个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功时返回执行设备的个数，失败返回0。

#### HMS_HiAIOptions_GetModelDeviceOrder()

```ets
HiAI_ExecuteDevice* HMS_HiAIOptions_GetModelDeviceOrder (const OH_NNCompilation * compilation)
```

**描述**

查询模型级调优配置中模型的执行设备列表。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功时返回[HiAI_ExecuteDevice](#ZH-CN_TOPIC_0000002553362477__hiai_executedevice)执行设备列表，失败返回空指针。

#### HMS_HiAIOptions_GetOperatorDeviceCount()

```ets
size_t HMS_HiAIOptions_GetOperatorDeviceCount (const OH_NNCompilation * compilation, const char * operatorName)
```

**描述**

查询算子级调优配置中指定算子的执行设备个数。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回0。 |
| operatorName | 算子名称，非空，否则返回0。 |

**返回：**

成功时返回执行设备的个数，失败返回0。

#### HMS_HiAIOptions_GetOperatorDeviceOrder()

```ets
HiAI_ExecuteDevice* HMS_HiAIOptions_GetOperatorDeviceOrder (const OH_NNCompilation * compilation, const char * operatorName)
```

**描述**

查询算子级调优配置中指定算子的执行设备列表。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回空指针。 |
| operatorName | 算子名称，非空，否则返回空指针。 |

**返回：**

成功时返回[HiAI_ExecuteDevice](#ZH-CN_TOPIC_0000002553362477__hiai_executedevice)执行设备列表，失败返回空指针。

#### HMS_HiAIOptions_GetQuantConfigData()

```ets
void* HMS_HiAIOptions_GetQuantConfigData (const OH_NNCompilation * compilation)
```

**描述**

查询量化配置的数据地址。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功返回量化配置的数据地址，失败返回空指针。

#### HMS_HiAIOptions_GetQuantConfigSize()

```ets
size_t HMS_HiAIOptions_GetQuantConfigSize (const OH_NNCompilation * compilation)
```

**描述**

查询量化配置的数据大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回0。 |

**返回：**

成功返回量化配置的数据大小，失败返回0。

#### HMS_HiAIOptions_GetTuningCacheDir()

```ets
const char* HMS_HiAIOptions_GetTuningCacheDir (const OH_NNCompilation * compilation)
```

**描述**

查询辅助调优的缓存目录。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回空指针。 |

**返回：**

成功返回缓存目录，失败返回空指针。

#### HMS_HiAIOptions_GetTuningMode()

```ets
HiAI_TuningMode HMS_HiAIOptions_GetTuningMode (const OH_NNCompilation * compilation)
```

**描述**

查询辅助调优模式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

返回辅助调优模式[HiAI_TuningMode](#ZH-CN_TOPIC_0000002553362477__hiai_tuningmode)，失败返回默认值。

#### HMS_HiAIOptions_GetTuningStrategy()

```ets
HiAI_TuningStrategy HMS_HiAIOptions_GetTuningStrategy (const OH_NNCompilation * compilation)
```

**描述**

查询模型优化策略。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回默认值。 |

**返回：**

成功返回[HiAI_TuningStrategy](#ZH-CN_TOPIC_0000002553362477__hiai_tuningstrategy)，失败返回默认值。

#### HMS_HiAIOptions_SetBandMode()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetBandMode (OH_NNCompilation * compilation, HiAI_BandMode bandMode)
```

**描述**

设置NPU与周边硬件IO资源的带宽模式。

根据需要设置合适的值，带宽与功耗成正比，高带宽也意味着高功耗。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| bandMode | 带宽模式HiAI_BandMode。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetDeviceMemoryReusePlan()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetDeviceMemoryReusePlan (OH_NNCompilation * compilation, HiAI_DeviceMemoryReusePlan deviceMemoryReusePlan)
```

**描述**

设置调优配置中的设备内存复用参数。

本方法仅在模型编译阶段生效。用于在调优时，指定设备内存复用方式。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| deviceMemoryReusePlan | 设备内存复用HiAI_DeviceMemoryReusePlan。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetDynamicShapeCacheMode()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeCacheMode (OH_NNCompilation * compilation, HiAI_DynamicShapeCacheMode mode)
```

**描述**

设置编译前可变shape配置中的缓存模式参数。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS_HiAIOptions_SetDynamicShapeStatus](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapestatus)、[HMS_HiAIOptions_SetDynamicShapeMaxCache](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapemaxcache)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| mode | 编译前可变shape的缓存模式HiAI_DynamicShapeCacheMode。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetDynamicShapeMaxCache()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeMaxCache (OH_NNCompilation * compilation, size_t maxCacheCount)
```

**描述**

设置编译前可变shape配置中的最大缓存编译后模型数量。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS_HiAIOptions_SetDynamicShapeStatus](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapestatus)、[HMS_HiAIOptions_SetDynamicShapeCacheMode](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapecachemode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| maxCacheCount | 最大档位，取值范围[1, 10]。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetDynamicShapeStatus()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetDynamicShapeStatus (OH_NNCompilation * compilation, HiAI_DynamicShapeStatus status)
```

**描述**

设置编译前可变shape配置中的EnableMode参数。

本方法仅在模型编译阶段生效，用于在推理阶段期望变更shape，且模型的shape变化数量不超过10个场景。 本方法需与[HMS_HiAIOptions_SetDynamicShapeMaxCache](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapemaxcache)、[HMS_HiAIOptions_SetDynamicShapeCacheMode](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_setdynamicshapecachemode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| status | 是否使能编译前可变shapeHiAI_DynamicShapeStatus。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetFallbackMode()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetFallbackMode (OH_NNCompilation * compilation, HiAI_FallbackMode fallbackMode)
```

**描述**

设置调优配置中的回滚模式。

本方法仅在模型编译阶段生效。用于在模型级或算子级调优时，指定的执行设备列表出现不支持时，是否可回滚到其他硬件执行。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| fallbackMode | 是否使能回滚模式HiAI_FallbackMode。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetFormatMode()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetFormatMode (OH_NNCompilation * compilation, HiAI_FormatMode formatMode)
```

**描述**

设置模型编译时的数据排列格式。

本方法仅在模型编译阶段生效，用于模型中的数据排列格式与默认值不匹配时的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空。 |
| formatMode | 数据排列格式HiAI_FormatMode。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetInputTensorShapes()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetInputTensorShapes (OH_NNCompilation * compilation, NN_TensorDesc * inputTensorDescs[], size_t shapeCount)
```

**描述**

编译时更新模型输入shape。

本方法仅在模型编译阶段生效，用于模型结构及权重不变，模型输入shape需要变化的场景。数组的大小需要与模型的输入数量保持一致。 模型编译后，模型的输入shape将变更为新设置的shape，推理时输入输出数据需符合新的模型输入输出描述。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空。 |
| inputTensorDescs[] | 模型输入shape列表数组NN_TensorDesc，非空。 |
| shapeCount | 模型输入shape的个数，需与模型输入个数对应。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetModelDeviceOrder()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetModelDeviceOrder (OH_NNCompilation * compilation, HiAI_ExecuteDevice * executeDevices, size_t deviceCount)
```

**描述**

设置模型级调优配置中模型执行设备列表。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定模型的执行设备列表，按照优先级顺序排列。默认NPU优先。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| executeDevices | 支持的设备类型列表HiAI_ExecuteDevice，非空，否则返回失败。 |
| deviceCount | 支持的执行硬件个数。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetOmOptions()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetOmOptions (OH_NNCompilation * compilation, HiAI_OmType type, const char * outputDir)
```

**描述**

设置模型加载时的维测选项信息。

该方法属于可选接口，在模型加载阶段生效，用于模型的性能调试。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| type | 维测类型HiAI_OmType。 |
| outputDir | 维测输出目录，用于生产profiling相关文件。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetOperatorDeviceOrder()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetOperatorDeviceOrder (OH_NNCompilation * compilation, const char * operatorName, HiAI_ExecuteDevice * executeDevices, size_t deviceCount)
```

**描述**

设置算子级调优配置中算子执行设备列表。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定模型中算子的执行设备列表，按照优先级顺序排列，算子名称不可重复。 模型中的算子可以部分指定，不指定的算子以NPU优先，可以使用开源工具Netron查看模型中的算子名称。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| operatorName | 算子名称，非空，否则返回失败。 |
| executeDevices | 支持的设备类型列表HiAI_ExecuteDevice，非空，否则返回失败。 |
| deviceCount | 支持的执行硬件个数。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetQuantConfig()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetQuantConfig (OH_NNCompilation * compilation, void * data, size_t size)
```

**描述**

设置模型编译时量化配置。

本方法仅在模型编译阶段生效。用于模型编译时进行量化的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| data | 量化配置的数据地址，非空，否则返回失败。 |
| size | 量化配置的数据大小，大于0，否则返回失败。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetTuningCacheDir()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetTuningCacheDir (OH_NNCompilation * compilation, const char * cacheDir)
```

**描述**

设置辅助调优的缓存目录。

要求用户进程对缓存目录有读写权限。本方法需与[HMS_HiAIOptions_SetTuningMode](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_settuningmode)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| cacheDir | 缓存目录，非空，否则返回失败。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetTuningMode()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetTuningMode (OH_NNCompilation * compilation, HiAI_TuningMode tuningMode)
```

**描述**

选择辅助调优模式。

本方法仅在模型编译阶段生效，不可与其他调优混用。用于指定CANN Kit协助进行调优的场景。 本方法需与[HMS_HiAIOptions_SetTuningCacheDir](#ZH-CN_TOPIC_0000002553362477__hms_hiaioptions_settuningcachedir)搭配使用。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| tuningMode | 辅助调优模式HiAI_TuningMode。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAIOptions_SetTuningStrategy()

```ets
OH_NN_ReturnCode HMS_HiAIOptions_SetTuningStrategy (OH_NNCompilation * compilation, HiAI_TuningStrategy tuningStrategy)
```

**描述**

设置模型编译时的模型优化策略。

本方法仅在模型编译阶段生效。用于模型算子深度融合的场景。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| compilation | OH_NNCompilation指针实例，非空，否则返回失败。 |
| tuningStrategy | 模型优化策略配置HiAI_TuningStrategy。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpBuffer_Create()

```ets
HiAI_SingleOpBuffer* HMS_HiAISingleOpBuffer_Create (size_t dataSize)
```

**描述**

按照指定的内存大小创建[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象。

本方法用于根据指定的dataSize申请对应大小的ION内存，并创建[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象。当不再使用[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象时， 调用[HMS_HiAISingleOpBuffer_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopbuffer_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dataSize | 要申请的内存字节大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpBuffer_Destroy()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer ** buffer)
```

**描述**

释放[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象。

本方法用于释放调用[HMS_HiAISingleOpBuffer_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopbuffer_create)创建的[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向HiAI_SingleOpBuffer对象的二级指针。buffer和 *buffer不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpBuffer_GetData()

```ets
void* HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer * buffer)
```

**描述**

查询[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)的内存地址。

本方法用于获取指定[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象的内存地址。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向HiAI_SingleOpBuffer对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

Buffer的内存地址。

#### HMS_HiAISingleOpBuffer_GetSize()

```ets
size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer * buffer)
```

**描述**

查询[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)的字节大小。

本方法用于获取指定[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象的字节大小。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 指向HiAI_SingleOpBuffer对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

Buffer的字节大小。

#### HMS_HiAISingleOpDescriptor_CreateActivation()

```ets
HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateActivation (HiAI_SingleOpActivationType activationType, float coef)
```

**描述**

创建激活函数类的描述符对象。

本方法用于根据传入的参数创建激活函数类的[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象。当不再使用[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象时，调用[HMS_HiAISingleOpDescriptor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopdescriptor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| activationType | 激活模式。 |
| coef | 如果激活模式为带系数的激活类型，该值表示系数。否则，该值不会生效。 |

**返回：**

指向[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpDescriptor_CreateConvolution()

```ets
HiAI_SingleOpDescriptor* HMS_HiAISingleOpDescriptor_CreateConvolution (HiAISingleOpDescriptor_ConvolutionParam param)
```

**描述**

创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。

本方法用于根据传入的参数创建卷积类的[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象。当不再使用[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象时，调用[HMS_HiAISingleOpDescriptor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopdescriptor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAISingleOpDescriptor_ConvolutionParam](HiAISingleOpDescriptor_ConvolutionParam.md)。 |

**返回：**

指向[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpDescriptor_Destroy()

```ets
void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor ** opDesc)
```

**描述**

释放[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象。

当不再使用[HiAI_SingleOpDescriptor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopdescriptor)对象时，调用该接口销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| opDesc | 指向HiAI_SingleOpDescriptor对象的二级指针。opDesc和 *opDesc不能是空指针，否则销毁失败。 |

#### HMS_HiAISingleOpExecutor_CreateConvolution()

```ets
HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateConvolution (HiAI_SingleOpExecutorConvolutionParam param)
```

**描述**

创建卷积类算子对应的[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象。

当不再使用[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象时，调用[HMS_HiAISingleOpExecutor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_destroy)销毁，否则会造成内存泄漏。

对于输出Tensor描述，其数据类型和排布格式可以同时为HIAI_SINGLEOP_DT_UNDEFINED和HIAI_SINGLEOP_FORMAT_RESERVED。在这种情况下，执行器会将输出的数据类型和排布格式设置为适配硬件的类型。该接口执行成功后，可以调用[HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_updateoutputtensordesc)更新输出Tensor描述的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md)。 |

**返回：**

指向[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象的指针，如果创建失败，则返回空指针。

#### HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation()

```ets
HiAI_SingleOpExecutor* HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param)
```

**描述**

创建卷积和激活融合算子对应的[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象。

当不再使用[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象时，调用[HMS_HiAISingleOpExecutor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_destroy)销毁，否则会造成内存泄漏。

对于输出Tensor描述，其数据类型和排布格式可以为HIAI_SINGLEOP_DT_UNDEFINED和HIAI_SINGLEOP_FORMAT_RESERVED。在这种情况下，执行器会将输出的数据类型和排布格式设置为适配硬件的类型。该接口执行成功后，可以调用[HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_updateoutputtensordesc)更新输出Tensor描述的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md)。 |

**返回：**

指向[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象的指针，如果创建失败，则返回空指针。

#### HMS_HiAISingleOpExecutor_Destroy()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor ** executor)
```

**描述**

销毁[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象，释放执行器占用的内存。

当不再使用[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)对象时，调用该接口销毁，否则会造成内存泄漏。

注意：该接口不会释放传递给[HMS_HiAISingleOpExecutor_Init](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_init)的工作空间内存，工作空间所属的[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)需要单独释放。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向HiAI_SingleOpExecutor对象的二级指针。executor和 *executor不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpExecutor_Execute()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor * executor, HiAI_SingleOpTensor * input[], int32_t inputNum, HiAI_SingleOpTensor * output[], int32_t outputNum)
```

**描述**

执行同步运算推理。

在调用该接口前，需要先通过[HMS_HiAISingleOpTensor_CreateFromTensorDesc](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_createfromtensordesc)或[HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_createfromsingleopbuffer)接口创建输入和输出Tensor并填充输入Tensor数据。执行器会通过执行推理产生推理结果，并将结果写入输出Tensor中。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向HiAI_SingleOpExecutor对象的指针。该值不能为空指针，否则返回错误码。 |
| input[] | 输入Tensor的数组。 |
| inputNum | 输入Tensor的数量。 |
| output[] | 输出Tensor的数组。 |
| outputNum | 输出Tensor的数量。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpExecutor_GetWorkspaceSize()

```ets
size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor * executor)
```

**描述**

查询[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)所需的ION内存工作空间的字节大小。

在成功创建[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)后，调用该接口获取执行器所需的ION内存工作空间的字节大小，然后需要调用[HMS_HiAISingleOpBuffer_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopbuffer_create)申请足够的工作空间内存，将分配的工作空间传入[HMS_HiAISingleOpExecutor_Init](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_init)接口。

注意：同一个执行器的工作空间内存和输入、输出Tensor内存不能复用，不同执行器的工作空间内存可以复用。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向HiAI_SingleOpExecutor对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

工作空间的字节大小。

#### HMS_HiAISingleOpExecutor_Init()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor * executor, void * workspace, size_t workspaceSize)
```

**描述**

加载[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)。

在调用该接口之前，需要申请执行器所需的工作空间内存。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向HiAI_SingleOpExecutor对象的指针。该值不能为空指针，否则返回错误码。 |
| workspace | 工作空间地址。当workspaceSize不为0时，该值必须为HiAI_SingleOpBuffer中的内存地址，否则返回错误码。 |
| workspaceSize | 提供的workspace的字节大小。该值必须大于等于HMS_HiAISingleOpExecutor_GetWorkspaceSize获取的所需工作空间大小， 否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpExecutor_PreCheckConvolution()

```ets
HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckConvolution (HiAI_SingleOpExecutorConvolutionParam param)
```

**描述**

预查询卷积算子的支持状态。

根据该接口的返回值确定是否调用[HMS_HiAISingleOpExecutor_CreateConvolution](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_createconvolution)来创建卷积执行器，也可以不调用本方法，直接调用创建卷积执行器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI_SingleOpExecutorConvolutionParam](HiAI_SingleOpExecutorConvolutionParam.md)。 |

**返回：**

支持状态。具体状态请参考[HiAI_SingleOpSupportStatus](#ZH-CN_TOPIC_0000002553362477__hiai_singleopsupportstatus)。

#### HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation()

```ets
HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param)
```

**描述**

预查询卷积和激活融合算子的支持状态。

根据该接口的返回值确定是否调用[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopexecutor_createfusedconvolutionactivation)来创建卷积激活融合执行器，也可以不调用本方法，直接创建卷积激活融合执行器。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| param | 详细输入参数参见[HiAI_SingleOpExecutorFusedConvolutionActivationParam](HiAI_SingleOpExecutorFusedConvolutionActivationParam.md)。 |

**返回：**

支持状态。具体状态请参考[HiAI_SingleOpSupportStatus](#ZH-CN_TOPIC_0000002553362477__hiai_singleopsupportstatus)。

#### HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc (const HiAI_SingleOpExecutor * executor, uint32_t index, HiAI_SingleOpTensorDesc * output)
```

**描述**

更新[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)的输出tensor描述。

如果在创建[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)时，输入参数output数据类型为HIAI_SINGLEOP_DT_UNDEFINED，且排布格式为HIAI_SINGLEOP_FORMAT_RESERVED，那么在成功创建[HiAI_SingleOpExecutor](#ZH-CN_TOPIC_0000002553362477__hiai_singleopexecutor)后，调用该接口将输出Tensor描述更新为硬件适配的数据类型和排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| executor | 指向HiAI_SingleOpExecutor对象的指针。该值不能为空指针，否则返回错误码。 |
| index | 输出Tensor描述的索引，与创建executor时的输出顺序一致。索引值从0开始。 |
| output | 需要更新的[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpOptions_Create()

```ets
HiAI_SingleOpOptions* HMS_HiAISingleOpOptions_Create (void)
```

**描述**

创建[HiAI_SingleOpOptions](#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象。

当不再使用[HiAI_SingleOpOptions](#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象时，调用[HMS_HiAISingleOpOptions_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopoptions_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**返回：**

指向[HiAI_SingleOpOptions](#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpOptions_Destroy()

```ets
void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions ** options)
```

**描述**

释放[HiAI_SingleOpOptions](#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象。

本方法用于释放调用[HMS_HiAISingleOpOptions_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopoptions_create)创建的[HiAI_SingleOpOptions](#ZH-CN_TOPIC_0000002553362477__hiai_singleopoptions)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向HiAI_SingleOpOptions对象的二级指针。options和 *options不能是空指针，否则销毁失败。 |

#### HMS_HiAISingleOpTensor_CreateFromConst()

```ets
HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromConst (const HiAI_SingleOpTensorDesc * desc, void * data, size_t dataSize)
```

**描述**

根据[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象。

本方法用于根据[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)和常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象。

本方法直接复用**data**和**dataSize**对应的常量数据，不会进行数据的拷贝。因此，在本方法创建的Tensor仍要被使用时，不要释放该Tensor对应的常量数据内存。本方法仅读取**data**和**dataSize**对应的常量数据，不会修改其数据。

注意：该接口会将desc拷贝到[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)中。因此，当desc不再使用时，请使用[HMS_HiAISingleOpTensorDesc_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_destroy)销毁desc。

当不再使用[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象时，调用[HMS_HiAISingleOpTensor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |
| data | 常量数据地址。该值不能为空指针，否则返回空指针。 |
| dataSize | 常量数据大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer()

```ets
HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer (const HiAI_SingleOpTensorDesc * desc, void * data, size_t dataSize)
```

**描述**

根据[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)、[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)的内存地址和数据大小创建[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象。

本方法复用[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)的ION内存，所复用的内存地址和大小由data和dataSize确定。dataSize必须等于通过[HMS_HiAISingleOpTensorDesc_GetByteSize](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_getbytesize)计算得到的desc的字节大小。当调用[HMS_HiAISingleOpTensor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_destroy)接口销毁该接口创建的Tensor时，不会释放该Tensor数据的内存。

注意：该接口会将desc拷贝到[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)中。因此，当desc不再使用时，请使用[HMS_HiAISingleOpTensorDesc_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_destroy)销毁desc。

当不再使用[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象时，调用[HMS_HiAISingleOpTensor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |
| data | Tensor数据地址。该值必须是HiAI_SingleOpBuffer中的内存地址，否则返回空指针。 |
| dataSize | Tensor数据大小。该值不能为0，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpTensor_CreateFromTensorDesc()

```ets
HiAI_SingleOpTensor* HMS_HiAISingleOpTensor_CreateFromTensorDesc (const HiAI_SingleOpTensorDesc * desc)
```

**描述**

根据[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)创建[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象。

本方法使用[HMS_HiAISingleOpTensorDesc_GetByteSize](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_getbytesize)计算Tensor数据的字节数， 并使用[HMS_HiAISingleOpBuffer_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleopbuffer_create)为Tensor数据分配ION内存。设备驱动将通过“零拷贝”的方式直接获取张量数据。

注意：该接口会将desc拷贝到[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)中。因此，当desc不再使用时，请使用[HMS_HiAISingleOpTensorDesc_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_destroy)销毁desc。

当不再使用[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象时，调用[HMS_HiAISingleOpTensor_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_destroy)销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象的指针，如果创建失败则返回空指针。

#### HMS_HiAISingleOpTensor_Destroy()

```ets
OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor ** tensor)
```

**描述**

释放[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象。

当不再使用[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象时，需要调用该接口销毁该对象，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向HiAI_SingleOpTensor对象的二级指针。tensor和 *tensor不能是空指针，否则返回错误码。 |

**返回：**

函数执行的结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。

#### HMS_HiAISingleOpTensor_GetBuffer()

```ets
HiAI_SingleOpBuffer* HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor * tensor)
```

**描述**

获取[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)的Buffer。

本方法用于获取指定[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象的[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向HiAI_SingleOpTensor对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hiai_singleopbuffer)对象的指针。

#### HMS_HiAISingleOpTensor_GetTensorDesc()

```ets
HiAI_SingleOpTensorDesc* HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor * tensor)
```

**描述**

获取[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)的Tensor描述。

本方法用于获取指定[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象的[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | 指向HiAI_SingleOpTensor对象的指针。该值不能为空指针，否则返回空指针。 |

**返回：**

指向[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的指针。

#### HMS_HiAISingleOpTensorDesc_Create()

```ets
HiAI_SingleOpTensorDesc* HMS_HiAISingleOpTensorDesc_Create (const int64_t * dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual)
```

**描述**

创建[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象。

本方法用于根据传入的维度、数据类型、排布格式等参数创建[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象。

可以调用以下接口，基于传入的[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)指针创建[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)对象： [HMS_HiAISingleOpTensor_CreateFromTensorDesc](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_createfromtensordesc)、[HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_createfromsingleopbuffer)、 [HMS_HiAISingleOpTensor_CreateFromConst](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensor_createfromconst)。

注意：这些接口会将[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象复制到[HiAI_SingleOpTensor](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensor)中。 当[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象不再使用时，调用[HMS_HiAISingleOpTensorDesc_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_destroy)接口销毁，否则会造成内存泄漏。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| dims | 张量维度列表。该值不能为空指针，否则返回空指针。 |
| dimNum | 张量维度数量。该值不能为0，否则返回空指针。 |
| dataType | 张量数据类型。 |
| format | 张量排布格式。 |
| isVirtual | 表示张量是否是虚拟张量。true表示该张量为虚拟张量，false表示该张量为非虚拟张量。虚拟张量是相连的CANN Kit单算子之间的中间张量，其中的数据仅暂时存在，不经非CANN Kit单算子内存读取或写入。例如， 若CANN Kit单算子A的输出张量T1仅作为CANN Kit单算子B的输入张量，且用户只读取单算子B的输出张量T2，不会读取或写入T1，那么T1需要被设置为虚拟张量，而T2则是非虚拟张量。 |

**返回：**

指向[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的指针，如果创建失败，则返回空指针。

#### HMS_HiAISingleOpTensorDesc_Destroy()

```ets
void HMS_HiAISingleOpTensorDesc_Destroy (HiAI_SingleOpTensorDesc ** tensorDesc)
```

**描述**

释放[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象。

本方法用于释放调用[HMS_HiAISingleOpTensorDesc_Create](#ZH-CN_TOPIC_0000002553362477__hms_hiaisingleoptensordesc_create)创建的[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的二级指针。 tensorDesc和 *tensorDesc不能为空指针。 |

#### HMS_HiAISingleOpTensorDesc_GetByteSize()

```ets
size_t HMS_HiAISingleOpTensorDesc_GetByteSize (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询基于[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)的维度和数据类型计算的数据占用字节数。

本方法用于获取基于[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)的维度和数据类型计算得到的数据占用字节数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

张量的数据字节数。

#### HMS_HiAISingleOpTensorDesc_GetDataType()

```ets
HiAI_SingleOpDataType HMS_HiAISingleOpTensorDesc_GetDataType (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)的数据类型。

本方法用于获取指定[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的数据类型。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回HIAI_SINGLEOP_DT_UNDEFINED。 |

**返回：**

张量的数据类型。

#### HMS_HiAISingleOpTensorDesc_GetDimension()

```ets
int64_t HMS_HiAISingleOpTensorDesc_GetDimension (const HiAI_SingleOpTensorDesc * tensorDesc, size_t index)
```

**描述**

查询[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)指定索引的维度长度。

本方法用于获取指定[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的某个维度的长度。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |
| index | 维度的索引值。索引从0开始。 |

**返回：**

张量的索引为**index**的维度的长度，如果执行失败，则返回0。

#### HMS_HiAISingleOpTensorDesc_GetDimensionCount()

```ets
size_t HMS_HiAISingleOpTensorDesc_GetDimensionCount (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)的维度数量。

本方法用于获取指定[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的维度数量。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回0。 |

**返回：**

张量的维度数量，如果执行失败，则返回0。

#### HMS_HiAISingleOpTensorDesc_GetFormat()

```ets
HiAI_SingleOpFormat HMS_HiAISingleOpTensorDesc_GetFormat (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)的排布格式。

本方法用于获取指定[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)对象的排布格式。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回HIAI_SINGLEOP_FORMAT_RESERVED。 |

**返回：**

张量的排布格式。

#### HMS_HiAISingleOpTensorDesc_IsVirtual()

```ets
bool HMS_HiAISingleOpTensorDesc_IsVirtual (const HiAI_SingleOpTensorDesc * tensorDesc)
```

**描述**

查询[HiAI_SingleOpTensorDesc](#ZH-CN_TOPIC_0000002553362477__hiai_singleoptensordesc)是否为虚拟张量。

虚拟张量是相连的CANN Kit单算子之间的中间张量，其中的数据仅暂时存在，不经非CANN Kit单算子内存读取或写入。例如，若CANN Kit单算子A的输出张量T1仅作为CANN Kit单算子B的输入张量，且用户只读取单算子B的输出张量T2，不会读取或写入T1， 那么T1需要被设置为虚拟张量，而T2则是非虚拟张量。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensorDesc | 指向[HiAI_SingleOpTensorDesc](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象的指针。该值不能为空指针，否则返回false。 |

**返回：**

如果张量是虚拟张量，则返回true，否则返回false。

#### HMS_HiAITensor_GetSizeWithImageFormat()

```ets
size_t HMS_HiAITensor_GetSizeWithImageFormat (NN_TensorDesc * desc, HiAI_ImageFormat format)
```

**描述**

根据NN_TensorDesc和HiAI_ImageFormat计算申请tensor的大小。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| desc | NN_TensorDesc指针实例，非空，否则返回0。 |
| format | 图像的格式HiAI_[Image](../../types/interfaces/Image.md#ZH-CN_TOPIC_0000002497444922__image-1)Format。 |

**返回：**

成功时返回计算后需要申请的tensor的大小，失败返回0。

#### HMS_HiAITensor_SetAippParams()

```ets
OH_NN_ReturnCode HMS_HiAITensor_SetAippParams (NN_Tensor * tensor, HiAI_AippParam * aippParams[], size_t aippNum)
```

**描述**

给NN_Tensor设置AippParams。

AIPP参数设置给NN_Tensor后，其内存在tensor使用完成后，调用[HMS_HiAIAippParam_Destroy](#ZH-CN_TOPIC_0000002553362477__hms_hiaiaippparam_destroy)释放。

**起始版本：** 4.1.0(11)

**参数:**

| 名称 | 描述 |
| --- | --- |
| tensor | NN_Tensor指针实例，非空，否则返回空指针。 |
| aippParams[] | AIPP参数数组。 |
| aippNum | AIPP参数数量。 |

**返回：**

函数执行结果状态。执行成功返回OH_NN_SUCCESS；失败返回具体错误码，具体失败错误码可参考[OH_NN_ReturnCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h#oh_nn_returncode)。
