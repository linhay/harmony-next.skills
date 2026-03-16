# OH_AVScreenCaptureHighlightConfig

```ets
typedef struct OH_AVScreenCaptureHighlightConfig {...} OH_AVScreenCaptureHighlightConfig
```

#### 概述

表示高亮边框的样式，包括高亮边框的模式、边框宽度和边框颜色。

**起始版本：** 22

**相关模块：**[AVScreenCapture](AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](../../capi/headers/native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_ScreenCaptureHighlightMode](../../capi/headers/native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_screencapturehighlightmode) mode高亮边框的模式，不设置默认为方形全包边框。uint32_t lineThickness高亮边框的宽度，不设置默认不显示线宽，宽度有效值范围在1vp-8vp。uint32_t lineColor高亮边框的颜色，不设置默认为黑色，颜色有效值为RGB（0-0xffffff）格式和非透明的ARGB（0xff000000-0xffffffff）格式。