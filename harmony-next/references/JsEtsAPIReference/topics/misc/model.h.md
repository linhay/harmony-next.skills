# model.h

**概述**

提供了模型相关接口，可以用于模型创建、模型推理等，该接口是非线程安全的。

引用文件： <mindspore/model.h>

库： libmindspore_lite_ndk.so

系统能力： SystemCapability.Ai.MindSpore

起始版本： 9

相关模块： [MindSpore](MindSpore.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| OH_AI_TensorHandleArray | 张量数组结构体，用于存储张量数组指针和张量数组长度。 |
| OH_AI_ShapeInfo | 形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。 |
| OH_AI_CallBackParam | 回调函数中传入的算子信息。 |
| OH_AI_ModelHandle | 指向模型对象的指针。 |
| OH_AI_TrainCfgHandle | 指向训练配置对象的指针。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef bool (*OH_AI_KernelCallBack)(const OH_AI_TensorHandleArray inputs, const OH_AI_TensorHandleArray outputs,const OH_AI_CallBackParam kernel_Info) | OH_AI_KernelCallBack | 回调函数指针。  该函数指针是用于设置OH_AI_ModelPredict函数参数中的两个回调函数。  该指针指向的函数需要包含三个参数，其中inputs和outputs对应了算子的输入和输出张量，kernel_Info表示当前算子的信息。  可以通过回调函数监控算子执行的情况，例如统计算子的执行时间，校验算子的正确性等等。 |
| OH_AI_API OH_AI_ModelHandle OH_AI_ModelCreate(void) | - | 创建一个模型对象。 |
| OH_AI_API void OH_AI_ModelDestroy(OH_AI_ModelHandle *model) | - | 释放一个模型对象。 |
| OH_AI_API OH_AI_Status OH_AI_ModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context) | - | 从内存缓冲区加载并编译MindSpore Lite模型。  注意，同一个OH_AI_ContextHandle对象仅能传递给OH_AI_ModelBuild或者OH_AI_ModelBuildFromFile一次，如果多次调用该函数需要创建多个不同的OH_AI_ContextHandle。 |
| OH_AI_API OH_AI_Status OH_AI_ModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context) | - | 通过模型文件加载并编译MindSpore Lite模型。  注意，同一个OH_AI_ContextHandle对象仅能传递给OH_AI_ModelBuild或者OH_AI_ModelBuildFromFile一次，如果多次调用该函数需要创建多个不同的OH_AI_ContextHandle。 |
| OH_AI_API OH_AI_Status OH_AI_ModelResize(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_ShapeInfo *shape_infos, size_t shape_info_num) | - | 调整已编译模型的输入形状。 |
| OH_AI_API OH_AI_Status OH_AI_ModelPredict(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_TensorHandleArray *outputs, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after) | - | 执行模型推理。 |
| OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetInputs(const OH_AI_ModelHandle model) | - | 获取模型的输入张量数组结构体。 |
| OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetOutputs(const OH_AI_ModelHandle model) | - | 获取模型的输出张量数组结构体。 |
| OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetInputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name) | - | 通过张量名获取模型的输入张量。 |
| OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetOutputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name) | - | 通过张量名获取模型的输出张量。 |
| OH_AI_API OH_AI_TrainCfgHandle OH_AI_TrainCfgCreate() | - | 创建训练配置对象指针，仅用于端侧训练。 |
| OH_AI_API void OH_AI_TrainCfgDestroy(OH_AI_TrainCfgHandle *train_cfg) | - | 销毁训练配置对象指针，仅用于端侧训练。 |
| OH_AI_API char **OH_AI_TrainCfgGetLossName(OH_AI_TrainCfgHandle train_cfg, size_t *num) | - | 获取损失函数的名称列表，仅用于端侧训练。 |
| OH_AI_API void OH_AI_TrainCfgSetLossName(OH_AI_TrainCfgHandle train_cfg, const char **loss_name, size_t num) | - | 设置损失函数的名称列表，仅用于端侧训练。 |
| OH_AI_API OH_AI_OptimizationLevel OH_AI_TrainCfgGetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg) | - | 获取训练配置的优化等级，仅用于端侧训练。 |
| OH_AI_API void OH_AI_TrainCfgSetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg, OH_AI_OptimizationLevel level) | - | 设置训练配置的优化等级，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_TrainModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg) | - | 从内存缓冲区加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_TrainModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type,const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg) | - | 根据路径读取加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_RunStep(OH_AI_ModelHandle model, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after) | - | 单步训练模型，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ModelSetLearningRate(OH_AI_ModelHandle model, float learning_rate) | - | 设置训练的学习率，仅用于端侧训练。 |
| OH_AI_API float OH_AI_ModelGetLearningRate(OH_AI_ModelHandle model) | - | 获取训练的学习率，仅用于端侧训练。 |
| OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetWeights(OH_AI_ModelHandle model) | - | 获取模型的所有权重Tensors，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ModelUpdateWeights(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray new_weights) | - | 更新模型的权重Tensor内容，仅用于端侧训练。 |
| OH_AI_API bool OH_AI_ModelGetTrainMode(OH_AI_ModelHandle model) | - | 获取训练模式。 |
| OH_AI_API OH_AI_Status OH_AI_ModelSetTrainMode(OH_AI_ModelHandle model, bool train) | - | 设置训练模式，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ModelSetupVirtualBatch(OH_AI_ModelHandle model, int virtual_batch_multiplier, float lr,float momentum) | - | 设置虚拟batch用于训练，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ExportModel(OH_AI_ModelHandle model, OH_AI_ModelType model_type, const char *model_file,OH_AI_QuantizationType quantization_type, bool export_inference_only,char **output_tensor_name, size_t num) | - | 导出训练模型，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ExportModelBuffer(OH_AI_ModelHandle model, OH_AI_ModelType model_type, void *model_data,size_t *data_size, OH_AI_QuantizationType quantization_type,bool export_inference_only, char **output_tensor_name, size_t num) | - | 导出训练模型内存缓存，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ExportWeightsCollaborateWithMicro(OH_AI_ModelHandle model, OH_AI_ModelType model_type,const char *weight_file, bool is_inference,bool enable_fp16, char **changeable_weights_name,size_t num) | - | 导出模型权重，只能用于micro推理，仅用于端侧训练。 |
| OH_AI_API OH_AI_Status OH_AI_ModelLoadConfig(OH_AI_ModelHandle model, const char *config_path) | - | 加载模型配置文件。 |
| OH_AI_API OH_AI_Status OH_AI_ModelPredictWithConfig(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs, OH_AI_TensorHandleArray *outputs, const char *config, const OH_AI_KernelCallBack before, const OH_AI_KernelCallBack after) | - | 执行模型推理，支持每次推理设置不同推理参数。 |

**函数说明**

**OH_AI_KernelCallBack()**

```ets
typedef bool (*OH_AI_KernelCallBack)(const OH_AI_TensorHandleArray inputs, const OH_AI_TensorHandleArray outputs,const OH_AI_CallBackParam kernel_Info)
```

描述

回调函数指针。

该函数指针是用于设置[OH_AI_ModelPredict](model.h.md#ZH-CN_TOPIC_0000002522082582__oh_ai_modelpredict)函数参数中的两个回调函数。

该指针指向的函数需要包含三个参数，其中inputs和outputs对应了算子的输入和输出张量，kernel_Info表示当前算子的信息。

可以通过回调函数监控算子执行的情况，例如统计算子的执行时间，校验算子的正确性等等。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_AI_TensorHandleArray inputs | 模型输入对应的张量数组结构体。 |
| const OH_AI_TensorHandleArray outputs | 模型输出对应的张量数组结构体。 |
| const OH_AI_CallBackParam kernel_Info | 当前算子的信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 回调执行是否成功，若成功返回true，失败则返回false。 |

**OH_AI_ModelCreate()**

```ets
OH_AI_API OH_AI_ModelHandle OH_AI_ModelCreate(void)
```

描述

创建一个模型对象。

起始版本： 9

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_ModelHandle | 模型对象指针。 |

**OH_AI_ModelDestroy()**

```ets
OH_AI_API void OH_AI_ModelDestroy(OH_AI_ModelHandle *model)
```

描述

释放一个模型对象。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle *model | 模型对象指针。 |

**OH_AI_ModelBuild()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context)
```

描述

从内存缓冲区加载并编译MindSpore Lite模型。

注意，同一个[OH_AI_ContextHandle](OH_AI_ContextHandle.md)对象仅能传递给[OH_AI_ModelBuild](model.h.md#ZH-CN_TOPIC_0000002522082582__oh_ai_modelbuild)或者[OH_AI_ModelBuildFromFile](model.h.md#ZH-CN_TOPIC_0000002522082582__oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH_AI_ContextHandle](OH_AI_ContextHandle.md)。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const void *model_data | 内存中已经加载的模型数据地址。 |
| size_t data_size | 模型数据的长度。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const OH_AI_ContextHandle model_context | 模型运行时的上下文环境，具体见 OH_AI_ContextHandle。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelBuildFromFile()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context)
```

描述

通过模型文件加载并编译MindSpore Lite模型。

注意，同一个[OH_AI_ContextHandle](OH_AI_ContextHandle.md)对象仅能传递给[OH_AI_ModelBuild](model.h.md#ZH-CN_TOPIC_0000002522082582__oh_ai_modelbuild)或者[OH_AI_ModelBuildFromFile](model.h.md#ZH-CN_TOPIC_0000002522082582__oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH_AI_ContextHandle](OH_AI_ContextHandle.md)。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const char *model_path | 模型文件路径。字符串长度限制跟随文件系统。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const OH_AI_ContextHandle model_context | 模型运行时的上下文环境，具体见 OH_AI_ContextHandle。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelResize()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelResize(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_ShapeInfo *shape_infos, size_t shape_info_num)
```

描述

调整已编译模型的输入形状。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const OH_AI_TensorHandleArray inputs | 模型输入对应的张量数组结构体。 |
| OH_AI_ShapeInfo *shape_infos | 输入形状信息数组，按模型输入顺序排列的由形状信息组成的数组，模型会按顺序依次调整张量形状。 |
| size_t shape_info_num | 形状信息数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelPredict()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelPredict(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_TensorHandleArray *outputs, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after)
```

描述

执行模型推理。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const OH_AI_TensorHandleArray inputs | 模型输入对应的张量数组结构体。 |
| OH_AI_TensorHandleArray *outputs | 模型输出对应的张量数组结构体的指针。 |
| const OH_AI_KernelCallBack before | 模型推理前执行的回调函数。 |
| const OH_AI_KernelCallBack after | 模型推理后执行的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelGetInputs()**

```ets
OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetInputs(const OH_AI_ModelHandle model)
```

描述

获取模型的输入张量数组结构体。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_AI_ModelHandle model | 模型对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TensorHandleArray | 模型输入对应的张量数组结构体。 |

**OH_AI_ModelGetOutputs()**

```ets
OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetOutputs(const OH_AI_ModelHandle model)
```

描述

获取模型的输出张量数组结构体。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_AI_ModelHandle model | 模型对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TensorHandleArray | 模型输出对应的张量数组结构体。 |

**OH_AI_ModelGetInputByTensorName()**

```ets
OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetInputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name)
```

描述

通过张量名获取模型的输入张量。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_AI_ModelHandle model | 模型对象指针。 |
| const char *tensor_name | 张量名称。字符串长度跟随系统限制。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TensorHandle | tensor_name所对应的输入张量的张量指针，如果输入中没有该张量则返回空。 |

**OH_AI_ModelGetOutputByTensorName()**

```ets
OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetOutputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name)
```

描述

通过张量名获取模型的输出张量。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_AI_ModelHandle model | 模型对象指针。 |
| const char *tensor_name | 张量名称。字符串长度跟随系统限制。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TensorHandle | tensor_name所对应的输入张量的张量指针，如果输出中没有该张量则返回空。 |

**OH_AI_TrainCfgCreate()**

```ets
OH_AI_API OH_AI_TrainCfgHandle OH_AI_TrainCfgCreate()
```

描述

创建训练配置对象指针，仅用于端侧训练。

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TrainCfgHandle | 训练配置对象指针。 |

**OH_AI_TrainCfgDestroy()**

```ets
OH_AI_API void OH_AI_TrainCfgDestroy(OH_AI_TrainCfgHandle *train_cfg)
```

描述

销毁训练配置对象指针，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_TrainCfgHandle *train_cfg | 训练配置对象指针。 |

**OH_AI_TrainCfgGetLossName()**

```ets
OH_AI_API char **OH_AI_TrainCfgGetLossName(OH_AI_TrainCfgHandle train_cfg, size_t *num)
```

描述

获取损失函数的名称列表，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |
| size_t *num | 损失函数数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API char ** | 损失函数的名称列表。 |

**OH_AI_TrainCfgSetLossName()**

```ets
OH_AI_API void OH_AI_TrainCfgSetLossName(OH_AI_TrainCfgHandle train_cfg, const char **loss_name, size_t num)
```

描述

设置损失函数的名称列表，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |
| const char **loss_name | 损失函数的名称列表。 |
| size_t num | 损失函数数量。 |

**OH_AI_TrainCfgGetOptimizationLevel()**

```ets
OH_AI_API OH_AI_OptimizationLevel OH_AI_TrainCfgGetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg)
```

描述

获取训练配置的优化等级，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_OptimizationLevel | 优化等级。 |

**OH_AI_TrainCfgSetOptimizationLevel()**

```ets
OH_AI_API void OH_AI_TrainCfgSetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg, OH_AI_OptimizationLevel level)
```

描述

设置训练配置的优化等级，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |
| OH_AI_OptimizationLevel level | 优化等级。 |

**OH_AI_TrainModelBuild()**

```ets
OH_AI_API OH_AI_Status OH_AI_TrainModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg)
```

描述

从内存缓冲区加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const void *model_data | 指向存储读入模型文件缓冲区的指针。 |
| size_t data_size | 缓冲区大小。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const OH_AI_ContextHandle model_context | 模型运行时的上下文环境，具体见 OH_AI_ContextHandle。 |
| const OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_TrainModelBuildFromFile()**

```ets
OH_AI_API OH_AI_Status OH_AI_TrainModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type,const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg)
```

描述

根据路径读取加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const char *model_path | 模型文件路径。字符串长度限制跟随文件系统。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const OH_AI_ContextHandle model_context | 模型运行时的上下文环境，具体见 OH_AI_ContextHandle。 |
| const OH_AI_TrainCfgHandle train_cfg | 训练配置对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_RunStep()**

```ets
OH_AI_API OH_AI_Status OH_AI_RunStep(OH_AI_ModelHandle model, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after)
```

描述

单步训练模型，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const OH_AI_KernelCallBack before | 模型推理前执行的回调函数。 |
| const OH_AI_KernelCallBack after | 模型推理后执行的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelSetLearningRate()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelSetLearningRate(OH_AI_ModelHandle model, float learning_rate)
```

描述

设置训练的学习率，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| float learning_rate | 学习率。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelGetLearningRate()**

```ets
OH_AI_API float OH_AI_ModelGetLearningRate(OH_AI_ModelHandle model)
```

描述

获取训练的学习率，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API float | 学习率，没有设置优化器时为0.0。 |

**OH_AI_ModelGetWeights()**

```ets
OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetWeights(OH_AI_ModelHandle model)
```

描述

获取模型的所有权重Tensors，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_TensorHandleArray | 模型的所有权重Tensor。 |

**OH_AI_ModelUpdateWeights()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelUpdateWeights(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray new_weights)
```

描述

更新模型的权重Tensor内容，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const OH_AI_TensorHandleArray new_weights | 要更新的权重Tensor。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelGetTrainMode()**

```ets
OH_AI_API bool OH_AI_ModelGetTrainMode(OH_AI_ModelHandle model)
```

描述

获取训练模式。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API bool | 表示是否是训练模式。true表示是训练模式，false表示不是训练模式。 |

**OH_AI_ModelSetTrainMode()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelSetTrainMode(OH_AI_ModelHandle model, bool train)
```

描述

设置训练模式，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| bool train | 是否为训练模式。true表示是训练模式，false表示不是训练模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelSetupVirtualBatch()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelSetupVirtualBatch(OH_AI_ModelHandle model, int virtual_batch_multiplier, float lr,float momentum)
```

描述

设置虚拟batch用于训练，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| int virtual_batch_multiplier | 虚拟batch乘法器，当设置值小于1时，表示禁用虚拟batch。长度跟随系统限制。 |
| float lr | 学习率，默认为-1.0f。 |
| float momentum | 动量，默认为-1.0f。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ExportModel()**

```ets
OH_AI_API OH_AI_Status OH_AI_ExportModel(OH_AI_ModelHandle model, OH_AI_ModelType model_type, const char *model_file,OH_AI_QuantizationType quantization_type, bool export_inference_only,char **output_tensor_name, size_t num)
```

描述

导出训练模型，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const char *model_file | 导出的模型文件路径。字符串长度限制跟随文件系统。 |
| OH_AI_QuantizationType quantization_type | 量化类型。 |
| bool export_inference_only | 是否导出推理模型。true表示导出推理模型，false表示不导出推理模型。 |
| char **output_tensor_name | 设置导出模型的输出Tensor，默认为空表示全量导出。 |
| size_t num | 输出Tensor的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ExportModelBuffer()**

```ets
OH_AI_API OH_AI_Status OH_AI_ExportModelBuffer(OH_AI_ModelHandle model, OH_AI_ModelType model_type, void *model_data,size_t *data_size, OH_AI_QuantizationType quantization_type,bool export_inference_only, char **output_tensor_name, size_t num)
```

描述

导出训练模型内存缓存，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| void *model_data | 指向导出模型文件缓冲区的指针。 |
| size_t *data_size | 缓冲区大小。 |
| OH_AI_QuantizationType quantization_type | 量化类型。 |
| bool export_inference_only | 是否导出推理模型。true表示导出推理模型，false表示不导出推理模型。 |
| char **output_tensor_name | 设置导出模型的输出Tensor，默认为空表示全量导出。 |
| size_t num | 输出Tensor的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ExportWeightsCollaborateWithMicro()**

```ets
OH_AI_API OH_AI_Status OH_AI_ExportWeightsCollaborateWithMicro(OH_AI_ModelHandle model, OH_AI_ModelType model_type,const char *weight_file, bool is_inference,bool enable_fp16, char **changeable_weights_name,size_t num)
```

描述

导出模型权重，只能用于micro推理，仅用于端侧训练。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| OH_AI_ModelType model_type | 模型文件类型，具体见OH_AI_ModelType。 |
| const char *weight_file | 导出的权重文件路径。字符串长度限制跟随文件系统。 |
| bool is_inference | 是否导出推理模型，当前只支持设置为true。 |
| bool enable_fp16 | 浮点权重是否保存为float16格式。true表示保存为float16格式，false表示不保存为float16格式。 |
| char **changeable_weights_name | shape可变的权重Tensor名称。 |
| size_t num | shape可变的权重Tensor名称的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelLoadConfig()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelLoadConfig(OH_AI_ModelHandle model, const char *config_path);
```

描述

加载模型配置文件。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const char *config_path | 配置文件路径。字符串长度限制跟随文件系统。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |

**OH_AI_ModelPredictWithConfig()**

```ets
OH_AI_API OH_AI_Status OH_AI_ModelPredictWithConfig(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs, OH_AI_TensorHandleArray *outputs, const char *config, const OH_AI_KernelCallBack before, const OH_AI_KernelCallBack after)

```

描述

执行模型推理，支持每次推理设置不同推理参数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AI_ModelHandle model | 模型对象指针。 |
| const OH_AI_TensorHandleArray inputs | 模型输入对应的张量数组结构体。 |
| OH_AI_TensorHandleArray *outputs | 模型输出对应的张量数组结构体的指针。 |
| const char *config | 模型配置文件。字符串长度限制跟随文件系统。 |
| const OH_AI_KernelCallBack before | 模型推理前执行的回调函数。 |
| after | 模型推理后执行的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AI_API OH_AI_Status | 枚举类型的状态码OH_AI_Status，若成功返回OH_AI_STATUS_SUCCESS，失败则返回具体错误码。 |