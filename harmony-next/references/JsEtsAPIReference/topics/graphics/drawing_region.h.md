# drawing_region.h

**概述**

定义了与区域相关的功能函数，包括区域的创建，边界设置和销毁等。

引用文件： <native_drawing/drawing_region.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

相关模块： [Drawing](Drawing.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_RegionOpMode | OH_Drawing_RegionOpMode | 区域操作类型枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Region* OH_Drawing_RegionCreate(void) | 用于创建一个区域对象，实现更精确的图形控制。 |
| OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region) | 用于创建一个区域对象的拷贝。 |
| bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y) | 判断区域是否包含指定坐标点。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op) | 将两个区域按照指定的区域操作类型合并。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect) | 用于尝试给区域对象设置矩形边界。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip) | 给区域对象设置为指定区域内路径表示的范围。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RegionDestroy(OH_Drawing_Region* region) | 用于销毁区域对象并回收该对象占有的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region) | 设置当前区域为空。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionGetBoundaryPath(const OH_Drawing_Region* region, OH_Drawing_Path* path) | 设置路径为区域的边界。如果区域为空，则路径也将为空。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionGetBounds(const OH_Drawing_Region* region, OH_Drawing_Rect* rect) | 获取包含该区域的最小边界矩形。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionIsComplex(const OH_Drawing_Region* region, bool* isComplex) | 检查该区域是否包含多个（两个及两个以上）矩形。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionIsEmpty(const OH_Drawing_Region* region, bool* isEmpty) | 检查该区域是否为空。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionIsRect(const OH_Drawing_Region* region, bool* isRect) | 检查该区域是否等同于一个矩形。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionQuickContains(const OH_Drawing_Region* region, int32_t left, int32_t top, int32_t right, int32_t bottom, bool* isContained) | 检查该区域是否等同于单个矩形并且包含指定的矩形。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionQuickReject(const OH_Drawing_Region* region, int32_t left, int32_t top, int32_t right, int32_t bottom, bool* isReject) | 检查当前区域是否为空或是否与指定矩形不相交。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionTranslate(OH_Drawing_Region* region, int32_t dx, int32_t dy) | 将当前区域在x轴和y轴上按指定距离平移。如果当前区域为空，则不执行任何操作。 |

**枚举类型说明**

**OH_Drawing_RegionOpMode**

```ets
enum OH_Drawing_RegionOpMode
```

描述

区域操作类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| REGION_OP_MODE_DIFFERENCE | 差集操作。 |
| REGION_OP_MODE_INTERSECT | 交集操作。 |
| REGION_OP_MODE_UNION | 并集操作。 |
| REGION_OP_MODE_XOR | 异或操作。 |
| REGION_OP_MODE_REVERSE_DIFFERENCE | 反向差集操作。 |
| REGION_OP_MODE_REPLACE | 替换操作。 |

**函数说明**

**OH_Drawing_RegionCreate()**

```ets
OH_Drawing_Region* OH_Drawing_RegionCreate(void)
```

描述

用于创建一个区域对象，实现更精确的图形控制。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Region* | 函数会返回一个指针，指针指向创建的区域对象OH_Drawing_Region。 |

**OH_Drawing_RegionCopy()**

```ets
OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region)
```

描述

用于创建一个区域对象的拷贝。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向用于拷贝的区域对象OH_Drawing_Region的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Region* | 函数会返回一个指针，指针指向创建的新区域对象。 |

**OH_Drawing_RegionContains()**

```ets
bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y)
```

描述

判断区域是否包含指定坐标点。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| int32_t x | 表示指定坐标点的x轴坐标。 |
| int32_t y | 表示指定坐标点的y轴坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回区域是否包含指定坐标点。true表示区域包含该坐标点，false表示区域不包含该坐标点。 |

**OH_Drawing_RegionOp()**

```ets
bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op)
```

描述

将两个区域按照指定的区域操作类型合并。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针，操作完成后的区域结果将会保存在此区域对象中。 |
| const OH_Drawing_Region* other | 指向区域对象OH_Drawing_Region的指针。 |
| OH_Drawing_RegionOpMode op | 区域操作枚举类型，支持可选的具体模式可见OH_Drawing_RegionOpMode枚举。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。 |

**OH_Drawing_RegionSetRect()**

```ets
bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect)
```

描述

用于尝试给区域对象设置矩形边界。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| const OH_Drawing_Rect* rect | 指向矩形对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回区域对象设置矩形边界是否成功的结果。true表示设置矩形边界成功，false表示设置矩形边界失败。 |

**OH_Drawing_RegionSetPath()**

```ets
bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip)
```

描述

给区域对象设置为指定区域内路径表示的范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| const OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Region* clip | 指向区域对象OH_Drawing_Region的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。 |

**OH_Drawing_RegionDestroy()**

```ets
void OH_Drawing_RegionDestroy(OH_Drawing_Region* region)
```

描述

用于销毁区域对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |

**OH_Drawing_RegionEmpty()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region)
```

描述

设置当前区域为空。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数region为空。 |

**OH_Drawing_RegionGetBoundaryPath()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionGetBoundaryPath(const OH_Drawing_Region* region, OH_Drawing_Path* path)
```

描述

设置路径为区域的边界。如果区域为空，则路径也将为空。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或path是空指针。 |

**OH_Drawing_RegionGetBounds()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionGetBounds(const OH_Drawing_Region* region, OH_Drawing_Rect* rect)
```

描述

获取包含该区域的最小边界矩形。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或rect是空指针。 |

**OH_Drawing_RegionIsComplex()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionIsComplex(const OH_Drawing_Region* region, bool* isComplex)
```

描述

检查该区域是否包含多个（两个及两个以上）矩形。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| bool* isComplex | 表示该区域是否包含多个矩形。作为出参使用。true表示该区域包含多个矩形，false表示该区域不包含多个矩形。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或isComplex是空指针。 |

**OH_Drawing_RegionIsEmpty()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionIsEmpty(const OH_Drawing_Region* region, bool* isEmpty)
```

描述

检查该区域是否为空。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| bool* isEmpty | 表示该区域是否为空。作为出参使用。true表示该区域为空，false表示该区域不为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或isEmpty是空指针。 |

**OH_Drawing_RegionIsRect()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionIsRect(const OH_Drawing_Region* region, bool* isRect)
```

描述

检查该区域是否等同于一个矩形。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| bool* isRect | 表示该区域是否等同于一个矩形。作为出参使用。true表示该区域等同于一个矩形，false表示该区域不等同于一个矩形。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或isRect是空指针。 |

**OH_Drawing_RegionQuickContains()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionQuickContains(const OH_Drawing_Region* region, int32_t left, int32_t top, int32_t right, int32_t bottom, bool* isContained)
```

描述

检查该区域是否等同于单个矩形并且包含指定的矩形。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| int32_t left | 表示指定矩形左上角的x轴坐标。 |
| int32_t top | 表示指定矩形左上角的y轴坐标。 |
| int32_t right | 表示指定矩形右下角的x轴坐标。 |
| int32_t bottom | 表示指定矩形右下角的y轴坐标。 |
| bool* isContained | 指示该区域是否等同于单个矩形并且包含指定的矩形。作为出参使用。 true表示该区域等同于单个矩形并且包含指定的矩形，false表示该区域不等同于单个矩形或不包含指定的矩形。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或isContained是空指针。 |

**OH_Drawing_RegionQuickReject()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionQuickReject(const OH_Drawing_Region* region, int32_t left, int32_t top, int32_t right, int32_t bottom, bool* isReject)
```

描述

检查当前区域是否为空或是否与指定矩形不相交。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| int32_t left | 表示指定矩形左上角的x轴坐标。 |
| int32_t top | 表示指定矩形左上角的y轴坐标。 |
| int32_t right | 表示指定矩形右下角的x轴坐标。 |
| int32_t bottom | 表示指定矩形右下角的y轴坐标。 |
| bool* isReject | 表示检查区域是否为空或指定的矩形是否与区域不相交。作为出参使用。 true表示当前区域为空或与指定矩形不相交；false表示当前区域不为空且与指定矩形相交。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region或isReject是空指针。 |

**OH_Drawing_RegionTranslate()**

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionTranslate(OH_Drawing_Region* region, int32_t dx, int32_t dy)
```

描述

将当前区域在x轴和y轴上按指定距离平移。如果当前区域为空，则不执行任何操作。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region* region | 指向区域对象OH_Drawing_Region的指针。 |
| int32_t dx | 表示在x轴上要平移的距离，单位为像素px。 |
| int32_t dy | 表示在y轴上要平移的距离，单位为像素px。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示region是空指针。 |