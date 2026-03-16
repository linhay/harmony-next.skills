# OH_AI_TensorHandleArray

```ets
typedef struct OH_AI_TensorHandleArray {...} OH_AI_TensorHandleArray
```

#### 概述

张量数组结构体，用于存储张量数组指针和张量数组长度。

**起始版本：** 9

**相关模块：**[MindSpore](../misc/MindSpore.md)

**所在头文件：**[model.h](../../capi/headers/model.h.md)

#### 汇总

#### 成员变量

名称描述size_t handle_num张量数组长度。[OH_AI_TensorHandle](../misc/OH_AI_TensorHandle.md)* handle_list指向张量数组的指针。