# neural_network_runtime_type.h

#### 概述

Neural Network Runtime定义的结构体和枚举值。

**引用文件：** <neural_network_runtime/neural_network_runtime_type.h>

**库：** libneural_network_runtime.so

**系统能力：** SystemCapability.AI.NeuralNetworkRuntime

**起始版本：** 9

**相关模块：**[NeuralNetworkRuntime](../../topics/system-services/NeuralNetworkRuntime.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NN_UInt32Array](../../topics/media/OH_NN_UInt32Array.md)OH_NN_UInt32Array该结构体用于存储32位无符号整型数组。[OH_NN_QuantParam](../../topics/media/OH_NN_QuantParam.md)OH_NN_QuantParam量化信息。[OH_NN_Tensor](../../topics/misc/OH_NN_Tensor.md)OH_NN_Tensor

张量结构体。

通常用于构造模型图中的数据节点和算子参数，在构造张量时需要明确数据类型、维数、维度信息和量化信息。

[OH_NN_Memory](../../topics/misc/OH_NN_Memory.md)OH_NN_Memory内存结构体。[OH_NNModel](../../topics/misc/OH_NNModel.md)OH_NNModel模型句柄。[OH_NNCompilation](../../topics/misc/OH_NNCompilation.md)OH_NNCompilation编译器句柄。[OH_NNExecutor](../../topics/misc/OH_NNExecutor.md)OH_NNExecutor执行器句柄。[NN_QuantParam](../../topics/media/NN_QuantParam.md)NN_QuantParam量化参数的句柄。[NN_TensorDesc](../../topics/misc/NN_TensorDesc.md)NN_TensorDescTensor描述的句柄。[NN_Tensor](../../topics/misc/NN_Tensor.md)NN_TensorTensor句柄。

#### 枚举

名称typedef关键字描述[OH_NN_PerformanceMode](#ZH-CN_TOPIC_0000002497606150__oh_nn_performancemode)OH_NN_PerformanceMode硬件的性能模式。[OH_NN_Priority](#ZH-CN_TOPIC_0000002497606150__oh_nn_priority)OH_NN_Priority模型推理任务优先级。[OH_NN_ReturnCode](#ZH-CN_TOPIC_0000002497606150__oh_nn_returncode)OH_NN_ReturnCodeNeural Network Runtime 定义的错误码类型。[OH_NN_FuseType](#ZH-CN_TOPIC_0000002497606150__oh_nn_fusetype)OH_NN_FuseTypeNeural Network Runtime 融合算子中激活函数的类型。[OH_NN_Format](#ZH-CN_TOPIC_0000002497606150__oh_nn_format)OH_NN_Format张量数据的排布类型。[OH_NN_DeviceType](#ZH-CN_TOPIC_0000002497606150__oh_nn_devicetype)OH_NN_DeviceTypeNeural Network Runtime 支持的设备类型。[OH_NN_DataType](#ZH-CN_TOPIC_0000002497606150__oh_nn_datatype)OH_NN_DataTypeNeural Network Runtime 支持的数据类型。[OH_NN_OperationType](#ZH-CN_TOPIC_0000002497606150__oh_nn_operationtype)OH_NN_OperationTypeNeural Network Runtime 支持算子的类型。[OH_NN_TensorType](#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)OH_NN_TensorType

张量的类型。

张量通常用于设置模型的输入、输出和算子参数。作为模型（或算子）的输入和输出时，需要将张量类型设置为[OH_NN_TENSOR](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)；当张量作为算子参数时，需要选择除[OH_NN_TENSOR](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)以外合适的枚举值，作为张量的类型。

假设正在设置[OH_NN_OPS_CONV2D](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_operationtype)算子的pad参数，则需要将[OH_NN_Tensor](../../topics/misc/OH_NN_Tensor.md)实例的type属性设置为[OH_NN_CONV2D_PAD](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)。其他算子参数的设置以此类推，枚举值的命名遵守 OH_NN_{算子名称}_{属性名} 的格式。

#### 函数

名称typedef关键字描述[typedef void (*NN_OnRunDone)(void *userData, OH_NN_ReturnCode errCode, void *outputTensor[], int32_t outputCount)](#ZH-CN_TOPIC_0000002497606150__nn_onrundone)NN_OnRunDone

异步推理结束后的回调处理函数句柄。

使用参数**userData**来查询希望获取的那次异步推理执行。**userData**与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**是一致的。使用参数**errCode**（[OH_NN_ReturnCode](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_returncode)类型）来获取该次异步推理的返回状态。

[typedef void (*NN_OnServiceDied)(void *userData)](#ZH-CN_TOPIC_0000002497606150__nn_onservicedied)NN_OnServiceDied

异步推理执行期间设备驱动服务异常终止时的回调处理函数句柄。

如果该回调函数被调用，您需要重新编译模型。

使用参数**userData**来查询希望获取的那次异步推理执行。**userData**与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**是一致的。

#### 枚举类型说明

#### OH_NN_PerformanceMode

```ets
enum OH_NN_PerformanceMode
```

**描述**

硬件的性能模式。

**起始版本：** 9

枚举项描述OH_NN_PERFORMANCE_NONE = 0无性能模式偏好。OH_NN_PERFORMANCE_LOW = 1低能耗模式。OH_NN_PERFORMANCE_MEDIUM = 2中性能模式。OH_NN_PERFORMANCE_HIGH = 3高性能模式。OH_NN_PERFORMANCE_EXTREME = 4极致性能模式。

#### OH_NN_Priority

```ets
enum OH_NN_Priority
```

**描述**

模型推理任务优先级。

**起始版本：** 9

枚举项描述OH_NN_PRIORITY_NONE = 0无优先级偏好。OH_NN_PRIORITY_LOW = 1低优先级。OH_NN_PRIORITY_MEDIUM = 2中优先级。OH_NN_PRIORITY_HIGH = 3高优先级。

#### OH_NN_ReturnCode

```ets
enum OH_NN_ReturnCode
```

**描述**

Neural Network Runtime 定义的错误码类型。

**起始版本：** 9

枚举项描述OH_NN_SUCCESS = 0操作成功。OH_NN_FAILED = 1操作失败。OH_NN_INVALID_PARAMETER = 2非法参数。OH_NN_MEMORY_ERROR = 3内存相关的错误，包括：内存不足、内存数据拷贝失败、内存申请失败等。OH_NN_OPERATION_FORBIDDEN = 4非法操作。OH_NN_NULL_PTR = 5空指针异常。OH_NN_INVALID_FILE = 6无效文件。OH_NN_UNAVALIDABLE_DEVICE = 7

硬件发生错误，错误可能包含：HDL服务崩溃。

**废弃版本：** 11

**替代接口：** OH_NN_UNAVAILABLE_DEVICE

OH_NN_INVALID_PATH = 8非法路径。OH_NN_TIMEOUT = 9

执行超时。

**起始版本：** 11

OH_NN_UNSUPPORTED = 10

未支持。

**起始版本：** 11

OH_NN_CONNECTION_EXCEPTION = 11

连接异常。

**起始版本：** 11

OH_NN_SAVE_CACHE_EXCEPTION = 12

保存cache异常。

**起始版本：** 11

OH_NN_DYNAMIC_SHAPE = 13

动态shape。

**起始版本：** 11

OH_NN_UNAVAILABLE_DEVICE = 14

硬件发生错误，错误可能包含：HDL服务崩溃。

**起始版本：** 11

#### OH_NN_FuseType

```ets
enum OH_NN_FuseType
```

**描述**

Neural Network Runtime 融合算子中激活函数的类型。

**起始版本：** 9

枚举项描述OH_NN_FUSED_NONE = 0未指定融合激活函数。OH_NN_FUSED_RELU = 1融合relu激活函数。OH_NN_FUSED_RELU6 = 2融合relu6激活函数。

#### OH_NN_Format

```ets
enum OH_NN_Format
```

**描述**

张量数据的排布类型。

**起始版本：** 9

枚举项描述OH_NN_FORMAT_NONE = 0当张量没有特定的排布类型时（如标量或矢量），使用本枚举值。OH_NN_FORMAT_NCHW = 1当张量按照NCHW的格式排布数据时，使用本枚举值。OH_NN_FORMAT_NHWC = 2当张量按照NHWC的格式排布数据时，使用本枚举值。OH_NN_FORMAT_ND = 3

当张量按照ND的格式排布数据时，使用本枚举值。

**起始版本：** 11

#### OH_NN_DeviceType

```ets
enum OH_NN_DeviceType
```

**描述**

Neural Network Runtime 支持的设备类型。

**起始版本：** 9

枚举项描述OH_NN_OTHERS = 0不属于CPU、GPU、专用加速器的设备。OH_NN_CPU = 1CPU设备。OH_NN_GPU = 2GPU设备。OH_NN_ACCELERATOR = 3专用硬件加速器。

#### OH_NN_DataType

```ets
enum OH_NN_DataType
```

**描述**

Neural Network Runtime 支持的数据类型。

**起始版本：** 9

枚举项描述OH_NN_UNKNOWN = 0张量数据类型未知。OH_NN_BOOL = 1张量数据类型为bool。OH_NN_INT8 = 2张量数据类型为int8。OH_NN_INT16 = 3张量数据类型为int16。OH_NN_INT32 = 4张量数据类型为int32。OH_NN_INT64 = 5张量数据类型为int64。OH_NN_UINT8 = 6张量数据类型为uint8。OH_NN_UINT16 = 7张量数据类型为uint16。OH_NN_UINT32 = 8张量数据类型为uint32。OH_NN_UINT64 = 9张量数据类型为uint64。OH_NN_FLOAT16 = 10张量数据类型为float16。OH_NN_FLOAT32 = 11张量数据类型为float32。OH_NN_FLOAT64 = 12张量数据类型为float64。

#### OH_NN_OperationType

```ets
enum OH_NN_OperationType
```

**描述**

Neural Network Runtime 支持算子的类型。

**起始版本：** 9

枚举项描述OH_NN_OPS_ADD = 1

返回两个输入张量对应元素相加的和的张量。

输入：

input1，第一个输入的张量，数据类型要求为布尔值或者数字。

input2，第二个输入的张量，数据类型和形状需要和第一个输入保持一致。

参数：

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，input1和input2的和，数据形状与输入broadcast之后一样，数据类型与较高精度的输入精度一致。

OH_NN_OPS_AVG_POOL = 2

在输入张量上应用2D平均池化，仅支持NHWC格式的张量。支持int8量化输入。

如果输入中含有padMode参数，输入：

input，一个张量。参数：

kernelSize，用来取平均值的kernel大小，是一个长度为2的int数组[kernelHeight，kernelWeight]，第一个数表示kernel高度，第二个数表示kernel宽度。

strides，kernel移动的距离，是一个长度为2的int数组[strideHeight，strideWeight]，第一个数表示高度上的移动步幅，第二个数表示宽度上的移动步幅。

padMode，填充模式，int类型的可选值，0表示same，1表示valid，并且以最近邻的值填充。

same，输出的高度和宽度与input相同，填充总数将在水平和垂直方向计算，并在可能的情况下均匀分布到顶部和底部、左侧和右侧。否则，最后一个额外的填充将从底部和右侧完成。

valid，输出的可能最大高度和宽度将在不填充的情况下返回。额外的像素将被丢弃。

roundMode，边界处理方式，int类型的可选值，当池化核不能完全覆盖输入特征图时，对输出特征图进行取整的方式，0表示向下取整，1表示向上取整。

global，bool值，是否对整个输入张量进行平均池化操作。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。如果输入中含有padList参数，输入：

input，一个张量。

参数：

kernelSize，用来取平均值的kernel大小，是一个长度为2的int数组[kernelHeight，kernelWeight]，第一个数表示kernel高度，第二个数表示kernel宽度。

strides，kernel移动的距离，是一个长度为2的int数组[strideHeight，strideWeight]，第一个数表示高度上的移动步幅，第二个数表示宽度上的移动步幅。

padList，input周围的填充，是一个长度为4的int数组[top，bottom，left，right]，并且以最近邻的值填充。

roundMode，边界处理方式，int类型的可选值，当池化核不能完全覆盖输入特征图时，对输出特征图进行取整的方式，0表示向下取整，1表示向上取整。

global，bool值，是否对整个输入张量进行平均池化操作。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，对input进行平均池化后的结果。

OH_NN_OPS_BATCH_NORM = 3

对输入张量做批量归一化，应用一种变换使平均输出保持接近0，输出标准差接近1。

输入：

input，一个n维的张量，要求形状为[N，...，C]，即第n维是通道数（channel）。

scale，缩放因子的1D张量，用于缩放归一化的第一个张量。

offset，用于偏移的1D张量，以移动到归一化的第一个张量。

mean，总体均值的一维张量，仅用于推理；对于训练，必须为空。

variance，用于总体方差的一维张量。仅用于推理；对于训练，必须为空。

参数：

epsilon，数值稳定性的小附加值。

输出：

output，n维输出张量，其形状和数据类型与input一致。

OH_NN_OPS_BATCH_TO_SPACE_ND = 4

将一个4维张量的batch维度按blockSize切分成小块，并将这些小块拼接到空间维度。

输入：

input，输入张量，维将被切分，拼接回空间维度。参数：

blockSize，一个长度为2的数组[heightBlock，weightBlock]，指定切分到空间维度上的block大小。

crops，一个shape为(2，2)的二维数组[[crop0Start，crop0End]，[crop1Start，crop1End]]，表示在output的空间维度上截掉部分元素。

输出：

output，假设input的形状为(n，h，w，c)，output的形状为（n'，h'，w'，c'）：

n' = n / (blockSize[0] * blockSize[1])

h' = h * blockSize[0] - crops[0][0] - crops[0][1]

w' = w * blockSize[1] - crops[1][0] - crops[1][1]

c'= c

OH_NN_OPS_BIAS_ADD = 5

对给出的输入张量上的各个维度方向上的数据进行偏置。

输入：

input，输入张量，可为2-5维度。

bias，参数对应输入维度数量的偏移值。

输出：

output，根据输入中每个维度方向偏移后的结果。

OH_NN_OPS_CAST = 6

对输入张量中的数据类型进行转换。

输入：

input，输入张量。

type，转换后的数据类型。

输出：

output，转换后的张量。

OH_NN_OPS_CONCAT = 7

在指定维度上连接张量。

输入：

input，N个输入张量。

参数：

axis，指定张量连接的维度。

输出：

output，输出N个张量沿axis连接的结果。

OH_NN_OPS_CONV2D = 8

二维卷积层。如果输入中含有padMode参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，inChannel/group]，inChannel必须要能整除group。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias参数不需要量化参数，其量化版本要求输入 OH_NN_INT32类型数据，实际量化参数由input和weight共同决定。

参数：

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]，值必须大于或等于1，并且不能超过input的height和width。

padMode，input的填充模式，支持same和valid，int类型，0表示same，1表示valid。

same，输出的高度和宽度与input相同，填充总数将在水平和垂直方向计算，并在可能的情况下均匀分布到顶部和底部、左侧和右侧。否则，最后一个额外的填充将从底部和右侧完成。

Valid，输出的可能最大高度和宽度将在不填充的情况下返回。额外的像素将被丢弃。

group，将input按inChannel分组，int类型。group等于1，这是常规卷积；group大于1且小于或等于inChannel，这是分组卷积。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。如果输入中含有padList参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，inChannel/group]，inChannel必须要能整除group。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias 参数不需要量化参数，其量化版本要求输入 OH_NN_INT32类型数据，实际量化参数由input和weight共同决定。

参数：

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]。值必须大于或等于1，并且不能超过input的height和width。

padList，input周围的填充，是一个长度为4的int数组[top，bottom，left，right]。

group，将input按inChannel分组，int类型。group等于1，这是常规卷积。group等于inChannel，这是depthwiseConv2d，此时group==inChannel==outChannel。group大于1且小于inChannel，这是分组卷积，outChannel==group。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。

输出：

output，卷积计算结果。

OH_NN_OPS_CONV2D_TRANSPOSE = 9

二维卷积转置。如果输入中含有padMode参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，inChannel/group]，inChannel必须要能整除group。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias 参数不需要量化参数，其量化版本要求输入 OH_NN_INT32 类型数据，实际量化参数由input和weight共同决定。

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

参数：

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]。值必须大于或等于1，并且不能超过input的height和width。

padMode，input的填充模式，支持same和valid，int类型，0表示same，1表示valid。

same，输出的高度和宽度与input相同，填充总数将在水平和垂直方向计算，并在可能的情况下均匀分布到顶部和底部、左侧和右侧。否则，最后一个额外的填充将从底部和右侧完成。

Valid，输出的可能最大高度和宽度将在不填充的情况下返回。额外的像素将被丢弃。

group，将input按inChannel分组，int类型。group等于1，这是常规卷积；group大于1且小于或等于inChannel，这是分组卷积。

outputPads，一个整数或元组/2 个整数的列表，指定沿输出张量的高度和宽度的填充量。可以是单个整数，用于为所有空间维度指定相同的值。沿给定维度的输出填充量必须小于沿同一维度的步幅。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。如果输入中含有padList参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，inChannel/group]，inChannel必须要能整除group。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias 参数不需要量化参数，其量化版本要求输入 OH_NN_INT32类型数据，实际量化参数由input和weight共同决定。

参数：

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]。值必须大于或等于1，并且不能超过input的height和width。

padList，input周围的填充，是一个长度为4的int数组[top，bottom，left，right]。

group，将input按inChannel分组，int类型。group等于1，这是常规卷积；group大于1且小于或等于inChannel，这是分组卷积。

outputPads，一个整数或元组/2 个整数的列表，指定沿输出张量的高度和宽度的填充量。可以是单个整数，用于为所有空间维度指定相同的值。沿给定维度的输出填充量必须小于沿同一维度的步幅。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，卷积转置后的计算结果。

OH_NN_OPS_DEPTHWISE_CONV2D_NATIVE = 10

二维深度可分离卷积。如果输入中含有padMode参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，1]，outChannel = channelMultiplier * inChannel。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias参数不需要量化参数，其量化版本要求输入 OH_NN_INT32类型数据，实际量化参数由input和weight共同决定。

参数：

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]。值必须大于或等于1，并且不能超过input的height和width。

padMode，input的填充模式，支持same和valid，int类型，0表示same，1表示valid。

same，输出的高度和宽度与input相同，填充总数将在水平和垂直方向计算，并在可能的情况下均匀分布到顶部和底部、左侧和右侧。否则，最后一个额外的填充将从底部和右侧完成。

Valid，输出的可能最大高度和宽度将在不填充的情况下返回。额外的像素将被丢弃。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。如果输入中含有padList 参数，输入：

input，输入张量。

weight，卷积的权重，要求weight排布为[outChannel，kernelHeight，kernelWidth，1]，outChannel = channelMultiplier * inChannel。

bias，卷积的偏置，是长度为[outChannel]的数组。在量化场景下，bias 参数不需要量化参数，其量化版本要求输入 OH_NN_INT32 类型数据，实际量化参数由input和weight共同决定。

参数：

stride，卷积核在height和weight上的步幅，是一个长度为2的int数组[strideHeight，strideWidth]。

dilation，表示扩张卷积在height和weight上的扩张率，是一个长度为2的int数组[dilationHeight，dilationWidth]。值必须大于或等于1，并且不能超过input的height和width。

padList，input周围的填充，是一个长度为4的int数组[top，bottom，left，right]。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。

输出：

output，卷积计算的结果。

OH_NN_OPS_DIV = 11

对输入的两个标量或张量做除法。

输入：

input1，第一个输入是标量或布尔值或数据类型为数字或布尔值的张量。* input2，数据类型根据input1的类型，要求有所不同：当第一个输入是张量时，第二个输入可以是实数或布尔值或数据类型为实数/布尔值的张量。当第一个输入是实数或布尔值时，第二个输入必须是数据类型为实数/布尔值的张量。参数：

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，input1和input2相除的结果。

OH_NN_OPS_ELTWISE = 12

设置参数对输入进行product(点乘)、sum(相加减)或max(取大值)。

输入：

input1，第一个输入张量。

input2，第二个输入张量。参数：

mode，枚举，选择操作方式。输出：

output，计算后的结果，output和input1拥有相同的数据类型和形状。

OH_NN_OPS_EXPAND_DIMS = 13

在给定维度上为张量添加一个额外的维度。

输入：

input，输入张量。

axis，需要添加的维度的index，int32_t类型，值必须在[-dim-1，dim]，且只允许常量值。

输出：

output，维度拓展后的张量。

OH_NN_OPS_FILL = 14

根据指定的维度，创建由一个标量填充的张量。

输入：

value，填充的标量。

shape，指定创建张量的形状。

输出：

output，生成的张量，和value具有相同的数据类型，张量形状由shape参数指定。

OH_NN_OPS_FULL_CONNECTION = 15

全连接，整个输入作为feature map，进行特征提取。

输入：

input，全连接的输入张量。

weight，全连接的权重张量。

bias，全连接的偏置，在量化场景下，bias 参数不需要量化参数，其量化版本要求输入OH_NN_INT32类型数据，实际量化参数由input和weight共同决定。

参数：

hasBias，bool值，是否使用bias偏置。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，输出运算后的张量。

如果输入中含有axis参数或useAxis参数，输入：

input，全连接的输入张量。

weight，全连接的权重张量。

bias，全连接的偏置，在量化场景下，bias 参数不需要量化参数，其量化版本要求输入 OH_NN_INT32 类型数据，实际量化参数由input和weight共同决定。

参数：

axis，默认0，input做全连接的轴，从指定轴axis开始，将axis和axis后面的轴展开成一维去做全连接。

useAxis，bool值，是否使用axis参数，默认false，如果用户设置axis参数，则useAxis自动调整为true；如果用户设置useAxis为true不指定axis，使用默认axis执行展开全连接，不支持用户同时设置useAxis为false并指定axis参数。

hasBias，bool值，是否使用bias偏置。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，输出运算后的张量。

OH_NN_OPS_GATHER = 16

根据指定的索引和轴返回输入张量的切片。

输入：

input，输入待切片的张量。

inputIndices，指定input在axis上的索引，是一个int类型的数组，值必须在[0,input.shape[axis])范围内。

axis，input被切片的轴，int32_t类型的数组，数组长度为1。

输出：

output，输出切片后的张量。

OH_NN_OPS_HSWISH = 17

计算输入的Hardswish激活值。

输入：

一个n维输入张量。

输出：

n维Hardswish激活值，数据类型和shape和input一致。

OH_NN_OPS_LESS_EQUAL = 18

对input1和input2，计算每对元素的input1[i]<=input2[i]的结果，i是输入张量中每个元素的索引。输入：

 input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。* input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数/OH_NN_BOOL。输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

OH_NN_OPS_MATMUL = 19

计算input1和input2的内积。

输入：

input1，n维输入张量。

input2，n维输入张量。

参数：

TransposeX，布尔值，是否对input1进行转置。

TransposeY，布尔值，是否对input2进行转置。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，计算得到内积，当type!=OH_NN_UNKNOWN时，output数据类型由type决定；当type==OH_NN_UNKNOWN时，output的数据类型取决于inputX和inputY进行计算时转化的数据类型。

OH_NN_OPS_MAXIMUM = 20

计算input1和input2对应元素最大值，input1和input2的输入遵守隐式类型转换规则，使数据类型一致。

输入必须是两个张量或一个张量和一个标量。当输入是两个张量时，它们的数据类型不能同时为OH_NN_BOOL。

它们的形状支持broadcast成相同的大小。当输入是一个张量和一个标量时，标量只能是一个常数。

输入：

 input1，n维输入张量，实数或OH_NN_BOOL类型。

input2，n维输入张量，实数或OH_NN_BOOL类型。

输出：

output，n维输出张量，output的shape和数据类型和两个input中精度或者位数高的相同。

OH_NN_OPS_MAX_POOL = 21

在输入张量上应用 2D 最大值池化。如果输入中含有padMode参数，输入：

input，一个张量。

参数：

kernelSize，用来取最大值的kernel大小，是一个长度为2的int数组[kernelHeight，kernelWeight]，第一个数表示kernel高度，第二个数表示kernel宽度。

strides，kernel移动的距离，是一个长度为2的int数组[strideHeight，strideWeight]，第一个数表示高度上的移动步幅，第二个数表示宽度上的移动步幅。

padMode，填充模式，int类型的可选值，0表示same，1表示valid，并且以最近邻的值填充。

same，输出的高度和宽度与input相同，填充总数将在水平和垂直方向计算，并在可能的情况下均匀分布到顶部和底部、左侧和右侧。否则，最后一个额外的填充将从底部和右侧完成。

valid，输出的可能最大高度和宽度将在不填充的情况下返回。额外的像素将被丢弃。

roundMode，边界处理方式，int类型的可选值，当池化核不能完全覆盖输入特征图时，对输出特征图进行取整的方式，0表示向下取整，1表示向上取整。

global，bool值，是否对整个输入张量进行平均池化操作。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。如果输入中含有padList参数，输入：

input，一个张量。

参数：

kernelSize，用来取最大值的kernel大小，是一个长度为2的int数组[kernelHeight，kernelWeight]，第一个数表示kernel高度，第二个数表示kernel宽度。

strides，kernel移动的距离，是一个长度为2的int数组[strideHeight，strideWeight]，第一个数表示高度上的移动步幅，第二个数表示宽度上的移动步幅。

padList，input周围的填充，是一个长度为4的int数组[top，bottom，left，right]，并且以最近邻的值填充。

roundMode，边界处理方式，int类型的可选值，当池化核不能完全覆盖输入特征图时，对输出特征图进行取整的方式，0表示向下取整，1表示向上取整。

global，bool值，是否对整个输入张量进行平均池化操作。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。

输出：

output，对input最大值池化后的张量。

OH_NN_OPS_MUL = 22

将input1和input2相同的位置的元素相乘得到output。如果input1和input2的shape不同，要求input1和input2可以通过broadcast扩充成相同的shape进行相乘。

输入：

input1，一个n维张量。

input2，一个n维张量。

参数：

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，input1和input2每个元素的乘积。

OH_NN_OPS_ONE_HOT = 23

根据indices指定的位置，生成一个由one-hot向量构成的张量。每个onehot向量中的有效值由onValue决定，其他位置由offValue决定。

输入：

 indices，n维张量。indices中每个元素决定每个one-hot向量，onValue的位置。

depth，一个整型标量，决定one-hot向量的深度。要求depth>0。

onValue，一个标量，指定one-hot向量中的有效值。

offValue，一个标量，指定one-hot向量中除有效位以外，其他位置的值。

参数：

axis，一个整型标量，指定插入one-hot的维度。indices的形状是[N，C]，depth的值是D，当axis=0时，output形状为[D，N，C]，indices的形状是[N，C]，depth的值是D，当axis=-1时，output形状为[N，C，D]，indices的形状是[N，C]，depth的值是D，当axis=1时，output形状为[N，D，C]。

输出：

output，如果indices时n维张量，则output是(n+1)维张量。output的形状由indices和axis共同决定。

OH_NN_OPS_PAD = 24

在inputX指定维度的数据前后，添加指定数值进行增广。

输入：

inputX，一个n维张量，要求inputX的排布为[BatchSize，…]。

paddings，一个二维张量，指定每一维度增补的长度，shape为[n，2]。paddings[i][0]表示第i维上，需要在inputX前增补的数量；paddings[i][1]表示第i维上，需要在inputX后增补的数量。

参数：

constantValues，一个常数，数据类型和inputX一致，指定Pad操作补全的数值。

paddingMode，指定填充模式，OH_NN_INT32类型，0表示使用常量0填充，1表示镜像填充(不包含对称轴)，2表示镜像填充(包含对称轴)，3为预留填充方式。

输出：

output，一个n维张量，维数和数据类型和inputX保持一致。shape由inputX和paddings共同决定output.shape[i] = input.shape[i] + paddings[i][0]+paddings[i][1]。

OH_NN_OPS_POW = 25

求input的y次幂，输入必须是两个张量或一个张量和一个标量。当输入是两个张量时，它们的数据类型不能同时为OH_NN_BOOL，且要求两个张量的shape相同。当输入是一个张量和一个标量时，标量只能是一个常数。

输入：

input，实数、bool值或张量，张量的数据类型为实数/OH_NN_BOOL。

y，实数、bool值或张量，张量的数据类型为实数/OH_NN_BOOL。

参数：

scale，一个OH_NN_FLOAT32标量，表示缩放融合的因子。

shift，一个OH_NN_FLOAT32标量，表示缩放融合的偏置。

输出：

output，形状由input和y broadcast后的形状决定。

OH_NN_OPS_SCALE = 26

给定一个张量，计算其缩放后的值。

输入：

input，一个n维张量。

scale，缩放张量。

bias，偏置张量。

参数：

axis，指定缩放的维度。

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。

输出：

output，scale的计算结果，一个n维张量，类型和input一致，shape由axis决定。

OH_NN_OPS_SHAPE = 27

输入一个张量，计算其shape。

输入：

input，一个n维张量。

输出：

output，输出张量的维度，一个整型数组。

OH_NN_OPS_SIGMOID = 28

给定一个张量，计算其sigmoid结果。

输入：

input，一个n维张量。

输出：

output，sigmoid的计算结果，一个n维张量，类型和shape和input一致。

OH_NN_OPS_SLICE = 29

在input 张量各维度，以begin为起点，截取size长度的切片。

输入：

input，n维输入张量。

begin，一组不小于0的整数，指定每个维度上的起始切分点。

size，一组不小于1的整数，指定每个维度上切片的长度。假设某一维度i，1<=size[i]<=input.shape[i]-begin[i]。

参数：

axes，指定切片的轴。

输出：

output，切片得到的n维张量，其TensorType和input一致，shape和size相同。

OH_NN_OPS_SOFTMAX = 30

给定一个张量，计算其softmax结果。

输入：

input，n维输入张量。

参数：

axis，int64类型，指定计算softmax的维度。整数取值范围为[-n，n)。

输出：

output，softmax的计算结果，一个n维张量，类型和shape和input一致。

OH_NN_OPS_SPACE_TO_BATCH_ND = 31

将4维张量在空间维度上进行切分成blockShape[0] * blockShape[1]个小块，然后在batch维度上拼接这些小块。

输入：

input，一个四维张量。

参数：

blockShape，一对整数，每个整数不小于1。

paddings，一对数组，每个数组由两个整数组成。组成paddings的4个整数都不小于0。paddings[0][0]和paddings[0][1]指定了第三个维度上padding的数量，paddings[1][0]和paddings[1][1]指定了第四个维度上padding的数量。

输出：

output，一个4维张量，数据类型和input一致。shape由input，blockShape和paddings共同决定，假设input shape为[n,c,h,w]，则有

output.shape[0] = n * blockShape[0] * blockShape[1]

output.shape[1] = c

output.shape[2] = (h + paddings[0][0] + paddings[0][1]) / blockShape[0]

output.shape[3] = (w + paddings[1][0] + paddings[1][1]) / blockShape[1]

要求(h + paddings[0][0] + paddings[0][1])和(w + paddings[1][0] + paddings[1][1])能被blockShape[0]和blockShape[1]整除。

OH_NN_OPS_SPLIT = 32

Split 算子沿axis维度将input拆分成多个张量，张量数量由outputNum指定。

输入：

input，n维张量。参数：

outputNum，输出张量的数量，outputNum类型为int。

sizeSplits，一维张量，指定 张量 沿 axis 轴拆分后，每个 张量 的大小，sizeSplits 类型为 int。如果 sizeSplits 的数据为空，则 张量 被拆分成大小均等的 张量，此时要求 input.shape[axis] 可以被 outputNum 整除；如果 sizeSplits 不为空，则要求 sizeSplits 所有元素之和等于 input.shape[axis]。

axis，指定拆分的维度，axis类型为int。

输出：

outputs，一组n维张量，每一个张量类型和shape相同，每个张量的类型和input一致。

OH_NN_OPS_SQRT = 33

给定一个张量，计算其平方根。

输入：

input，一个n维张量。

输出：

output，输入的平方根，一个n维张量，类型和shape和input一致。

OH_NN_OPS_SQUARED_DIFFERENCE = 34

计算两个输入的差值并返回差值的平方。SquaredDifference算子支持张量和张量相减。

如果两个张量的TensorType不相同，算子会将低精度的张量转成更高精度的类型。

如果两个张量的shape不同，要求两个张量可以通过broadcast拓展成相同shape的张量。

输入：

input1，被减数，input1是一个张量，张量的类型可以是OH_NN_FLOAT16、OH_NN_FLOAT32、OH_NN_INT32或OH_NN_BOOL。

input2，减数，input2是一个张量，张量的类型可以是OH_NN_FLOAT16、OH_NN_FLOAT32、OH_NN_INT32或OH_NN_BOOL。

输出：

output，两个输入差值的平方。output的shape由input1和input2共同决定，input1和input2的shape相同时，output的shape和input1、input2相同；shape不同时，需要将input1或input2做broadcast操作后，相减得到output。output的TensorType由两个输入中更高精度的TensorType决定。

OH_NN_OPS_SQUEEZE = 35

去除axis中，长度为1的维度。支持int8量化输入假设input的shape为[2，1，1，2，2]，axis为[0,1]，则output的shape为[2，1，2，2]。第0维到第一维之间，长度为0的维度被去除。

输入：

input，n维张量。

参数：

axis，指定删除的维度。axis可以是一个int64_t的整数或数组，整数的取值范围为[-n，n)。

输出：

output，输出张量。

OH_NN_OPS_STACK = 36

将一组张量沿axis维度进行堆叠，堆叠前每个张量的维数为n，则堆叠后output维数为n+1。

输入：

input，Stack支持传入多个输入n维张量，每个张量要求shape相同且类型相同。

参数：

axis，一个整数，指定张量堆叠的维度。axis可以是负数，axis取值范围为[-(n+1)，(n+1))。

输出：

output，将input沿axis维度堆叠的输出，n+1维张量，TensorType和input相同。

OH_NN_OPS_STRIDED_SLICE = 37

跨步截取张量。

输入：

input，n维输入张量。

begin，一维张量，begin的长度等于n，begin[i]指定第i维上截取的起点。

end，一维张量，end的长度等于n，end[i]指定第i维上截取的终点。

strides，一维张量，strides的长度等于n，strides[i]指定第i维上截取的步长。

参数：

beginMask，一个整数，用于解除begin的限制。将beginMask转成二进制表示，如果binary(beginMask)[i]==1，则对于第i维，从第一个元素开始，以strides[i]为步长截取元素直到第end[i]-1个元素。

endMask，一个整数，用于解除end的限制。将endMask转成二进制表示，如果binary(endMask)[i]==1，则对于第i维，从第begin[i]个元素起，以strides[i]为步长截取元素直到张量边界。

ellipsisMask，一个整数，用于解除begin和end的限制。将ellipsisMask转成二进制表示，如果binary(ellipsisMask)[i]==1，则对于第i维，从第一个元素开始，以strides[i]为补偿，截取元素直到张量边界。binary(ellipsisMask)仅允许有一位不为0。

newAxisMask，一个整数，用于新增维度。将newAxisMask转成二进制表示，如果binary(newAxisMask)[i]==1，则在第i维插入长度为1的新维度。

shrinkAxisMask，一个整数，用于压缩指定维度。将shrinkAxisMask转成二进制表示，如果binary(shrinkAxisMask)[i]==1，则舍去第i维所有元素，第i维长度压缩至1。

输出：

堆叠运算后的张量，数据类型与input相同。输出维度rank(input[0])+1 维。

OH_NN_OPS_SUB = 38

计算两个输入的差值。

输入：

input1，被减数，input1是一个张量。

input2，减数，input2是一个张量。

参数：

activationType，是一个整型常量，且必须是OH_NN_FuseType中含有的值。在输出之前调用指定的激活。输出：

output，两个输入相减的差。output的shape由input1和input2共同决定，当input1和input2的shape相同时，output的shape和input1、input2相同；shape不同时，需要将input1或input2做broadcast操作后，相减得到output。output的TensorType由两个输入中更高精度的TensorType决定。

OH_NN_OPS_TANH = 39

计算输入张量的双曲正切值。

输入：

input，n维张量。

输出：

output，input的双曲正切，TensorType和张量 shape和input相同。

OH_NN_OPS_TILE = 40

以multiples指定的次数拷贝input。

输入：

input，n维张量。

multiples，一维张量，指定各个维度拷贝的次数。其长度m不小于input的维数n。

参数：

dims，1维张量，指定需要复制的维度的索引。

输出：

output，m维张量，TensorType与input相同。如果input和multiples长度相同，则output和input维数一致，都是n维张量；如果multiples长度大于n，则用1填充input的维度，再在各个维度上拷贝相应的次数，得到m维张量。

OH_NN_OPS_TRANSPOSE = 41

根据permutation对input进行数据重排。

输入：

input，n维张量，待重排的张量。

perm，一维张量，其长度和input的维数一致。

输出：

output，n维张量，output的TensorType与input相同，shape由input的shape和permutation共同决定。

OH_NN_OPS_REDUCE_MEAN = 42

keepDims为false时，计算指定维度上的平均值，减少input的维数；当keepDims为true时，计算指定维度上的平均值，保留相应的维度。

输入：

 input，n维输入张量，n<8。

axis，一维张量，指定计算均值的维度，axis中每个元素的取值范围为[-n，n)。

参数：

 keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

OH_NN_OPS_RESIZE_BILINEAR = 43

采用Bilinear方法，按给定的参数对input进行变形。

输入：

input，四维输入张量，input中的每个元素不能小于0。input排布必须是[batchSize，height，width，channels]。

参数：

newHeight，resize之后4维张量的height值。

newWidth，resize之后4维张量的width值。

preserveAspectRatio，一个布尔值，指示resize操作是否保持input 张量的height/width比例。

coordinateTransformMode，一个int32整数，指示Resize操作所使用的坐标变换方法，目前支持以下方法：0表示“ASYMMETRIC”，1表示“ALIGN_CORNERS”，2表示“HALF_PIXEL”。

excludeOutside，一个int64浮点数。当excludeOutside=1时，超出input边界的采样权重被置为0，其余权重重新归一化处理。

输出：

output，n维输出张量，output的shape和数据类型和input相同。

OH_NN_OPS_RSQRT = 44

求input平方根的倒数。

输入：

input，n维输入张量，input中的每个元素不能小于0，n<8。

输出：

output，n维输出张量，output的shape和数据类型和input相同。

OH_NN_OPS_RESHAPE = 45

根据inputShape调整input的形状。

输入：

 input，一个n维输入张量。

inputShape，一个一维张量，表示输出张量的shape，需要是一个常量张量。

输出：

output，输出张量，数据类型和input一致，shape由inputShape决定。

OH_NN_OPS_PRELU = 46

计算input和weight的PReLU激活值。

输入：

 input，一个n维张量，如果n>=2，则要求inputX的排布为[BatchSize，…，Channels]，第二个维度为通道数。

weight，一个一维张量。weight的长度只能是1或者等于通道数。当weight长度为1，则input所有通道共享一个权重值。若weight长度等于通道数，每个通道独享一个权重，若input维数n<2，weight长度只能为1。

输出：

output，input的PReLU激活值。形状和数据类型和input保持一致。

OH_NN_OPS_RELU = 47

计算input的Relu激活值。

输入：

input，一个n维输入张量。

输出：

output，n维Relu输出张量，数据类型和shape和input一致。

OH_NN_OPS_RELU6 = 48

计算input的Relu6激活值，即对input中每个元素x，计算min(max(x，0)，6)。

输入：

input，一个n维输入张量。

输出：

output，n维Relu6输出张量，数据类型和shape和input一致。

OH_NN_OPS_LAYER_NORM = 49

对一个张量从某一axis开始做层归一化。

输入：

input，一个n维输入张量。

gamma，一个m维张量，gamma维度应该与input做归一化部分的shape一致。

beta，一个m维张量，shape与gamma一样。参数：

beginAxis，是一个OH_NN_INT32的标量，指定开始做归一化的轴，取值范围是[1，rank(input))。

epsilon，是一个OH_NN_FLOAT32的标量，是归一化公式中的微小量，常用值是1e-5。

beginParamsAxis，指定输入(gamma, beta)需要进行层归一化的开始轴。

输出：

output，n维输出张量，数据类型和shape和input一致。

OH_NN_OPS_REDUCE_PROD = 50

沿着axis指定的维度，计算input的累积值。

输入：

input，n维输入张量，n<8。

axis，一维张量，指定计算乘的维度，axis中每个元素的取值范围为[-n，n)。

参数：

 keepDims，布尔值，是否保留维度的标志位。当keepDims为true时，output的维数和input保持一致；当keepDims为false时，output的维数缩减。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

OH_NN_OPS_REDUCE_ALL = 51

计算指定维度上的逻辑与。当keepDims为false时，减少input的维数；当keepDims为true时，保留相应的维度。

输入：

input，n维输入张量，n<8。

axis，一维张量，指定计算逻辑与的维度，axis中每个元素的取值范围为[-n，n)。

参数：

keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。

输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

OH_NN_OPS_QUANT_DTYPE_CAST = 52

数据类型转换。

输入：

input，n维张量，如果是量化类型和浮点类型之间的转换，输入张量应包含量化参数。

参数：

srcT，定义输入的数据类型。

dstT，定义输出的数据类型。

axis，指定提取量化参数的维度，如果输入张量量化参数的size为1，算子功能是层量化转换，该参数不生效；如果输入张量量化参数的size大于1，算子功能是通道量化转换，该参数生效。

输出：

output，n维张量，数据类型由dstT决定 输出shape和输入相同。

OH_NN_OPS_TOP_K = 53

查找沿最后一个维度的k个最大条目的值和索引。

输入：

input，n维张量。

k，指明是得到前k个数据以及其index。

参数：

sorted，如果为true，按照大到小排序，如果为false，按照小到大排序。

axis，一个OH_NN_INT32标量，指定需要排序的维度，默认-1，指向最后一个维度。

输出：

output0，最后一维的每个切片中的k个最大元素。

output1，输入的最后一个维度内的值的索引。

OH_NN_OPS_ARG_MAX = 54

返回跨轴的张量最大值的索引。

输入：

input，n维张量，输入张量(N，∗)，其中∗意味着任意数量的附加维度。

参数：

axis，指定求最大值索引的维度。

keepDims，bool值，是否维持输入张量维度。

topK，要返回最大值的数量，默认为1，当topK等于1时，将返回输入张量中最大值的索引；当topK大于1时，返回输入张量中前topK个最大值的索引。如果输入张量中有多个值相同且都是最大值，则返回其中任意一个。

outMaxValue，是否输出最大值，默认为false。

输出：

output，张量，轴上输入张量最大值的索引。

OH_NN_OPS_UNSQUEEZE = 55

根据输入axis的值。增加一个维度。

输入：

input，n维张量。

参数：

axis，指定增加的维度。axis可以是一个整数或一组整数，整数的取值范围为[-n，n)。

输出：

output，输出张量。

OH_NN_OPS_GELU = 56

高斯误差线性单元激活函数。output=0.5∗input∗(1+tanh(input/2))，不支持int量化输入。

输入：

input，一个n维输入张量。

参数：

approximate，bool值，近似函数的选项，值为true时，近似函数为Tanh函数，值为false时，近似函数为Erf函数。

输出：

output，n维Relu输出张量，数据类型和shape和input一致。

OH_NN_OPS_UNSTACK = 57

把输入张量按照axis轴分解。

输入：

input，n维张量。

参数：

axis，一个OH_NN_INT32标量，指定矩阵分解的轴，取值范围是[-n，n)。

输出：

output，从输入分解出来的多个张量，每个张量的形状相同。

**起始版本：** 12

OH_NN_OPS_ABS = 58

计算输入数据的绝对值。

输入：

input，n维张量。

输出：

output，n维张量，形状、数据类型与输入保持一致。

**起始版本：** 12

OH_NN_OPS_ERF = 59

高斯误差函数，对输入数据逐元素做误差计算。

输入：

input，n维张量，维度必须小于8，数据类型仅支持OH_NN_FLOAT32和OH_NN_FLOAT16。

输出：

output，n维张量，数据类型和形状与输入相同。

**起始版本：** 12

OH_NN_OPS_EXP = 60

逐元素计算输入的指数。计算公式为 output = base ^ (shift + scale * input)，其中要求底数base>0，默认为-1，表示底数为自然常数e。

输入：

input，n维张量。

参数：

base，指数函数的底数，默认-1，表示底数为自然常数e。

scale，指数的缩放因子，默认1。

shift，指数的偏置，默认0。

输出：

output，n维张量，指数函数的输出结果。

**起始版本：** 12

OH_NN_OPS_LESS = 61

对input1和input2逐元素计算input1[i]<input2[i]的结果，i是输入张量中每个元素的索引。

输入：

input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数或OH_NN_BOOL。

输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

**起始版本：** 12

OH_NN_OPS_SELECT = 62

根据输入条件逐元素判定输出是从输入1还是输入2中选取值；当条件为true时，从输入1中取元素；当条件为false时，从输入2中取元素。当条件为张量时，三个输入的形状需要保持一致。

输入：

condition，判定条件，实数或n维张量。input1，待挑选的输入1。input2，待挑选的输入2。

输出：

output，n维张量，形状和数据类型和输入保持一致。

**起始版本：** 12

OH_NN_OPS_SQUARE = 63

逐元素计算输入的平方。

输入：

input，n维张量。

输出：

output，n维张量，数据类型和形状和输入一致。

**起始版本：** 12

OH_NN_OPS_FLATTEN = 64

指定axis轴将输入Tensor扁平化。

输入：

input，n维张量。

参数：

axis, 扁平化轴，将输入沿着axis维展平，对于输入维度为(d_0, d_1, ..., d_n)的张量，输出的维度应为(d_0*\d_1*...*d_(axis-1)， d_axis*d_(axis+1)*...*d_n)。

输出：

output，展平后的2维张量。

**起始版本：** 12

OH_NN_OPS_DEPTH_TO_SPACE = 65

将输入张量的深度数据块重新排列为空间维度。

输入：

input，4维张量，NHWC或NCHW格式，目前仅支持NHWC，形状为[batchSize, height, width, channels]。参数：

blockSize，指定转换的块大小，必须是整数。

mode，指定转换的方式，0表示"DCR"，1表示"CRD"，"DCR"是深度-列-行顺序重排，"CRD"是列-行-深度顺序重排。

输出：

output，4维张量，format格式和输入一致，形状为[batchSize, height * blockSize, weight * blockSize, channel / blockSize^2]。

**起始版本：** 12

OH_NN_OPS_RANGE = 66

生成一个序列张量，其生成范围为[start, limit)，步长为delta。

输入：

input，n维张量，输出的数据类型和输入保持一致。参数：

start，生成序列的起始数。

limit，生成序列的截止数，不包括该数值。delta，步长，从生成序列范围中按步长跳过部分数据。

输出：

output，生成的1维序列张量。

**起始版本：** 12

OH_NN_OPS_INSTANCE_NORM = 67

对输入的每个通道进行标准化处理，使得输入的每个通道的均值为0，方差为1。

输入：

input，4维张量。

scale，1维张量，缩放系数，尺寸和输入的通道数一致。

bias，1维张量，偏置常量，尺寸和输入的通道数一致。

参数：

epsilon，加在分母上一个很小的数值，保证计算稳定性。

输出：

output，4维张量，形状与输入相同。

**起始版本：** 12

OH_NN_OPS_CONSTANT_OF_SHAPE = 68

生成一个指定shape的张量。

输入：

input，1维张量，表示目标张量的shape。

参数：

dataType，目标张量的数据类型。

value，目标张量的数值，数据类型为OH_NN_FLOAT32的单元素数组。

输出：

output，生成的目标张量。

**起始版本：** 12

OH_NN_OPS_BROADCAST_TO = 69

把一个张量广播到适配的形状。输入：

input，n维张量。参数：

shape，1维张量。输出期望的形状。输出：

output，广播后的张量。

**起始版本：** 12

OH_NN_OPS_EQUAL = 70

对input1和input2逐元素计算input1[i] = input2[i]的结果，i是输入张量中每个元素的索引。

输入：

input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。

input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数或OH_NN_BOOL。

输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

**起始版本：** 12

OH_NN_OPS_GREATER = 71

对input1和input2逐元素计算input1[i]>input2[i]的结果，i是输入张量中每个元素的索引。

输入：

input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。

input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数或OH_NN_BOOL。

输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

**起始版本：** 12

OH_NN_OPS_NOT_EQUAL = 72

对input1和input2逐元素计算input1[i] != input2[i]的结果，i是输入张量中每个元素的索引。

输入：

input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。

input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数或OH_NN_BOOL。

输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

**起始版本：** 12

OH_NN_OPS_GREATER_EQUAL = 73

对input1和input2逐元素计算input1[i]>=input2[i]的结果，i是输入张量中每个元素的索引。

输入：

input1，可以是实数、布尔值或数据类型是实数/OH_NN_BOOL的张量。

input2，如果input1是张量，input2可以是实数、布尔值，否则只能是张量，其数据类型是实数或OH_NN_BOOL。

输出：

output，数据类型为OH_NN_BOOL的张量，使用量化模型时，output的量化参数不可省略，但量化参数的数值不会对输入结果产生影响。

**起始版本：** 12

OH_NN_OPS_LEAKY_RELU = 74

计算输入的leakyRelu激活值。

输入：

input，n维张量。

参数：

negativeSlope，当输入小于0时的斜率，控制输出的大小，数据类型为OH_NN_FLOAT32。

输出：

output，n维张量，数据类型和形状和输入一致。

**起始版本：** 12

OH_NN_OPS_LSTM = 75

对输入执行长短期记忆(LSTM)网络计算。

输入：

input，3维张量，形状为[seqLen, batchSize, inputSize]。

wIh，输入到隐藏层的权重参数，形状为[numDirections*numLayers, 4*hiddenSize, inputSize]。

wHh，隐藏层到隐藏层的权重参数，形状为[numDirections*numLayers, 4*hiddenSize, inputSize]。

bias，输入和隐藏层到隐藏层的偏置，形状为[numDirections*numLayers, 8*hiddenSize]。

hx，单元门的初始隐藏状态，形状为[numDirections*numLayers, batchSize, hiddenSize]。

cx，单元门的初始细胞状态，形状为[numDirections*numLayers, batchSize, hiddenSize]。

参数：

bidirectional，bool值，是否为双向LSTM。

hasBias，bool值，单元门是否有偏置。

inputSize，输入的大小。

hiddenSize，隐藏层的状态大小。

numLayers，LSTM的网络层数。

numDirections，LSTM网络的方向数。

dropout，除第一层外每层输入被丢弃的概率[0.0, 1.0]。

zoneoutCell，控制单元保持上次状态的概率，默认为0。

zoneoutHidden，控制隐藏层状态保持上次的概率，默认为0。

projSize，如果该值>0，使用LSTM的投影，默认0。

输出：

output，3维张量，所有输出张量的通道拼接输出，形状为[seqLen, batchSize, numDirections*realHiddenSize]。

hy，最后一层隐层的输出张量，形状是[numDirections*numLayers, batchSize, realHiddenSize]。

cy，最后一层单元门的输出张量，形状是[numDirections*numLayers, batchSize, HiddenSize]。

**起始版本：** 12

OH_NN_OPS_CLIP = 76

将输入张量的值裁剪到指定的最小值和最大值之间。

输入：

input，n维张量或者张量的列表或元组，支持任意维度的张量。

参数：

min，裁剪的最小值限制。

max，裁剪的最大值限制。

输出：

output，数值裁剪后的张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_ALL = 77

判断输入中指定维度的所有元素是否都为非0值，如果都为非0值，则对应维度返回true，否则对应维度返回false。

输入：

input，n维张量，形状为(N, )，其中表示任意数量的附加维度。

axis，1维张量，要计算的维度。

参数：

keepDims，输出张量的维度是否保持。

输出：

output，1维张量或n维张量，数值类型为OH_NN_BOOL，完成非0判断后的输出张量。

**起始版本：** 12

OH_NN_OPS_ASSERT = 78

断言给定条件是否为真，如果给定条件的结果为假，打印data中的张量列表，summarize用来确定要打印的张量的条目数量。

输入：

condition，评估条件。

data，当条件为假时需要打印的张量。

参数：

summarize，打印每个张量的条目数。

输出：

output，如果条件不为真，返回Error。

**起始版本：** 12

OH_NN_OPS_COS = 79

逐元素计算输入数据的余弦值。

输入：

input，n维张量，数值类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

output，n维张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_LOG = 80

逐元素计算输入的自然对数。

输入：

input，n维张量，数值必须大于0，数值类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

output，n维张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_LOGICAL_AND = 81

逐元素计算两个输入张量的逻辑与运算。

输入：

input1，n维张量，数值类型是OH_NN_BOOL。input2，n维张量，数值类型是OH_NN_BOOL，形状与input1相同。

输出：

output，n维张量，逻辑与的计算结果，数值类型是OH_NN_BOOL。

**起始版本：** 12

OH_NN_OPS_LOGICAL_NOT = 82

逐元素计算两个输入张量的逻辑非运算。

输入：

input，n维张量，数值类型是OH_NN_BOOL。

输出：

output，n维张量，逻辑非的计算结果，数值类型是OH_NN_BOOL。

**起始版本：** 12

OH_NN_OPS_MOD = 83

对输入张量做求余运算，input1和input2需要遵循数据类型转换的规则转成一致的数据类型；输入必须是两个张量或一个张量和一个标量。当输入是两个张量时，数据类型都不能是OH_NN_BOOL，可以广播为相同的形状；当输入是一个张量和一个标量时，标量输入只能是一个常量数值。

输入：

input1，被求余的标量或张量，数值型或OH_NN_BOOL类型，或数值类型维数值型的n维张量。

input2，求余因子；当第一个输入是n维张量时，第二个输入可以是数值型、OH_NN_BOOL类型，或数值类型维数值型的n维张量；当第一个输入是数值型、OH_NN_BOOL类型时，第二个输入必须是数据类型维数值型的张量。

输出：

output，n维张量，形状与广播后的输入相同，数据类型为两个输入中精度较高的数据类型。

**起始版本：** 12

OH_NN_OPS_NEG = 84

逐元素计算输入的相反数。

输入：

input，n维张量，数据类型为数值型。

输出：

output，n维张量，形状和数据类型和输入一致。

**起始版本：** 12

OH_NN_OPS_RECIPROCAL = 85

逐元素计算输入的倒数。

输入：

input，n维张量，数据类型为数值类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

output，n维张量，形状和数据类型和输入一致。

**起始版本：** 12

OH_NN_OPS_SIN = 86

逐元素计算输入的正弦值。

输入：

input，n维张量，数值类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

output，n维张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_WHERE = 87

根据condition从input1和input2中选取合适的元素。

输入：

condition，判定条件，数值类型为OH_NN_BOOL的n维张量；如果元素是true，则选取input1对应位置的元素，如果为false，则选取input2对应位置的元素。

input1，待选择的n维张量。

input2，待选择的n维张量。

输出：

output。

**起始版本：** 12

OH_NN_OPS_SPARSE_TO_DENSE = 88

将稀疏张量转换为密集张量。

输入：

indices，2维张量，表示元素在稀疏张量中的位置。

values，1维张量，表示indices位置上对应的值。sparseShape，稀疏张量的形状，由两个正整数组成，形状为(N, C)。

输出：

output，转换后的张量，数据类型和value相同，形状由参数sparseShape指定。

**起始版本：** 12

OH_NN_OPS_LOGICAL_OR = 89

逐元素计算两个输入张量的逻辑或运算。

输入：

input1，n维张量，数值类型是OH_NN_BOOL。

input2，n维张量，数值类型是OH_NN_BOOL，形状与输入1相同。

输出：

output，n维张量，逻辑或的计算结果，数值类型是OH_NN_BOOL。

**起始版本：** 12

OH_NN_OPS_CEIL = 90

对输入的每个元素做向上取整。

输入：

input，n维张量，数据类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

n维张量，形状和数据类型与输入相同。

**起始版本：** 12

OH_NN_OPS_CROP = 91

对输入张量根据axis和offset参数裁剪指定shape大小的张量。

输入：

input，n维待裁剪的张量。shape，1维张量，表示要裁剪的张量大小。

参数：

axis，裁剪区域开始的轴。取值范围为[0,1,...,r-1]，其中r是输入张量的秩，负数表示反向取值。

offset，裁剪区域的起始偏移量。

输出：

output，裁剪后的张量。

**起始版本：** 12

OH_NN_OPS_DETECTION_POST_PROCESS = 92

对目标检测模型的输出进行后处理。包括对模型输出的边界框、类别概率和分数进行解码，然后执行非极大值抑制（NMS）以去除重叠的边界框，最终输出检测结果。

输入：

bbox，模型输出的边界框。

scores，模型输出的类别得分概率。

anchors，用于生成检测框的候选框的坐标和大小信息。在目标检测任务中，候选框指在图像中按照一定的规则预设的一系列矩形框，这些矩形框通常具有不同的大小和长宽比，用于对图像中的目标进行初步的预测和筛选。

参数：

inputSize，输入张量的尺寸。

scale，用于将输出图片从归一化的形式转换到原始图像坐标的缩放因子。

nmsIoUThreshold，非极大值抑制的阈值，用于去除重复的检测框。

nmsScoreThreshold，置信度阈值，用于过滤低置信度的检测框。

maxDetections，每张图片最多输出的检测框数量。

detectionsPerClass，每个类别的最大检测数量。

maxClassesPerDetection，每个检测框中的最大检测类别数。

numClasses，检测总类别数量。

useRegularNms，bool值，是否使用基于IoU阈值的非极大值抑制算法，当为true时，使用基于IoU阈值的NMS算法来过滤重叠的目标框，保留得分最高的目标框；当为false时，不适用基于IoU阈值的NMS算法，进根据得分对目标框进行排序，保留最高得分的目标框。

outQuantized，bool值，表示输出是否需要做量化。

输出：

bboxes，3维张量，内部数组表示目标检测框的坐标值。

classes，2维张量，内部数值表示每个检测框对应的分类索引。

confidences，2维张量，内部数值表示检测到的物体的置信度。

numDetections，检测结果的数量。

**起始版本：** 12

OH_NN_OPS_FLOOR = 93

对输入的每个元素做向下取整。

输入：

input，n维张量，数据类型为OH_NN_FLOAT64、OH_NN_FLOAT32或OH_NN_FLOAT16。

输出：

n维张量，形状和数据类型与输入相同。

**起始版本：** 12

OH_NN_OPS_L2_NORMALIZE = 94

根据指定的axis轴对输入张量做L2-正则化。

输入：

input，需要做L2正则化的n维张量。

参数：

axis，做正则化的指定维度，-1表示最后一个维度。

epsilon，保持计算稳定性，在分母上加上一个很小的数值，默认为1e-6。activationType，激活函数类型。

输出：

output，输出张量，和输入相同的数据类型和形状。

**起始版本：** 12

OH_NN_OPS_LOG_SOFTMAX = 95

对输入张量的每个元素做指数运算，然后将运算结果进行归一化处理，最终得到一个概率分布向量。

输入：

2维张量，形状为[batchSize，numClasses]，数据类型为OH_NN_FLOAT64、OH_NN_FLOAT32、OH_NN_FLOAT16。

参数：

axis，指定进行计算的维度。

输出：

output，2维张量，完成计算后的概率向量。

**起始版本：** 12

OH_NN_OPS_LRN = 96

对输入做局部响应归一化操作。

输入：

input，4维张量，待归一化的输入张量。

参数：

depthRadius，标量，归一化窗口的半宽。

bias，偏移量，通常为正避免除零问题，默认为1。

alpha，比例系数，默认为1。

beta，指数变量，默认为0.5。

normRegion，指定归一化的区域，默认0，代表归一化区域为"ACROSS_CHANNELS"，目前仅支持该模式。

输出：

output，归一化的输出张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_MINIMUM = 97

逐元素计算两个张量的最小值，输入必须是两个张量，或一个张量和一个标量。当输入是两个张量是，数据类型不能同时是bool值，并且两个要能广播到相同的形状。当输入是一个张量和一个常量时，标量必须是常量。

输入：

input1，n维张量，数据类型可以是数值类型或bool值。

input2，n维张量，数据类型可以是数值类型或bool值。

输出：

output，比较结果张量，形状和数据类型和输入相同。

**起始版本：** 12

OH_NN_OPS_RANK = 98

计算张量的秩。

输入：

input，n维张量。

输出：

output，0维的int32结果张量，表示输入的秩。

**起始版本：** 12

OH_NN_OPS_REDUCE_MAX = 99

计算输入张量在指定维度上的最大值，如果keepDims是false，输出张量的维度将会缩减；如果keepDims为true，输出张量的维度和输入张量保持不变。

输入：

input，n维张量，其中n<8。

axis，用于计算最大值的维度。

参数：

keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。

输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

**起始版本：** 12

OH_NN_OPS_REDUCE_MIN = 100

计算输入张量在指定维度上的最小值，如果keepDims是false，输出张量的维度将会缩减；如果keepDims为true，输出张量的维度和输入张量保持不变。

输入：

input，n维张量，其中n<8。

axis，用于计算最小值的维度。

参数：

keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。

输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

**起始版本：** 12

OH_NN_OPS_REDUCE_SUM = 101

计算输入张量在指定维度上的求和，如果keepDims是false，输出张量的维度将会缩减；如果keepDims为true，输出张量的维度和输入张量保持不变。

输入：

input，n维张量，其中n<8。

axis，用于计算求和的维度。

参数：

keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。

输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

**起始版本：** 12

OH_NN_OPS_ROUND = 102

对输入张量进行四舍五入近似计算数值。

输入：

input，n维张量。

输出：

output，结果张量，数据类型和形状和输入一致。

**起始版本：** 12

OH_NN_OPS_SCATTER_ND = 103

根据指定的索引将更新值散布到新的Tensor上。

输入：

indices，指定新张量中散布的索引值，数值类型为OH_NN_INT64或OH_NN_INT32，索引的秩至少为2，并且indices最后一维的数值小于输入shape的尺寸。

updates，指定更新的Tensor。

shape，指定输出张量的形状，数据类型和输入indices相同。

输出：

output，更新后的张量，数据类型和输入update相同，形状和输入shape相同。

**起始版本：** 12

OH_NN_OPS_SPACE_TO_DEPTH = 104

将输入张量的空间维度数据块重新排列为深度维度。

输入：

input，4维张量，NHWC或NCHW格式，目前仅支持NHWC，形状为[batchSize, height, width, channels]。参数：

blockSize，指定转换的块大小，必须是整数。

输出：

output，4维张量，format格式和输入一致，形状为[batchSize, height / blockSize, weight / blockSize, channel * blockSize^2]。

**起始版本：** 12

OH_NN_OPS_SWISH = 105

逐元素对输入张量计算Swish激活。输入：

input，n维张量。输出：

n维张量，数据类型和形状与输入相同。

**起始版本：** 12

OH_NN_OPS_REDUCE_L2 = 106

计算输入张量在指定维度上的L2范数，如果keepDims是false，输出张量的维度将会缩减；如果keepDims为true，输出张量的维度和输入张量保持不变。

输入：

input，n维张量，其中n<8。

axis，用于计算L2范数的维度。

参数：

keepDims，布尔值，是否保留维度的标志位。

reduceToEnd，bool值，是否需要执行reduce操作直到最后一轴。

coeff，一个OH_NN_FLOAT32标量，表示输出的缩放因子。

输出：

output，m维输出张量，数据类型和input相同。当keepDims为false时，m<n；当keepDims为true时，m==n。

**起始版本：** 12

OH_NN_OPS_HARD_SIGMOID = 107

逐元素对输入张量计算HardSigmoid激活。

输入：

input，n维张量。

输出：

n维张量，数据类型和形状与输入相同。

**起始版本：** 12

OH_NN_OPS_GATHER_ND = 108

根据索引获取输入张量指定位置上的元素。

输入：

input，n维张量。

indices，m维索引张量，其数据类型为OH_NN_INT64或OH_NN_INT32。

输出：

n维张量，数据类型与输入相同，形状为indices的前（m-1）维和input的后（n-indices最后一维的尺寸）维的拼接。

**起始版本：** 12

#### OH_NN_TensorType

```ets
enum OH_NN_TensorType
```

**描述**

张量的类型。

张量通常用于设置模型的输入、输出和算子参数。作为模型（或算子）的输入和输出时，需要将张量类型设置为[OH_NN_TENSOR](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)；当张量作为算子参数时，需要选择除[OH_NN_TENSOR](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)以外合适的枚举值，作为张量的类型。

假设正在设置[OH_NN_OPS_CONV2D](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_operationtype)算子的pad参数，则需要将[OH_NN_Tensor](../../topics/misc/OH_NN_Tensor.md)实例的type属性设置为[OH_NN_CONV2D_PAD](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_tensortype)。其他算子参数的设置以此类推，枚举值的命名遵守 OH_NN_{算子名称}_{属性名} 的格式。

**起始版本：** 9

枚举项描述OH_NN_TENSOR = 0当张量作为模型（或算子）的输入或输出时，使用本枚举值。OH_NN_ADD_ACTIVATIONTYPE = 1当张量作为Add算子的activationType参数时，使用本枚举值。OH_NN_AVG_POOL_KERNEL_SIZE = 2当张量作为AvgPool算子的kernelSize参数时，使用本枚举值。OH_NN_AVG_POOL_STRIDE = 3当张量作为AvgPool算子的stride参数时，使用本枚举值。OH_NN_AVG_POOL_PAD_MODE = 4当张量作为AvgPool算子的padMode参数时，使用本枚举值。OH_NN_AVG_POOL_PAD = 5当张量作为AvgPool算子的pad参数时，使用本枚举值。OH_NN_AVG_POOL_ACTIVATION_TYPE = 6当张量作为AvgPool算子的activationType参数时，使用本枚举值。OH_NN_BATCH_NORM_EPSILON = 7当张量作为BatchNorm算子的epsilon参数时，使用本枚举值。OH_NN_BATCH_TO_SPACE_ND_BLOCKSIZE = 8当张量作为BatchToSpaceND算子的blockSize参数时，使用本枚举值。OH_NN_BATCH_TO_SPACE_ND_CROPS = 9当张量作为BatchToSpaceND算子的crops参数时，使用本枚举值。OH_NN_CONCAT_AXIS = 10当张量作为Concat算子的axis参数时，使用本枚举值。OH_NN_CONV2D_STRIDES = 11当张量作为Conv2D算子的strides参数时，使用本枚举值。OH_NN_CONV2D_PAD = 12当张量作为Conv2D算子的pad参数时，使用本枚举值。OH_NN_CONV2D_DILATION = 13当张量作为Conv2D算子的dilation参数时，使用本枚举值。OH_NN_CONV2D_PAD_MODE = 14当张量作为Conv2D算子的padMode参数时，使用本枚举值。OH_NN_CONV2D_ACTIVATION_TYPE = 15当张量作为Conv2D算子的activationType参数时，使用本枚举值。OH_NN_CONV2D_GROUP = 16当张量作为Conv2D算子的group参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_STRIDES = 17当张量作为Conv2DTranspose算子的strides参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_PAD = 18当张量作为Conv2DTranspose算子的pad参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_DILATION = 19当张量作为Conv2DTranspose算子的dilation参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_OUTPUT_PADDINGS = 20当张量作为Conv2DTranspose算子的outputPaddings参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_PAD_MODE = 21当张量作为Conv2DTranspose算子的padMode参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_ACTIVATION_TYPE = 22当张量作为Conv2DTranspose算子的activationType参数时，使用本枚举值。OH_NN_CONV2D_TRANSPOSE_GROUP = 23当张量作为Conv2DTranspose算子的group参数时，使用本枚举值。OH_NN_DEPTHWISE_CONV2D_NATIVE_STRIDES = 24当张量作为DepthwiseConv2dNative算子的strides参数时，使用本枚举值。OH_NN_DEPTHWISE_CONV2D_NATIVE_PAD = 25当张量作为DepthwiseConv2dNative算子的pad参数时，使用本枚举值。OH_NN_DEPTHWISE_CONV2D_NATIVE_DILATION = 26当张量作为DepthwiseConv2dNative算子的dilation参数时，使用本枚举值。OH_NN_DEPTHWISE_CONV2D_NATIVE_PAD_MODE = 27当张量作为DepthwiseConv2dNative算子的padMode参数时，使用本枚举值。OH_NN_DEPTHWISE_CONV2D_NATIVE_ACTIVATION_TYPE = 28当张量作为DepthwiseConv2dNative算子的activationType参数时，使用本枚举值。OH_NN_DIV_ACTIVATIONTYPE = 29当张量作为Div算子的activationType参数时，使用本枚举值。OH_NN_ELTWISE_MODE = 30当张量作为Eltwise算子的mode参数时，使用本枚举值。OH_NN_FULL_CONNECTION_AXIS = 31当张量作为FullConnection算子的axis参数时，使用本枚举值。OH_NN_FULL_CONNECTION_ACTIVATIONTYPE = 32当张量作为FullConnection算子的activationType参数时，使用本枚举值。OH_NN_MATMUL_TRANSPOSE_A = 33当张量作为Matmul算子的transposeA参数时，使用本枚举值。OH_NN_MATMUL_TRANSPOSE_B = 34当张量作为Matmul算子的transposeB参数时，使用本枚举值。OH_NN_MATMUL_ACTIVATION_TYPE = 35当张量作为Matmul算子的activationType参数时，使用本枚举值。OH_NN_MAX_POOL_KERNEL_SIZE = 36当张量作为MaxPool算子的kernelSize参数时，使用本枚举值。OH_NN_MAX_POOL_STRIDE = 37当张量作为MaxPool算子的stride参数时，使用本枚举值。OH_NN_MAX_POOL_PAD_MODE = 38当张量作为MaxPool算子的padMode参数时，使用本枚举值。OH_NN_MAX_POOL_PAD = 39当张量作为MaxPool算子的pad参数时，使用本枚举值。OH_NN_MAX_POOL_ACTIVATION_TYPE = 40当张量作为MaxPool算子的activationType参数时，使用本枚举值。OH_NN_MUL_ACTIVATION_TYPE = 41当张量作为Mul算子的activationType参数时，使用本枚举值。OH_NN_ONE_HOT_AXIS = 42当张量作为OneHot算子的axis参数时，使用本枚举值。OH_NN_PAD_CONSTANT_VALUE = 43当张量作为Pad算子的constantValue参数时，使用本枚举值。OH_NN_SCALE_ACTIVATIONTYPE = 44当张量作为Scale算子的activationType参数时，使用本枚举值。OH_NN_SCALE_AXIS = 45当张量作为Scale算子的axis参数时，使用本枚举值。OH_NN_SOFTMAX_AXIS = 46当张量作为Softmax算子的axis参数时，使用本枚举值。OH_NN_SPACE_TO_BATCH_ND_BLOCK_SHAPE = 47当张量作为SpaceToBatchND算子的BlockShape参数时，使用本枚举值。OH_NN_SPACE_TO_BATCH_ND_PADDINGS = 48当张量作为SpaceToBatchND算子的Paddings参数时，使用本枚举值。OH_NN_SPLIT_AXIS = 49当张量作为Split算子的Axis参数时，使用本枚举值。OH_NN_SPLIT_OUTPUT_NUM = 50当张量作为Split算子的OutputNum参数时，使用本枚举值。OH_NN_SPLIT_SIZE_SPLITS = 51当张量作为Split算子的SizeSplits参数时，使用本枚举值。OH_NN_SQUEEZE_AXIS = 52当张量作为Squeeze算子的Axis参数时，使用本枚举值。OH_NN_STACK_AXIS = 53当张量作为Stack算子的Axis参数时，使用本枚举值。OH_NN_STRIDED_SLICE_BEGIN_MASK = 54当张量作为StridedSlice算子的BeginMask参数时，使用本枚举值。OH_NN_STRIDED_SLICE_END_MASK = 55当张量作为StridedSlice算子的EndMask参数时，使用本枚举值。OH_NN_STRIDED_SLICE_ELLIPSIS_MASK = 56当张量作为StridedSlice算子的EllipsisMask参数时，使用本枚举值。OH_NN_STRIDED_SLICE_NEW_AXIS_MASK = 57当张量作为StridedSlice算子的NewAxisMask参数时，使用本枚举值。OH_NN_STRIDED_SLICE_SHRINK_AXIS_MASK = 58当张量作为StridedSlice算子的ShrinkAxisMask参数时，使用本枚举值。OH_NN_SUB_ACTIVATIONTYPE = 59当张量作为Sub算子的ActivationType参数时，使用本枚举值。OH_NN_REDUCE_MEAN_KEEP_DIMS = 60当张量作为ReduceMean算子的keepDims参数时，使用本枚举值。OH_NN_RESIZE_BILINEAR_NEW_HEIGHT = 61当张量作为ResizeBilinear算子的newHeight参数时，使用本枚举值。OH_NN_RESIZE_BILINEAR_NEW_WIDTH = 62当张量作为ResizeBilinear算子的newWidth参数时，使用本枚举值。OH_NN_RESIZE_BILINEAR_PRESERVE_ASPECT_RATIO = 63当张量作为ResizeBilinear算子的preserveAspectRatio参数时，使用本枚举值。OH_NN_RESIZE_BILINEAR_COORDINATE_TRANSFORM_MODE = 64当张量作为ResizeBilinear算子的coordinateTransformMode参数时，使用本枚举值。OH_NN_RESIZE_BILINEAR_EXCLUDE_OUTSIDE = 65当张量作为ResizeBilinear算子的excludeOutside参数时，使用本枚举值。OH_NN_LAYER_NORM_BEGIN_NORM_AXIS = 66当张量作为LayerNorm算子的beginNormAxis参数时，使用本枚举值。OH_NN_LAYER_NORM_EPSILON = 67当张量作为LayerNorm算子的epsilon参数时，使用本枚举值。OH_NN_LAYER_NORM_BEGIN_PARAM_AXIS = 68当张量作为LayerNorm算子的beginParamsAxis参数时，使用本枚举值。OH_NN_LAYER_NORM_ELEMENTWISE_AFFINE = 69当张量作为LayerNorm算子的elementwiseAffine参数时，使用本枚举值。OH_NN_REDUCE_PROD_KEEP_DIMS = 70当张量作为ReduceProd算子的keepDims参数时，使用本枚举值。OH_NN_REDUCE_ALL_KEEP_DIMS = 71当张量作为ReduceAll算子的keepDims参数时，使用本枚举值。OH_NN_QUANT_DTYPE_CAST_SRC_T = 72当张量作为QuantDTypeCast算子的srcT参数时，使用本枚举值。OH_NN_QUANT_DTYPE_CAST_DST_T = 73当张量作为QuantDTypeCast算子的dstT参数时，使用本枚举值。OH_NN_TOP_K_SORTED = 74当张量作为Topk算子的Sorted参数时，使用本枚举值。OH_NN_ARG_MAX_AXIS = 75当张量作为ArgMax算子的axis参数时，使用本枚举值。OH_NN_ARG_MAX_KEEPDIMS = 76当张量作为ArgMax算子的keepDims参数时，使用本枚举值。OH_NN_UNSQUEEZE_AXIS = 77当张量作为Unsqueeze算子的Axis参数时，使用本枚举值。OH_NN_UNSTACK_AXIS = 78

当张量作为Unstack算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_FLATTEN_AXIS = 79

当张量作为Flatten算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DEPTH_TO_SPACE_BLOCK_SIZE = 80

当张量作为DepthToSpace算子的blockSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DEPTH_TO_SPACE_MODE = 81

当张量作为DepthToSpace算子的mode参数时，使用本枚举值。

**起始版本：** 12

OH_NN_RANGE_START = 82

当张量作为Range算子的start参数时，使用本枚举值。

**起始版本：** 12

OH_NN_RANGE_LIMIT = 83

当张量作为Range算子的limit参数时，使用本枚举值。

**起始版本：** 12

OH_NN_RANGE_DELTA = 84

当张量作为Range算子的delta参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CONSTANT_OF_SHAPE_DATA_TYPE = 85

当张量作为ConstantOfShape算子的dataType参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CONSTANT_OF_SHAPE_VALUE = 86

当张量作为ConstantOfShape算子的value参数时，使用本枚举值。

**起始版本：** 12

OH_NN_BROADCAST_TO_SHAPE = 87

当张量作为BroadcastTo算子的shape参数时，使用本枚举值。

**起始版本：** 12

OH_NN_INSTANCE_NORM_EPSILON = 88

当张量作为InstanceNorm算子的epsilon参数时，使用本枚举值。

**起始版本：** 12

OH_NN_EXP_BASE = 89

当张量作为Exp算子的base参数时，使用本枚举值。

**起始版本：** 12

OH_NN_EXP_SCALE = 90

当张量作为Exp算子的scale参数时，使用本枚举值。

**起始版本：** 12

OH_NN_EXP_SHIFT = 91

当张量作为Exp算子的shift参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LEAKY_RELU_NEGATIVE_SLOPE = 92

当张量作为LeakyRelu算子的negativeSlope参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_BIDIRECTIONAL = 93

当张量作为LSTM算子的bidirectional参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_HAS_BIAS = 94

当张量作为LSTM算子的hasBias参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_INPUT_SIZE = 95

当张量作为LSTM算子的inputSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_HIDDEN_SIZE = 96

当张量作为LSTM算子的hiddenSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_NUM_LAYERS = 97

当张量作为LSTM算子的numLayers参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_NUM_DIRECTIONS = 98

当张量作为LSTM算子的numDirections参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_DROPOUT = 99

当张量作为LSTM算子的dropout参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_ZONEOUT_CELL = 100

当张量作为LSTM算子的zoneoutCell参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_ZONEOUT_HIDDEN = 101

当张量作为LSTM算子的zoneoutHidden参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LSTM_PROJ_SIZE = 102

当张量作为LSTM算子的projSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CLIP_MAX = 103

当张量作为Clip算子的max参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CLIP_MIN = 104

当张量作为Clip算子的min参数时，使用本枚举值。

**起始版本：** 12

OH_NN_ALL_KEEP_DIMS = 105

当张量作为All算子的keepDims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_ASSERT_SUMMARIZE = 106

当张量作为Assert算子的summarize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_POW_SCALE = 107

当张量作为Pow算子的scale参数时，使用本枚举值。

**起始版本：** 12

OH_NN_POW_SHIFT = 108

当张量作为Pow算子的shift参数时，使用本枚举值。

**起始版本：** 12

OH_NN_AVG_POOL_ROUND_MODE = 109

当张量作为AvgPool算子的RoundMode参数时，使用本枚举值。

**起始版本：** 12

OH_NN_AVG_POOL_GLOBAL = 110

当张量作为AvgPool算子的global参数时，使用本枚举值。

**起始版本：** 12

OH_NN_FULL_CONNECTION_HAS_BIAS = 111

当张量作为FullConnection算子的hasBias参数时，使用本枚举值。

**起始版本：** 12

OH_NN_FULL_CONNECTION_USE_AXIS = 112

当张量作为FullConnection算子的useAxis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_GELU_APPROXIMATE = 113

当张量作为GeLU算子的approximate参数时，使用本枚举值。

**起始版本：** 12

OH_NN_MAX_POOL_ROUND_MODE = 114

当张量作为MaxPool算子的RoundMode参数时，使用本枚举值。

**起始版本：** 12

OH_NN_MAX_POOL_GLOBAL = 115

当张量作为MaxPool算子的global参数时，使用本枚举值。

**起始版本：** 12

OH_NN_PAD_PADDING_MODE = 116

当张量作为Pad算子的paddingMode参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MEAN_REDUCE_TO_END = 117

当张量作为ReduceMean算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MEAN_COEFF = 118

当张量作为ReduceMean算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_PROD_REDUCE_TO_END = 119

当张量作为ReduceProd算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_PROD_COEFF = 120

当张量作为ReduceProd算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_ALL_REDUCE_TO_END = 121

当张量作为ReduceAll算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_ALL_COEFF = 122

当张量作为ReduceAll算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_TOP_K_AXIS = 123

当张量作为TopK算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_ARG_MAX_TOP_K = 124

当张量作为ArgMax算子的topK参数时，使用本枚举值。

**起始版本：** 12

OH_NN_ARG_MAX_OUT_MAX_VALUE = 125

当张量作为ArgMax算子的outMaxValue参数时，使用本枚举值。

**起始版本：** 12

OH_NN_QUANT_DTYPE_CAST_AXIS = 126

当张量作为QuantDTypeCast算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_SLICE_AXES = 127

当张量作为Slice算子的axes参数时，使用本枚举值。

**起始版本：** 12

OH_NN_TILE_DIMS = 128

当张量作为Tile算子的dims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CROP_AXIS = 129

当张量作为Crop算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_CROP_OFFSET = 130

当张量作为Crop算子的offset参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_INPUT_SIZE = 131

当张量作为DetectionPostProcess算子的inputSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_SCALE = 132

当张量作为DetectionPostProcess算子的scale参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_NMS_IOU_THRESHOLD = 133

当张量作为DetectionPostProcess算子的nmsIouThreshold参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_NMS_SCORE_THRESHOLD = 134

当张量作为DetectionPostProcess算子的nmsScoreThreshold参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_MAX_DETECTIONS = 135

当张量作为DetectionPostProcess算子的maxDetections参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_DETECTIONS_PER_CLASS = 136

当张量作为DetectionPostProcess算子的perClass参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_MAX_CLASSES_PER_DETECTION = 137

当张量作为DetectionPostProcess算子的maxClassPerDetection参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_NUM_CLASSES = 138

当张量作为DetectionPostProcess算子的numClasses参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_USE_REGULAR_NMS = 139

当张量作为DetectionPostProcess算子的useRegularNms参数时，使用本枚举值。

**起始版本：** 12

OH_NN_DETECTION_POST_PROCESS_OUT_QUANTIZED = 140

当张量作为DetectionPostProcess算子的outQuantized参数时，使用本枚举值。

**起始版本：** 12

OH_NN_L2_NORMALIZE_AXIS = 141

当张量作为L2Normalize算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_L2_NORMALIZE_EPSILON = 142

当张量作为L2Normalize算子的epsilon参数时，使用本枚举值。

**起始版本：** 12

OH_NN_L2_NORMALIZE_ACTIVATION_TYPE = 143

当张量作为L2Normalize算子的activationType参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LOG_SOFTMAX_AXIS = 144

当张量作为LogSoftmax算子的axis参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LRN_DEPTH_RADIUS = 145

当张量作为LRN算子的depthRadius参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LRN_BIAS = 146

当张量作为LRN算子的bias参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LRN_ALPHA = 147

当张量作为LRN算子的alpha参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LRN_BETA = 148

当张量作为LRN算子的beta参数时，使用本枚举值。

**起始版本：** 12

OH_NN_LRN_NORM_REGION = 149

当张量作为LRN算子的normRegion参数时，使用本枚举值。

**起始版本：** 12

OH_NN_SPACE_TO_DEPTH_BLOCK_SIZE = 150

当张量作为SpaceToDepth算子的blockSize参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MAX_KEEP_DIMS = 151

当张量作为ReduceMax算子的keepDims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MAX_REDUCE_TO_END = 152

当张量作为ReduceMax算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MAX_COEFF = 153

当张量作为ReduceMax算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MIN_KEEP_DIMS = 154

当张量作为ReduceMin算子的keepDims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MIN_REDUCE_TO_END = 155

当张量作为ReduceMin算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_MIN_COEFF = 156

当张量作为ReduceMin算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_SUM_KEEP_DIMS = 157

当张量作为ReduceSum算子的keepDims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_SUM_REDUCE_TO_END = 158

当张量作为ReduceSum算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_SUM_COEFF = 159

当张量作为ReduceSum算子的coeff参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_L2_KEEP_DIMS = 160

当张量作为ReduceL2算子的keepDims参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_L2_REDUCE_TO_END = 161

当张量作为ReduceL2算子的reduceToEnd参数时，使用本枚举值。

**起始版本：** 12

OH_NN_REDUCE_L2_COEFF = 162

当张量作为ReduceL2算子的coeff参数时，使用本枚举值。

**起始版本：** 12

#### 函数说明

#### NN_OnRunDone()

```ets
typedef void (*NN_OnRunDone)(void *userData, OH_NN_ReturnCode errCode, void *outputTensor[], int32_t outputCount)
```

**描述**

异步推理结束后的回调处理函数句柄。

使用参数**userData**来查询希望获取的那次异步推理执行。**userData**与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**是一致的。使用参数**errCode**（[OH_NN_ReturnCode](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_returncode)类型）来获取该次异步推理的返回状态。

**起始版本：** 11

**参数：**

参数项描述void *userData异步推理执行的标识符，与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**一致。[ OH_NN_ReturnCode](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_returncode) errCode该次异步推理的返回状态（[OH_NN_ReturnCode](neural_network_runtime_type.h.md#ZH-CN_TOPIC_0000002497606150__oh_nn_returncode)类型）。void *outputTensor[]异步推理的输出张量，与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**outputTensor**一致。int32_t outputCount异步推理输出张量的数量，与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**outputCount**一致。

#### NN_OnServiceDied()

```ets
typedef void (*NN_OnServiceDied)(void *userData)
```

**描述**

异步推理执行期间设备驱动服务异常终止时的回调处理函数句柄。

如果该回调函数被调用，您需要重新编译模型。

使用参数**userData**来查询希望获取的那次异步推理执行。**userData**与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**是一致的。

**起始版本：** 11

**参数：**

参数项描述void *userData异步推理执行的标识符，与调用异步推理[OH_NNExecutor_RunAsync](neural_network_core.h.md#ZH-CN_TOPIC_0000002529286139__oh_nnexecutor_runasync)接口时传入的参数**userData**一致。