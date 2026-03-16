# types.h

#### 概述

提供了MindSpore Lite支持的模型文件类型和设备类型。

**引用文件：** <mindspore/types.h>

**库：** libmindspore_lite_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：**[MindSpore](../../topics/misc/MindSpore.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NNRTDeviceDesc](../../topics/system-services/NNRTDeviceDesc.md)NNRTDeviceDescNNRt设备信息描述，包含设备ID，设备名称等信息。

#### 枚举

名称typedef关键字描述[OH_AI_ModelType](#ZH-CN_TOPIC_0000002497446160__oh_ai_modeltype)OH_AI_ModelType模型文件的类型。[OH_AI_DeviceType](#ZH-CN_TOPIC_0000002497446160__oh_ai_devicetype)OH_AI_DeviceType设备类型信息，包含了目前支持的设备类型。[OH_AI_NNRTDeviceType](#ZH-CN_TOPIC_0000002497446160__oh_ai_nnrtdevicetype)OH_AI_NNRTDeviceTypeNNRt管理的硬件设备类型。[OH_AI_PerformanceMode](#ZH-CN_TOPIC_0000002497446160__oh_ai_performancemode)OH_AI_PerformanceModeNNRt硬件的工作性能模式。[OH_AI_Priority](#ZH-CN_TOPIC_0000002497446160__oh_ai_priority)OH_AI_PriorityNNRt推理任务优先级。[OH_AI_OptimizationLevel](#ZH-CN_TOPIC_0000002497446160__oh_ai_optimizationlevel)OH_AI_OptimizationLevel训练优化等级。[OH_AI_QuantizationType](#ZH-CN_TOPIC_0000002497446160__oh_ai_quantizationtype)OH_AI_QuantizationType量化类型信息。

#### 枚举类型说明

#### OH_AI_ModelType

```ets
enum OH_AI_ModelType
```

**描述**

模型文件的类型。

**起始版本：** 9

枚举项描述OH_AI_MODELTYPE_MINDIR = 0模型类型是MindIR，对应的模型文件后缀为.ms。OH_AI_MODELTYPE_INVALID = 0xFFFFFFFF模型类型无效。

#### OH_AI_DeviceType

```ets
enum OH_AI_DeviceType
```

**描述**

设备类型信息，包含了目前支持的设备类型。

**起始版本：** 9

枚举项描述OH_AI_DEVICETYPE_CPU = 0设备类型是CPU。OH_AI_DEVICETYPE_GPUDevice type: GPU。预留选项，暂不支持。OH_AI_DEVICETYPE_KIRIN_NPU设备类型是麒麟NPU。预留选项，暂不支持。OH_AI_DEVICETYPE_NNRT = 60设备类型是NNRt。OH_AI_DEVICETYPE_INVALID = 100设备类型无效。

#### OH_AI_NNRTDeviceType

```ets
enum OH_AI_NNRTDeviceType
```

**描述**

NNRt管理的硬件设备类型。

**起始版本：** 10

枚举项描述OH_AI_NNRTDEVICE_OTHERS = 0设备类型不属于以下3种，则属于其它。OH_AI_NNRTDEVICE_CPU = 1CPU设备。OH_AI_NNRTDEVICE_GPU = 2GPU设备。OH_AI_NNRTDEVICE_ACCELERATOR = 3特定的加速设备。

#### OH_AI_PerformanceMode

```ets
enum OH_AI_PerformanceMode
```

**描述**

NNRt硬件的工作性能模式。

**起始版本：** 10

枚举项描述OH_AI_PERFORMANCE_NONE = 0无特殊设置。OH_AI_PERFORMANCE_LOW = 1低功耗模式。OH_AI_PERFORMANCE_MEDIUM = 2功耗-性能均衡模式。OH_AI_PERFORMANCE_HIGH = 3高性能模式。OH_AI_PERFORMANCE_EXTREME = 4极致性能模式。

#### OH_AI_Priority

```ets
enum OH_AI_Priority
```

**描述**

NNRt推理任务优先级。

**起始版本：** 10

枚举项描述OH_AI_PRIORITY_NONE = 0无优先级偏好。OH_AI_PRIORITY_LOW = 1低优先级任务。OH_AI_PRIORITY_MEDIUM = 2中优先级任务。OH_AI_PRIORITY_HIGH = 3高优先级。

#### OH_AI_OptimizationLevel

```ets
enum OH_AI_OptimizationLevel
```

**描述**

训练优化等级。

**起始版本：** 11

枚举项描述OH_AI_KO0 = 0无优化等级。OH_AI_KO2 = 2将网络转换为float16，保持批量归一化层和损失函数为float32。OH_AI_KO3 = 3将网络转换为float16，包括批量归一化层。OH_AI_KAUTO = 4根据设备选择优化等级。OH_AI_KOPTIMIZATIONTYPE = 0xFFFFFFFF无效优化等级。

#### OH_AI_QuantizationType

```ets
enum OH_AI_QuantizationType
```

**描述**

量化类型信息。

**起始版本：** 11

枚举项描述OH_AI_NO_QUANT = 0不做量化。OH_AI_WEIGHT_QUANT = 1权重量化。OH_AI_FULL_QUANT = 2全量化。OH_AI_UNKNOWN_QUANT_TYPE = 0xFFFFFFFF无效量化类型。