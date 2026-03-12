# OH_NativeBuffer_Config

```ets
typedef struct {...} OH_NativeBuffer_Config
```

#### 概述

OH_NativeBuffer的属性配置，用于申请新的OH_NativeBuffer实例或查询现有实例的相关属性。

**起始版本：** 9

**相关模块：**[OH_NativeBuffer](OH_NativeBuffer.md)

**所在头文件：**[native_buffer.h](native_buffer.h.md)

#### 汇总

#### 成员变量

名称描述int32_t width宽度（像素）。int32_t height高度（像素）。int32_t format像素格式，具体可参见[OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)枚举。int32_t usagebuffer的用途说明，具体可参见[OH_NativeBuffer_Usage](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_usage)枚举。int32_t stride

输出参数。本地窗口缓冲区步幅，单位为Byte。

**起始版本：** 10