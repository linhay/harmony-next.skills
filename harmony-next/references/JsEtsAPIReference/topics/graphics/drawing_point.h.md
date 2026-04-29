# drawing_point.h

**概述**

文件中定义了与坐标点相关的功能函数。

引用文件： <native_drawing/drawing_point.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y) | 用于创建一个坐标点对象。 |
| OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x) | 用于获取点的x轴坐标。 |
| OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y) | 用于获取点的y轴坐标。 |
| OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y) | 用于设置点的x轴和y轴坐标。 |
| void OH_Drawing_PointDestroy(OH_Drawing_Point* point) | 用于销毁坐标点对象并回收该对象占有的内存。 |

**函数说明**

**OH_Drawing_PointCreate()**

```ets
OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y)
```

描述

用于创建一个坐标点对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| float x | X轴坐标。 |
| float y | Y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Point* | 函数会返回一个指针，指针指向创建的坐标点对象。 |

**OH_Drawing_PointGetX()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x)
```

描述

用于获取点的x轴坐标。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float* x | 表示点的x轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point或者x为空。 |

**OH_Drawing_PointGetY()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y)
```

描述

用于获取点的y轴坐标。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float* y | 表示点的y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point或者y为空。 |

**OH_Drawing_PointSet()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y)
```

描述

用于设置点的x轴和y轴坐标。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float x | 表示点的x轴坐标。 |
| float y | 表示点的y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point为空。 |

**OH_Drawing_PointDestroy()**

```ets
void OH_Drawing_PointDestroy(OH_Drawing_Point* point)
```

描述

用于销毁坐标点对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象的指针。 |