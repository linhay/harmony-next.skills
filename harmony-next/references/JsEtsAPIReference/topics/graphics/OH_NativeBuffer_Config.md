# OH_NativeBuffer_Config

```ets
typedef struct {...} OH_NativeBuffer_Config
```

**概述**

OH_NativeBuffer的属性配置，用于申请新的OH_NativeBuffer实例或查询现有实例的相关属性。

起始版本： 9

相关模块： [OH_NativeBuffer](OH_NativeBuffer.md)

所在头文件： [native_buffer.h](native_buffer.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t width | 宽度（像素）。 |
| int32_t height | 高度（像素）。 |
| int32_t format | 像素格式，具体可参见OH_NativeBuffer_Format枚举。 |
| int32_t usage | buffer的用途说明，具体可参见OH_NativeBuffer_Usage枚举。 |
| int32_t stride | 输出参数。本地窗口缓冲区步幅，单位为Byte。 起始版本： 10 |