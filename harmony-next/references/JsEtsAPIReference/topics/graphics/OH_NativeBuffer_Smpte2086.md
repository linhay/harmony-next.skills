# OH_NativeBuffer_Smpte2086

```ets
typedef struct OH_NativeBuffer_Smpte2086 {...} OH_NativeBuffer_Smpte2086
```

**概述**

表示smpte2086静态元数据。

起始版本： 12

相关模块： [OH_NativeBuffer](OH_NativeBuffer.md)

所在头文件： [buffer_common.h](buffer_common.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_NativeBuffer_ColorXY displayPrimaryRed | 红基色。 |
| OH_NativeBuffer_ColorXY displayPrimaryGreen | 绿基色。 |
| OH_NativeBuffer_ColorXY displayPrimaryBlue | 蓝基色。 |
| OH_NativeBuffer_ColorXY whitePoint | 白点。 |
| float maxLuminance | 最大的光亮度。 |
| float minLuminance | 最小的光亮度。 |