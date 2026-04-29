# NativeDisplayManager_CutoutInfo

```ets
typedef struct {...} NativeDisplayManager_CutoutInfo
```

#### 概述

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**相关模块：**[OH_DisplayManager](OH_DisplayManager.md)

所在头文件： [oh_display_info.h](oh_display_info.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32_t boundingRectsLength | 挖孔屏、刘海屏不可用屏幕区域长度。 |
| [NativeDisplayManager_Rect](NativeDisplayManager_Rect.md)* boundingRects | 挖孔屏、刘海屏等区域的边界矩形。 |
| [NativeDisplayManager_WaterfallDisplayAreaRects](NativeDisplayManager_WaterfallDisplayAreaRects.md) waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
