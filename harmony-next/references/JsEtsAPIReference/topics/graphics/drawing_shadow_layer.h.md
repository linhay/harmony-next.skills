# drawing_shadow_layer.h

**概述**

声明与绘图模块中的阴影层对象相关的函数。

引用文件： <native_drawing/drawing_shadow_layer.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_ShadowLayer* OH_Drawing_ShadowLayerCreate(float blurRadius, float x, float y, uint32_t color) | 创建一个阴影层对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 blurRadius小于等于0时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_ShadowLayerDestroy(OH_Drawing_ShadowLayer* shadowLayer) | 销毁阴影层对象，并收回该对象占用的内存。 |

**函数说明**

**OH_Drawing_ShadowLayerCreate()**

```ets
OH_Drawing_ShadowLayer* OH_Drawing_ShadowLayerCreate(float blurRadius, float x, float y, uint32_t color)
```

描述

创建一个阴影层对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

blurRadius小于等于0时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| float blurRadius | 表示阴影的半径，必须大于零。 |
| float x | 表示x轴上的偏移点。 |
| float y | 表示y轴上的偏移点。 |
| uint32_t color | 表示阴影的颜色。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ShadowLayer* | 返回创建的阴影层对象的指针。 |

**OH_Drawing_ShadowLayerDestroy()**

```ets
void OH_Drawing_ShadowLayerDestroy(OH_Drawing_ShadowLayer* shadowLayer)
```

描述

销毁阴影层对象，并收回该对象占用的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_ShadowLayer* shadowLayer | 表示指向阴影层对象的指针。 |