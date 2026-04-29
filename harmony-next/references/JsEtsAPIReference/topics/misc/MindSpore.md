# MindSpore

#### 概述

提供MindSpore Lite的模型推理相关接口，该模块下的接口是非线程安全的。

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

#### 文件汇总

| 名称 | 描述 |
| --- | --- |
| [context.h](context.h.md) | 提供了Context相关的接口，可以配置运行时信息，该接口是非线程安全的。 |
| [data_type.h](data_type.h.md) | 声明了张量的数据的类型。 |
| [format.h](format.h.md) | 提供张量数据的排列格式。 |
| [model.h](model.h.md) | 提供了模型相关接口，可以用于模型创建、模型推理等，该接口是非线程安全的。 |
| [status.h](status.h.md) | 提供了MindSpore Lite运行时的状态码。 |
| [tensor.h](tensor.h.md) | 提供了张量相关的接口，可用于创建和修改张量信息，该接口是非线程安全的。 |
| [types.h](types.h.md) | 提供了MindSpore Lite支持的模型文件类型和设备类型。 |
