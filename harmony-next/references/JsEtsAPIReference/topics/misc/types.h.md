# types.h

**概述**

提供了MindSpore Lite支持的模型文件类型和设备类型。

引用文件： <mindspore/types.h>

库： libmindspore_lite_ndk.so

系统能力： SystemCapability.Ai.MindSpore

起始版本： 9

相关模块： [MindSpore](MindSpore.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NNRTDeviceDesc | NNRTDeviceDesc | NNRt设备信息描述，包含设备ID，设备名称等信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AI_ModelType | OH_AI_ModelType | 模型文件的类型。 |
| OH_AI_DeviceType | OH_AI_DeviceType | 设备类型信息，包含了目前支持的设备类型。 |
| OH_AI_NNRTDeviceType | OH_AI_NNRTDeviceType | NNRt管理的硬件设备类型。 |
| OH_AI_PerformanceMode | OH_AI_PerformanceMode | NNRt硬件的工作性能模式。 |
| OH_AI_Priority | OH_AI_Priority | NNRt推理任务优先级。 |
| OH_AI_OptimizationLevel | OH_AI_OptimizationLevel | 训练优化等级。 |
| OH_AI_QuantizationType | OH_AI_QuantizationType | 量化类型信息。 |

**枚举类型说明**

**OH_AI_ModelType**

```ets
enum OH_AI_ModelType
```

描述

模型文件的类型。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_MODELTYPE_MINDIR = 0 | 模型类型是MindIR，对应的模型文件后缀为.ms。 |
| OH_AI_MODELTYPE_INVALID = 0xFFFFFFFF | 模型类型无效。 |

**OH_AI_DeviceType**

```ets
enum OH_AI_DeviceType
```

描述

设备类型信息，包含了目前支持的设备类型。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_DEVICETYPE_CPU = 0 | 设备类型是CPU。 |
| OH_AI_DEVICETYPE_GPU | Device type: GPU。预留选项，暂不支持。 |
| OH_AI_DEVICETYPE_KIRIN_NPU | 设备类型是麒麟NPU。预留选项，暂不支持。 |
| OH_AI_DEVICETYPE_NNRT = 60 | 设备类型是NNRt。 |
| OH_AI_DEVICETYPE_INVALID = 100 | 设备类型无效。 |

**OH_AI_NNRTDeviceType**

```ets
enum OH_AI_NNRTDeviceType
```

描述

NNRt管理的硬件设备类型。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_NNRTDEVICE_OTHERS = 0 | 设备类型不属于以下3种，则属于其它。 |
| OH_AI_NNRTDEVICE_CPU = 1 | CPU设备。 |
| OH_AI_NNRTDEVICE_GPU = 2 | GPU设备。 |
| OH_AI_NNRTDEVICE_ACCELERATOR = 3 | 特定的加速设备。 |

**OH_AI_PerformanceMode**

```ets
enum OH_AI_PerformanceMode
```

描述

NNRt硬件的工作性能模式。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_PERFORMANCE_NONE = 0 | 无特殊设置。 |
| OH_AI_PERFORMANCE_LOW = 1 | 低功耗模式。 |
| OH_AI_PERFORMANCE_MEDIUM = 2 | 功耗-性能均衡模式。 |
| OH_AI_PERFORMANCE_HIGH = 3 | 高性能模式。 |
| OH_AI_PERFORMANCE_EXTREME = 4 | 极致性能模式。 |

**OH_AI_Priority**

```ets
enum OH_AI_Priority
```

描述

NNRt推理任务优先级。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_PRIORITY_NONE = 0 | 无优先级偏好。 |
| OH_AI_PRIORITY_LOW = 1 | 低优先级任务。 |
| OH_AI_PRIORITY_MEDIUM = 2 | 中优先级任务。 |
| OH_AI_PRIORITY_HIGH = 3 | 高优先级。 |

**OH_AI_OptimizationLevel**

```ets
enum OH_AI_OptimizationLevel
```

描述

训练优化等级。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_KO0 = 0 | 无优化等级。 |
| OH_AI_KO2 = 2 | 将网络转换为float16，保持批量归一化层和损失函数为float32。 |
| OH_AI_KO3 = 3 | 将网络转换为float16，包括批量归一化层。 |
| OH_AI_KAUTO = 4 | 根据设备选择优化等级。 |
| OH_AI_KOPTIMIZATIONTYPE = 0xFFFFFFFF | 无效优化等级。 |

**OH_AI_QuantizationType**

```ets
enum OH_AI_QuantizationType
```

描述

量化类型信息。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_NO_QUANT = 0 | 不做量化。 |
| OH_AI_WEIGHT_QUANT = 1 | 权重量化。 |
| OH_AI_FULL_QUANT = 2 | 全量化。 |
| OH_AI_UNKNOWN_QUANT_TYPE = 0xFFFFFFFF | 无效量化类型。 |