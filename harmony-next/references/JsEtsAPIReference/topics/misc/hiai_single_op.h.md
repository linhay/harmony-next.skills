# hiai_single_op.h

**概述**

定义CANN Kit单算子接口，用于单算子的创建、计算以及Tensor和Buffer的管理。

引用文件： <CANNKit/hiai_single_op.h>

库： libhiai_foundation.so

系统能力： SystemCapability.AI.HiAIFoundation

起始版本： 5.0.0(12)

相关模块： [CANN](CANN.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct HiAISingleOpDescriptor_ConvolutionParam | HMS_HiAISingleOpDescriptor_CreateConvolution输入参数。 |
| struct HiAI_SingleOpExecutorConvolutionParam | HMS_HiAISingleOpExecutor_CreateConvolution输入参数。 |
| struct HiAI_SingleOpExecutorFusedConvolutionActivationParam | HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation输入参数。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct HiAI_SingleOpTensorDesc HiAI_SingleOpTensorDesc | 单算子Tensor描述的句柄。 |
| typedef struct HiAI_SingleOpBuffer HiAI_SingleOpBuffer | 单算子Buffer句柄。 |
| typedef struct HiAI_SingleOpTensor HiAI_SingleOpTensor | 单算子Tensor句柄。 |
| typedef struct HiAI_SingleOpOptions HiAI_SingleOpOptions | 单算子选项句柄。 |
| typedef struct HiAI_SingleOpDescriptor HiAI_SingleOpDescriptor | 单算子的算子描述句柄。 |
| typedef struct HiAISingleOpDescriptor_ConvolutionParam | HMS_HiAISingleOpDescriptor_CreateConvolution输入参数。 |
| typedef struct HiAI_SingleOpExecutorConvolutionParam | HMS_HiAISingleOpExecutor_CreateConvolution输入参数。 |
| typedef struct HiAI_SingleOpExecutorFusedConvolutionActivationParam | HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation输入参数。 |
| typedef struct HiAI_SingleOpExecutor HiAI_SingleOpExecutor | 单算子执行器句柄。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpDataType { HIAI_SINGLEOP_DT_FLOAT = 0, HIAI_SINGLEOP_DT_FLOAT16 = 1, HIAI_SINGLEOP_DT_UNDEFINED = 17 } | 单算子张量数据类型枚举。 |
| HiAI_SingleOpFormat { HIAI_SINGLEOP_FORMAT_NCHW = 0, HIAI_SINGLEOP_FORMAT_NHWC = 1, HIAI_SINGLEOP_FORMAT_ND = 2, HIAI_SINGLEOP_FORMAT_NC1HWC0 = 3, HIAI_SINGLEOP_FORMAT_NC4HW4 = 28, HIAI_SINGLEOP_FORMAT_NC8HW8 = 31, HIAI_SINGLEOP_FORMAT_RESERVED = 255 } | 单算子张量排布格式枚举。 |
| HiAI_SingleOpConvMode { HIAI_SINGLEOP_CONV_MODE_COMMON = 0, HIAI_SINGLEOP_CONV_MODE_TRANSPOSED = 1, HIAI_SINGLEOP_CONV_MODE_DEPTHWISE = 2 } | 单算子卷积模式枚举。 |
| HiAI_SingleOpPadMode { HIAI_SINGLEOP_PAD_MODE_SPECIFIC = 0, HIAI_SINGLEOP_PAD_MODE_SAME = 1, HIAI_SINGLEOP_PAD_MODE_SAME_UPPER = 2, HIAI_SINGLEOP_PAD_MODE_SAME_LOWER = 3, HIAI_SINGLEOP_PAD_MODE_VALID = 4 } | 单算子填充模式枚举。 |
| HiAI_SingleOpActivationType { HIAI_SINGLEOP_ACTIVATION_TYPE_RELU = 0, HIAI_SINGLEOP_ACTIVATION_TYPE_RELU6 = 1 } | 单算子激活模式枚举。 |
| HiAI_SingleOpSupportStatus { HIAI_SINGLEOP_OPTIMIZED = 0, HIAI_SINGLEOP_COMMON = 1, HIAI_SINGLEOP_UNSUPPORTED = 2 } | 单算子支持状态枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensorDesc_Create (const int64_t *dims, size_t dimNum, HiAI_SingleOpDataType dataType, HiAI_SingleOpFormat format, bool isVirtual) | 创建HiAI_SingleOpTensorDesc对象。 |
| size_t HMS_HiAISingleOpTensorDesc_GetDimensionCount (const HiAI_SingleOpTensorDesc *tensorDesc) | 查询HiAI_SingleOpTensorDesc的维度数量。 |
| int64_t HMS_HiAISingleOpTensorDesc_GetDimension (const HiAI_SingleOpTensorDesc *tensorDesc, size_t index) | 查询HiAI_SingleOpTensorDesc指定索引的维度长度。 |
| HiAI_SingleOpDataType HMS_HiAISingleOpTensorDesc_GetDataType (const HiAI_SingleOpTensorDesc *tensorDesc) | 查询HiAI_SingleOpTensorDesc的数据类型。 |
| HiAI_SingleOpFormat HMS_HiAISingleOpTensorDesc_GetFormat (const HiAI_SingleOpTensorDesc *tensorDesc) | 查询HiAI_SingleOpTensorDesc的排布格式。 |
| bool HMS_HiAISingleOpTensorDesc_IsVirtual (const HiAI_SingleOpTensorDesc *tensorDesc) | 查询HiAI_SingleOpTensorDesc是否为虚拟张量。 |
| size_t HMS_HiAISingleOpTensorDesc_GetByteSize (const HiAI_SingleOpTensorDesc *tensorDesc) | 查询基于HiAI_SingleOpTensorDesc的维度和数据类型计算的数据占用字节数。 |
| void HMS_HiAISingleOpTensorDesc_Destroy (HiAI_SingleOpTensorDesc **tensorDesc) | 释放HiAI_SingleOpTensorDesc对象。 |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpBuffer_Create (size_t dataSize) | 按照指定的内存大小创建HiAI_SingleOpBuffer对象。 |
| size_t HMS_HiAISingleOpBuffer_GetSize (const HiAI_SingleOpBuffer *buffer) | 查询HiAI_SingleOpBuffer的字节大小。 |
| void * HMS_HiAISingleOpBuffer_GetData (const HiAI_SingleOpBuffer *buffer) | 查询HiAI_SingleOpBuffer的内存地址。 |
| OH_NN_ReturnCode HMS_HiAISingleOpBuffer_Destroy (HiAI_SingleOpBuffer **buffer) | 释放HiAI_SingleOpBuffer对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromTensorDesc (const HiAI_SingleOpTensorDesc *desc) | 根据HiAI_SingleOpTensorDesc创建HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromSingleOpBuffer (const HiAI_SingleOpTensorDesc *desc, void *data, size_t dataSize) | 根据HiAI_SingleOpTensorDesc、HiAI_SingleOpBuffer的内存地址和数据大小创建HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpTensor * HMS_HiAISingleOpTensor_CreateFromConst (const HiAI_SingleOpTensorDesc *desc, void *data, size_t dataSize) | 根据HiAI_SingleOpTensorDesc、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpTensorDesc * HMS_HiAISingleOpTensor_GetTensorDesc (const HiAI_SingleOpTensor *tensor) | 获取HiAI_SingleOpTensor的Tensor描述。 |
| HiAI_SingleOpBuffer * HMS_HiAISingleOpTensor_GetBuffer (const HiAI_SingleOpTensor *tensor) | 获取HiAI_SingleOpTensor的Buffer。 |
| OH_NN_ReturnCode HMS_HiAISingleOpTensor_Destroy (HiAI_SingleOpTensor **tensor) | 释放HiAI_SingleOpTensor对象。 |
| HiAI_SingleOpOptions * HMS_HiAISingleOpOptions_Create (void) | 创建HiAI_SingleOpOptions对象。 |
| void HMS_HiAISingleOpOptions_Destroy (HiAI_SingleOpOptions **options) | 释放HiAI_SingleOpOptions对象。 |
| HiAI_SingleOpDescriptor * HMS_HiAISingleOpDescriptor_CreateConvolution (HiAISingleOpDescriptor_ConvolutionParam param) | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。 |
| HiAI_SingleOpDescriptor * HMS_HiAISingleOpDescriptor_CreateActivation (HiAI_SingleOpActivationType activationType, float coef) | 创建激活函数类的描述符对象。 |
| void HMS_HiAISingleOpDescriptor_Destroy (HiAI_SingleOpDescriptor **opDesc) | 释放HiAI_SingleOpDescriptor对象。 |
| HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckConvolution (HiAI_SingleOpExecutorConvolutionParam param) | 预查询卷积算子的支持状态。 |
| HiAI_SingleOpSupportStatus HMS_HiAISingleOpExecutor_PreCheckFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param) | 预查询卷积和激活融合算子的支持状态。 |
| HiAI_SingleOpExecutor * HMS_HiAISingleOpExecutor_CreateConvolution (HiAI_SingleOpExecutorConvolutionParam param) | 创建卷积类算子对应的HiAI_SingleOpExecutor对象。 |
| HiAI_SingleOpExecutor * HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation (HiAI_SingleOpExecutorFusedConvolutionActivationParam param) | 创建卷积和激活融合算子对应的HiAI_SingleOpExecutor对象。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc (const HiAI_SingleOpExecutor *executor, uint32_t index, HiAI_SingleOpTensorDesc *output) | 更新HiAI_SingleOpExecutor的输出tensor描述。 |
| size_t HMS_HiAISingleOpExecutor_GetWorkspaceSize (const HiAI_SingleOpExecutor *executor) | 查询HiAI_SingleOpExecutor所需的ION内存工作空间的字节大小。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Init (HiAI_SingleOpExecutor *executor, void *workspace, size_t workspaceSize) | 加载HiAI_SingleOpExecutor。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Execute (HiAI_SingleOpExecutor *executor, HiAI_SingleOpTensor *input[], int32_t inputNum, HiAI_SingleOpTensor *output[], int32_t outputNum) | 执行同步运算推理。 |
| OH_NN_ReturnCode HMS_HiAISingleOpExecutor_Destroy (HiAI_SingleOpExecutor **executor) | 销毁HiAI_SingleOpExecutor对象，释放执行器占用的内存。 |