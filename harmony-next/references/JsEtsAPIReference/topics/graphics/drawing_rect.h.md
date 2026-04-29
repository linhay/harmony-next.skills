# drawing_rect.h

**概述**

文件中定义了与矩形相关的功能函数。

相关示例： [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

引用文件： <native_drawing/drawing_rect.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Rect* OH_Drawing_RectCreate(float left, float top, float right, float bottom) | 用于创建一个矩形对象，不会对设置的坐标排序，即允许矩形设置的左上角坐标大于对应的矩形右下角坐标。 |
| bool OH_Drawing_RectIntersect(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other) | 用于判断两个矩形是否相交，若相交，将rect设置为两个矩形的交集。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_RectJoin(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other) | 将两个矩形取并集。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectSetLeft(OH_Drawing_Rect* rect, float left) | 用于设置矩形左上角的横坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectSetTop(OH_Drawing_Rect* rect, float top) | 用于设置矩形左上角的纵坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectSetRight(OH_Drawing_Rect* rect, float right) | 用于设置矩形右下角的横坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectSetBottom(OH_Drawing_Rect* rect, float bottom) | 用于设置矩形右下角的纵坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetLeft(OH_Drawing_Rect* rect) | 用于获取给矩形设置的左上角的横坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetTop(OH_Drawing_Rect* rect) | 用于获取给矩形设置的左上角的纵坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetRight(OH_Drawing_Rect* rect) | 用于获取给矩形设置的右下角的横坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetBottom(OH_Drawing_Rect* rect) | 用于获取给矩形设置的右下角的纵坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetHeight(OH_Drawing_Rect* rect) | 用于获取矩形对象高度，计算方式为设置的矩形的右下角纵坐标减去左上角纵坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| float OH_Drawing_RectGetWidth(OH_Drawing_Rect* rect) | 用于获取矩形对象的宽度，计算方式为设置的矩形的右下角横坐标减去左上角横坐标。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectCopy(OH_Drawing_Rect* src, OH_Drawing_Rect* dst) | 用于将源矩形对象复制到目标矩形对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RectDestroy(OH_Drawing_Rect* rect) | 用于销毁矩形对象并回收该对象占有的内存。 |
| OH_Drawing_Array* OH_Drawing_RectCreateArray(size_t size) | 用于创建一个矩形数组对象，用来存储多个矩形对象。不再需要OH_Drawing_Array时，请使用OH_Drawing_RectDestroyArray接口释放该对象的指针。 |
| OH_Drawing_ErrorCode OH_Drawing_RectGetArraySize(OH_Drawing_Array* rectArray, size_t* pSize) | 用于获取矩形数组对象OH_Drawing_Array的大小。 |
| OH_Drawing_ErrorCode OH_Drawing_RectGetArrayElement(OH_Drawing_Array* rectArray, size_t index,OH_Drawing_Rect** rect) | 用于获取矩形数组对象中指定索引的矩形对象。 |
| OH_Drawing_ErrorCode OH_Drawing_RectDestroyArray(OH_Drawing_Array* rectArray) | 用于销毁矩形数组对象并回收该对象占有的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_RectContains(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other, bool* isContains) | 用于判断一个矩形是否完全包含另外一个矩形。 |
| OH_Drawing_ErrorCode OH_Drawing_RectInset(OH_Drawing_Rect* rect, float left, float top, float right, float bottom) | 将指定的值添加到矩形边界。 |
| OH_Drawing_ErrorCode OH_Drawing_RectIsEmpty(const OH_Drawing_Rect* rect, bool* isEmpty) | 判断矩形是否为空。 |
| OH_Drawing_ErrorCode OH_Drawing_RectOffset(OH_Drawing_Rect* rect, float dx, float dy) | 将矩形分别沿x轴方向和y轴方向偏移一定距离。 |
| OH_Drawing_ErrorCode OH_Drawing_RectOffsetTo(OH_Drawing_Rect* rect, float newLeft, float newTop) | 将矩形偏移到特定位置，并保持宽度和高度不变。 |
| OH_Drawing_ErrorCode OH_Drawing_RectSetEmpty(OH_Drawing_Rect* rect) | 将矩形置空（矩形左上角和右下角的x轴、y轴坐标都置为0）。 |
| OH_Drawing_ErrorCode OH_Drawing_RectSort(OH_Drawing_Rect* rect) | 将矩形坐标按照实际位置排序。 若左上角x轴坐标大于右下角x轴坐标，则交换两者；若左上角y轴坐标大于右下角y轴坐标，则交换两者。如果坐标已经有序，则不执行任何操作。 |
| OH_Drawing_ErrorCode OH_Drawing_RectUnion(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other) | 将当前矩形设置为本矩形与另一个矩形的并集。 |

**函数说明**

**OH_Drawing_RectCreate()**

```ets
OH_Drawing_Rect* OH_Drawing_RectCreate(float left, float top, float right, float bottom)
```

描述

用于创建一个矩形对象，不会对设置的坐标排序，即允许矩形设置的左上角坐标大于对应的矩形右下角坐标。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| float left | 矩形左上角的横坐标。 |
| float top | 矩形左上角的纵坐标。 |
| float right | 矩形右下角的横坐标。 |
| float bottom | 矩形右下角的纵坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Rect* | 函数会返回一个指针，指针指向创建的矩形对象。 |

**OH_Drawing_RectIntersect()**

```ets
bool OH_Drawing_RectIntersect(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

描述

用于判断两个矩形是否相交，若相交，将rect设置为两个矩形的交集。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| const OH_Drawing_Rect* other | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个矩形是否相交的结果。true表示这两个矩形相交，rect被设置为两个矩形的交集；false表示不相交，rect保持不变。 |

**OH_Drawing_RectJoin()**

```ets
bool OH_Drawing_RectJoin(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

描述

将两个矩形取并集。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| const OH_Drawing_Rect* other | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个矩形取并集的结果。true表示成功，false表示失败，失败的原因可能是两个矩形至少有一个为NULL或者other矩形大小为空。 |

**OH_Drawing_RectSetLeft()**

```ets
void OH_Drawing_RectSetLeft(OH_Drawing_Rect* rect, float left)
```

描述

用于设置矩形左上角的横坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| float left | 矩形左上角的横坐标。 |

**OH_Drawing_RectSetTop()**

```ets
void OH_Drawing_RectSetTop(OH_Drawing_Rect* rect, float top)
```

描述

用于设置矩形左上角的纵坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| float top | 矩形左上角的纵坐标。 |

**OH_Drawing_RectSetRight()**

```ets
void OH_Drawing_RectSetRight(OH_Drawing_Rect* rect, float right)
```

描述

用于设置矩形右下角的横坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| float right | 矩形右下角的横坐标。 |

**OH_Drawing_RectSetBottom()**

```ets
void OH_Drawing_RectSetBottom(OH_Drawing_Rect* rect, float bottom)
```

描述

用于设置矩形右下角的纵坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |
| float bottom | 矩形右下角的纵坐标。 |

**OH_Drawing_RectGetLeft()**

```ets
float OH_Drawing_RectGetLeft(OH_Drawing_Rect* rect)
```

描述

用于获取给矩形设置的左上角的横坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 矩形左上角的横坐标。 |

**OH_Drawing_RectGetTop()**

```ets
float OH_Drawing_RectGetTop(OH_Drawing_Rect* rect)
```

描述

用于获取给矩形设置的左上角的纵坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 矩形左上角的纵坐标。 |

**OH_Drawing_RectGetRight()**

```ets
float OH_Drawing_RectGetRight(OH_Drawing_Rect* rect)
```

描述

用于获取给矩形设置的右下角的横坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 矩形右下角的横坐标。 |

**OH_Drawing_RectGetBottom()**

```ets
float OH_Drawing_RectGetBottom(OH_Drawing_Rect* rect)
```

描述

用于获取给矩形设置的右下角的纵坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 矩形右下角的纵坐标。 |

**OH_Drawing_RectGetHeight()**

```ets
float OH_Drawing_RectGetHeight(OH_Drawing_Rect* rect)
```

描述

用于获取矩形对象高度，计算方式为设置的矩形的右下角纵坐标减去左上角纵坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形对象的高度，单位为像素。 |

**OH_Drawing_RectGetWidth()**

```ets
float OH_Drawing_RectGetWidth(OH_Drawing_Rect* rect)
```

描述

用于获取矩形对象的宽度，计算方式为设置的矩形的右下角横坐标减去左上角横坐标。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 返回矩形对象的宽度，单位为像素。 |

**OH_Drawing_RectCopy()**

```ets
void OH_Drawing_RectCopy(OH_Drawing_Rect* src, OH_Drawing_Rect* dst)
```

描述

用于将源矩形对象复制到目标矩形对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* src | 指向源矩形对象的指针。 |
| OH_Drawing_Rect* dst | 指向目标矩形对象的指针。 |

**OH_Drawing_RectDestroy()**

```ets
void OH_Drawing_RectDestroy(OH_Drawing_Rect* rect)
```

描述

用于销毁矩形对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

**OH_Drawing_RectCreateArray()**

```ets
OH_Drawing_Array* OH_Drawing_RectCreateArray(size_t size)
```

描述

用于创建一个矩形数组对象，用来存储多个矩形对象。不再需要[OH_Drawing_Array](OH_Drawing_Array.md)时，请使用[OH_Drawing_RectDestroyArray](drawing_rect.h.md#ZH-CN_TOPIC_0000002522082162__oh_drawing_rectdestroyarray)接口释放该对象的指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| size_t size | 指定矩形数组的大小，不超过字形索引数量最大值65536。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回创建的数组对象OH_Drawing_Array指针，如果返回的对象指针为空，表示创建失败。  失败的原因可能为：没有可用的内存或参数错误。 |

**OH_Drawing_RectGetArraySize()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectGetArraySize(OH_Drawing_Array* rectArray, size_t* pSize)
```

描述

用于获取矩形数组对象[OH_Drawing_Array](OH_Drawing_Array.md)的大小。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* rectArray | 指向矩形数组对象OH_Drawing_Array的指针。 |
| size_t* pSize | 指向size_t类型的指针，用于存储矩形数组大小，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数rectArray或者pSize为空。 |

**OH_Drawing_RectGetArrayElement()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectGetArrayElement(OH_Drawing_Array* rectArray, size_t index,OH_Drawing_Rect** rect)
```

描述

用于获取矩形数组对象中指定索引的矩形对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* rectArray | 指向矩形数组对象OH_Drawing_Array的指针。 |
| size_t index | 矩形数组的索引。 |
| OH_Drawing_Rect** rect | 指向OH_Drawing_Rect的二级指针，作为出参，返回给调用者。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数rectArray或者rect为空，或者index越界。 |

**OH_Drawing_RectDestroyArray()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectDestroyArray(OH_Drawing_Array* rectArray)
```

描述

用于销毁矩形数组对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* rectArray | 指向矩形数组对象OH_Drawing_Array的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数rectArray为空。 |

**OH_Drawing_RectContains()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectContains(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other, bool* isContains)
```

描述

用于判断一个矩形是否完全包含另外一个矩形。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。此矩形用于判断是否包含另一个矩形（other）。 |
| const OH_Drawing_Rect* other | 指向矩形对象OH_Drawing_Rect的指针。此矩形用于判断是否被另一个矩形（rect）所包含。 |
| bool* isContains | 表示一个矩形是否完全包含另外一个矩形的结果，作为出参使用。true表示rect完全包含other，false表示rect不完全包含other。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数rect或other或isContains为空。 |

**OH_Drawing_RectInset()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectInset(OH_Drawing_Rect* rect, float left, float top, float right, float bottom)
```

描述

将指定的值添加到矩形边界。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| float left | 添加到矩形左边界的值（矩形左上角横坐标）。 |
| float top | 添加到矩形上边界的值（矩形左上角纵坐标）。 |
| float right | 添加到矩形右边界的值（矩形右下角横坐标）。 |
| float bottom | 添加到矩形下边界的值（矩形右下角纵坐标）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数rect为空。 |

**OH_Drawing_RectIsEmpty()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectIsEmpty(const OH_Drawing_Rect* rect, bool* isEmpty)
```

描述

判断矩形是否为空。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| bool* isEmpty | 表示矩形是否为空。作为出参使用。true表示矩形为空，false表示矩形不为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect或isEmpty是空指针。 |

**OH_Drawing_RectOffset()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectOffset(OH_Drawing_Rect* rect, float dx, float dy)
```

描述

将矩形分别沿x轴方向和y轴方向偏移一定距离。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| float dx | 表示在x轴上的偏移距离。正数表示沿x轴正方向偏移，负数表示沿x轴负方向偏移。 |
| float dy | 表示在y轴上的偏移距离。正数表示沿y轴正方向偏移，负数表示沿y轴负方向偏移。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect是空指针。 |

**OH_Drawing_RectOffsetTo()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectOffsetTo(OH_Drawing_Rect* rect, float newLeft, float newTop)
```

描述

将矩形偏移到特定位置，并保持宽度和高度不变。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| float newLeft | 表示偏移后矩形左上角的x轴坐标。 |
| float newTop | 表示偏移后矩形左上角的y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect是空指针。 |

**OH_Drawing_RectSetEmpty()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectSetEmpty(OH_Drawing_Rect* rect)
```

描述

将矩形置空（矩形左上角和右下角的x轴、y轴坐标都置为0）。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect是空指针。 |

**OH_Drawing_RectSort()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectSort(OH_Drawing_Rect* rect)
```

描述

将矩形坐标按照实际位置排序。

若左上角x轴坐标大于右下角x轴坐标，则交换两者；若左上角y轴坐标大于右下角y轴坐标，则交换两者。如果坐标已经有序，则不执行任何操作。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect是空指针。 |

**OH_Drawing_RectUnion()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RectUnion(OH_Drawing_Rect* rect, const OH_Drawing_Rect* other)
```

描述

将当前矩形设置为本矩形与另一个矩形的并集。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向当前矩形对象OH_Drawing_Rect的指针。 |
| const OH_Drawing_Rect* other | 指向另一个矩形对象OH_Drawing_Rect的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示rect或other是空指针。 |