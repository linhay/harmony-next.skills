# drawing_region.h

#### 概述

定义了与区域相关的功能函数，包括区域的创建，边界设置和销毁等。

**引用文件：** <native_drawing/drawing_region.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_RegionOpMode](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionopmode)OH_Drawing_RegionOpMode区域操作类型枚举。

#### 函数

名称描述[OH_Drawing_Region* OH_Drawing_RegionCreate(void)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regioncreate)用于创建一个区域对象，实现更精确的图形控制。[OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regioncopy)用于创建一个区域对象的拷贝。[bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regioncontains)

判断区域是否包含指定坐标点。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionop)

将两个区域按照指定的区域操作类型合并。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionsetrect)

用于尝试给区域对象设置矩形边界。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionsetpath)

给区域对象设置为指定区域内路径表示的范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_RegionDestroy(OH_Drawing_Region* region)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regiondestroy)用于销毁区域对象并回收该对象占有的内存。[OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region)](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionempty)设置当前区域为空。

#### 枚举类型说明

#### OH_Drawing_RegionOpMode

```ets
enum OH_Drawing_RegionOpMode
```

**描述**

区域操作类型枚举。

**起始版本：** 12

枚举项描述REGION_OP_MODE_DIFFERENCE差集操作。REGION_OP_MODE_INTERSECT交集操作。REGION_OP_MODE_UNION并集操作。REGION_OP_MODE_XOR异或操作。REGION_OP_MODE_REVERSE_DIFFERENCE反向差集操作。REGION_OP_MODE_REPLACE替换操作。

#### 函数说明

#### OH_Drawing_RegionCreate()

```ets
OH_Drawing_Region* OH_Drawing_RegionCreate(void)
```

**描述**

用于创建一个区域对象，实现更精确的图形控制。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

类型说明[OH_Drawing_Region](OH_Drawing_Region.md)*函数会返回一个指针，指针指向创建的区域对象[OH_Drawing_Region](OH_Drawing_Region.md)。

#### OH_Drawing_RegionCopy()

```ets
OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region)
```

**描述**

用于创建一个区域对象的拷贝。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Region](OH_Drawing_Region.md)* region指向用于拷贝的区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。

**返回：**

类型说明[OH_Drawing_Region](OH_Drawing_Region.md)*函数会返回一个指针，指针指向创建的新区域对象。

#### OH_Drawing_RegionContains()

```ets
bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y)
```

**描述**

判断区域是否包含指定坐标点。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。int32_t x表示指定坐标点的x轴坐标。int32_t y表示指定坐标点的y轴坐标。

**返回：**

类型说明bool返回区域是否包含指定坐标点。true表示区域包含该坐标点，false表示区域不包含该坐标点。

#### OH_Drawing_RegionOp()

```ets
bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op)
```

**描述**

将两个区域按照指定的区域操作类型合并。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针，操作完成后的区域结果将会保存在此区域对象中。const [OH_Drawing_Region](OH_Drawing_Region.md)* other指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。[OH_Drawing_RegionOpMode](#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionopmode) op区域操作枚举类型，支持可选的具体模式可见[OH_Drawing_RegionOpMode](zh-cn_topic_0000002529285999.html#ZH-CN_TOPIC_0000002529285999__oh_drawing_regionopmode)枚举。

**返回：**

类型说明bool返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。

#### OH_Drawing_RegionSetRect()

```ets
bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect)
```

**描述**

用于尝试给区域对象设置矩形边界。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。const [OH_Drawing_Rect](OH_Drawing_Rect.md)* rect指向矩形对象的指针。

**返回：**

类型说明bool返回区域对象设置矩形边界是否成功的结果。true表示设置矩形边界成功，false表示设置矩形边界失败。

#### OH_Drawing_RegionSetPath()

```ets
bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip)
```

**描述**

给区域对象设置为指定区域内路径表示的范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。const [OH_Drawing_Path](OH_Drawing_Path.md)* path指向路径对象[OH_Drawing_Path](OH_Drawing_Path.md)的指针。const [OH_Drawing_Region](OH_Drawing_Region.md)* clip指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。

**返回：**

类型说明bool返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。

#### OH_Drawing_RegionDestroy()

```ets
void OH_Drawing_RegionDestroy(OH_Drawing_Region* region)
```

**描述**

用于销毁区域对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。

#### OH_Drawing_RegionEmpty()

```ets
OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region)
```

**描述**

设置当前区域为空。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述[OH_Drawing_Region](OH_Drawing_Region.md)* region指向区域对象[OH_Drawing_Region](OH_Drawing_Region.md)的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

返回OH_DRAWING_SUCCESS，表示执行成功。

返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数region为空。