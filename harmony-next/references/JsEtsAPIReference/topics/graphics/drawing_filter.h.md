# drawing_filter.h

**概述**

声明与绘图模块中的滤波器对象相关的函数。

引用文件： <native_drawing/drawing_filter.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Filter* OH_Drawing_FilterCreate(void) | 创建一个滤波器对象。 |
| void OH_Drawing_FilterSetImageFilter(OH_Drawing_Filter* filter, OH_Drawing_ImageFilter* imageFilter) | 为滤波器对象设置图像滤波器对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_FilterSetMaskFilter(OH_Drawing_Filter* filter, OH_Drawing_MaskFilter* maskFilter) | 为滤波器对象设置蒙版滤波器对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_FilterSetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter) | 为滤波器对象设置颜色滤波器对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_FilterGetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter) | 从滤波器对象获取颜色滤波器对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 filter、colorFilter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_FilterDestroy(OH_Drawing_Filter* filter) | 销毁滤波器对象，并收回该对象占用的内存。 |

**函数说明**

**OH_Drawing_FilterCreate()**

```ets
OH_Drawing_Filter* OH_Drawing_FilterCreate(void)
```

描述

创建一个滤波器对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Filter* | 返回创建的滤波器对象的指针。 |

**OH_Drawing_FilterSetImageFilter()**

```ets
void OH_Drawing_FilterSetImageFilter(OH_Drawing_Filter* filter, OH_Drawing_ImageFilter* imageFilter)
```

描述

为滤波器对象设置图像滤波器对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Filter* filter | 指示指向滤波器对象OH_Drawing_Filter的指针。 |
| OH_Drawing_ImageFilter* imageFilter | 指示指向图像滤波器OH_Drawing_ImageFilter对象的指针，为NULL表示清空滤波器对象中的图像滤波器效果。 |

**OH_Drawing_FilterSetMaskFilter()**

```ets
void OH_Drawing_FilterSetMaskFilter(OH_Drawing_Filter* filter, OH_Drawing_MaskFilter* maskFilter)
```

描述

为滤波器对象设置蒙版滤波器对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Filter* filter | 指示指向滤波器对象OH_Drawing_Filter的指针。 |
| OH_Drawing_MaskFilter* maskFilter | 指示指向蒙版滤波器对象OH_Drawing_ColorFilter的指针，为NULL表示清空滤波器对象中的蒙版滤波器效果。 |

**OH_Drawing_FilterSetColorFilter()**

```ets
void OH_Drawing_FilterSetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter)
```

描述

为滤波器对象设置颜色滤波器对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Filter* filter | 指示指向滤波器对象OH_Drawing_Filter的指针。 |
| OH_Drawing_ColorFilter* colorFilter | 指示指向颜色滤波器对象OH_Drawing_ColorFilter的指针，为NULL表示清空滤波器对象中的颜色滤波器效果。 |

**OH_Drawing_FilterGetColorFilter()**

```ets
void OH_Drawing_FilterGetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter)
```

描述

从滤波器对象获取颜色滤波器对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

filter、colorFilter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Filter* filter | 指示指向滤波器对象OH_Drawing_Filter的指针。 |
| OH_Drawing_ColorFilter* colorFilter | 指示指向颜色滤波器对象OH_Drawing_ColorFilter的指针。 |

**OH_Drawing_FilterDestroy()**

```ets
void OH_Drawing_FilterDestroy(OH_Drawing_Filter* filter)
```

描述

销毁滤波器对象，并收回该对象占用的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Filter* filter | 指示指向滤波器对象OH_Drawing_Filter的指针。 |