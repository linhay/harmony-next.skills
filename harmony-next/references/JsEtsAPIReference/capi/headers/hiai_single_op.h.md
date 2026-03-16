# hiai_single_op.h

#### 概述

定义CANN Kit单算子接口，用于单算子的创建、计算以及Tensor和Buffer的管理。

**库：** libhiai_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 5.0.0(12)

**相关模块：**[CANN](../../topics/misc/CANN.md)

#### 汇总

#### 结构体

名称

描述

struct [HiAISingleOpDescriptor_ConvolutionParam](../../topics/media/HiAISingleOpDescriptor_ConvolutionParam.md)

[HMS_HiAISingleOpDescriptor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_createconvolution)输入参数。

struct [HiAI_SingleOpExecutorConvolutionParam](../../topics/media/HiAI_SingleOpExecutorConvolutionParam.md)

[HMS_HiAISingleOpExecutor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createconvolution)输入参数。

struct [HiAI_SingleOpExecutorFusedConvolutionActivationParam](../../topics/media/HiAI_SingleOpExecutorFusedConvolutionActivationParam.md)

[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

#### 类型定义

名称

描述

typedef struct [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)

单算子Tensor描述的句柄。

typedef struct [HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)

单算子Buffer句柄。

typedef struct [HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)

单算子Tensor句柄。

typedef struct [HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)[HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)

单算子选项句柄。

typedef struct [HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)[HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)

单算子的算子描述句柄。

typedef struct [HiAISingleOpDescriptor_ConvolutionParam](../../topics/media/HiAISingleOpDescriptor_ConvolutionParam.md)

[HMS_HiAISingleOpDescriptor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_createconvolution)输入参数。

typedef struct [HiAI_SingleOpExecutorConvolutionParam](../../topics/media/HiAI_SingleOpExecutorConvolutionParam.md)

[HMS_HiAISingleOpExecutor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createconvolution)输入参数。

typedef struct [HiAI_SingleOpExecutorFusedConvolutionActivationParam](../../topics/media/HiAI_SingleOpExecutorFusedConvolutionActivationParam.md)

[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

typedef struct [HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)

单算子执行器句柄。

#### 枚举

名称

描述

[HiAI_SingleOpDataType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdatatype) {

HIAI_SINGLEOP_DT_FLOAT = 0,

HIAI_SINGLEOP_DT_FLOAT16 = 1,

HIAI_SINGLEOP_DT_UNDEFINED = 17

}

单算子张量数据类型枚举。

[HiAI_SingleOpFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopformat) {

HIAI_SINGLEOP_FORMAT_NCHW = 0,

HIAI_SINGLEOP_FORMAT_NHWC = 1,

HIAI_SINGLEOP_FORMAT_ND = 2,

HIAI_SINGLEOP_FORMAT_NC1HWC0 = 3,

HIAI_SINGLEOP_FORMAT_NC4HW4 = 28,

HIAI_SINGLEOP_FORMAT_NC8HW8 = 31,

HIAI_SINGLEOP_FORMAT_RESERVED = 255

}

单算子张量排布格式枚举。

[HiAI_SingleOpConvMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopconvmode) {

HIAI_SINGLEOP_CONV_MODE_COMMON = 0,

HIAI_SINGLEOP_CONV_MODE_TRANSPOSED = 1,

HIAI_SINGLEOP_CONV_MODE_DEPTHWISE = 2

}

单算子卷积模式枚举。

[HiAI_SingleOpPadMode](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoppadmode) {

HIAI_SINGLEOP_PAD_MODE_SPECIFIC = 0,

HIAI_SINGLEOP_PAD_MODE_SAME = 1,

HIAI_SINGLEOP_PAD_MODE_SAME_UPPER = 2,

HIAI_SINGLEOP_PAD_MODE_SAME_LOWER = 3,

HIAI_SINGLEOP_PAD_MODE_VALID = 4

}

单算子填充模式枚举。

[HiAI_SingleOpActivationType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopactivationtype) {

HIAI_SINGLEOP_ACTIVATION_TYPE_RELU = 0,

HIAI_SINGLEOP_ACTIVATION_TYPE_RELU6 = 1

}

单算子激活模式枚举。

[HiAI_SingleOpSupportStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopsupportstatus) {

HIAI_SINGLEOP_OPTIMIZED = 0,

HIAI_SINGLEOP_COMMON = 1,

HIAI_SINGLEOP_UNSUPPORTED = 2

}

单算子支持状态枚举。

#### 函数

名称

描述

[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * [HMS_HiAISingleOpTensorDesc_Create](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_create) (const int64_t *dims, size_t dimNum, [HiAI_SingleOpDataType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdatatype) dataType, [HiAI_SingleOpFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopformat) format, bool isVirtual)

创建[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象。

size_t [HMS_HiAISingleOpTensorDesc_GetDimensionCount](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_getdimensioncount) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc)

查询[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)的维度数量。

int64_t [HMS_HiAISingleOpTensorDesc_GetDimension](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_getdimension) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc, size_t index)

查询[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)指定索引的维度长度。

[HiAI_SingleOpDataType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdatatype)[HMS_HiAISingleOpTensorDesc_GetDataType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_getdatatype) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc)

查询[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)的数据类型。

[HiAI_SingleOpFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopformat)[HMS_HiAISingleOpTensorDesc_GetFormat](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_getformat) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc)

查询[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)的排布格式。

bool [HMS_HiAISingleOpTensorDesc_IsVirtual](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_isvirtual) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc)

查询[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)是否为虚拟张量。

size_t [HMS_HiAISingleOpTensorDesc_GetByteSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_getbytesize) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *tensorDesc)

查询基于[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)的维度和数据类型计算的数据占用字节数。

void [HMS_HiAISingleOpTensorDesc_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensordesc_destroy) ([HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) **tensorDesc)

释放[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)对象。

[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer) * [HMS_HiAISingleOpBuffer_Create](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopbuffer_create) (size_t dataSize)

按照指定的内存大小创建[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)对象。

size_t [HMS_HiAISingleOpBuffer_GetSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopbuffer_getsize) (const [HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer) *buffer)

查询[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)的字节大小。

void * [HMS_HiAISingleOpBuffer_GetData](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopbuffer_getdata) (const [HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer) *buffer)

查询[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)的内存地址。

OH_NN_ReturnCode [HMS_HiAISingleOpBuffer_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopbuffer_destroy) ([HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer) **buffer)

释放[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)对象。

[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) * [HMS_HiAISingleOpTensor_CreateFromTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_createfromtensordesc) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc)

根据[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)创建[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)对象。

[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) * [HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_createfromsingleopbuffer) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc, void *data, size_t dataSize)

根据[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)、[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer)的内存地址和数据大小创建[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)对象。

[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) * [HMS_HiAISingleOpTensor_CreateFromConst](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_createfromconst) (const [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *desc, void *data, size_t dataSize)

根据[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc)、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)对象。

[HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) * [HMS_HiAISingleOpTensor_GetTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_gettensordesc) (const [HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) *tensor)

获取[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)的Tensor描述。

[HiAI_SingleOpBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopbuffer) * [HMS_HiAISingleOpTensor_GetBuffer](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_getbuffer) (const [HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) *tensor)

获取[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)的Buffer。

OH_NN_ReturnCode [HMS_HiAISingleOpTensor_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleoptensor_destroy) ([HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) **tensor)

释放[HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor)对象。

[HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions) * [HMS_HiAISingleOpOptions_Create](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopoptions_create) (void)

创建[HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)对象。

void [HMS_HiAISingleOpOptions_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopoptions_destroy) ([HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions) **options)

释放[HiAI_SingleOpOptions](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopoptions)对象。

[HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor) * [HMS_HiAISingleOpDescriptor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_createconvolution) ([HiAISingleOpDescriptor_ConvolutionParam](../../topics/media/HiAISingleOpDescriptor_ConvolutionParam.md) param)

创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。

[HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor) * [HMS_HiAISingleOpDescriptor_CreateActivation](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_createactivation) ([HiAI_SingleOpActivationType](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopactivationtype) activationType, float coef)

创建激活函数类的描述符对象。

void [HMS_HiAISingleOpDescriptor_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopdescriptor_destroy) ([HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor) **opDesc)

释放[HiAI_SingleOpDescriptor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopdescriptor)对象。

[HiAI_SingleOpSupportStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopsupportstatus)[HMS_HiAISingleOpExecutor_PreCheckConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_precheckconvolution) ([HiAI_SingleOpExecutorConvolutionParam](../../topics/media/HiAI_SingleOpExecutorConvolutionParam.md) param)

预查询卷积算子的支持状态。

[HiAI_SingleOpSupportStatus](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopsupportstatus)[HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_precheckfusedconvolutionactivation) ([HiAI_SingleOpExecutorFusedConvolutionActivationParam](../../topics/media/HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) param)

预查询卷积和激活融合算子的支持状态。

[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) * [HMS_HiAISingleOpExecutor_CreateConvolution](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createconvolution) ([HiAI_SingleOpExecutorConvolutionParam](../../topics/media/HiAI_SingleOpExecutorConvolutionParam.md) param)

创建卷积类算子对应的[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)对象。

[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) * [HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_createfusedconvolutionactivation) ([HiAI_SingleOpExecutorFusedConvolutionActivationParam](../../topics/media/HiAI_SingleOpExecutorFusedConvolutionActivationParam.md) param)

创建卷积和激活融合算子对应的[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)对象。

OH_NN_ReturnCode [HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_updateoutputtensordesc) (const [HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) *executor, uint32_t index, [HiAI_SingleOpTensorDesc](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensordesc) *output)

更新[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)的输出tensor描述。

size_t [HMS_HiAISingleOpExecutor_GetWorkspaceSize](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_getworkspacesize) (const [HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) *executor)

查询[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)所需的ION内存工作空间的字节大小。

OH_NN_ReturnCode [HMS_HiAISingleOpExecutor_Init](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_init) ([HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) *executor, void *workspace, size_t workspaceSize)

加载[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)。

OH_NN_ReturnCode [HMS_HiAISingleOpExecutor_Execute](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_execute) ([HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) *executor, [HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) *input[], int32_t inputNum, [HiAI_SingleOpTensor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleoptensor) *output[], int32_t outputNum)

执行同步运算推理。

OH_NN_ReturnCode [HMS_HiAISingleOpExecutor_Destroy](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaisingleopexecutor_destroy) ([HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor) **executor)

销毁[HiAI_SingleOpExecutor](../../topics/misc/CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_singleopexecutor)对象，释放执行器占用的内存。