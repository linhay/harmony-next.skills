# hiai_options.h

#### 概述

选项参数的接口。

支持设置动态shape、变更模型shape、设置数据排列格式、算子融合策略、量化配置、算子级调优、模型级调优、辅助调优、带宽模式等参数配置。

**库：** libhiai_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：**[CANN](../../topics/misc/CANN.md)

#### 汇总

#### 枚举

名称

描述

[HiAI_FormatMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_formatmode) {

HIAI_FORMAT_MODE_NCHW = 0,

HIAI_FORMAT_MODE_ORIGIN = 1

}

模型编译时数据的排列格式。

[HiAI_DynamicShapeStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapestatus) {

HIAI_DYNAMIC_SHAPE_DISABLED = 0,

HIAI_DYNAMIC_SHAPE_ENABLED = 1

}

是否使能编译前可变shape。

[HiAI_DynamicShapeCacheMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapecachemode) {

HIAI_DYNAMIC_SHAPE_CACHE_BUILT_MODEL = 0,

HIAI_DYNAMIC_SHAPE_CACHE_LOADED_MODEL = 1

}

编译前可变shape支持的模式。

[HiAI_ExecuteDevice](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_executedevice) {

HIAI_EXECUTE_DEVICE_NPU = 0,

HIAI_EXECUTE_DEVICE_CPU = 1,

HIAI_EXECUTE_DEVICE_GPU = 2

}

模型运行时支持的设备类型。

[HiAI_FallbackMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_fallbackmode) {

HIAI_FALLBACK_ENABLED = 0,

HIAI_FALLBACK_DISABLED = 1

}

指定的硬件设备无法编译模型时，是否允许CANN Kit选择其他硬件设备，例如CPU。

[HiAI_DeviceMemoryReusePlan](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_devicememoryreuseplan) {

HIAI_DEVICE_MEMORY_REUSE_PLAN_UNSET = 0,

HIAI_DEVICE_MEMORY_REUSE_PLAN_LOW = 1,

HIAI_DEVICE_MEMORY_REUSE_PLAN_HIGH = 2

}

设备内存复用配置选项。

[HiAI_TuningStrategy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningstrategy) {

HIAI_TUNING_STRATEGY_OFF = 0,

HIAI_TUNING_STRATEGY_ON_DEVICE_TUNING = 1,

HIAI_TUNING_STRATEGY_ON_DEVICE_PREPROCESS_TUNING = 2,

HIAI_TUNING_STRATEGY_ON_CLOUD_TUNING = 3

}

模型优化策略配置选项。

[HiAI_TuningMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningmode) {

HIAI_TUNING_MODE_UNSET = 0,

HIAI_TUNING_MODE_AUTO = 1,

HIAI_TUNING_MODE_HETER = 2

}

辅助调优模式。

[HiAI_BandMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_bandmode) {

HIAI_BANDMODE_UNSET = 0,

HIAI_BANDMODE_LOW = 1,

HIAI_BANDMODE_NORMAL = 2,

HIAI_BANDMODE_HIGH = 3

}

定义硬件之间带宽模式。

[HiAI_OmType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_omtype) {

HIAI_OM_TYPE_OFF = 0,

HIAI_OM_TYPE_PROFILING = 1,

HIAI_OM_TYPE_DUMP = 2

}

维测类型定义。

#### 函数

名称

描述

OH_NN_ReturnCode [HMS_HiAIOptions_SetInputTensorShapes](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setinputtensorshapes) (OH_NNCompilation *compilation, NN_TensorDesc *inputTensorDescs[], size_t shapeCount)

编译时更新模型输入shape。

size_t [HMS_HiAIOptions_GetInputTensorShapeSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getinputtensorshapesize) (const OH_NNCompilation *compilation)

查询选项参数中shape描述的个数。

NN_TensorDesc * [HMS_HiAIOptions_GetInputTensorShape](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getinputtensorshape) (const OH_NNCompilation *compilation, size_t index)

查询选项参数中指定索引的shape描述。

OH_NN_ReturnCode [HMS_HiAIOptions_SetFormatMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setformatmode) (OH_NNCompilation *compilation, [HiAI_FormatMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_formatmode) formatMode)

设置模型编译时的数据排列格式。

[HiAI_FormatMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_formatmode)[HMS_HiAIOptions_GetFormatMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getformatmode) (const OH_NNCompilation *compilation)

查询模型编译参数中的数据排列格式。

OH_NN_ReturnCode [HMS_HiAIOptions_SetDynamicShapeStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setdynamicshapestatus) (OH_NNCompilation *compilation, [HiAI_DynamicShapeStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapestatus) status)

设置编译前可变shape配置中的EnableMode参数。

OH_NN_ReturnCode [HMS_HiAIOptions_SetDynamicShapeMaxCache](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setdynamicshapemaxcache) (OH_NNCompilation *compilation, size_t maxCacheCount)

设置编译前可变shape配置中的最大缓存编译后模型数量。

OH_NN_ReturnCode [HMS_HiAIOptions_SetDynamicShapeCacheMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setdynamicshapecachemode) (OH_NNCompilation *compilation, [HiAI_DynamicShapeCacheMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapecachemode) mode)

设置编译前可变shape配置中的缓存模式参数。

[HiAI_DynamicShapeStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapestatus)[HMS_HiAIOptions_GetDynamicShapeStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getdynamicshapestatus) (const OH_NNCompilation *compilation)

查询编译前可变shape配置中的状态参数。

size_t [HMS_HiAIOptions_GetDynamicShapeMaxCache](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getdynamicshapemaxcache) (const OH_NNCompilation *compilation)

查询编译前可变shape配置中的最大缓存数量。

[HiAI_DynamicShapeCacheMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_dynamicshapecachemode)[HMS_HiAIOptions_GetDynamicShapeCacheMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getdynamicshapecachemode) (const OH_NNCompilation *compilation)

查询编译前可变shape配置中的cacheMode参数。

OH_NN_ReturnCode [HMS_HiAIOptions_SetOperatorDeviceOrder](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setoperatordeviceorder) (OH_NNCompilation *compilation, const char *operatorName, [HiAI_ExecuteDevice](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_executedevice) *executeDevices, size_t deviceCount)

设置算子级调优配置中算子执行设备列表。

size_t [HMS_HiAIOptions_GetOperatorDeviceCount](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getoperatordevicecount) (const OH_NNCompilation *compilation, const char *operatorName)

查询算子级调优配置中指定算子的执行设备个数。

[HiAI_ExecuteDevice](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_executedevice) * [HMS_HiAIOptions_GetOperatorDeviceOrder](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getoperatordeviceorder) (const OH_NNCompilation *compilation, const char *operatorName)

查询算子级调优配置中指定算子的执行设备列表。

OH_NN_ReturnCode [HMS_HiAIOptions_SetModelDeviceOrder](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setmodeldeviceorder) (OH_NNCompilation *compilation, [HiAI_ExecuteDevice](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_executedevice) *executeDevices, size_t deviceCount)

设置模型级调优配置中模型执行设备列表。

size_t [HMS_HiAIOptions_GetModelDeviceCount](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getmodeldevicecount) (const OH_NNCompilation *compilation)

查询模型级调优配置中模型的执行设备个数。

[HiAI_ExecuteDevice](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_executedevice) * [HMS_HiAIOptions_GetModelDeviceOrder](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getmodeldeviceorder) (const OH_NNCompilation *compilation)

查询模型级调优配置中模型的执行设备列表。

OH_NN_ReturnCode [HMS_HiAIOptions_SetFallbackMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setfallbackmode) (OH_NNCompilation *compilation, [HiAI_FallbackMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_fallbackmode) fallbackMode)

设置调优配置中的回滚模式。

[HiAI_FallbackMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_fallbackmode)[HMS_HiAIOptions_GetFallbackMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getfallbackmode) (const OH_NNCompilation *compilation)

查询调优配置中的回滚模式。

OH_NN_ReturnCode [HMS_HiAIOptions_SetDeviceMemoryReusePlan](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setdevicememoryreuseplan) (OH_NNCompilation *compilation, [HiAI_DeviceMemoryReusePlan](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_devicememoryreuseplan) deviceMemoryReusePlan)

设置调优配置中的设备内存复用参数。

[HiAI_DeviceMemoryReusePlan](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_devicememoryreuseplan)[HMS_HiAIOptions_GetDeviceMemoryReusePlan](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getdevicememoryreuseplan) (const OH_NNCompilation *compilation)

查询调优配置中的设备内存复用参数。

OH_NN_ReturnCode [HMS_HiAIOptions_SetTuningStrategy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_settuningstrategy) (OH_NNCompilation *compilation, [HiAI_TuningStrategy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningstrategy) tuningStrategy)

设置模型编译时的模型优化策略。

[HiAI_TuningStrategy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningstrategy)[HMS_HiAIOptions_GetTuningStrategy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_gettuningstrategy) (const OH_NNCompilation *compilation)

查询模型优化策略。

OH_NN_ReturnCode [HMS_HiAIOptions_SetQuantConfig](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setquantconfig) (OH_NNCompilation *compilation, void *data, size_t size)

设置模型编译时量化配置。

void * [HMS_HiAIOptions_GetQuantConfigData](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getquantconfigdata) (const OH_NNCompilation *compilation)

查询量化配置的数据地址。

size_t [HMS_HiAIOptions_GetQuantConfigSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getquantconfigsize) (const OH_NNCompilation *compilation)

查询量化配置的数据大小。

OH_NN_ReturnCode [HMS_HiAIOptions_SetTuningMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_settuningmode) (OH_NNCompilation *compilation, [HiAI_TuningMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningmode) tuningMode)

选择辅助调优模式。

OH_NN_ReturnCode [HMS_HiAIOptions_SetTuningCacheDir](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_settuningcachedir) (OH_NNCompilation *compilation, const char *cacheDir)

设置辅助调优的缓存目录。

[HiAI_TuningMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_tuningmode)[HMS_HiAIOptions_GetTuningMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_gettuningmode) (const OH_NNCompilation *compilation)

查询辅助调优模式。

const char * [HMS_HiAIOptions_GetTuningCacheDir](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_gettuningcachedir) (const OH_NNCompilation *compilation)

查询辅助调优的缓存目录。

OH_NN_ReturnCode [HMS_HiAIOptions_SetBandMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setbandmode) (OH_NNCompilation *compilation, [HiAI_BandMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_bandmode) bandMode)

设置NPU与周边硬件IO资源的带宽模式。

[HiAI_BandMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_bandmode)[HMS_HiAIOptions_GetBandMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_getbandmode) (const OH_NNCompilation *compilation)

查询带宽模式。

OH_NN_ReturnCode [HMS_HiAIOptions_SetOmOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaioptions_setomoptions)(OH_NNCompilation *compilation, [HiAI_OmType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_omtype) type, const char *outputDir)

设置模型加载时的维测选项信息。