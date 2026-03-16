# OH_Drawing_Image_Info

```ets
typedef struct {...} OH_Drawing_Image_Info
```

#### 概述

定义图片信息结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

**所在头文件：**[drawing_types.h](../../capi/headers/drawing_types.h.md)

#### 汇总

#### 成员变量

名称描述int32_t width宽度，单位为像素。int32_t height高度，单位为像素。[OH_Drawing_ColorFormat](../../capi/headers/drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_colorformat) colorType颜色类型[OH_Drawing_ColorFormat](../../capi/headers/drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_colorformat)。[OH_Drawing_AlphaFormat](../../capi/headers/drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_alphaformat) alphaType透明度类型[OH_Drawing_AlphaFormat](../../capi/headers/drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_alphaformat)。